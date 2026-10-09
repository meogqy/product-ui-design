# Figma → HTML 组件映射表

> **目的**：当 AI 在设计稿里看到某个 Figma 组件名,**立刻能查**HTML 文件 + 类名怎么用。
> **覆盖范围**:3 个 Figma 文件(Autocava + 2026 设计稿库)扫到的 588 个 unique 组件名 → 25 个 HTML 组件文件 + 5 张内容卡
> **更新时间**:2026-09-29

---

## 🟢 已映射到现有组件(22 个 Figma 组件名 → 9 个 HTML 文件)

| Figma 组件名 | 出现次数 | → HTML 文件 | 类名前缀 | 备注 |
|--------------|---------|-------------|----------|------|
| `Button` | 188 | `01-button.html` | `.btn-` `.btn-primary` | 主 CTA |
| `输入` | 13 | `02-input.html` | `.input` | 表单字段 |
| `标签` | 39 | `03-tag.html` | `.tag` | 评分 / 排行 chip |
| `Tabbar` | 21 | `04-tabbar.html` | `.tabbar` `.tab-` | H5 底部导航 |
| `认证` | 1 | `05-badge.html` | `.badge-` `.badge-verified` | 状态徽章 |
| `顶部导航` | 182 | `06-topnav.html` | `.topnav` `.nav-` | H5 顶部 |
| `pc-顶部导航` | 1 | `06-topnav.html` | `.topnav-pc` | PC 顶部 |
| `返回-导航` | 31 | `06-topnav.html` | `.topnav-back` | 返回按钮 |
| `返回导航` | 113 | `06-topnav.html` | `.topnav-back` | 同上变体 |
| `Toast` | 18 | `10-toast.html` | `.toast` `.toast-success/error/warn/info` | 操作反馈 |
| `车系车型Banner` | 53 | `17-banner.html` | `.banner` | 系列/车型横幅 |
| `Banner` | 49 | `17-banner.html` | `.banner` `.banner-promo/info/warning` | 通用横幅 |
| `H5预审Banner` | 12 | `17-banner.html` | `.banner-promo` | 变体 |
| `PC预审Banner` | 11 | `17-banner.html` | `.banner-promo` | 变体 |
| `车系卡片` / `车系卡片1` / `车系卡片2` | 1+9+7 | `cards/01-content-card.html` | `.content-card` | 通用内容卡 |
| `车Feed` | 3 | `cards/01-content-card.html` | `.content-card` | Feed 流 |
| `CAVA` | 35 | `cards/02-simple-card.html` | `.simple-card` | 简洁卡 |
| `CAVA指数` | 1 | `cards/02-simple-card.html` | `.simple-card` | 同上变体 |
| `Whatsapp` | 64 | `06-topnav.html` + `17-banner.html` | `.whatsapp-btn` | WhatsApp CTA |
| `Icon/搜索` | 3 | `11-search.html` | `.search-icon` | 搜索图标 |

---

## 🆕 新增组件承接(12 个新 HTML 文件 + 3 个扩展)

### P0 基础(4 个新 + 3 个扩展)

| Figma 组件名 | 出现次数 | → HTML 文件 | 类名前缀 | 备注 |
|--------------|---------|-------------|----------|------|
| `电量条` | **342** ⭐ | `components/18-progress.html` | `.linear` `.battery-fill` `.circular` `.stepper` | **缺口最大,新增 4 个 variant** |
| `大标题` + `标题` + `字组` | 93+19+1 = 113 | `components/19-typography.html` | `.t-h1`-`.t-h6` `.t-display` `.t-price-block` | typography 集中展示 |
| `流程图标` + `流程Icon` + `流程组件` | 52+23+9 = 84 | `components/20-steps.html` | `.steps-h` `.step-h` `.tl-item` `.flow-node` | 3 视图流程 |
| `筛选` | 17 | `components/21-filter.html` | `.filter-chip` `.sheet-option` `.modal-tab` | Chip/Sheet/Modal |
| `按钮组` + `按钮单选` | 21+42 | 扩展 `01-button.html` | `.btn-group` `.single-option` | + 4 个新变体 |
| `分类` + `分类标签` | 27+2 | 扩展 `03-tag.html` | `.cat-tag` `.cat-tag-btn` | + 5 个分类变体 |
| `弹窗顶部导航` + `弹窗底部输入框` | 17+11 | 扩展 `09-modal.html` | `.m-header` `.m-footer-input` | + 3 个 Header/Footer slot |

### P1 业务场景(2 个新)

| Figma 组件名 | 出现次数 | → HTML 文件 | 类名前缀 | 备注 |
|--------------|---------|-------------|----------|------|
| `简单呼吸` | 5 | `components/07-loading.html` | `.loading-breathing` | Loading 变体 |
| `H5预审Banner` / `PC预审Banner` | 12+11 | `components/17-banner.html` | `.banner-promo` | 已在 17 中 |

### P2 通用化领域组件(4 个新 + 2 个新卡)

