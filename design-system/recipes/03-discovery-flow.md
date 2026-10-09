# Recipe 03 · 发现流(Brand Grid + Ranking + Filter + Favorite)

> **典型场景**:用户在浏览页面选车型 →看排行榜 →筛选 →收藏
> **使用组件**:22-brand-grid + 23-ranking + 21-filter + 24-favorite

---

## 🎬 完整交互剧本

```
[用户进入"选车"页面]
    ↓
① 品牌墙 (22-brand-grid.html)
   12 个品牌 Logo 网格,点击 Nissan 进入 Nissan 车型列表
    ↓
② 排行榜(销量榜) (23-ranking.html)
   Top 5 销量车型
   "查看完整榜单"链接
    ↓
③ 筛选 (21-filter.html)
   顶部 Chip 行:品牌 / 价格 / 能源 / 排序
   点击"价格"展开 Sheet / Modal
   选 $300k-$500k
    ↓
④ 筛选后 → 列表
   每个 Product Card 上有 ❤ 收藏按钮 (24-favorite.html)
   点击 ❤ → 变 ♥ 红心
   +1 到 "我的收藏" Tab
```

---

## 💻 完整页面结构

```html
<!-- 1. Hero 顶部品牌墙 -->
<section>
  <h2>选车</h2>
  <div class="brand-grid col-6">
    <div class="brand-cell"><div class="brand-logo brand-nissan">N</div><div class="brand-name">Nissan</div></div>
    <div class="brand-cell active"><div class="brand-logo brand-mg">MG</div><div class="brand-name">MG</div></div>
    <!-- ...更多品牌 -->
  </div>
</section>

<!-- 2. 销量榜(Ranking) -->
<section>
  <h2>本月销量榜</h2>
  <div class="rank-list">
    <div class="rank-item top3">
      <div class="rank-num-badge gold">1</div>
      <div class="rank-thumb">🚗</div>
      <div class="rank-info">
        <div class="rank-title">Nissan Versa 2026</div>
        <div class="rank-sub">1.6L · CVT</div>
      </div>
      <div class="rank-value">
        <div class="rank-value-main">3,842</div>
        <div class="rank-value-sub">↑ 12.5%</div>
      </div>
    </div>
    <!-- ...更多 -->
  </div>
</section>

<!-- 3. 筛选条 (顶部 Chip 行) -->
<section>
  <div class="chip-row">
    <button class="filter-chip active">综合排序 ▾</button>
    <button class="filter-chip">品牌 ▾</button>
    <button class="filter-chip">价格 ▾</button>
    <button class="filter-chip">能源 ▾</button>
    <button class="filter-chip active with-count" data-count="3">已选 (3)</button>
  </div>
</section>

<!-- 4. 产品列表 + 收藏按钮 -->
<section class="product-grid">
  <article class="product-card">
    <div class="product-thumb">
      🚗
      <div class="product-tag new">NEW</div>
      <button class="product-fav" onclick="toggleFav(this)">♡</button>
    </div>
    <div class="product-body">
      <div class="product-brand">NISSAN</div>
      <div class="product-name">Versa 2026</div>
      <div class="product-price">$389,900</div>
    </div>
  </article>
  <!-- ...更多 -->
</section>

<!-- 5. 底部导航 -->
<nav class="bottom-tabbar">
  <div class="bottom-tab active">🏠 首页</div>
  <div class="bottom-tab">🚗 车型</div>
  <div class="bottom-tab">❤️ 收藏 (3)</div>
  <div class="bottom-tab">👤 我的</div>
</nav>
```

---

## 🔧 JS 交互

### 收藏切换

```javascript
let favCount = 0;

function toggleFav(btn) {
  btn.classList.toggle('active');
  if (btn.classList.contains('active')) {
    btn.textContent = '♥';
    favCount++;
    showToast('已加入收藏', 'success');
  } else {
    btn.textContent = '♡';
    favCount--;
    showToast('已取消收藏', 'info');
  }
  // 更新底部导航角标
  document.querySelector('.bottom-tab:nth-child(3)').textContent = `❤️ 收藏 (${favCount})`;
}
```

### 筛选 Chip 点击 → 展开 Modal

```javascript
document.querySelectorAll('.filter-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    const filterType = chip.textContent.trim();
    openFilterSheet(filterType);
  });
});

function openFilterSheet(type) {
  // 复用 21-filter.html 的 Sheet 容器
  document.getElementById('filterSheet').classList.add('open');
  document.getElementById('sheetTitle').textContent = `选择${type}`;
}
```

### 品牌点击 → 跳列表

```javascript
document.querySelectorAll('.brand-cell').forEach(cell => {
  cell.addEventListener('click', () => {
    const brand = cell.querySelector('.brand-name').textContent;
    window.location.location = `/cars?brand=${brand}`;
  });
});
```

---

## ⚠️ 易错点

1. **筛选条件展示**:用户选了 N 个条件 → 用 `.with-count` chip 显示"已选 (N)"而非隐藏条件
2. **排序默认值**:"综合排序"必须是第一项 active,不能空
3. **收藏跨页面同步**:在产品列表收藏,到"我的收藏"页面要立即可见
4. **Ranking 升降箭头**:`↑` 用绿色 / `↓` 用红色,不能都是黑色
5. **Brand Grid 黑白版**:极简风页面用 `.bw` 类,品牌官网用彩色,两种风格别混
6. **底部分页**:PC 端用分页器,H5 端用"加载更多"按钮

---

## 🎯 适用页面

| 页面 | 用此 recipe |
|------|-------------|
| 首页"选车"模块 | ✅ Brand Grid + Ranking |
| 车型列表 | ✅ Filter Chip + Product Card + Favorite |
| 排行榜页 | ✅ Ranking Top10 + Filter |
| "我的收藏"页 | ✅ Favorite Tab + Product Card |
| 品牌官网首页 | ✅ Brand Grid 6 列 |

---

## 📚 相关组件

- [`../components/22-brand-grid.html`](../components/22-brand-grid.html)
- [`../components/23-ranking.html`](../components/23-ranking.html)
- [`../components/21-filter.html`](../components/21-filter.html)
- [`../components/24-favorite.html`](../components/24-favorite.html)
- [`../components/cards/05-product-card.html`](../components/cards/05-product-card.html)
- [`../components/25-footer.html`](../components/25-footer.html) (移动端 Tabbar)
- [Recipe 02: 进度流](./02-progress-flow.md)
- [Recipe 04: 内容卡组合](./04-card-composition.md)