
<template>
  <div class="home" @wheel="handleWheel">
    <!-- 顶部轮播Banner -->
    <section class="banner">
      <div class="banner-slider">
        <router-link v-for="(slide, index) in originalSlides" :key="slide.id" :to="slide.path" class="banner-slide" :class="{ active: currentIndex === index }">
          <img :src="slide.image" :alt="slide.title" />
          <div class="banner-content">
            <h1>{{ slide.title }}</h1>
            <p>{{ slide.description }}</p>
            <button class="btn btn-banner">立即探索</button>
          </div>
        </router-link>
      </div>
      <div class="banner-dots">
        <span v-for="(slide, index) in originalSlides" :key="slide.id" class="dot" :class="{ active: currentIndex === index }" @click="showSlide(index)"></span>
      </div>
      
      <!-- 滚动提示 -->
      <div class="scroll-hint">
        <span class="scroll-text">向下滚动跳过</span>
        <div class="scroll-arrow"></div>
      </div>
    </section>

    <!-- 非遗计划介绍区 -->
    <section class="heritage-plans" :style="heritagePlansStyle">
      <div class="plan-bg-image"></div>
      <div class="korean-video-container">
        <video class="korean-video" autoplay loop muted playsinline>
          <source src="@/assets/bg/2.mp4" type="video/mp4">
        </video>
      </div>
      <div class="plan-card plan-card-left">
        <div class="plan-decor">
          <svg viewBox="0 0 400 400" class="fan-pattern">
            <path d="M200 0 L0 200 L400 200 Z" fill="rgba(255,255,255,0.03)"/>
            <path d="M200 0 L80 200 L320 200 Z" fill="rgba(255,255,255,0.05)"/>
            <path d="M200 0 L160 200 L240 200 Z" fill="rgba(255,255,255,0.08)"/>
            <path d="M200 0 L190 200 L210 200 Z" fill="rgba(255,255,255,0.1)"/>
            <circle cx="200" cy="200" r="60" fill="none" stroke="rgba(212,165,116,0.2)" stroke-width="1"/>
            <circle cx="200" cy="200" r="40" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
            <circle cx="200" cy="200" r="20" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          </svg>
        </div>
        <div class="plan-content">
          <h3 class="plan-title">
            <span class="decor-icon">◈</span>
            满族剪纸工坊
            <span class="decor-icon">◈</span>
          </h3>
          <p class="plan-description">
            满族剪纸是中国传统民间艺术之一，具有悠久的历史和独特的艺术风格。本工坊展示了满族剪纸的制作过程，包括设计、裁剪、染色等工序，传承了这一珍贵的非物质文化遗产。
          </p>
          <div class="plan-action">
            <router-link to="/cloud-workshop" class="view-more-btn">
              查看更多
              <span class="arrow-icon">⤵</span>
            </router-link>
          </div>
        </div>
      </div>
      
      <div class="plan-card plan-card-right">
        <div class="plan-content">
          <h3 class="plan-title">
            <span class="decor-icon">◈</span>
            朝鲜族打糕
            <span class="decor-icon">◈</span>
          </h3>
          <p class="plan-description">
            朝鲜族打糕是朝鲜族传统美食之一，以糯米为主要原料，经过捶打制成。打糕口感软糯香甜，是朝鲜族节庆和重要场合不可或缺的传统食品，承载着丰富的文化内涵和民族特色。
          </p>
          <div class="plan-action">
            <router-link to="/cloud-workshop?workshop=rice-cake" class="view-more-btn">
              <span class="arrow-icon">⤵</span>
              查看更多
            </router-link>
          </div>
        </div>
        <div class="korean-pattern-bg"></div>
        <div class="plan-decor">
          <svg viewBox="0 0 400 400" class="korean-decoration">
            <defs>
              <pattern id="korean-geometric" patternUnits="userSpaceOnUse" width="40" height="40">
                <path d="M20 0 L20 40 M0 20 L40 20" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
                <circle cx="20" cy="20" r="8" fill="none" stroke="rgba(212,165,116,0.12)" stroke-width="1"/>
              </pattern>
            </defs>
            <rect width="400" height="400" fill="url(#korean-geometric)"/>
            <path d="M30 100 Q60 60 100 80 Q140 100 160 60 Q180 30 220 50 Q260 70 280 40 Q300 10 350 30" 
                  stroke="rgba(212,165,116,0.25)" stroke-width="2" fill="none"/>
            <path d="M40 150 Q80 120 120 140 Q160 160 180 120" 
                  stroke="rgba(212,165,116,0.2)" stroke-width="1.5" fill="none"/>
            <path d="M250 180 Q280 150 320 170 Q360 190 380 160" 
                  stroke="rgba(212,165,116,0.2)" stroke-width="1.5" fill="none"/>
            <ellipse cx="320" cy="280" rx="60" ry="45" fill="rgba(212,165,116,0.08)"/>
            <ellipse cx="320" cy="280" rx="50" ry="35" fill="rgba(212,165,116,0.05)"/>
            <rect x="270" y="325" width="100" height="12" rx="6" fill="rgba(212,165,116,0.15)"/>
            <rect x="280" y="327" width="80" height="8" rx="4" fill="rgba(212,165,116,0.1)"/>
            <g class="rice-cake-hammer">
              <rect x="295" y="200" width="8" height="80" fill="rgba(212,165,116,0.6)" rx="2"/>
              <ellipse cx="299" cy="205" rx="12" ry="8" fill="rgba(212,165,116,0.5)"/>
            </g>
            <g class="rice-grains">
              <circle cx="260" cy="270" r="4" fill="rgba(255,248,220,0.6)"/>
              <circle cx="280" cy="260" r="3" fill="rgba(255,248,220,0.5)"/>
              <circle cx="300" cy="255" r="4" fill="rgba(255,248,220,0.6)"/>
              <circle cx="320" cy="250" r="3" fill="rgba(255,248,220,0.4)"/>
              <circle cx="340" cy="255" r="4" fill="rgba(255,248,220,0.5)"/>
              <circle cx="360" cy="265" r="3" fill="rgba(255,248,220,0.6)"/>
              <circle cx="350" cy="280" r="3" fill="rgba(255,248,220,0.5)"/>
              <circle cx="270" cy="285" r="3" fill="rgba(255,248,220,0.4)"/>
            </g>
            <circle cx="380" cy="380" r="15" fill="rgba(212,165,116,0.08)"/>
            <circle cx="380" cy="380" r="8" fill="rgba(212,165,116,0.12)"/>
            <path d="M372 380 L388 380 M380 372 L380 388" stroke="rgba(212,165,116,0.2)" stroke-width="1"/>
          </svg>
        </div>
      </div>
    </section>

    <!-- 非遗横向滚动画廊 -->
    <div class="heritage-scroll-gallery-wrapper">
      <HeritageScrollGallery />
    </div>

    <!-- 为你精选区 -->
    <section class="heritage-figures" :style="heritageFiguresStyle">
      <div class="figures-left">
        <img :src="currentFigureImage" alt="展示图片" class="figure-main-image" :class="{ active: activeFigureIndex >= 0 }"/>
        <svg viewBox="0 0 80 80" class="corner-pattern top-left">
          <circle cx="40" cy="40" r="35" fill="none" stroke="rgba(0,0,0,0.12)" stroke-width="1.5"/>
          <circle cx="40" cy="40" r="25" fill="none" stroke="rgba(0,0,0,0.1)" stroke-width="1"/>
          <circle cx="40" cy="40" r="15" fill="none" stroke="rgba(0,0,0,0.08)" stroke-width="1"/>
          <path d="M40 5 L40 75 M5 40 L75 40" stroke="rgba(0,0,0,0.06)" stroke-width="1"/>
        </svg>
        <svg viewBox="0 0 80 80" class="corner-pattern bottom-right">
          <circle cx="40" cy="40" r="35" fill="none" stroke="rgba(0,0,0,0.12)" stroke-width="1.5"/>
          <circle cx="40" cy="40" r="25" fill="none" stroke="rgba(0,0,0,0.1)" stroke-width="1"/>
          <circle cx="40" cy="40" r="15" fill="none" stroke="rgba(0,0,0,0.08)" stroke-width="1"/>
          <path d="M40 5 L40 75 M5 40 L75 40" stroke="rgba(0,0,0,0.06)" stroke-width="1"/>
        </svg>
      </div>
      <div class="figures-right">
        <svg viewBox="0 0 200 400" class="vase-pattern top-left">
          <path d="M20 380 Q60 380 80 320 L80 120 Q80 60 60 40 Q50 30 40 35 Q30 40 35 60 L35 320 Q35 360 20 380" fill="none" stroke="rgba(100,100,100,0.1)" stroke-width="1.5"/>
          <circle cx="40" cy="40" r="15" fill="none" stroke="rgba(100,100,100,0.08)" stroke-width="1"/>
          <path d="M30 50 Q40 45 50 50 Q40 55 30 50" fill="rgba(100,100,100,0.06)"/>
        </svg>
        <svg viewBox="0 0 250 150" class="bowl-pattern bottom-right">
          <path d="M20 150 L20 80 Q20 50 50 50 L200 50 Q230 50 230 80 L230 150" fill="none" stroke="rgba(100,100,100,0.1)" stroke-width="1.5"/>
          <ellipse cx="125" cy="50" rx="100" ry="8" fill="none" stroke="rgba(100,100,100,0.08)" stroke-width="1"/>
          <circle cx="125" cy="70" r="40" fill="none" stroke="rgba(100,100,100,0.06)" stroke-width="1"/>
          <path d="M105 70 Q125 55 145 70 Q125 85 105 70" fill="rgba(100,100,100,0.04)"/>
        </svg>
        <div class="figures-content">
          <div class="title-column">
            <svg viewBox="0 0 60 60" class="title-frame">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
            <div class="main-title">为你精选</div>
            <svg viewBox="0 0 60 60" class="title-frame">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
          </div>
          <div class="items-column">
            <router-link to="/heritage-experience-detail" class="figure-link" @mouseenter="setActiveFigure(0)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-1">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-gray"></span>
                <div class="figure-info">
                  <span class="figure-name">朝鲜族打糕制作体验</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
            <router-link to="/homestay-detail/1" class="figure-link" @mouseenter="setActiveFigure(1)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-2">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-red"></span>
                <div class="figure-info">
                  <span class="figure-name">长白山脚下农家院</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
            <router-link to="/product-detail/1" class="figure-link" @mouseenter="setActiveFigure(2)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-3">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-gray"></span>
                <div class="figure-info">
                  <span class="figure-name">长白山野生人参</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
            <router-link to="/tour-route-detail" class="figure-link" @mouseenter="setActiveFigure(3)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-4">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-gray"></span>
                <div class="figure-info">
                  <span class="figure-name">长白山满族寻根2日游</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
            <router-link to="/korean-village-tour-detail" class="figure-link" @mouseenter="setActiveFigure(4)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-5">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-gray"></span>
                <div class="figure-info">
                  <span class="figure-name">朝鲜族民俗村1日游</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
            <router-link to="/chagan-lake-tour-detail" class="figure-link" @mouseenter="setActiveFigure(5)" @mouseleave="setActiveFigure(0)">
              <div class="figure-item item-6">
                <svg viewBox="0 0 20 20" class="line-decoration top">
                  <path d="M10 0 L10 8 M4 4 L16 12 M16 4 L4 12" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
                <span class="figure-line line-gray"></span>
                <div class="figure-info">
                  <span class="figure-name">查干湖冬捕3日游</span>
                </div>
                <svg viewBox="0 0 20 20" class="line-decoration bottom">
                  <path d="M10 12 L10 20 M4 8 L16 16 M16 8 L4 16" stroke="rgba(212,165,116,0.6)" stroke-width="1"/>
                </svg>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- 助农好物推荐 -->
    <section class="agricultural-products">
      <div class="section-decoration-top"></div>
      
      <!-- 四角装饰 -->
      <div class="corner-decoration corner-tl">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M5 40 L5 5 L40 5" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M15 30 L15 15 L30 15" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="5" cy="5" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-tr">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M75 40 L75 5 L40 5" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M65 30 L65 15 L50 15" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="75" cy="5" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-bl">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M5 40 L5 75 L40 75" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M15 50 L15 65 L30 65" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="5" cy="75" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-br">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M75 40 L75 75 L40 75" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M65 50 L65 65 L50 65" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="75" cy="75" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      
      <!-- 左侧装饰滑块 -->
      <div class="side-decoration left-decoration">
        <div class="deco-slider deco-slider-1"></div>
        <div class="deco-slider deco-slider-2"></div>
        <div class="deco-slider deco-slider-3"></div>
        <div class="deco-dot"></div>
        <div class="deco-line"></div>
        <div class="deco-diamond"></div>
      </div>
      
      <!-- 右侧装饰滑块 -->
      <div class="side-decoration right-decoration">
        <div class="deco-slider deco-slider-1"></div>
        <div class="deco-slider deco-slider-2"></div>
        <div class="deco-slider deco-slider-3"></div>
        <div class="deco-dot"></div>
        <div class="deco-line"></div>
        <div class="deco-diamond"></div>
      </div>
      
      <!-- 漂浮装饰元素 -->
      <div class="floating-deco floating-deco-1">
        <svg viewBox="0 0 40 40" class="deco-flower">
          <circle cx="20" cy="20" r="8" fill="rgba(212,165,116,0.15)"/>
          <path d="M20 5 L23 18 L20 15 L17 18 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M20 35 L23 22 L20 25 L17 22 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M5 20 L18 23 L15 20 L18 17 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M35 20 L22 23 L25 20 L22 17 Z" fill="rgba(212,165,116,0.2)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-2">
        <svg viewBox="0 0 30 30" class="deco-pattern">
          <circle cx="15" cy="15" r="12" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1"/>
          <circle cx="15" cy="15" r="8" fill="none" stroke="rgba(154,41,41,0.15)" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="rgba(154,41,41,0.1)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-3">
        <svg viewBox="0 0 50 50" class="deco-cloud">
          <path d="M10 35 Q5 35 5 30 Q5 25 10 25 Q10 20 15 20 Q20 15 25 18 Q30 15 35 20 Q40 20 42 25 Q48 25 48 32 Q48 38 42 38 Z" fill="rgba(212,165,116,0.08)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-4">
        <svg viewBox="0 0 25 25" class="deco-star">
          <path d="M12.5 2 L15 9 L22 9 L16.5 14 L18.5 22 L12.5 17 L6.5 22 L8.5 14 L3 9 L10 9 Z" fill="rgba(212,165,116,0.15)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-5">
        <svg viewBox="0 0 35 35" class="deco-knot">
          <path d="M17.5 5 L25 12.5 L17.5 20 L10 12.5 Z" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
          <path d="M17.5 15 L25 22.5 L17.5 30 L10 22.5 Z" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
          <circle cx="17.5" cy="17.5" r="3" fill="rgba(154,41,41,0.15)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-6">
        <svg viewBox="0 0 45 45" class="deco-leaf">
          <path d="M22.5 5 Q35 15 35 25 Q35 38 22.5 42 Q10 38 10 25 Q10 15 22.5 5" fill="rgba(212,165,116,0.08)" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
          <path d="M22.5 10 L22.5 38" stroke="rgba(212,165,116,0.1)" stroke-width="1"/>
        </svg>
      </div>
      
      <!-- 顶部装饰条 -->
      <div class="top-deco-bar">
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
      </div>
      
      <!-- 底部装饰条 -->
      <div class="bottom-deco-bar">
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
      </div>
      
      <!-- 背景装饰图案 -->
      <div class="bg-pattern-overlay">
        <svg viewBox="0 0 200 200" class="pattern-svg">
          <defs>
            <pattern id="chinesePattern" x="0" y="0" width="60" height="60" patternUnits="userSpaceOnUse">
              <circle cx="30" cy="30" r="25" fill="none" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
              <circle cx="30" cy="30" r="15" fill="none" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
              <circle cx="30" cy="30" r="5" fill="rgba(212,165,116,0.02)"/>
              <path d="M30 5 L30 10 M30 50 L30 55 M5 30 L10 30 M50 30 L55 30" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#chinesePattern)"/>
        </svg>
      </div>
      
      <!-- 更多漂浮装饰元素 -->
      <div class="floating-deco floating-deco-7">
        <svg viewBox="0 0 40 40" class="deco-bamboo">
          <path d="M20 2 L20 38" stroke="rgba(154,41,41,0.15)" stroke-width="2"/>
          <path d="M20 8 Q28 12 20 16 Q12 12 20 8" fill="rgba(212,165,116,0.1)"/>
          <path d="M20 20 Q28 24 20 28 Q12 24 20 20" fill="rgba(212,165,116,0.1)"/>
          <path d="M20 32 Q28 36 20 38 Q12 36 20 32" fill="rgba(212,165,116,0.1)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-8">
        <svg viewBox="0 0 35 35" class="deco-fan">
          <path d="M17.5 30 Q5 20 5 10 Q5 5 10 5 Q17.5 5 25 10 Q30 5 30 10 Q30 20 17.5 30" fill="rgba(212,165,116,0.08)" stroke="rgba(212,165,116,0.15)" stroke-width="0.5"/>
          <path d="M17.5 8 L17.5 28" stroke="rgba(154,41,41,0.1)" stroke-width="0.5"/>
          <path d="M12 12 L17.5 26" stroke="rgba(154,41,41,0.1)" stroke-width="0.5"/>
          <path d="M23 12 L17.5 26" stroke="rgba(154,41,41,0.1)" stroke-width="0.5"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-9">
        <svg viewBox="0 0 50 50" class="deco-lantern">
          <ellipse cx="25" cy="25" rx="12" ry="18" fill="rgba(154,41,41,0.08)" stroke="rgba(154,41,41,0.15)" stroke-width="1"/>
          <path d="M25 7 Q20 5 18 7" stroke="rgba(154,41,41,0.2)" stroke-width="1" fill="none"/>
          <path d="M25 43 Q30 45 32 43" stroke="rgba(154,41,41,0.2)" stroke-width="1" fill="none"/>
          <path d="M20 15 L20 35" stroke="rgba(212,165,116,0.1)" stroke-width="0.5"/>
          <path d="M30 15 L30 35" stroke="rgba(212,165,116,0.1)" stroke-width="0.5"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-10">
        <svg viewBox="0 0 30 30" class="deco-spiral">
          <path d="M15 15 Q15 10 20 10 Q25 10 25 15 Q25 20 20 20 Q15 20 15 15 Q15 12 18 12 Q21 12 21 15 Q21 18 18 18" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
        </svg>
      </div>
      
      <!-- 粒子装饰 -->
      <div class="particles-container">
        <div class="particle particle-1"></div>
        <div class="particle particle-2"></div>
        <div class="particle particle-3"></div>
        <div class="particle particle-4"></div>
        <div class="particle particle-5"></div>
        <div class="particle particle-6"></div>
        <div class="particle particle-7"></div>
        <div class="particle particle-8"></div>
      </div>
      
      <!-- 左右边缘装饰带 -->
      <div class="edge-ribbon left-ribbon">
        <div class="ribbon-pattern"></div>
      </div>
      <div class="edge-ribbon right-ribbon">
        <div class="ribbon-pattern"></div>
      </div>
      
      <!-- 中间装饰分隔符 -->
      <div class="section-divider">
        <div class="divider-line"></div>
        <svg viewBox="0 0 60 30" class="divider-ornament">
          <path d="M0 15 Q15 5 30 15 Q45 25 60 15" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <circle cx="30" cy="15" r="4" fill="rgba(154,41,41,0.2)"/>
        </svg>
        <div class="divider-line"></div>
      </div>
      
      <!-- 波浪装饰线条 -->
      <div class="wave-decoration wave-top">
        <svg viewBox="0 0 1200 40" class="wave-svg">
          <path d="M0 20 Q150 0 300 20 T600 20 T900 20 T1200 20" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M0 25 Q150 5 300 25 T600 25 T900 25 T1200 25" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="1.5"/>
        </svg>
      </div>
      <div class="wave-decoration wave-bottom">
        <svg viewBox="0 0 1200 40" class="wave-svg">
          <path d="M0 20 Q150 40 300 20 T600 20 T900 20 T1200 20" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M0 15 Q150 35 300 15 T600 15 T900 15 T1200 15" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="1.5"/>
        </svg>
      </div>
      
      <!-- 动态光晕效果 -->
      <div class="glow-effect glow-top-left"></div>
      <div class="glow-effect glow-top-right"></div>
      <div class="glow-effect glow-bottom-left"></div>
      <div class="glow-effect glow-bottom-right"></div>
      
      <!-- 装饰性边框框架 -->
      <div class="frame-decoration frame-top"></div>
      <div class="frame-decoration frame-bottom"></div>
      <div class="frame-decoration frame-left"></div>
      <div class="frame-decoration frame-right"></div>
      
      <!-- 灯笼流苏装饰 -->
      <div class="lantern-tassel tassel-left">
        <div class="tassel-knot"></div>
        <div class="tassel-line"></div>
        <div class="tassel-fringe">
          <span></span><span></span><span></span><span></span><span></span>
        </div>
      </div>
      <div class="lantern-tassel tassel-right">
        <div class="tassel-knot"></div>
        <div class="tassel-line"></div>
        <div class="tassel-fringe">
          <span></span><span></span><span></span><span></span><span></span>
        </div>
      </div>
      
      <!-- 花瓣飘落装饰 -->
      <div class="petal-container">
        <div class="petal petal-1"></div>
        <div class="petal petal-2"></div>
        <div class="petal petal-3"></div>
        <div class="petal petal-4"></div>
        <div class="petal petal-5"></div>
      </div>
      
      <!-- 装饰云朵 -->
      <div class="cloud-decoration cloud-1">
        <svg viewBox="0 0 100 60" class="cloud-svg">
          <ellipse cx="30" cy="40" rx="25" ry="18" fill="rgba(212,165,116,0.06)"/>
          <ellipse cx="55" cy="35" rx="30" ry="22" fill="rgba(212,165,116,0.08)"/>
          <ellipse cx="75" cy="40" rx="20" ry="15" fill="rgba(212,165,116,0.06)"/>
        </svg>
      </div>
      <div class="cloud-decoration cloud-2">
        <svg viewBox="0 0 80 50" class="cloud-svg">
          <ellipse cx="25" cy="35" rx="20" ry="14" fill="rgba(154,41,41,0.05)"/>
          <ellipse cx="45" cy="30" rx="25" ry="18" fill="rgba(154,41,41,0.06)"/>
          <ellipse cx="60" cy="35" rx="15" ry="12" fill="rgba(154,41,41,0.05)"/>
        </svg>
      </div>
      
      <!-- 装饰灯笼 -->
      <div class="lantern-decoration lantern-1">
        <svg viewBox="0 0 40 50" class="lantern-svg">
          <rect x="8" y="10" width="24" height="30" rx="4" fill="rgba(154,41,41,0.1)" stroke="rgba(154,41,41,0.2)" stroke-width="1"/>
          <circle cx="20" cy="10" r="5" fill="rgba(212,165,116,0.2)"/>
          <circle cx="20" cy="40" r="5" fill="rgba(212,165,116,0.2)"/>
          <line x1="20" y1="5" x2="20" y2="10" stroke="rgba(212,165,116,0.3)" stroke-width="2"/>
          <path d="M15 40 Q20 48 25 40" fill="none" stroke="rgba(212,165,116,0.2)" stroke-width="1.5"/>
        </svg>
      </div>
      <div class="lantern-decoration lantern-2">
        <svg viewBox="0 0 35 45" class="lantern-svg">
          <rect x="6" y="8" width="23" height="28" rx="3" fill="rgba(212,165,116,0.1)" stroke="rgba(212,165,116,0.2)" stroke-width="1"/>
          <circle cx="17.5" cy="8" r="4" fill="rgba(154,41,41,0.2)"/>
          <circle cx="17.5" cy="36" r="4" fill="rgba(154,41,41,0.2)"/>
          <line x1="17.5" y1="4" x2="17.5" y2="8" stroke="rgba(154,41,41,0.3)" stroke-width="2"/>
          <path d="M13 36 Q17.5 44 22 36" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
        </svg>
      </div>
      
      <!-- 星光闪烁装饰 -->
      <div class="stars-container">
        <div class="star star-1"></div>
        <div class="star star-2"></div>
        <div class="star star-3"></div>
        <div class="star star-4"></div>
        <div class="star star-5"></div>
        <div class="star star-6"></div>
        <div class="star star-7"></div>
        <div class="star star-8"></div>
      </div>
      
      <!-- 装饰性拱门 -->
      <div class="arch-decoration arch-1">
        <svg viewBox="0 0 200 100" class="arch-svg">
          <path d="M0 100 L0 60 Q100 0 200 60 L200 100" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
          <circle cx="100" cy="60" r="40" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="0.5" stroke-dasharray="5,5"/>
        </svg>
      </div>
      
      <!-- 丝带装饰 -->
      <div class="ribbon-decoration ribbon-1">
        <svg viewBox="0 0 60 80" class="ribbon-svg">
          <path d="M30 0 L30 20 Q45 30 30 40 Q15 50 30 60 L30 80" fill="none" stroke="rgba(154,41,41,0.15)" stroke-width="2"/>
          <path d="M30 25 Q40 30 30 35 Q20 40 30 45" fill="rgba(154,41,41,0.08)"/>
        </svg>
      </div>
      <div class="ribbon-decoration ribbon-2">
        <svg viewBox="0 0 50 70" class="ribbon-svg">
          <path d="M25 0 L25 18 Q38 28 25 38 Q12 48 25 58 L25 70" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M25 23 Q33 28 25 33 Q17 38 25 43" fill="rgba(212,165,116,0.08)"/>
        </svg>
      </div>
      
      <div class="container">
        <div class="section-header-wrapper">
          <div class="header-border-left">
            <svg viewBox="0 0 60 60" class="header-corner">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
          </div>
          <div class="section-title-row">
            <div class="title-line"></div>
            <h2 class="section-title">助农好物推荐</h2>
            <div class="title-line"></div>
          </div>
          <div class="header-border-right">
            <svg viewBox="0 0 60 60" class="header-corner">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
          </div>
        </div>
        <div class="products-grid">
          <router-link to="/ginseng-product-detail" class="product-card-link">
            <div class="product-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/0a683fbea0790d2d9b52343c43e708ef.jpeg" alt="长白山野生人参" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>长白山野生人参</h3>
                <p>地道长白山特产，营养丰富</p>
                <div class="card-footer">
                  <span class="price">¥298/盒</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/corn-product-detail" class="product-card-link">
            <div class="product-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/b444fbd3022c929763d19b9bd24c60ea.jpeg" alt="吉林玉米" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>吉林有机玉米</h3>
                <p>无污染有机种植，口感香甜</p>
                <div class="card-footer">
                  <span class="price">¥39.9/5斤</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/honey-product-detail" class="product-card-link">
            <div class="product-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/5621c600388bf6b85901d32b95e97ada.jpeg" alt="吉林蜂蜜" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>长白山天然蜂蜜</h3>
                <p>采自长白山原始森林，纯天然无添加</p>
                <div class="card-footer">
                  <span class="price">¥88/瓶</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/kimchi-product-detail" class="product-card-link">
            <div class="product-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/092061c705761e245bb56444c885c6e8.jpeg" alt="朝鲜族泡菜" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>朝鲜族传统泡菜</h3>
                <p>传统工艺制作，酸辣可口</p>
                <div class="card-footer">
                  <span class="price">¥45/瓶</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <div class="section-decoration-bottom"></div>
    </section>

    <!-- 用户足迹/社区 -->
    <section class="user-community">
      <div class="section-decoration-top"></div>
      
      <!-- 四角装饰 -->
      <div class="corner-decoration corner-tl">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M5 40 L5 5 L40 5" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M15 30 L15 15 L30 15" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="5" cy="5" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-tr">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M75 40 L75 5 L40 5" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M65 30 L65 15 L50 15" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="75" cy="5" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-bl">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M5 40 L5 75 L40 75" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M15 50 L15 65 L30 65" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="5" cy="75" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      <div class="corner-decoration corner-br">
        <svg viewBox="0 0 80 80" class="corner-svg">
          <path d="M75 40 L75 75 L40 75" fill="none" stroke="rgba(212,165,116,0.3)" stroke-width="1"/>
          <path d="M65 50 L65 65 L50 65" fill="none" stroke="rgba(212,165,116,0.4)" stroke-width="1"/>
          <circle cx="75" cy="75" r="3" fill="rgba(154,41,41,0.3)"/>
        </svg>
      </div>
      
      <!-- 左侧装饰滑块 -->
      <div class="side-decoration left-decoration">
        <div class="deco-slider deco-slider-1"></div>
        <div class="deco-slider deco-slider-2"></div>
        <div class="deco-slider deco-slider-3"></div>
        <div class="deco-dot"></div>
        <div class="deco-line"></div>
        <div class="deco-diamond"></div>
      </div>
      
      <!-- 右侧装饰滑块 -->
      <div class="side-decoration right-decoration">
        <div class="deco-slider deco-slider-1"></div>
        <div class="deco-slider deco-slider-2"></div>
        <div class="deco-slider deco-slider-3"></div>
        <div class="deco-dot"></div>
        <div class="deco-line"></div>
        <div class="deco-diamond"></div>
      </div>
      
      <!-- 漂浮装饰元素 -->
      <div class="floating-deco floating-deco-1">
        <svg viewBox="0 0 40 40" class="deco-flower">
          <circle cx="20" cy="20" r="8" fill="rgba(212,165,116,0.15)"/>
          <path d="M20 5 L23 18 L20 15 L17 18 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M20 35 L23 22 L20 25 L17 22 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M5 20 L18 23 L15 20 L18 17 Z" fill="rgba(212,165,116,0.2)"/>
          <path d="M35 20 L22 23 L25 20 L22 17 Z" fill="rgba(212,165,116,0.2)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-2">
        <svg viewBox="0 0 30 30" class="deco-pattern">
          <circle cx="15" cy="15" r="12" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1"/>
          <circle cx="15" cy="15" r="8" fill="none" stroke="rgba(154,41,41,0.15)" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="rgba(154,41,41,0.1)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-3">
        <svg viewBox="0 0 50 50" class="deco-cloud">
          <path d="M10 35 Q5 35 5 30 Q5 25 10 25 Q10 20 15 20 Q20 15 25 18 Q30 15 35 20 Q40 20 42 25 Q48 25 48 32 Q48 38 42 38 Z" fill="rgba(212,165,116,0.08)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-4">
        <svg viewBox="0 0 25 25" class="deco-star">
          <path d="M12.5 2 L15 9 L22 9 L16.5 14 L18.5 22 L12.5 17 L6.5 22 L8.5 14 L3 9 L10 9 Z" fill="rgba(212,165,116,0.15)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-5">
        <svg viewBox="0 0 35 35" class="deco-knot">
          <path d="M17.5 5 L25 12.5 L17.5 20 L10 12.5 Z" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
          <path d="M17.5 15 L25 22.5 L17.5 30 L10 22.5 Z" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
          <circle cx="17.5" cy="17.5" r="3" fill="rgba(154,41,41,0.15)"/>
        </svg>
      </div>
      <div class="floating-deco floating-deco-6">
        <svg viewBox="0 0 45 45" class="deco-leaf">
          <path d="M22.5 5 Q35 15 35 25 Q35 38 22.5 42 Q10 38 10 25 Q10 15 22.5 5" fill="rgba(212,165,116,0.08)" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
          <path d="M22.5 10 L22.5 38" stroke="rgba(212,165,116,0.1)" stroke-width="1"/>
        </svg>
      </div>
      
      <!-- 顶部装饰条 -->
      <div class="top-deco-bar">
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
      </div>
      
      <!-- 底部装饰条 -->
      <div class="bottom-deco-bar">
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
        <div class="deco-bar-item"></div>
      </div>
      
      <!-- 背景装饰图案 -->
      <div class="bg-pattern-overlay">
        <svg viewBox="0 0 200 200" class="pattern-svg">
          <defs>
            <pattern id="chinesePattern2" x="0" y="0" width="60" height="60" patternUnits="userSpaceOnUse">
              <circle cx="30" cy="30" r="25" fill="none" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
              <circle cx="30" cy="30" r="15" fill="none" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
              <circle cx="30" cy="30" r="5" fill="rgba(212,165,116,0.02)"/>
              <path d="M30 5 L30 10 M30 50 L30 55 M5 30 L10 30 M50 30 L55 30" stroke="rgba(212,165,116,0.03)" stroke-width="0.5"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#chinesePattern2)"/>
        </svg>
      </div>
      
      <!-- 粒子装饰 -->
      <div class="particles-container">
        <div class="particle particle-1"></div>
        <div class="particle particle-2"></div>
        <div class="particle particle-3"></div>
        <div class="particle particle-4"></div>
        <div class="particle particle-5"></div>
        <div class="particle particle-6"></div>
        <div class="particle particle-7"></div>
        <div class="particle particle-8"></div>
      </div>
      
      <!-- 左右边缘装饰带 -->
      <div class="edge-ribbon left-ribbon">
        <div class="ribbon-pattern"></div>
      </div>
      <div class="edge-ribbon right-ribbon">
        <div class="ribbon-pattern"></div>
      </div>
      
      <!-- 波浪装饰线条 -->
      <div class="wave-decoration wave-top">
        <svg viewBox="0 0 1200 40" class="wave-svg">
          <path d="M0 20 Q150 0 300 20 T600 20 T900 20 T1200 20" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M0 25 Q150 5 300 25 T600 25 T900 25 T1200 25" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="1.5"/>
        </svg>
      </div>
      <div class="wave-decoration wave-bottom">
        <svg viewBox="0 0 1200 40" class="wave-svg">
          <path d="M0 20 Q150 40 300 20 T600 20 T900 20 T1200 20" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M0 15 Q150 35 300 15 T600 15 T900 15 T1200 15" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="1.5"/>
        </svg>
      </div>
      
      <!-- 动态光晕效果 -->
      <div class="glow-effect glow-top-left"></div>
      <div class="glow-effect glow-top-right"></div>
      <div class="glow-effect glow-bottom-left"></div>
      <div class="glow-effect glow-bottom-right"></div>
      
      <!-- 装饰性边框框架 -->
      <div class="frame-decoration frame-top"></div>
      <div class="frame-decoration frame-bottom"></div>
      <div class="frame-decoration frame-left"></div>
      <div class="frame-decoration frame-right"></div>
      
      <!-- 灯笼流苏装饰 -->
      <div class="lantern-tassel tassel-left">
        <div class="tassel-knot"></div>
        <div class="tassel-line"></div>
        <div class="tassel-fringe">
          <span></span><span></span><span></span><span></span><span></span>
        </div>
      </div>
      <div class="lantern-tassel tassel-right">
        <div class="tassel-knot"></div>
        <div class="tassel-line"></div>
        <div class="tassel-fringe">
          <span></span><span></span><span></span><span></span><span></span>
        </div>
      </div>
      
      <!-- 花瓣飘落装饰 -->
      <div class="petal-container">
        <div class="petal petal-1"></div>
        <div class="petal petal-2"></div>
        <div class="petal petal-3"></div>
        <div class="petal petal-4"></div>
        <div class="petal petal-5"></div>
      </div>
      
      <!-- 装饰云朵 -->
      <div class="cloud-decoration cloud-1">
        <svg viewBox="0 0 100 60" class="cloud-svg">
          <ellipse cx="30" cy="40" rx="25" ry="18" fill="rgba(212,165,116,0.06)"/>
          <ellipse cx="55" cy="35" rx="30" ry="22" fill="rgba(212,165,116,0.08)"/>
          <ellipse cx="75" cy="40" rx="20" ry="15" fill="rgba(212,165,116,0.06)"/>
        </svg>
      </div>
      <div class="cloud-decoration cloud-2">
        <svg viewBox="0 0 80 50" class="cloud-svg">
          <ellipse cx="25" cy="35" rx="20" ry="14" fill="rgba(154,41,41,0.05)"/>
          <ellipse cx="45" cy="30" rx="25" ry="18" fill="rgba(154,41,41,0.06)"/>
          <ellipse cx="60" cy="35" rx="15" ry="12" fill="rgba(154,41,41,0.05)"/>
        </svg>
      </div>
      
      <!-- 装饰灯笼 -->
      <div class="lantern-decoration lantern-1">
        <svg viewBox="0 0 40 50" class="lantern-svg">
          <rect x="8" y="10" width="24" height="30" rx="4" fill="rgba(154,41,41,0.1)" stroke="rgba(154,41,41,0.2)" stroke-width="1"/>
          <circle cx="20" cy="10" r="5" fill="rgba(212,165,116,0.2)"/>
          <circle cx="20" cy="40" r="5" fill="rgba(212,165,116,0.2)"/>
          <line x1="20" y1="5" x2="20" y2="10" stroke="rgba(212,165,116,0.3)" stroke-width="2"/>
          <path d="M15 40 Q20 48 25 40" fill="none" stroke="rgba(212,165,116,0.2)" stroke-width="1.5"/>
        </svg>
      </div>
      <div class="lantern-decoration lantern-2">
        <svg viewBox="0 0 35 45" class="lantern-svg">
          <rect x="6" y="8" width="23" height="28" rx="3" fill="rgba(212,165,116,0.1)" stroke="rgba(212,165,116,0.2)" stroke-width="1"/>
          <circle cx="17.5" cy="8" r="4" fill="rgba(154,41,41,0.2)"/>
          <circle cx="17.5" cy="36" r="4" fill="rgba(154,41,41,0.2)"/>
          <line x1="17.5" y1="4" x2="17.5" y2="8" stroke="rgba(154,41,41,0.3)" stroke-width="2"/>
          <path d="M13 36 Q17.5 44 22 36" fill="none" stroke="rgba(154,41,41,0.2)" stroke-width="1.5"/>
        </svg>
      </div>
      
      <!-- 星光闪烁装饰 -->
      <div class="stars-container">
        <div class="star star-1"></div>
        <div class="star star-2"></div>
        <div class="star star-3"></div>
        <div class="star star-4"></div>
        <div class="star star-5"></div>
        <div class="star star-6"></div>
        <div class="star star-7"></div>
        <div class="star star-8"></div>
      </div>
      
      <!-- 装饰性拱门 -->
      <div class="arch-decoration arch-1">
        <svg viewBox="0 0 200 100" class="arch-svg">
          <path d="M0 100 L0 60 Q100 0 200 60 L200 100" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="1"/>
          <circle cx="100" cy="60" r="40" fill="none" stroke="rgba(154,41,41,0.1)" stroke-width="0.5" stroke-dasharray="5,5"/>
        </svg>
      </div>
      
      <!-- 丝带装饰 -->
      <div class="ribbon-decoration ribbon-1">
        <svg viewBox="0 0 60 80" class="ribbon-svg">
          <path d="M30 0 L30 20 Q45 30 30 40 Q15 50 30 60 L30 80" fill="none" stroke="rgba(154,41,41,0.15)" stroke-width="2"/>
          <path d="M30 25 Q40 30 30 35 Q20 40 30 45" fill="rgba(154,41,41,0.08)"/>
        </svg>
      </div>
      <div class="ribbon-decoration ribbon-2">
        <svg viewBox="0 0 50 70" class="ribbon-svg">
          <path d="M25 0 L25 18 Q38 28 25 38 Q12 48 25 58 L25 70" fill="none" stroke="rgba(212,165,116,0.15)" stroke-width="2"/>
          <path d="M25 23 Q33 28 25 33 Q17 38 25 43" fill="rgba(212,165,116,0.08)"/>
        </svg>
      </div>
      
      <div class="container">
        <div class="section-header-wrapper">
          <div class="header-border-left">
            <svg viewBox="0 0 60 60" class="header-corner">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
          </div>
          <div class="section-title-row">
            <div class="title-line"></div>
            <h2 class="section-title">用户足迹</h2>
            <div class="title-line"></div>
          </div>
          <div class="header-border-right">
            <svg viewBox="0 0 60 60" class="header-corner">
              <rect x="5" y="5" width="50" height="50" fill="none" stroke="#9A2929" stroke-width="1.5" rx="4"/>
              <path d="M15 25 L22 30 L15 35" fill="#9A2929"/>
              <path d="M45 25 L38 30 L45 35" fill="#9A2929"/>
              <path d="M25 15 L30 22 L35 15" fill="#9A2929"/>
              <path d="M25 45 L30 38 L35 45" fill="#9A2929"/>
            </svg>
          </div>
        </div>
        <div class="community-grid">
          <router-link to="/travel-note-detail" class="community-card-link">
            <div class="community-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/6c0c36bc5ead9e4d0631905de00957a7.jpeg" alt="用户游记" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="community-content">
                <div class="content-decoration"></div>
                <h3>长白山之旅</h3>
                <p class="user-name">@旅行含小明</p>
                <p>太美了！长白山的雪景令人震撼，非遗体验也很有趣。</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>128</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>32</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/korean-rice-cake-note-detail" class="community-card-link">
            <div class="community-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/092061c705761e245bb56444c885c6e8.jpeg" alt="用户体验" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="community-content">
                <div class="content-decoration"></div>
                <h3>朝鲜族打糕体验</h3>
                <p class="user-name">@美食爱好者</p>
                <p>第一次体验打糕制作，很有趣，味道也很棒！</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>89</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>15</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/homestay-experience-note-detail" class="community-card-link">
            <div class="community-card">
              <div class="card-pattern-overlay"></div>
              <div class="card-image-wrapper">
                <img src="/image/Home/24bac5360c1ea7ec00b1036fccfd2135.jpeg" alt="用户住宿" />
                <div class="card-corner top-left"></div>
                <div class="card-corner top-right"></div>
                <div class="card-corner bottom-left"></div>
                <div class="card-corner bottom-right"></div>
              </div>
              <div class="community-content">
                <div class="content-decoration"></div>
                <h3>农家院住宿体验</h3>
                <p class="user-name">@城市逃离者</p>
                <p>远离城市喧嚣，感受乡村宁静，太惬意了！</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>156</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>42</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <div class="section-decoration-bottom"></div>
    </section>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import dongbu from '@/assets/冬捕.jpg'
