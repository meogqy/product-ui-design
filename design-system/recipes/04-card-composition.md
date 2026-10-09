# Recipe 04 · 内容卡组合(Content + Article + Product + Brand Card)

> **典型场景**:列表页 / 详情页 / 搜索结果页 — 各种内容卡的混排展示
> **使用组件**:01-content-card + 02-simple-card + 03-brand-card + 04-article-card + 05-product-card

---

## 🎬 典型页面构成

```
[首页 / 列表页]
├── 顶部 Banner (促销 / 公告)
├── Brand Grid (品牌入口)
├── Ranking (销量榜)
├── Content Card 列表(精选内容)
├── Product Card 列表(在售车型)
├── Article Card 列表(资讯)
└── Footer
```

---

## 💻 完整页面片段

### 首页布局

```html
<!-- 1. Banner 顶部促销 -->
<section>
  <div class="banner banner-promo">
    🔥 9 月购车节 · 最高优惠 $40,000 · <a>查看详情</a>
  </div>
</section>

<!-- 2. 品牌入口(Brand Grid) -->
<section>
  <h2>选品牌</h2>
  <div class="brand-grid col-6">
    <!-- 12 个品牌 -->
  </div>
</section>

<!-- 3. 销量榜(Ranking) -->
<section>
  <h2>本月销量榜 Top 5</h2>
  <div class="rank-list">
    <!-- 5 个排行项 -->
  </div>
</section>

<!-- 4. 精选内容卡(Content Card - 横向大卡) -->
<section>
  <h2>编辑推荐</h2>
  <div class="article-h">
    <div class="article-h-thumb">📊</div>
    <div class="article-h-content">
      <div class="article-h-meta">
        <span class="article-cat">市场分析</span>
      </div>
      <h3 class="article-h-title">2026 年墨西哥汽车市场报告</h3>
      <p class="article-h-desc">电动车销量首次突破 8%...</p>
      <div class="article-h-foot">
        <span>👁 3.2k</span>
        <span>💬 24</span>
      </div>
    </div>
  </div>
</section>

<!-- 5. 在售车型(Product Card 网格) -->
<section>
  <h2>推荐车型</h2>
  <div class="product-grid">
    <article class="product-card">
      <div class="product-thumb">🚗<button class="product-fav">♡</button></div>
      <div class="product-body">
        <div class="product-brand">NISSAN</div>
        <div class="product-name">Versa 2026 Exclusive</div>
        <div class="product-price">$389,900</div>
        <div class="product-financing">月供 $6,499 起</div>
      </div>
    </article>
    <!-- ...更多 -->
  </div>
</section>

<!-- 6. 资讯流(Article Card 网格) -->
<section>
  <h2>最新资讯</h2>
  <div class="article-grid">
    <article class="article-v">
      <div class="article-v-thumb">📈</div>
      <div class="article-v-body">
        <h3 class="article-v-title">8 月销量榜:Nissan 蝉联榜首</h3>
        <p class="article-v-desc">2026 年 8 月数据出炉...</p>
      </div>
    </article>
    <!-- ...更多 -->
  </div>
</section>
```

### 搜索结果页

```html
<!-- 顶部筛选条 + 列表 -->
<section>
  <div class="chip-row">
    <button class="filter-chip active">综合 ▾</button>
    <button class="filter-chip">价格 ▾</button>
    <button class="filter-chip active with-count" data-count="2">已选 (2)</button>
  </div>
  
  <!-- 紧凑型产品卡(列表式) -->
  <div class="product-list">
    <article class="product-compact">
      <div class="product-compact-thumb">🚗</div>
      <div class="product-compact-body">
        <div class="product-compact-name">Nissan Versa 2026</div>
        <div class="product-compact-bottom">
          <span class="product-compact-price">$389,900</span>
          <span class="product-compact-rate">8.9% APR</span>
        </div>
      </div>
    </article>
    <!-- ...更多 -->
  </div>
</section>
```

### 文章详情页

