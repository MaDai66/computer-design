<template>
  <footer class="footer">
    <div class="footer-image">
      <img src="../assets/底部.png" alt="底部装饰" />
    </div>
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3 class="footer-title">吉韵遗风</h3>
          <p class="footer-description">
            吉林非遗文化与乡村旅游融合平台，让您感受吉林的自然之美与文化底蕴。
          </p>
        </div>
        
        <div class="footer-section">
          <h4 class="footer-subtitle">快速链接</h4>
          <ul class="footer-links">
            <li><router-link to="/">首页</router-link></li>
            <li><router-link to="/smart-tour">智游</router-link></li>
            <li><router-link to="/heritage">遗珍</router-link></li>
            <li><router-link to="/homestay">乡宿</router-link></li>
            <li><router-link to="/gifts">吉礼</router-link></li>
            <li><router-link to="/profile">我的</router-link></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4 class="footer-subtitle">帮助中心</h4>
          <ul class="footer-links">
            <li><a href="#">常见问题</a></li>
            <li><a href="#">预订指南</a></li>
            <li><a href="#">支付方式</a></li>
            <li><a href="#">联系我们</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4 class="footer-subtitle">关注我们</h4>
          <div class="social-links">
            <a href="#" class="social-link">微信</a>
            <a href="#" class="social-link">微博</a>
            <a href="#" class="social-link">抖音</a>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p class="footer-copyright">
          © 2026 吉韵遗风·乡旅吉林. 保留所有权利.
        </p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: var(--primary-dark);
  color: var(--white);
  padding: 0 0 24px;
  margin-top: 64px;
}

.footer-image {
  width: 100%;
  overflow: hidden;
}

.footer-image img {
  width: 100%;
  height: auto;
  display: block;
}

.social-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.social-link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: var(--transition);
  font-size: 14px;
}

.social-link:hover {
  color: var(--primary-color);
  padding-left: 4px;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 32px;
  margin-bottom: 32px;
}

.footer-section h3 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--white);
  font-family: var(--font-serif);
}

.footer-section h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--white);
}

.footer-description {
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0;
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 8px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: var(--transition);
  font-size: 14px;
}

.footer-links a:hover {
  color: var(--primary-color);
  padding-left: 4px;
}

.qrcode {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.qrcode img {
  width: 120px;
  height: 120px;
  border-radius: 8px;
  background-color: var(--white);
  padding: 8px;
}

.qrcode p {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 24px;
  text-align: center;
}

.footer-copyright {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .footer {
    padding: 32px 0 16px;
  }
  
  .footer-content {
    gap: 24px;
  }
  
  .footer-section h3 {
    font-size: 20px;
  }
  
  .footer-section h4 {
    font-size: 16px;
  }
}
</style>