import jianzhi from '@/assets/剪纸.jpg'
import nonglew from '@/assets/农乐舞.jpg'
import bgImage from '@/assets/bg/3.jpg'
import figuresBgImage from '@/assets/bg/4.png'
import defaultBgImage from '@/assets/bg/5.png'
import homestayBgImage from '@/assets/bg/6.png'
import ginsengBgImage from '@/assets/bg/7.png'
import manchuTourBgImage from '@/assets/bg/8.png'
import koreanVillageBgImage from '@/assets/bg/9.png'
import winterFishingBgImage from '@/assets/bg/10.png'
import HeritageScrollGallery from '@/components/HeritageScrollGallery.vue'

const heritagePlansStyle = computed(() => ({
  background: `linear-gradient(135deg, rgba(44, 62, 80, 0.25) 0%, rgba(52, 73, 94, 0.25) 50%, rgba(44, 62, 80, 0.25) 100%), url(${bgImage})`,
  backgroundSize: 'cover',
  backgroundPosition: 'center'
}))

const heritageFiguresStyle = computed(() => ({
  background: `url(${figuresBgImage})`,
  backgroundSize: 'cover',
  backgroundPosition: 'center'
}))

// 原始幻灯片数据
const originalSlides = ref([
  {
    id: 1,
    image: dongbu,
    title: '冬捕千年 · 吉地有礼',
    description: '探索吉林非遗文化与乡村旅游的独特魅力',
    path: '/activity-detail'
  },
  {
    id: 2,
    image: jianzhi,
    title: '剪纸艺术 · 传承千年',
    description: '体验满族传统剪纸技艺，感受民间艺术魅力',
    path: '/paper-cutting-detail'
  },
  {
    id: 3,
    image: nonglew,
    title: '农乐舞韵 · 民族风情',
    description: '感受朝鲜族传统农乐舞，体验民族文化魅力',
    path: '/nongak-dance-detail'
  }
])