```html
<!-- 视频缩略图卡(文章详情头部) -->
<header>
  <div class="article-video">
    <div class="article-video-thumb">
      <div class="video-play">▶</div>
      <div class="video-duration">12:34</div>
    </div>
    <div class="article-video-body">
      <h1>2026 墨西哥汽车市场深度报告</h1>
      <div class="article-c-meta">
        <span>视频</span> · <span>3 天前</span>
      </div>
    </div>
  </div>
</header>

<!-- 文章正文... -->

<!-- 相关推荐(Article Card 列表) -->
<section>
  <h3>相关阅读</h3>
  <div class="article-c">
    <div class="article-c-thumb">📊</div>
    <div class="article-c-body">
      <h4 class="article-c-title">电动车销量报告</h4>
      <div class="article-c-meta"><span>市场</span> · <span>1 天前</span></div>
    </div>
  </div>
  <!-- ...更多 -->
</section>
```

---

## 🎨 卡片选择决策表

| 场景 | 用哪种卡 | 理由 |
|------|---------|------|
| **精选 1 篇重点文章** | `Content Card` 或 `Article Horizontal` | 大图 + 完整信息 |
| **3+ 篇资讯列表** | `Article Vertical` (3 列网格) | 信息密度高 |
| **侧边栏 / 嵌入式** | `Article Compact` | 小图 + 标题 |
| **视频内容** | `Article Video` | 自动播放感 + 时长 |
| **在售车型展示** | `Product Card` 标准竖版 | 价格 + 月供 + 收藏 |
| **车型详情推荐** | `Product Card` 横版 | 大图 + 完整规格 |
| **促销/优惠车型** | `Product Card` 优惠角标版 | 突出折扣感 |
| **品牌入口(首页)** | `Brand Grid` 6 列 | 网格浏览 |
| **品牌详情页** | `Brand Card` 或 `Brand List` | 单列带说明 |
| **榜单页** | `Ranking` + `Content Card` | Top 3 高亮 + 完整卡 |

---

## 📐 卡片尺寸规范

| 卡片 | 推荐尺寸 | 适配场景 |
|------|---------|---------|
| Content Card | 宽 100% / 高 ~120px | 列表项 |
| Article Horizontal | 240×160px 缩略图 + 完整右栏 | 推荐位 |
| Article Vertical | 1fr/3 列网格 | 资讯流 |
| Article Compact | 80×80px 缩略图 | 侧边栏 |
| Article Video | 16:9 缩略图 | 视频页 |
| Product Card | 1fr/3 列网格 | 商品流 |
| Product Card Horizontal | 240×180px 缩略图 | 详情推荐 |
| Product Compact | 56×56px 缩略图 | 嵌入式 |
| Brand Cell | 6 列网格 / 48×48px logo | 首页入口 |
| Brand Card | 200×80px | 品牌详情 |

---

## ⚠️ 易错点

1. **图片比例**:
   - 车型 / 商品 → 4:3 或 16:9
   - 资讯 / 文章 → 16:9 或 3:2
   - 头像 / Logo → 1:1 圆形

2. **卡片高度一致**:网格布局必须等高,不等高用 `align-items: stretch` 或固定高度

3. **价格突出**:`$389,900` 必须用大字号 + tabular-nums + 加粗

5. **缩略图占位**:未加载前用灰色背景 + emoji,避免布局抖动(CLS)

6. **角标位置**:NEW / HOT / 折扣 永远在**左上角**,收藏按钮在**右上角**

7. **Hover 反馈**:列表卡 hover 必须有视觉反馈(边框色 / 阴影 / 上移),不能"死卡"

---

## 🎯 适用页面

| 页面 | 用此 recipe |
|------|-------------|
| 首页 | ✅ Banner + Brand Grid + Ranking + Content + Product + Article |
| 车型列表页 | ✅ Filter + Product Card(网格/紧凑) |
| 车型详情页 | ✅ Product Card 横版 + 收藏 + 相关推荐 |
| 文章列表页 | ✅ Article Vertical 网格 |
| 文章详情页 | ✅ Article Video + Content Card + Article Compact |
| 搜索结果页 | ✅ Product Compact + Filter Chip |
| 品牌列表页 | ✅ Brand List 单列 |
| 排行榜页 | ✅ Ranking + Product Card |

---

## 📚 相关组件

- [`../components/cards/01-content-card.html`](../components/cards/01-content-card.html)
- [`../components/cards/02-simple-card.html`](../components/cards/02-simple-card.html)
- [`../components/cards/03-brand-card.html`](../components/cards/03-brand-card.html)
- [`../components/cards/04-article-card.html`](../components/cards/04-article-card.html)
- [`../components/cards/05-product-card.html`](../components/cards/05-product-card.html)
- [Recipe 03: 发现流](./03-discovery-flow.md)