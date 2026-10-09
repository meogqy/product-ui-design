# Components · 组件库

> **参考组件库**（共 25 个核心组件 + 5 张内容卡，约 90+ 个变体）
> **覆盖**：任何 UI 场景的 95%+ 通用组件需求
> **来源**：综合 Figma 588 个组件名（[Autocava + 2026 设计稿库]）去重、通用化而来

---

## 📦 25 个核心组件 + 5 张内容卡

### 🎨 P0 基础交互（按钮 · 表单 · 反馈）

| # | 文件 | 组件 | 变体 | 用法 |
|---|------|------|------|------|
| 1 | [`01-button.html`](01-button.html) | **Button** | 22+ | 所有 CTA 按钮（2 尺寸 × 3 颜色 × 4 状态）+ **按钮组 / 单选 / 操作栏 / 浮动操作栏** |
| 2 | [`02-input.html`](02-input.html) | **Input** | 4 | 任何表单字段 |
| 3 | [`03-tag.html`](03-tag.html) | **Tag / Score chip / Pill** | 2+ | 评分 / 排行 / **分类标签（基础/可关闭/可计数/可单选/大尺寸）** |
| 4 | [`04-tabbar.html`](04-tabbar.html) | **Tabbar** | 2 | H5 底部主导航 |
| 5 | [`05-badge.html`](05-badge.html) | **Badge** | 2 | 认证 / 状态徽章 |
| 6 | [`09-modal.html`](09-modal.html) | **Modal** | 3+ | 信息提示 / 确认 / 自定义 + **带 Header 导航 / Footer 输入 / Header+Footer 全功能型** |
| 7 | [`10-toast.html`](10-toast.html) | **Toast** | 4 | success / info / warning / error |
| 8 | [`12-select.html`](12-select.html) | **Select** | 3 | 基本 / 带搜索 / 多选 |
| 9 | [`13-checkbox.html`](13-checkbox.html) | **Checkbox** | 4 | unchecked / checked / indeterminate / disabled |
| 10 | [`14-radio.html`](14-radio.html) | **Radio** | 3 | unchecked / checked / disabled |
| 11 | [`15-switch.html`](15-switch.html) | **Switch** | 3 | off / on / disabled |

### 🧭 P0 导航与容器

| # | 文件 | 组件 | 变体 | 用法 |
|---|------|------|------|------|
| 12 | [`06-topnav.html`](06-topnav.html) | **Top Nav** | 3 | H5 简单 / H5 完整 / PC 顶栏 |
| 13 | [`18-progress.html`](18-progress.html) | **Progress** 🆕 | 12+ | **4 视图 · Linear 线性 / Battery 电池 / Circular 环形 / Stepper 步进**（Figma 342 次使用 #1 高频缺失组件） |
| 14 | [`20-steps.html`](20-steps.html) | **Steps** 🆕 | 6+ | **3 视图 · 横排步骤条 / 竖排时间线 / 流程图节点**（Figma 84 次） |
| 15 | [`19-typography.html`](19-typography.html) | **Typography** 🆕 | 14+ | **Display + H1-H6 + Body + Caption + Overline + 数字大字 + 字组组合**（Figma 113 次） |

### 💬 P1 反馈与场景

| # | 文件 | 组件 | 变体 | 用法 |
|---|------|------|------|------|
| 16 | [`07-loading.html`](07-loading.html) | **Loading** | 3 | 卡片 / 列表行 / 全页骨架 |
| 17 | [`08-empty-state.html`](08-empty-state.html) | **Empty State** | 3 | 无数据 / 无结果 / 错误 |
| 18 | [`11-search.html`](11-search.html) | **Search** | 3 | 基本 / 带快捷键 / H5 嵌入 |
| 19 | [`16-avatar.html`](16-avatar.html) | **Avatar** | 4 | 字母 / 图片 / 状态点 / 头像组 |
| 20 | [`17-banner.html`](17-banner.html) | **Banner** | 3 | info / promo / warning |
| 21 | [`21-filter.html`](21-filter.html) | **Filter** 🆕 | 9+ | **3 视图 · 顶部 Chip 行 / 底部 Sheet / 居中 Modal**（Figma 17 次） |

### 🌍 P2 业务场景通用化（领域专属 → 通用）

| # | 文件 | 组件 | 变体 | 用法 |
|---|------|------|------|------|
| 22 | [`22-brand-grid.html`](22-brand-grid.html) | **Brand Grid** 🆕 | 12+ | **4 视图 · 6/4/3 列网格 / 单列品牌列表 / A-Z 索引 / 黑白版**（Figma 168+ 次·车品牌通用化） |
| 23 | [`23-ranking.html`](23-ranking.html) | **Ranking** 🆕 | 9+ | **3 视图 · 标准榜 / 金银铜 Top3 高亮 / 横向条形榜**（Figma 31 次·排行榜通用化） |
| 24 | [`24-favorite.html`](24-favorite.html) | **Favorite** 🆕 | 9+ | **4 视图 · 图标按钮 / 卡片角标 / 收藏 Tab / 收藏列表行**（Figma 57+ 次·车系收藏通用化） |
| 25 | [`25-footer.html`](25-footer.html) | **Footer** 🆕 | 8+ | **4 视图 · 链接版 / 简单版 / 完整版 / 移动端底部 Tabbar**（Figma 69+ 次·底部通用化） |

### 📁 内容卡库（[`cards/`](cards/)）

