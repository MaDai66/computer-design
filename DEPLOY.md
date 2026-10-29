# 服务器部署指南

以 Ubuntu / 阿里云 ECS 为例，前端 Nginx 直出，后端 systemd 托管，数据库 MySQL 8。

## 目录约定

```
/var/www/heritage/
├── hesitage-backend/     # Django 后端（注意目录名就是这样拼的，仓库保持一致）
└── heritage-tourism/     # Vue 前端
```

## 一、服务器准备

```bash
ssh root@<服务器IP>
apt update && apt upgrade -y
apt install -y python3-pip python3-venv nginx git mysql-server libmysqlclient-dev pkg-config build-essential
```

Node.js（构建前端用，18 及以上）：

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs
```

## 二、拉代码

```bash
mkdir -p /var/www/heritage && cd /var/www/heritage
git clone <your-repo-url> .
```

仓库含几百 MB 的媒体文件。只想要代码可以浅克隆，媒体另外传：

```bash
git clone --depth 1 --filter=blob:none --no-checkout <your-repo-url> .
git sparse-checkout set '/*' '!heritage-tourism/src/assets/**' '!heritage-tourism/public/**' '!hesitage-backend/media/**'
git checkout main
```

## 三、数据库

```bash
mysql -u root -p
```

```sql
CREATE DATABASE heritage_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 四、后端

### 4.1 虚拟环境与依赖

```bash
cd /var/www/heritage/hesitage-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

`mysqlclient` 需要编译，前面装的 `libmysqlclient-dev` + `pkg-config` 就是给它用的；编译不过时先补 `default-libmysqlclient-dev`。

### 4.2 环境变量

`settings.py` 里的密钥、数据库密码、模型 Key 都从环境变量读，**不要写回代码**。

```bash
cp .env.example .env
vim .env
```

```ini
DJANGO_SECRET_KEY=<随机长串>
MYSQL_PASSWORD=<MySQL 密码>
SILICONFLOW_API_KEY=<SiliconFlow 的 Key>
SILICONFLOW_API_BASE_URL=https://api.siliconflow.cn/v1
```

生成随机串：`python3 -c "import secrets;print(secrets.token_urlsafe(50))"`

### 4.3 初始化

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser     # 可选
```

### 4.4 systemd

仓库里已带 `hesitage-backend/heritage-backend.service`：

```bash
cp /var/www/heritage/hesitage-backend/heritage-backend.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now heritage-backend
systemctl status heritage-backend
```

> 该文件用的是 `manage.py runserver`，够跑演示。要上量请换成 Gunicorn：
> `ExecStart=/var/www/heritage/hesitage-backend/venv/bin/gunicorn backend.wsgi:application -w 3 -b 127.0.0.1:8000`

### 4.5 权限

上传目录要可写，否则头像上传会 500：

```bash
chown -R www-data:www-data /var/www/heritage/hesitage-backend/media /var/www/heritage/hesitage-backend/staticfiles
```

## 五、前端

```bash
cd /var/www/heritage/heritage-tourism
npm install
npm run build        # 产物在 dist/，由 Nginx 托管
```

构建前确认 `.env.production` 里的接口地址指向线上域名。

## 六、Nginx

```bash
cp /var/www/heritage/deploy/nginx.conf /etc/nginx/sites-available/heritage
ln -sf /etc/nginx/sites-available/heritage /etc/nginx/sites-enabled/heritage
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx
```

`deploy/nginx.conf` 里有三个容易漏的点，改配置时别删：

- `location /api/ai/` 必须 `proxy_buffering off`，否则对话要等全部生成完才一次性出现
- `/static/`、`/media/` 用 `^~`，否则会被下面的正则 location 抢走
- `client_max_body_size 20m`，管头像和图片上传

## 七、防火墙

```bash
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

域名与 HTTPS：用 `certbot --nginx -d <域名>` 自动签证书。

## 八、常用维护

```bash
systemctl status heritage-backend nginx
journalctl -u heritage-backend -f
tail -f /var/log/nginx/error.log
```

更新代码后：

```bash
cd /var/www/heritage && git pull

cd hesitage-backend && source venv/bin/activate \
  && pip install -r requirements.txt \
  && python manage.py migrate \
  && python manage.py collectstatic --noinput \
  && systemctl restart heritage-backend

cd ../heritage-tourism && npm install && npm run build
```

前端是纯静态，Nginx 不用重启；后端改完只重启 `heritage-backend` 即可。

## 九、上线前必改

代码里现在是开发配置，公网部署前务必处理（对应根 README 的「已知限制」第 1 条）：

- `DEBUG = True` → 关掉
- `ALLOWED_HOSTS = ['*']` → 换成真实域名
- `CORS_ALLOW_ALL_ORIGINS = True` → 白名单
- Django Admin 建议换非默认路径，或直接限制来源 IP
