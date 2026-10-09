# Cards · 内容卡样式库

> **3 个核心 card variant** · 单文件自适应 · 数据可替换

---

## 📦 3 个 card variant

| # | 文件 | 适用场景 | 关键特性 |
|---|------|---------|----------|
| 1 | [`01-content-card.html`](01-content-card.html) | 内容卡（榜单 / 资讯 / 商品列表） | 排名徽章 + 图片 + 标题 + 起售价 + 标签 pills + 主 CTA + 次 CTA |
| 2 | [`02-simple-card.html`](02-simple-card.html) | 简洁卡（列表 / 搜索结果） | 排名徽章 + 图片 + 标题 + 起售价 + 全宽 CTA |
| 3 | [`03-brand-card.html`](03-brand-card.html) | 品牌入口卡（横向品牌聚合） | 品牌 logo + 品牌名 + 副标 + CTA |

---

## 🛠️ 如何替换数据为你自己的

3 个 HTML 文件里的**示例数据**（标题、价格、图片 URL、CTA 文案）都是 Mstar / AutoCava 平台的示例。

**接到你的项目后**，每个文件做这 5 处替换：

```html
<!-- 1. 标题 -->
<h3>Nissan Magnite</h3> → <h3>Your Product Name</h3>

<!-- 2. 价格 -->
<span>$374,990</span> → <span>$XXX,XXX</span>

<!-- 3. 图片 URL -->
src="https://cdn.autocava.com.mx/..." → src="https://your-cdn.com/..."

<!-- 4. CTA 文案 -->
<button>Precio mínimo</button> → <button>Your CTA</button>

<!-- 5. 链接 -->
href="https://www.autocava.com.mx/..." → href="https://your-domain/..."
```

> **数据替换后**，card 结构和样式完全不变。

---

## 🧩 通用组件（跨 card 共用）

| 组件 | 描述 |
|------|------|
| **Card 容器** | 圆角 16px + 边框 + 阴影 |
| **排名徽章**（`#1` / `#2`） | 灰底小方块 28×28，圆角 8px |
| **价格块** | `From:` (灰) + `$X,XXX` (强调色) + `/mo` (灰) |
| **价格区间** | `$XXX,XXX-$XXX,XXX` 全价区间，12px 灰字 |
| **Tag pill** | 圆角 pill，灰底灰字，描述卖点 |
| **CTA 按钮** | 复用 `../01-button.html` |

---

## 🎨 颜色 token（与 [`../../tokens.md`](../../tokens.md) 对齐）

```css
--card-bg: #ffffff;
--card-border: rgba(0, 0, 0, 0.06);
--card-shadow: 0 4px 16px rgba(10, 25, 41, 0.06);
--text-primary: #222222;
--text-secondary: #6b7280;
--price-emphasis: #f57c00;  /* 起售价数字 */
--badge-bg: #f3f4f6;
--badge-text: #6b7280;
--tag-bg: #f3f4f6;
--tag-text: #4b5563;
--btn-border: #e5e7eb;
--gradient-brand: linear-gradient(135.81deg,
  #65c9ec 0%, #825aff 24.21%,
  #d750e8 48.42%, #f25ec7 72.63%);
```

---

## 🚫 禁止

- ❌ 在 cards 里放一次性样式（一次性 = 页面本地）
- ❌ 在 cards 里放未冻结的探索稿
- ❌ 改这里的样式而不更新对应项目中的引用
- ❌ 用 emoji 替代品牌图标

---

## 🔗 相关

- [`../../tokens.md`](../../tokens.md) — 设计变量
- [`../../principles.md`](../../principles.md) — 7 条跨线硬规则
- [`../README.md`](../README.md) — 组件库总目录
- [`../../demo/`](../../demo/) — 完整生产页 demo

---

## 📋 维护记录

| 日期 | 变更 | 作者 |
|------|------|------|
| 2026-09-29 | v1.0 初版：从 Mstar `visual-specs/cards/` 复制 + 通用化指南 | AI 起草，待 PM 审 |