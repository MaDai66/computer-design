# heritage-tourism · 吉韵遗风前端

Vue 3 + Vite 实现的前台与后台管理端。完整说明见[仓库根目录 README](../README.md)。

```bash
npm install
npm run dev     # http://localhost:5173，/api 已代理到 http://localhost:8000
npm run build   # 产物在 dist/，交给 Nginx 托管
```

环境变量：

| 文件 | 用途 |
|---|---|
| `.env.development` | 本地开发指向 `http://localhost:8000` |
| `.env.production` | 构建时指向线上域名 |

- `src/views/` 前台页面
- `src/admin/` 后台管理端（数据看板 / 内容 / 用户 / 订单）
- `src/api/` 按业务模块拆分的 axios 封装；`src/admin/api/adminAPI.js` 走 JWT（`/api/token/`）
- `src/components/PanoramaViewer.vue` 基于 Pannellum 的全景播放器
- `src/components/ChatPanel.vue` 右下角 AI 助手，对话地址由 `VITE_CHAT_API_BASE_URL` 指定（默认 `http://localhost:3000`）