const currentIndex = ref(0)
const showBackToTop = ref(false)
const activeFigureIndex = ref(0)
let isScrolling = false

const figureImages = [
  defaultBgImage,
  homestayBgImage,
  ginsengBgImage,
  manchuTourBgImage,
  koreanVillageBgImage,
  winterFishingBgImage
]

const currentFigureImage = computed(() => {
  return figureImages[activeFigureIndex.value] || defaultBgImage
})

const setActiveFigure = (index) => {
  activeFigureIndex.value = index
}

const showSlide = (index) => {
  currentIndex.value = index
}

const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % originalSlides.value.length
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

const handleWheel = (event) => {
  if (isScrolling) return
  
  event.preventDefault()
  
  const sections = [
    document.querySelector('.banner'),
    document.querySelector('.heritage-plans'),
    document.querySelector('.heritage-scroll-gallery-wrapper'),
    document.querySelector('.heritage-figures'),
    document.querySelector('.smart-recommend'),
    document.querySelector('.heritage-tour'),
    document.querySelector('.upcoming-events'),
    document.querySelector('.agricultural-products'),
    document.querySelector('.user-community')
  ].filter(Boolean)
  
  const currentScrollY = window.scrollY
  
  // 找到当前最接近视口顶部的section
  let currentSectionIndex = 0
  let minDistance = Infinity
  
  sections.forEach((section, index) => {
    const sectionTop = section.offsetTop
    const distance = Math.abs(sectionTop - currentScrollY)
    if (distance < minDistance) {
      minDistance = distance
      currentSectionIndex = index
    }
  })
  
  let targetIndex = currentSectionIndex
  
  if (event.deltaY > 50) {
    // 向下滚动
    targetIndex = Math.min(currentSectionIndex + 1, sections.length - 1)
  } else if (event.deltaY < -50) {
    // 向上滚动
    targetIndex = Math.max(currentSectionIndex - 1, 0)
  }
  
  if (targetIndex !== currentSectionIndex) {
    isScrolling = true
    const targetSection = sections[targetIndex]
    if (targetSection) {
      window.scrollTo({
        top: targetSection.offsetTop,
        behavior: 'smooth'
      })
    }
    
    // 800ms后允许再次滚动
    setTimeout(() => {
      isScrolling = false
    }, 800)
  }
}

