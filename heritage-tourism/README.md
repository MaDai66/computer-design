# heritage-tourism · 吉韵遗风前端

Vue 3 + Vite 实现的前台与后台管理端。完整说明见[仓库根目录 README](../README.md)。

```bash
npm install
npm run dev     # http://localhost:5173，/api 已代理到 http://localhost:8000
npm run build   # 产物在 dist/，交给 Nginx 托管
```

- `src/views/` 前台页面
- `src/admin/` 后台管理端（数据看板 / 内容 / 用户 / 订单）
- `src/api/` 按业务模块拆分的 axios 封装
- `src/components/PanoramaViewer.vue` 基于 Pannellum 的全景播放器