| # | 文件 | 适用场景 | 关键特性 |
|---|------|---------|----------|
| 1 | [`cards/01-content-card.html`](cards/01-content-card.html) | 内容卡（榜单 / 资讯 / 商品列表） | 排名徽章 + 图片 + 标题 + 起售价 + 标签 pills + 主 CTA + 次 CTA |
| 2 | [`cards/02-simple-card.html`](cards/02-simple-card.html) | 简洁卡（列表 / 搜索结果） | 排名徽章 + 图片 + 标题 + 起售价 + 全宽 CTA |
| 3 | [`cards/03-brand-card.html`](cards/03-brand-card.html) | 品牌入口卡 | 品牌 logo + 品牌名 + 副标 + CTA |
| 4 | [`cards/04-article-card.html`](cards/04-article-card.html) 🆕 | **文章 / 资讯卡**（通用化） | 4 视图 · 横版大卡 / 竖版网格 / 紧凑列表 / 视频缩略图（支持 LIVE 直播） |
| 5 | [`cards/05-product-card.html`](cards/05-product-card.html) 🆕 | **商品 / 车型卡**（通用化） | 4 视图 · 竖版标准 / 横版大卡 / 极简文字 / 优惠角标（含月供金融区） |

---

## 🚦 按场景选组件

| 场景 | 用哪个组件 |
|------|-----------|
| 任何 CTA 按钮 / 按钮组 / 单选套餐 | `01-button.html` |
| 表单输入（姓名 / 邮箱 / 电话） | `02-input.html` |
| 评分 / 排行 / 分类标签 | `03-tag.html` |
| H5 底部主导航 | `04-tabbar.html` |
| 身份 / 资质 / 售后标识 | `05-badge.html` |
| H5 / PC 顶部导航 | `06-topnav.html` |
| 异步加载占位 | `07-loading.html` |
| 空数据 / 无结果 / 错误页 | `08-empty-state.html` |
| 模态对话框 / 弹窗 / 表单弹窗 | `09-modal.html` |
| 操作反馈 / 提示消息 | `10-toast.html` |
| 搜索框（PC / H5 / 全局） | `11-search.html` |
| 下拉选择（选项 ≤ 20 个） | `12-select.html` |
| 复选（多选 / 协议） | `13-checkbox.html` |
| 单选（互斥选项） | `14-radio.html` |
| 开关（立即生效设置） | `15-switch.html` |
| 头像 / 品牌 logo / 多人组 | `16-avatar.html` |
| 站内横幅（公告 / 营销 / 警告） | `17-banner.html` |
| **电量 / 进度 / 多步加载** | `18-progress.html` 🆕 |
| **大标题 / 数字大字 / 字组** | `19-typography.html` 🆕 |
| **流程步骤 / 时间线 / 流程图** | `20-steps.html` 🆕 |
| **筛选（顶部 Chip / Sheet / Modal）** | `21-filter.html` 🆕 |
| **品牌 Logo 网格 / 品牌列表** | `22-brand-grid.html` 🆕 |
| **排行榜 / Top3 高亮 / 条形榜** | `23-ranking.html` 🆕 |
| **收藏切换 / 角标 / 收藏 Tab** | `24-favorite.html` 🆕 |
| **页面底部 / 移动端 Tabbar** | `25-footer.html` 🆕 |
| 内容卡 / 文章卡 / 商品卡 / 品牌卡 | `cards/` |

---

## 📊 组件优先级矩阵

| 优先级 | 组件 | Figma 使用频次 | 通用化收益 |
|--------|------|----------------|-----------|
| **P0** | Button, Input, Tag, Tabbar, Badge, Modal, Toast, Top Nav, Progress, Steps, Typography | ≥80 次/组件 | 跨所有 UI 场景 |
| **P1** | Select, Checkbox, Radio, Switch, Loading, Empty State, Search, Avatar, Banner, Filter | 20-80 次/组件 | 多数场景必需 |
| **P2** | Brand Grid, Ranking, Favorite, Footer, Article Card, Product Card | 通用化后跨场景 | 业务模块化 |

---

## 🛠️ 如何扩展

每个 HTML 文件都是**单文件 reference**，含：
- 完整 CSS（CSS 变量驱动）
- 所有 variant 演示
- Spec 详情 + Token 映射
- 使用规则

要新增组件：
1. 复制一个现有 HTML 作为模板
2. 改类名前缀（如 `btn-` → `card-`）
3. 加你的 variant
4. 在本 README 加一行

---

## 📐 设计原则

所有组件遵守 [`../principles.md`](../principles.md)：
- ✅ ICON 走 Iconify 单源
- ✅ 颜色用 CSS 变量（**0 硬编码 hex**）
- ✅ 单文件自适应（PC ≥1024px / H5 <1024px）
- ✅ Token 引用 [`../tokens.md`](../tokens.md)

---

## 🔗 相关文档

- [`../tokens.md`](../tokens.md) — 设计变量
- [`../principles.md`](../principles.md) — 7 条跨线硬规则
- [`../demo/`](../demo/) — 完整生产页 demo
- [`../SKILL.md`](../SKILL.md) — AI 加载的 skill 入口

---

## 📋 维护记录

| 日期 | 变更 | 作者 |
|------|------|------|
| 2026-09-29 | v1.0 初版：从生产项目整理 | AI 起草，待 PM 审 |
| 2026-09-29 | v1.1 新增 8 组件 + 2 卡 · 扩展 3 组件 · 升级为 25+5 全场景覆盖 | Figma 3 文件盘点后增量 |