onMounted(() => {
  // 自动轮播
  setInterval(nextSlide, 5000)
  
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Heritage Scroll Gallery Wrapper */
.heritage-scroll-gallery-wrapper {
  height: 100vh;
  width: 100%;
}

/* Heritage Figures Section */
.heritage-figures {
  display: flex;
  height: 100vh;
  width: 100%;
  position: relative;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-color: #f5f5f0;
}

.figures-left {
  width: 35%;
  background-color: #2A4033;
  position: relative;
  overflow: hidden;
}

.figure-main-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.figure-main-image.active {
  opacity: 0.8;
}

.corner-pattern {
  position: absolute;
  width: 80px;
  height: 80px;
  z-index: 1;
}

.corner-pattern.top-left {
  top: 40px;
  left: 40px;
}

.corner-pattern.bottom-right {
  bottom: 40px;
  right: 40px;
}

.figures-right {
  width: 65%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.vase-pattern {
  position: absolute;
  top: 30px;
  left: 30px;
  width: 120px;
  height: 250px;
}

.bowl-pattern {
  position: absolute;
  bottom: 30px;
  right: 30px;
  width: 180px;
  height: 100px;
}

.figures-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1400px;
  padding: 20px;
}

.title-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding-right: 20px;
  border-right: 2px solid rgba(212, 165, 116, 0.3);
  margin-right: 25px;
}

.title-frame {
  width: 40px;
  height: 40px;
}

.main-title {
  color: #333;
  font-size: 24px;
  font-weight: 600;
  writing-mode: vertical-rl;
  text-orientation: upright;
  letter-spacing: 10px;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.items-column {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 25px;
  flex: 1;
}

.figure-link {
  text-decoration: none;
  color: inherit;
}

.figure-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 10px;
  border-radius: 8px;
}

.figure-item:hover {
  background: rgba(212, 165, 116, 0.1);
}

.figure-item.item-1 {
  margin-top: 0;
}

.figure-item.item-2 {
  margin-top: 50px;
}

.figure-item.item-3 {
  margin-top: 15px;
}

.figure-item.item-4 {
  margin-top: 65px;
}

.figure-item.item-5 {
  margin-top: 30px;
}

.figure-item.item-6 {
  margin-top: 40px;
}

.line-decoration {
  width: 16px;
  height: 16px;
}

.figure-line {
  width: 2px;
  height: 50px;
  border-radius: 1px;
}

.figure-line.line-gray {
  background: rgba(150, 150, 150, 0.4);
}

.figure-line.line-red {
  background: #9A2929;
}

.figure-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.figure-name {
  color: #333;
  font-size: 22px;
  font-weight: 500;
  transition: color 0.3s ease;
  writing-mode: vertical-rl;
  text-orientation: upright;
  letter-spacing: 5px;
  line-height: 2.2;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.figure-item:hover .figure-name {
  color: #9A2929;
}

.figure-desc {
  color: rgba(100, 100, 100, 0.7);
  font-size: 12px;
  line-height: 1.5;
  writing-mode: vertical-rl;
  text-orientation: upright;
}

.porcelain-pattern {
  display: none;
}

.view-more-btn {
  margin-top: 30px;
  padding: 12px 30px;
  background: transparent;
  border: 1px solid rgba(212, 165, 116, 0.5);
  color: #d4a574;
  border-radius: 25px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 10px;
}

.view-more-btn:hover {
  background: rgba(212, 165, 116, 0.1);
  border-color: #d4a574;
  transform: translateX(5px);
}

/* Heritage Plans Section */
.heritage-plans {
  height: 100vh;
  width: 100%;
  position: relative;
  overflow: hidden;
}

.plan-card {
  display: flex;
  align-items: flex-start;
  padding: 30px;
  position: absolute;
  overflow: hidden;
  width: 50%;
  max-width: 700px;
}

.plan-bg-image {
  position: absolute;
  top: 80px;
  left: 30px;
  width: 55%;
  max-width: 750px;
  height: 400px;
  background-image: url('@/assets/bg/1.png');
  background-size: contain;
  background-position: center center;
  background-repeat: no-repeat;
  opacity: 0.85;
  z-index: 1;
}

.plan-card-left {
  flex-direction: row;
  bottom: 30px;
  left: 30px;
}

.plan-card-right {
  flex-direction: row-reverse;
  top: 120px;
  right: 30px;
}

.plan-decor {
  position: absolute;
  top: 0;
  width: 55%;
  height: 100%;
  opacity: 0.6;
  z-index: 1;
}

.plan-card-left .plan-decor {
  left: 0;
}

.korean-video-container {
  position: absolute;
  top: 400px;
  right: 80px;
  width: 40%;
  max-width: 600px;
  height: 280px;
  z-index: 2;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  background-image: url('@/assets/bg/3.jpg');
  background-size: cover;
  background-position: center;
}

.korean-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.korean-pattern-bg {
  position: absolute;
  top: 0;
  right: 0;
  width: 55%;
  height: 100%;
  background: 
    radial-gradient(circle at 20% 30%, rgba(212,165,116,0.05) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(212,165,116,0.08) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(212,165,116,0.03) 0%, transparent 60%);
  z-index: 0;
}

.korean-decoration {
  width: 100%;
  height: 100%;
}

.rice-cake-hammer {
  animation: hammerDown 2.5s ease-in-out infinite;
  transform-origin: top center;
}

@keyframes hammerDown {
  0%, 80%, 100% {
    transform: rotate(0deg) translateY(0);
  }
  90% {
    transform: rotate(-15deg) translateY(30px);
  }
}

.rice-grains circle {
  animation: grainFloat 3s ease-in-out infinite;
}

.rice-grains circle:nth-child(1) { animation-delay: 0s; }
.rice-grains circle:nth-child(2) { animation-delay: 0.3s; }
.rice-grains circle:nth-child(3) { animation-delay: 0.6s; }
.rice-grains circle:nth-child(4) { animation-delay: 0.9s; }
.rice-grains circle:nth-child(5) { animation-delay: 1.2s; }
.rice-grains circle:nth-child(6) { animation-delay: 1.5s; }
.rice-grains circle:nth-child(7) { animation-delay: 1.8s; }
.rice-grains circle:nth-child(8) { animation-delay: 2.1s; }

@keyframes grainFloat {
  0%, 100% {
    transform: translateY(0) scale(1);
    opacity: 0.6;
  }
  50% {
    transform: translateY(-8px) scale(1.1);
    opacity: 0.8;
  }
}

.plan-card-right .plan-decor {
  right: 0;
}

.fan-pattern {
  width: 100%;
  height: 100%;
}

.plan-content {
  flex: 1;
  max-width: 700px;
  position: relative;
  z-index: 2;
  padding: 20px;
}

.plan-card-left .plan-content {
  margin-left: 0;
  padding-left: 40px;
}

.plan-card-right .plan-content {
  margin-right: 0;
  padding-right: 40px;
}

.plan-title {
  font-size: 26px;
  font-weight: 600;
  color: #f0e6d3;
  margin-bottom: 20px;
  text-align: right;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 3px;
}

.plan-card-left .plan-title {
  text-align: left;
  justify-content: flex-start;
}

.plan-card-right .plan-title {
  color: #ffffff;
}

.decor-icon {
  color: #d4a574;
  font-size: 18px;
}

.plan-description {
  font-size: 15px;
  color: #e8d4bc;
  line-height: 1.8;
  margin-bottom: 20px;
  text-align: justify;
  opacity: 0.92;
}

.plan-card-left .plan-description {
  text-align: left;
}

.plan-card-right .plan-description {
  text-align: right;
  color: #ffffff;
  font-size: 16px;
}

.plan-action {
  display: flex;
  justify-content: flex-end;
}

.plan-card-left .plan-action {
  justify-content: flex-start;
}

.plan-card-right .plan-action {
  justify-content: flex-end;
}

.view-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #d4a574;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  padding: 8px 20px;
  border: 1px solid rgba(212, 165, 116, 0.5);
  border-radius: 20px;
  transition: all 0.3s ease;
  background: transparent;
}

.view-more-btn:hover {
  background: rgba(212, 165, 116, 0.1);
  border-color: #d4a574;
}

.arrow-icon {
  font-size: 14px;
  transition: transform 0.3s ease;
}

.view-more-btn:hover .arrow-icon {
  transform: translateY(2px);
}

/* Banner */
.banner {
  position: relative;
  height: 100vh;
  min-height: 600px;
  overflow: hidden;
  width: 100%;
}

.banner-slider {
  position: relative;
  width: 100%;
  height: 100%;
}

.banner-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
  z-index: 1;
}