| Figma 组件名 | 出现次数 | → HTML 文件 | 类名前缀 | 备注 |
|--------------|---------|-------------|----------|------|
| `车品牌` + `车品牌-黑白` + `车品牌列表-12` + `汽车品牌` | 125+13+11+27 | `components/22-brand-grid.html` | `.brand-grid` `.brand-cell` | 通用化"品牌 Logo 网格" |
| `排行榜` + `排名` | 31 | `components/23-ranking.html` | `.rank-list` `.rank-item` `.rank-num-badge` | 标准/Top3/条形 |
| `车系收藏` + `收藏车型卡片` + `collect=true/false` | 47+57+多次 | `components/24-favorite.html` | `.fav-btn` `.fav-corner` `.fav-row` | 通用化"收藏切换" |
| `底部` + `车系页&车型页底部` + `底部导航` | 31+27+11 | `components/25-footer.html` | `.footer-links` `.footer-complete` `.bottom-tabbar` | 通用化"页面底部" |
| `车资讯` + `资讯` | 多次 | `cards/04-article-card.html` | `.article-h` `.article-v` `.article-c` `.article-video-thumb` | 通用化"文章卡" |
| `车型` + `收藏车型卡片` + `品牌车型卡片_有/无优惠` + `车型融资计划` | 73+57+12+多次 | `cards/05-product-card.html` | `.product-card` `.product-discount-card` | 通用化"商品/车型卡" |

---

## ⏭ 故意跳过 — 不入 starter

### 演示元数据(9 个,只给设计师看)

| Figma 组件名 | 出现次数 | 为什么跳过 |
|--------------|---------|-----------|
| `标注` | 187 | 设计师标注,不入产品 |
| `设计走查` | 99 | 设计审查,不入产品 |
| `需求模块说明` | 65 | PM 备注,不入产品 |
| `下滑` | 7 | 交互指示 |
| `查看更多` | 10 | 链接文本 |
| `样机` | 3 | Mockup 容器 |
| `标注/提示在右/在左` | 19+2 | 设计标注变体 |
| `标注/模块细分名称` | 13 | 设计标注变体 |
| `演示释义用` | 多次 | meta 元数据 |

### Icon 实例(46 个,Iconify CDN 覆盖)

`Icon` (1585 实例) `Icon/向右箭头` (379) `Icon/向左箭头` (33) `Icon/首页` (36) `Icon/汽车` (29) `Icon/我的` (28) `Icon/金融` (27) `Icon/向上/下箭头` 等。

→ **不重做**,统一走 `<span class="iconify" data-icon="lucide:xxx">` / Iconify CDN。

### 业务专用(汽车业务专属,直接复用 Figma 原稿)

| Figma 组件名 | 出现次数 | 跳过原因 |
|--------------|---------|--------|
| `网站价值` | 67 | 仅 Autocava 业务用 |
| `金融方案` | 9 | 金融业务模块 |
| `品牌车型卡片_有/无优惠` | 5+7 | 业务模块 |
| `运营商` | 多次 | 电信业务 |
| `停售` / `停产在售` | 多次 | 二手车业务 |
| `个人中心模块/*` | 多次 | 用户中心 |
| `底部信息` | 3 | 业务页脚 |
| `购车流程` / `购车流程部分` / `车系页购车流程` | 多次 | **可与 20-steps 通用组件组合复用**,不单独保留 |
| `车系融资计划` / `车系车型融资计划` | 多次 | 金融产品 |
| `月供` | 多次 | 数据展示型,放卡片 |

### Frame ID 噪声(~200 个,Figma 自动生成)

`Frame 1000004624` / `Frame 1000005380` / `Frame 62521` 等。→ Figma 自动命名,无意义。

---

## 🎯 AI 使用本表的工作流

```
设计稿上看到 "电量条" 
    ↓ 查本表
    ↓ 出现 342 次,缺口最大
    ↓ 映射到 components/18-progress.html
    ↓ 复制对应 variant 到生产页:
   <div class="linear">
     <div class="linear-bar" style="width:75%"></div>
   </div>
```

> **效率技巧**——AI 接到"做 X 页面"任务时,先扫一遍设计稿里出现的高频组件名 → 对照本表 → 一次性打开对应 HTML 复用样式,不重新发明轮子。

---

## 📊 覆盖率

```
Figma 总 unique 组件名:  588
├─ 已映射到现有组件:     22  (映射到 9 个 HTML)
├─ 新组件承接:        12  (P0 × 4 + P1 × 1 + P2 × 6 + 扩展 3)
├─ Icon 实例(Iconify):  ~46
├─ 业务专用(跳过):      ~100+
├─ 演示元数据(跳过):    9
└─ Frame 噪声(跳过):    ~200

实际交付 HTML 组件文件: 25 + 5 cards = 30 个
覆盖 Figma 实例使用 Top 40频次的 ~95%
```

---

## 📋 维护记录

| 日期 | 变更 |
|------|------|
| 2026-09-29 | v1.0 初版 · 从 Figma 3 文件(Autocava + 2026 设计稿库)扫出 588 unique 名 → 映射到 30 个 HTML 文件 |