# 阿里云服务器部署指南

## 项目结构

```
heritage/
├── backend/          # Django 后端
├── heritage-tourism/ # Vue.js 前端
└── deploy/           # 部署配置文件
```

## 一、服务器准备

### 1.1 SSH 连接服务器

```bash
ssh root@8.136.212.209
```

### 1.2 更新系统包

```bash
apt update && apt upgrade -y
```

### 1.3 安装必要软件

```bash
apt install -y python3-pip python3-venv nginx git
```

## 二、上传项目文件

### 2.1 在服务器上创建项目目录

```bash
mkdir -p /var/www/heritage
cd /var/www/heritage
```

### 2.2 上传项目文件

方式一：使用 SCP（从本地 Windows 电脑）

```powershell
# 在本地 PowerShell 中执行
scp -r "c:\Users\sk\Desktop\计设666\heritage\*" root@8.136.212.209:/var/www/heritage/
```

方式二：使用 Git（如果项目已推送到 Git 仓库）

```bash
git clone <your-repo-url> .
```

## 三、后端部署

### 3.1 创建虚拟环境

```bash
cd /var/www/heritage/backend
python3 -m venv venv
source venv/bin/activate
```

### 3.2 安装依赖

```bash
pip install -r requirements.txt
```

### 3.3 配置生产环境

```bash
export DJANGO_SECRET_KEY="your-secret-key-here-change-this"
export DJANGO_SETTINGS_MODULE="backend.settings_prod"
```

### 3.4 收集静态文件

```bash
python manage.py collectstatic --noinput
```

### 3.5 运行数据库迁移

```bash
python manage.py migrate
```

### 3.6 创建超级用户（可选）

```bash
python manage.py createsuperuser
```

## 四、前端部署

### 4.1 安装 Node.js 和 npm

```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs
```

### 4.2 安装依赖并构建

```bash
cd /var/www/heritage/heritage-tourism
npm install
npm run build
```

## 五、配置 Gunicorn

### 5.1 复制 systemd 服务文件

```bash
cp /var/www/heritage/deploy/heritage.service /etc/systemd/system/
```

### 5.2 创建 www-data 用户（如果不存在）

```bash
chown -R www-data:www-data /var/www/heritage
```

### 5.3 启动服务

```bash
systemctl daemon-reload
systemctl start heritage
systemctl enable heritage
systemctl status heritage
```

## 六、配置 Nginx

### 6.1 复制 Nginx 配置

```bash
cp /var/www/heritage/deploy/nginx.conf /etc/nginx/sites-available/heritage
ln -s /etc/nginx/sites-available/heritage /etc/nginx/sites-enabled/
```

### 6.2 测试配置

```bash
nginx -t
```

### 6.3 重启 Nginx

```bash
systemctl restart nginx
systemctl enable nginx
```

## 七、防火墙配置

### 7.1 开放 HTTP 和 HTTPS 端口

```bash
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

## 八、访问网站

现在可以通过以下地址访问：

- 前端: <http://8.136.212.209>
- 后台管理: <http://8.136.212.209/admin/>

## 九、常用维护命令

### 查看服务状态

```bash
systemctl status heritage
systemctl status nginx
```

### 查看日志

```bash
journalctl -u heritage -f
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### 重启服务

```bash
systemctl restart heritage
systemctl restart nginx
```

### 更新代码后重新部署

```bash
cd /var/www/heritage
git pull  # 如果使用 git
# 或重新上传文件

# 后端更新
cd /var/www/heritage/backend
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
systemctl restart heritage

# 前端更新
cd /var/www/heritage/heritage-tourism
npm install
npm run build
systemctl restart nginx
```