.banner-slide.active {
  opacity: 1;
  z-index: 10;
}

.banner-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.banner-slide::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.1) 30%,
    rgba(0, 0, 0, 0) 50%,
    rgba(0, 0, 0, 0.4) 80%,
    rgba(0, 0, 0, 0.6) 100%
  );
  z-index: 5;
}

.banner-content {
  position: absolute;
  bottom: 120px;
  left: 10%;
  right: 10%;
  color: var(--white);
  z-index: 15;
  text-align: center;
}

.banner-content h1 {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--white);
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 4px;
}

.banner-content p {
  font-size: 18px;
  margin-bottom: 24px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
  opacity: 0.9;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.banner-content .btn {
  font-size: 16px;
  padding: 14px 32px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  border: 2px solid rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  color: var(--white);
  border-radius: 30px;
  transition: all 0.3s ease;
}

.banner-content .btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.banner-dots {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 20;
}

.dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.dot.active {
  background-color: var(--white);
  transform: scale(1.4);
  border-color: var(--white);
  box-shadow: 0 0 12px rgba(255, 255, 255, 0.6);
}

.scroll-hint {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 20;
  color: var(--white);
}

.scroll-text {
  font-size: 14px;
  margin-bottom: 12px;
  opacity: 0.8;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.scroll-arrow {
  width: 24px;
  height: 40px;
  border: 2px solid rgba(255, 255, 255, 0.6);
  border-radius: 12px;
  position: relative;
  animation: bounce 2s ease-in-out infinite;
}

.scroll-arrow::before {
  content: '';
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  width: 6px;
  height: 6px;
  background-color: var(--white);
  border-radius: 50%;
  animation: scrollDown 1.5s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(10px);
  }
}

@keyframes scrollDown {
  0% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) translateY(20px);
    opacity: 0;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .banner {
    height: 300px;
    margin: 10px 0;
  }
  
  .banner-slide {
    flex: 0 0 20%;
    height: 60%;
  }
  
  .banner-slide.active {
    flex: 0 0 60%;
    height: 100%;
  }
  
  .banner-content h1 {
    font-size: 16px;
  }
  
  .banner-content p {
    font-size: 10px;
  }
  
  .banner-content .btn {
    font-size: 10px;
    padding: 4px 8px;
  }
}

