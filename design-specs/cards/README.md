# Cards · 车系卡片样式库

> **用途**：AutoCava 全产品线（CAVI 首页 / 榜单 / 排行榜 / 对比页 / 订阅卡 / 留资卡）共用的卡片样式 reference。
>
> **查表顺序**：先看下方「样式索引」，找到最接近的 variant → 直接复用或小幅修改。

---

## 📋 样式索引

| # | 文件 | 适用场景 | 关键特性 |
|---|------|---------|---------|
| 01 | [`01-ranking-with-tags.html`](01-ranking-with-tags.html) | 排行榜 / 榜单 · 单卡内含卖点标签 + 双 CTA | 排名徽章 + 图片 + 车系名 + 起售价 + 标签 pills + 「Precio mínimo」+「Consultar planes」 |
| 02 | [`02-ranking-single-cta.html`](02-ranking-single-cta.html) | 排行榜 · 2x2 网格 · 单 CTA 精简卡 | 排名徽章 + 图片 + 车系名 + 起售价 + 全宽「Ver detalles」按钮 |
| 03 | [`03-brand-card.html`](03-brand-card.html) | 按品牌浏览入口 · 横向品牌聚合卡 | 品牌 logo + 品牌名 + 「Descubre tu auto ideal」副标 + 「Ver」按钮 |

---

## 🧩 通用组件（跨卡片共用）

| 组件 | 描述 | 位置 |
|------|------|------|
| **Ranking badge**（`#1` / `#2`） | 卡片左上角，灰底小方块 28×28，圆角 8px | 所有带排名的卡片 |
| **Chevron**（▶） | 卡片右上角，暗示"点击进入详情" | 长内容卡 |
| **Price block** | `Desde:` (灰) + `$X,XXX` (强调色 orange/amber) + `/mes` (灰) | 所有涉及月供的卡片 |
| **Price range** | `$XXX,XXX-$XXX,XXX` 全价区间，12px 灰字 | 补充信息 |
| **Tag pill** | 圆角 pill，灰底灰字，描述卖点 | 仅 `01-ranking-with-tags` |
| **Gradient CTA button** | 1.5px 渐变描边（青→紫→品红→粉）+ 渐变文字 + 白底 | `01` 的「Consultar planes」/`02` 的「Ver detalles」/`03` 的「Ver」 |
| **Plain CTA button** | 白底深字 + 1px 灰边 | `01` 的「Precio mínimo」 |

---

## 🎨 颜色 token（与 DESIGN_CONSTRAINTS.md / SKILL.md 对齐）

```css
--card-bg: #ffffff;
--card-border: rgba(0, 0, 0, 0.06);
--card-shadow: 0 4px 16px rgba(10, 25, 41, 0.06);
--text-primary: #0a1929;       /* 车系名 */
--text-secondary: #6b7280;     /* "Desde:" "/mes" 价格区间 */
--price-emphasis: #f57c00;     /* 起售价数字 · orange */
--badge-bg: #f3f4f6;           /* 排名徽章背景 */
--badge-text: #6b7280;
--tag-bg: #f3f4f6;             /* 卖点 pill */
--tag-text: #4b5563;
--btn-border: #e5e7eb;
--gradient-brand: linear-gradient(135.81deg,
  #65c9ec 0%, #825aff 24.21%,
  #d750e8 48.42%, #f25ec7 72.63%);
```

---

## 📐 尺寸规范

| 元素 | 桌面 (≥1024px) | 移动 (<1024px) |
|------|----------------|---------------|
| 卡片圆角 | 16px | 16px |
| 卡片内边距 | 20px | 16px |
| 车系图 | 56px × 56px | 56px × 56px |
| 排名徽章 | 28×28, 字号 12px | 28×28, 字号 12px |
| 起售价数字 | 24px / 600 | 20px / 600 |
| 车系名 | 16px / 600 | 16px / 600 |
| 价格区间 | 12px | 12px |
| Tag pill | 12px, py:4px px:10px | 同 |
| 按钮高度 | 44px | 44px |
| 品牌 logo（仅 03） | 48×48, 圆角 8px | 44×44, 圆角 8px |
| 品牌名（仅 03） | 16px / 700 | 16px / 700 |
| 品牌副标（仅 03） | 13px / 400 | 13px / 400 |

---

## 🔄 维护记录

| 日期 | 变更 |
|------|------|
| 2026-09-21 | 初版：新增 `01-ranking-with-tags` + `02-ranking-single-cta`，基于 CAVI 榜单原型截图（autos-mas-vendidos） |
| 2026-09-21 | +1：新增 `03-brand-card`（MG 品牌入口卡），横版 logo + 品牌名 + 「Ver」按钮 |
| 2026-09-21 | **合规修复**（按 `.cursor/rules/` 全套审查）：<br>1. 车图/品牌logo 全部替换为 autocava.com.mx 真实 CDN 地址（原编造 URL 全部 404）<br>2. 补齐全部数据字段 `<!-- source: ... -->` 溯源注释 + `ac_ab=stable` 环境标注<br>3. 修复图标误用：`simple-icons:right`（品牌库用于箭头）→ `lucide:chevron-right`（功能图标）<br>4. 标注 3 处已知差异：双CTA/渐变描边按钮、品牌卡副标+按钮、Mazda 中间两档 trim 月供均为**设计探索变体**，非线上 `/rank`／首页真实结构 1:1 复刻，中间两档 trim 数据标 `[待PM确认]` |
| 2026-09-21 | **修复渐变按钮文字隐形**：移除 `color:transparent` + `background-clip:text` 透明文字技巧，改为实心深色文字 + 渐变描边，3 处按钮（Consultar planes / Ver detalles / Ver）文字恢复可见 |
| 2026-09-21 | **新增画廊索引** `visual-specs/index.html`：导航页汇总 3 张卡片，含缩略预览 + 「打开 →」跳转；新增/改卡时需同步本表 + index.html `.card-grid` |