/* Section Header */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
}

.section-header h2 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 0;
}

.more-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition);
}

.more-link:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

/* Recommend Cards */
.recommend-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 20px;
}

.card-tags {
  margin-bottom: 12px;
}

.card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.card p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 16px;
  line-height: 1.5;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: var(--orange);
}

/* Tour Grid */
.tour-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 24px;
}

.tour-info {
  display: flex;
  gap: 16px;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--text-medium);
}

.tour-days,
.tour-experience {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* Events List */
.events-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.event-card {
  display: flex;
  gap: 20px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.event-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.event-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.event-date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background-color: var(--primary-color);
  color: var(--white);
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.event-day {
  font-size: 24px;
  font-weight: 700;
}

.event-month {
  font-size: 14px;
}

.event-content {
  flex: 1;
}

.event-content h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.event-content p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 12px;
}

.event-info {
  display: flex;
  gap: 24px;
  font-size: 14px;
  color: var(--text-light);
  margin-bottom: 16px;
}

.event-time,
.event-location {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* Agricultural Products Section */
.agricultural-products {
  background: linear-gradient(180deg, rgba(253, 248, 240, 1) 0%, rgba(245, 240, 230, 1) 100%);
  padding: 60px 0;
  position: relative;
  overflow: hidden;
}

/* 侧边装饰滑块 */
.side-decoration {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  z-index: 1;
}

.left-decoration {
  left: 40px;
}

.right-decoration {
  right: 40px;
}

.deco-slider {
  width: 6px;
  border-radius: 3px;
  background: linear-gradient(180deg, rgba(212, 165, 116, 0.4), rgba(154, 41, 41, 0.3));
  position: relative;
  overflow: hidden;
}

.deco-slider::before {
  content: '';
  position: absolute;
  top: -100%;
  left: 0;
  right: 0;
  height: 50%;
  background: linear-gradient(180deg, transparent, rgba(255, 255, 255, 0.5), transparent);
  animation: sliderFlow 3s ease-in-out infinite;
}

.deco-slider-1 {
  height: 120px;
  animation: sliderPulse 4s ease-in-out infinite;
}

.deco-slider-2 {
  height: 80px;
  animation: sliderPulse 4s ease-in-out infinite 0.5s;
}

.deco-slider-3 {
  height: 60px;
  animation: sliderPulse 4s ease-in-out infinite 1s;
}

.deco-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(154, 41, 41, 0.4), rgba(212, 165, 116, 0.2));
  animation: dotGlow 3s ease-in-out infinite;
}

.deco-diamond {
  width: 8px;
  height: 8px;
  background: rgba(212, 165, 116, 0.3);
  transform: rotate(45deg);
  animation: diamondPulse 2.5s ease-in-out infinite;
}

@keyframes diamondPulse {
  0%, 100% {
    opacity: 0.4;
    transform: rotate(45deg) scale(1);
  }
  50% {
    opacity: 0.8;
    transform: rotate(45deg) scale(1.3);
  }
}

/* 四角装饰 */
.corner-decoration {
  position: absolute;
  width: 80px;
  height: 80px;
  z-index: 1;
  pointer-events: none;
}

.corner-tl {
  top: 30px;
  left: 30px;
}

.corner-tr {
  top: 30px;
  right: 30px;
  transform: scaleX(-1);
}

.corner-bl {
  bottom: 30px;
  left: 30px;
  transform: scaleY(-1);
}

.corner-br {
  bottom: 30px;
  right: 30px;
  transform: scale(-1, -1);
}

.corner-svg {
  width: 100%;
  height: 100%;
  animation: cornerGlow 4s ease-in-out infinite;
}

@keyframes cornerGlow {
  0%, 100% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
}

/* 顶部底部装饰条 */
.top-deco-bar,
.bottom-deco-bar {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 15px;
  z-index: 1;
  pointer-events: none;
}

.top-deco-bar {
  top: 50px;
}

.bottom-deco-bar {
  bottom: 50px;
}

.deco-bar-item {
  width: 40px;
  height: 3px;
  background: linear-gradient(90deg, transparent, rgba(212, 165, 116, 0.4), transparent);
  border-radius: 2px;
  animation: barPulse 3s ease-in-out infinite;
}

.deco-bar-item:nth-child(1) { animation-delay: 0s; }
.deco-bar-item:nth-child(2) { animation-delay: 0.3s; }
.deco-bar-item:nth-child(3) { animation-delay: 0.6s; }
.deco-bar-item:nth-child(4) { animation-delay: 0.9s; }
.deco-bar-item:nth-child(5) { animation-delay: 1.2s; }

@keyframes barPulse {
  0%, 100% {
    opacity: 0.3;
    transform: scaleX(0.8);
  }
  50% {
    opacity: 0.8;
    transform: scaleX(1.2);
  }
}

.deco-line {
  width: 2px;
  height: 40px;
  background: linear-gradient(180deg, rgba(212, 165, 116, 0.3), transparent);
}

@keyframes sliderFlow {
  0% {
    top: -50%;
  }
  100% {
    top: 100%;
  }
}

@keyframes sliderPulse {
  0%, 100% {
    opacity: 0.5;
    transform: scaleY(1);
  }
  50% {
    opacity: 1;
    transform: scaleY(1.1);
  }
}

@keyframes dotGlow {
  0%, 100% {
    opacity: 0.5;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.3);
  }
}

/* 漂浮装饰元素 */
.floating-deco {
  position: absolute;
  z-index: 1;
  pointer-events: none;
}

.floating-deco-1 {
  top: 15%;
  left: 12%;
  width: 60px;
  height: 60px;
  animation: float1 6s ease-in-out infinite;
}

.floating-deco-2 {
  top: 25%;
  right: 10%;
  width: 50px;
  height: 50px;
  animation: float2 8s ease-in-out infinite;
}

.floating-deco-3 {
  bottom: 20%;
  left: 8%;
  width: 80px;
  height: 60px;
  animation: float3 7s ease-in-out infinite;
}

.floating-deco-4 {
  top: 40%;
  right: 15%;
  width: 35px;
  height: 35px;
  animation: float4 5s ease-in-out infinite;
}

.floating-deco-5 {
  bottom: 35%;
  right: 12%;
  width: 45px;
  height: 45px;
  animation: float5 9s ease-in-out infinite;
}

.floating-deco-6 {
  top: 60%;
  left: 15%;
  width: 55px;
  height: 55px;
  animation: float6 6.5s ease-in-out infinite;
}

.deco-flower,
.deco-pattern,
.deco-cloud,
.deco-star,
.deco-knot,
.deco-leaf {
  width: 100%;
  height: 100%;
}

@keyframes float1 {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-15px) rotate(10deg);
  }
}

@keyframes float2 {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(12px) rotate(-8deg);
  }
}

@keyframes float3 {
  0%, 100% {
    transform: translateX(0) translateY(0);
  }
  50% {
    transform: translateX(10px) translateY(-10px);
  }
}

@keyframes float4 {
  0%, 100% {
    transform: translateY(0) rotate(0deg) scale(1);
    opacity: 0.6;
  }
  50% {
    transform: translateY(-20px) rotate(180deg) scale(1.1);
    opacity: 0.9;
  }
}

@keyframes float5 {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-18px) rotate(15deg);
  }
}

@keyframes float6 {
  0%, 100% {
    transform: translateX(0) translateY(0) rotate(-5deg);
  }
  50% {
    transform: translateX(15px) translateY(-12px) rotate(5deg);
  }
}

/* 背景图案装饰 */
.bg-pattern-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.pattern-svg {
  width: 100%;
  height: 100%;
}

/* 更多漂浮装饰元素 */
.floating-deco-7 {
  top: 20%;
  left: 5%;
  width: 45px;
  height: 45px;
  animation: float7 7s ease-in-out infinite;
}

.floating-deco-8 {
  bottom: 25%;
  right: 5%;
  width: 40px;
  height: 40px;
  animation: float8 8s ease-in-out infinite;
}

.floating-deco-9 {
  top: 50%;
  left: 3%;
  width: 55px;
  height: 55px;
  animation: float9 6s ease-in-out infinite;
}

.floating-deco-10 {
  top: 70%;
  right: 8%;
  width: 35px;
  height: 35px;
  animation: float10 5.5s ease-in-out infinite;
}

.deco-bamboo,
.deco-fan,
.deco-lantern,
.deco-spiral {
  width: 100%;
  height: 100%;
}

@keyframes float7 {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-10px) rotate(5deg);
  }
}

@keyframes float8 {
  0%, 100% {
    transform: translateY(0) scale(1);
  }
  50% {
    transform: translateY(-15px) scale(1.05);
  }
}

@keyframes float9 {
  0%, 100% {
    transform: translateX(0) translateY(0) rotate(0deg);
  }
  50% {
    transform: translateX(8px) translateY(-12px) rotate(10deg);
  }
}

@keyframes float10 {
  0%, 100% {
    opacity: 0.5;
    transform: scale(1);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.2);
  }
}

/* 粒子装饰 */
.particles-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}

.particle {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(212,165,116,0.4), rgba(154,41,41,0.2));
  animation: particleFloat 8s ease-in-out infinite;
}

.particle-1 {
  width: 6px;
  height: 6px;
  top: 15%;
  left: 10%;
  animation-delay: 0s;
}

.particle-2 {
  width: 4px;
  height: 4px;
  top: 25%;
  right: 15%;
  animation-delay: 1s;
}

.particle-3 {
  width: 5px;
  height: 5px;
  top: 45%;
  left: 5%;
  animation-delay: 2s;
}

.particle-4 {
  width: 3px;
  height: 3px;
  bottom: 30%;
  right: 8%;
  animation-delay: 0.5s;
}

.particle-5 {
  width: 4px;
  height: 4px;
  top: 60%;
  left: 12%;
  animation-delay: 1.5s;
}

.particle-6 {
  width: 5px;
  height: 5px;
  top: 35%;
  right: 12%;
  animation-delay: 2.5s;
}

.particle-7 {
  width: 3px;
  height: 3px;
  bottom: 45%;
  left: 8%;
  animation-delay: 3s;
}

.particle-8 {
  width: 4px;
  height: 4px;
  top: 75%;
  right: 18%;
  animation-delay: 3.5s;
}

@keyframes particleFloat {
  0%, 100% {
    transform: translateY(0) translateX(0);
    opacity: 0.3;
  }
  25% {
    transform: translateY(-20px) translateX(10px);
    opacity: 0.6;
  }
  50% {
    transform: translateY(-15px) translateX(-5px);
    opacity: 0.8;
  }
  75% {
    transform: translateY(-25px) translateX(8px);
    opacity: 0.5;
  }
}

/* 左右边缘装饰带 */
.edge-ribbon {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 4px;
  z-index: 1;
  overflow: hidden;
}

.left-ribbon {
  left: 0;
}

.right-ribbon {
  right: 0;
}

.ribbon-pattern {
  width: 100%;
  height: 200%;
  background: repeating-linear-gradient(
    180deg,
    rgba(212, 165, 116, 0.15) 0px,
    rgba(212, 165, 116, 0.15) 10px,
    transparent 10px,
    transparent 20px,
    rgba(154, 41, 41, 0.1) 20px,
    rgba(154, 41, 41, 0.1) 30px,
    transparent 30px,
    transparent 50px
  );
  animation: ribbonFlow 4s linear infinite;
}

@keyframes ribbonFlow {
  0% {
    transform: translateY(-50%);
  }
  100% {
    transform: translateY(0%);
  }
}

/* 中间装饰分隔符 */
.section-divider {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 15px;
  z-index: 1;
}

.divider-line {
  width: 60px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212, 165, 116, 0.3), transparent);
}

.divider-ornament {
  width: 60px;
  height: 30px;
  animation: ornamentPulse 3s ease-in-out infinite;
}

@keyframes ornamentPulse {
  0%, 100% {
    opacity: 0.5;
  }
  50% {
    opacity: 1;
  }
}

/* 波浪装饰线条 */
.wave-decoration {
  position: absolute;
  left: 0;
  right: 0;
  z-index: 1;
  pointer-events: none;
}

.wave-top {
  top: 100px;
}

.wave-bottom {
  bottom: 100px;
}

.wave-svg {
  width: 100%;
  height: 100%;
  animation: waveMove 8s ease-in-out infinite;
}

@keyframes waveMove {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-20px);
  }
}

/* 动态光晕效果 */
.glow-effect {
  position: absolute;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  filter: blur(60px);
  z-index: 0;
  pointer-events: none;
  animation: glowPulse 6s ease-in-out infinite;
}

.glow-top-left {
  top: -50px;
  left: -50px;
  background: radial-gradient(circle, rgba(212, 165, 116, 0.15), transparent);
  animation-delay: 0s;
}

.glow-top-right {
  top: -50px;
  right: -50px;
  background: radial-gradient(circle, rgba(154, 41, 41, 0.1), transparent);
  animation-delay: 1.5s;
}

.glow-bottom-left {
  bottom: -50px;
  left: -50px;
  background: radial-gradient(circle, rgba(154, 41, 41, 0.1), transparent);
  animation-delay: 3s;
}

.glow-bottom-right {
  bottom: -50px;
  right: -50px;
  background: radial-gradient(circle, rgba(212, 165, 116, 0.15), transparent);
  animation-delay: 4.5s;
}

@keyframes glowPulse {
  0%, 100% {
    opacity: 0.4;
    transform: scale(1);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.2);
  }
}

/* 装饰性边框框架 */
.frame-decoration {
  position: absolute;
  background: linear-gradient(90deg, transparent, rgba(212, 165, 116, 0.2), transparent);
  z-index: 1;
  pointer-events: none;
}

.frame-top {
  top: 80px;
  left: 10%;
  right: 10%;
  height: 1px;
}

.frame-bottom {
  bottom: 80px;
  left: 10%;
  right: 10%;
  height: 1px;
}

.frame-left {
  top: 10%;
  bottom: 10%;
  left: 60px;
  width: 1px;
  background: linear-gradient(180deg, transparent, rgba(212, 165, 116, 0.2), transparent);
}

.frame-right {
  top: 10%;
  bottom: 10%;
  right: 60px;
  width: 1px;
  background: linear-gradient(180deg, transparent, rgba(212, 165, 116, 0.2), transparent);
}

/* 灯笼流苏装饰 */
.lantern-tassel {
  position: absolute;
  top: 60px;
  z-index: 2;
  pointer-events: none;
  animation: tasselSwing 4s ease-in-out infinite;
}

.tassel-left {
  left: 80px;
}

.tassel-right {
  right: 80px;
  animation-delay: 2s;
}

.tassel-knot {
  width: 12px;
  height: 12px;
  background: rgba(154, 41, 41, 0.3);
  border-radius: 50%;
  margin: 0 auto;
}

.tassel-line {
  width: 2px;
  height: 20px;
  background: rgba(212, 165, 116, 0.3);
  margin: 0 auto;
}

.tassel-fringe {
  display: flex;
  justify-content: center;
  gap: 3px;
  padding-top: 5px;
}

.tassel-fringe span {
  width: 2px;
  height: 25px;
  background: linear-gradient(to bottom, rgba(212, 165, 116, 0.4), rgba(154, 41, 41, 0.2));
  border-radius: 1px;
  animation: fringeWave 1.5s ease-in-out infinite;
}

.tassel-fringe span:nth-child(1) { animation-delay: 0s; }
.tassel-fringe span:nth-child(2) { animation-delay: 0.1s; }
.tassel-fringe span:nth-child(3) { animation-delay: 0.2s; }
.tassel-fringe span:nth-child(4) { animation-delay: 0.3s; }
.tassel-fringe span:nth-child(5) { animation-delay: 0.4s; }

@keyframes tasselSwing {
  0%, 100% {
    transform: rotate(-3deg);
  }
  50% {
    transform: rotate(3deg);
  }
}

@keyframes fringeWave {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(5px);
  }
}

/* 花瓣飘落装饰 */
.petal-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}

.petal {
  position: absolute;
  width: 12px;
  height: 12px;
  background: radial-gradient(ellipse, rgba(212, 165, 116, 0.3), rgba(154, 41, 41, 0.1));
  border-radius: 50% 0 50% 50%;
  animation: petalFall 12s linear infinite;
}

.petal-1 {
  left: 15%;
  top: -20px;
  animation-delay: 0s;
}

.petal-2 {
  left: 35%;
  top: -20px;
  animation-delay: 2s;
}

.petal-3 {
  left: 55%;
  top: -20px;
  animation-delay: 4s;
}

.petal-4 {
  left: 75%;
  top: -20px;
  animation-delay: 6s;
}

.petal-5 {
  left: 90%;
  top: -20px;
  animation-delay: 8s;
}

@keyframes petalFall {
  0% {
    transform: translateY(-20px) rotate(0deg) translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 0.6;
  }
  50% {
    transform: translateY(50vh) rotate(180deg) translateX(30px);
    opacity: 0.4;
  }
  90% {
    opacity: 0.3;
  }
  100% {
    transform: translateY(100vh) rotate(360deg) translateX(-20px);
    opacity: 0;
  }
}

/* 装饰云朵 */
.cloud-decoration {
  position: absolute;
  z-index: 1;
  pointer-events: none;
  animation: cloudFloat 10s ease-in-out infinite;
}

.cloud-1 {
  top: 15%;
  left: 5%;
  width: 120px;
  height: 70px;
}

.cloud-2 {
  top: 25%;
  right: 8%;
  width: 100px;
  height: 60px;
  animation-delay: 3s;
}

.cloud-svg {
  width: 100%;
  height: 100%;
}

@keyframes cloudFloat {
  0%, 100% {
    transform: translateX(0) translateY(0);
  }
  25% {
    transform: translateX(15px) translateY(-10px);
  }
  50% {
    transform: translateX(0) translateY(-5px);
  }
  75% {
    transform: translateX(-15px) translateY(-10px);
  }
}

/* 装饰灯笼 */
.lantern-decoration {
  position: absolute;
  z-index: 1;
  pointer-events: none;
  animation: lanternSwing 5s ease-in-out infinite;
}

.lantern-1 {
  top: 80px;
  right: 15%;
  width: 45px;
  height: 55px;
}

.lantern-2 {
  top: 100px;
  left: 15%;
  width: 40px;
  height: 50px;
  animation-delay: 2.5s;
}

.lantern-svg {
  width: 100%;
  height: 100%;
}

@keyframes lanternSwing {
  0%, 100% {
    transform: rotate(-5deg);
  }
  50% {
    transform: rotate(5deg);
  }
}

/* 星光闪烁装饰 */
.stars-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
}

.star {
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(212, 165, 116, 0.6);
  border-radius: 50%;
  animation: starTwinkle 3s ease-in-out infinite;
}

.star-1 { top: 20%; left: 20%; animation-delay: 0s; }
.star-2 { top: 35%; left: 7%; animation-delay: 0.5s; }
.star-3 { top: 50%; right: 18%; animation-delay: 1s; }
.star-4 { top: 65%; left: 12%; animation-delay: 1.5s; }
.star-5 { top: 75%; right: 10%; animation-delay: 2s; }
.star-6 { top: 15%; right: 25%; animation-delay: 2.5s; }
.star-7 { top: 45%; left: 3%; animation-delay: 0.8s; }
.star-8 { top: 85%; right: 22%; animation-delay: 1.2s; }

@keyframes starTwinkle {
  0%, 100% {
    opacity: 0.3;
    transform: scale(1);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.3);
  }
}

/* 装饰性拱门 */
.arch-decoration {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1;
  pointer-events: none;
}

.arch-1 {
  width: 300px;
  height: 150px;
}

.arch-svg {
  width: 100%;
  height: 100%;
  animation: archPulse 4s ease-in-out infinite;
}

@keyframes archPulse {
  0%, 100% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.8;
  }
}

/* 丝带装饰 */
.ribbon-decoration {
  position: absolute;
  z-index: 1;
  pointer-events: none;
  animation: ribbonWave 6s ease-in-out infinite;
}

.ribbon-1 {
  top: 120px;
  right: 40px;
  width: 50px;
  height: 70px;
}

.ribbon-2 {
  top: 140px;
  left: 40px;
  width: 45px;
  height: 60px;
  animation-delay: 3s;
}

.ribbon-svg {
  width: 100%;
  height: 100%;
}

@keyframes ribbonWave {
  0%, 100% {
    transform: rotate(-3deg) translateY(0);
  }
  50% {
    transform: rotate(3deg) translateY(-8px);
  }
}

.user-community {
  background: linear-gradient(180deg, rgba(245, 240, 230, 1) 0%, rgba(253, 248, 240, 1) 100%);
  padding: 60px 0;
  position: relative;
  overflow: hidden;
}

.section-decoration-top {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  height: 2px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 20px,
    rgba(212, 165, 116, 0.3) 20px,
    rgba(212, 165, 116, 0.3) 22px,
    transparent 22px,
    transparent 40px
  );
}

.section-decoration-bottom {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  height: 2px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 20px,
    rgba(212, 165, 116, 0.3) 20px,
    rgba(212, 165, 116, 0.3) 22px,
    transparent 22px,
    transparent 40px
  );
}

.section-header-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 30px;
  margin-top: 45px;
  margin-bottom: 138px;
}

.header-corner {
  width: 50px;
  height: 50px;
}

.section-title-row {
  display: flex;
  align-items: center;
  gap: 20px;
}

.title-line {
  width: 80px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(212, 165, 116, 0.6), transparent);
}

.section-title {
  font-size: 28px;
  font-weight: 600;
  color: #333;
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 8px;
}

/* Products Grid */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 30px;
}

.product-card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.product-card {
  background-color: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
  transition: all 0.4s ease;
  position: relative;
  border: 1px solid rgba(212, 165, 116, 0.1);
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

.card-pattern-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='30' cy='30' r='25' fill='none' stroke='rgba(212,165,116,0.03)' stroke-width='1'/%3E%3Ccircle cx='30' cy='30' r='15' fill='none' stroke='rgba(212,165,116,0.03)' stroke-width='1'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 1;
}

.card-image-wrapper {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.card-image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.product-card:hover .card-image-wrapper img {
  transform: scale(1.05);
}

.card-corner {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.8);
  z-index: 2;
}

.card-corner.top-left {
  top: 10px;
  left: 10px;
  border-right: none;
  border-bottom: none;
}

.card-corner.top-right {
  top: 10px;
  right: 10px;
  border-left: none;
  border-bottom: none;
}

.card-corner.bottom-left {
  bottom: 10px;
  left: 10px;
  border-right: none;
  border-top: none;
}

.card-corner.bottom-right {
  bottom: 10px;
  right: 10px;
  border-left: none;
  border-top: none;
}

.product-card .card-content {
  padding: 22px;
  position: relative;
  z-index: 2;
}

.product-card .card-tags {
  margin-bottom: 14px;
}

.product-card h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
  color: var(--text-dark);
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 1px;
}

.product-card p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 18px;
  line-height: 1.6;
}

.product-card .card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid rgba(212, 165, 116, 0.15);
}

.product-card .price {
  font-size: 20px;
  font-weight: 600;
  color: #9A2929;
}

.product-card .btn-secondary {
  padding: 8px 20px;
  font-size: 14px;
  border-radius: 20px;
  border: 1px solid #9A2929;
  color: #9A2929;
  background: transparent;
  transition: all 0.3s ease;
}

.product-card .btn-secondary:hover {
  background: #9A2929;
  color: white;
}

/* Community Grid */
.community-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
}

.community-card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.community-card {
  background-color: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
  transition: all 0.4s ease;
  position: relative;
  border: 1px solid rgba(212, 165, 116, 0.1);
}

.community-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

.community-card .card-image-wrapper {
  height: 220px;
}

.community-content {
  padding: 24px;
  position: relative;
  z-index: 2;
}

.content-decoration {
  width: 40px;
  height: 2px;
  background: linear-gradient(90deg, #d4a574, transparent);
  margin-bottom: 16px;
}

.community-content h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 2px;
}

.user-name {
  font-size: 14px;
  color: #9A2929;
  margin-bottom: 14px;
  font-weight: 500;
}

.community-content p {
  font-size: 14px;
  color: var(--text-medium);
  line-height: 1.6;
  margin-bottom: 18px;
}

.community-actions {
  display: flex;
  gap: 28px;
  padding-top: 16px;
  border-top: 1px solid rgba(212, 165, 116, 0.15);
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: none;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
  font-weight: 500;
}

.action-btn:hover {
  color: #9A2929;
  transform: translateY(-2px);
}

/* Back to Top Button */
.back-to-top {
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--shadow-hover);
  transition: var(--transition);
  z-index: 100;
}

.back-to-top:hover {
  background-color: var(--primary-dark);
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

/* Responsive */
@media (max-width: 768px) {
  .banner {
    height: 400px;
  }
  
  .banner-content {
    left: 20px;
    bottom: 20px;
  }
  
  .banner-content h1 {
    font-size: 32px;
  }
  
  .banner-content p {
    font-size: 16px;
  }
  
  .event-card {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .event-date {
    width: 60px;
    height: 60px;
  }
  
  .event-day {
    font-size: 20px;
  }
  
  .event-month {
    font-size: 12px;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}


</style>