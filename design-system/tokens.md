# Design Tokens v3 · 生产环境真实值

> **来源**：`https://www.autocava.com.mx` **生产环境真实渲染 DOM + CDN CSS**
> **采集方式**：
> - 浏览器实测 DOM class（`bg-ffcf20` / `text-8c7212` 等 utility class）
> - CDN CSS 9 个文件（334 KB）解析 `--color-*` 自定义属性定义
> **采集时间**：2026-09-29 · Desktop + 移动 viewport · `ac_ab=stable`
> **技术栈**：Nuxt UI v3 底座 + **Tailwind utility class 直写 hex**（不走 oklch 色板）
>
> 📄 **v4 追加 · 报告线独立产品线**（`/auto/report/*`）——
> 权威源 `_reportNo_.v3.C-YtWLJM.css`（scoped，11,703 B），采集 2026-09-30。
> **报告线 ≠ 主站**：品牌黄 `#dcad00`（非 `#FFCF20`）、字体 Roboto（MiSans 是未加载的死声明）、圆角主档 `10px`（非 4/6/8/12）。
> 详见 [📄 报告线 Tokens](#-报告线-tokens-autoreport--独立产品线)。

---

## ⚠️ v1 / v2 修订说明

| 版本 | 内容 | 状态 |
|------|------|------|
| v1 | Yellow 品牌期推测值（60 色） | ⚠️ 主色对，但**中性色和语义色是推测的**，命名与生产站不一致 |
| v2 | 误判为 Green primary（Nuxt UI 默认色板） | ❌ **已废弃** — 把框架未启用的默认色板当成了品牌色 |
| **v3** | **生产 DOM class + CSS 变量实测** | ✅ **权威** |

**v2 错在哪**：Nuxt UI 框架预置了完整的 `--color-green-*` / `--color-slate-*` 色板，但 Autocava 实际用 Tailwind utility class 直写 hex（`bg-ffcf20`），**根本没启用那套色板**。我看到变量定义就断定主色，犯了一个基础错误。

**v3 原则**：只看**真实渲染 DOM 的 class** 和**CSS 里的实际定义**，不看框架默认。

---

## 🎨 真实色板（15 色 · 全部实测）

> 这些是生产站 CSS 里**真实定义且被实际使用**的颜色，按使用频次排序。

### 🟡 Yellow · 品牌主色（7 色）

| CSS 变量 | Hex | 频次 | 用途 |
|----------|-----|------|------|
| `--color-ffcf20` | **`#FFCF20`** | **bg × 26** | **品牌主色** · 导航底 · 主 CTA · Buscar 按钮 |
| `--color-8c7212` | **`#8C7212`** | **text × 66** | **黄底上的强调文字**（白底上 4.63:1 ✅）|
| `--color-e0a504` | `#E0A504` | text × 19 | 黄底 hover / 强调文字 |
| `--color-b59317` | `#B59317` | text × 19 | 黄底次要文字 |
| `--color-744500` | `#744500` | 备用 | 深黄（黄底上的强对比）|
| `--color-ffc422` | `#FFC422` | 1 | `--color-primary` 的 fallback 值 |
| `--color-fffaed` | `#FFFAED` | 备用 | 极浅黄底 |
| `--color-fff6dc` | `#FFF6DC` | 备用 | 浅黄底（提示区）|
| `--color-ffd04e` | `#FFD04E` | 备用 | 中浅黄装饰 |

### ⚪ Neutral · 中性色（6 色）

| CSS 变量 | Hex | 频次 | 用途 |
|----------|-----|------|------|
| `--color-222` | **`#222222`** | **text × 114** | **正文主色**（全站最高频）|
| `--color-666` | `#666666` | text × 62 | 次要正文 |
| `--color-999` | `#999999` | text × 51 | 辅助 / 占位文字 |
| `--color-ddd` | `#DDDDDD` | bg × 1 / text × 4 | 边框 / 分割线 |
| `--color-f1` | `#F1F1F1` | CSS 已定义 | 浅灰底 / hover 背景 |
| `--color-f5` | `#F5F5F5` | CSS 已定义 | 更浅灰底 |
| `--color-f8` | `#F8F8F8` | CSS 已定义 | 浅灰底 |
| `--color-f0` | `#F0F0F0` | CSS 已定义 | 浅灰底 |
| `--color-e1` | `#E1E1E1` | CSS 已定义 | 极浅边框 |
| `--color-e6` | `#E6E6E6` | CSS 已定义 | 浅边框 |
| `--color-fff` | **`#FFFFFF`** | **bg × 13** | 卡片 / 内容区背景 |
| `--color-000` / `--color-black` | `#000000` | CSS 已定义 | 纯黑（极少用）|

### 🟠 状态色（生产 CSS 已定义）

| CSS 变量 | Hex | 说明 |
|----------|-----|------|
| `--color-error` | `#A8071A` | 错误 |
| `--color-success` | `#5CCD31` | 成功 |
| `--color-warning` | `#B00E16` | 警告 |
| `--color-orange` | `#FA4D02` | 强调橙 |

> 📌 **页面底色**：生产站主要用 `#FFF` + `#F1F1F1`/`#F5F5F5` 分层，靠边框和底色差而非阴影。

---

## 🔤 字体系统（生产真实值）

```css
/* 来自 CSS 的 --font-sans / --font-mono 实际定义 */
--font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
             "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
```

**字重**（CSS 实测）：
```
400 normal · 500 medium · 600 semibold · 700 bold · 800 extrabold · 900 black
```

**生产站实际用到的字号**（从 DOM class 反查 Tailwind scale）：

| 类名 | px | 用途 |
|------|-----|------|
| `text-xs` | 12 | 标签 / 辅助 |
| `text-sm` | 14 | **正文主力** |
| `text-base` | 16 | 强调正文 |
| `text-lg` | 18 | 卡片标题 |
| `text-xl` | 20 | 区块标题 |
| `text-2xl` | 24 | 大标题 |
| `text-3xl` | 30 | Hero 标题 |

**导航高度**（实测）：移动 `h-14` = 56px · 桌面 `h-16.5` = 66px

---

## 📐 尺度（CSS 实测）

```css
--spacing: .25rem;    /* 4px 基准 */
--ui-radius: .25rem;  /* 4px 基准圆角 */
```

**圆角**（生产站实际 class）：`rounded-md`（6px）· `rounded-lg`（8px）· `rounded-full`（胶囊）

---

## 🎯 语义映射（对齐生产站实际用法）

### 导航栏（实测 `bg-ffcf20` + `text-222`）

```css
.topnav {
  background: var(--color-ffcf20);   /* #FFCF20 */
  color: var(--color-222);           /* #222222 */
}
.topnav-link { color: #222; font-weight: 400; }
.topnav-link[data-active] { font-weight: 700; }
.topnav-link::after { background: #FFCF20; }  /* 激活下划线 */
```

### 主 CTA（实测 `bg-ffcf20` + `text-222`）

```css
.btn-primary {
  background: #FFCF20;
  color: #222222;
  font-weight: 600;
}
.btn-primary:hover { background: #E0A504; }  /* 生产站 hover 用这个 */
.btn-primary:active { background: #B59317; }
```

> ⚠️ **关键**：黄底配的是 **#222 深字**，不是白字。白字在 `#FFCF20` 上只有 **1.6:1**，完全不达标。

### 文字层级

| 用途 | Token | Hex | 频次 |
|------|-------|-----|------|
| **正文** | `--color-222` | `#222222` | 114 |
| 次要正文 | `--color-666` | `#666666` | 62 |
| 辅助 / 占位 | `--color-999` | `#999999` | 51 |
| 黄底正文 | `--color-8c7212` | `#8C7212` | 66 |
| 黄底强调 | `--color-e0a504` | `#E0A504` | 19 |

### 表面

| 用途 | Token | Hex |
|------|-------|-----|
| 卡片 / 内容底 | `--color-fff` | `#FFFFFF` |
| 品牌底 | `--color-ffcf20` | `#FFCF20` |
| 边框 / 分割 | `--color-ddd` | `#DDDDDD` |
| 浅黄提示底 | `--color-fff6dc` | `#FFF6DC` |
| 极浅黄底 | `--color-fffaed` | `#FFFAED` |

---

## 📋 WCAG AA 对比度速查（精确计算）

| 组合 | 对比度 | 达标 |
|------|--------|------|
| **`#222` on `#FFCF20`（生产站主 CTA）** | **10.76:1** | ✅ AAA |
| **`#222` on `#FFCF20`（黄底正文 · 实际方案）** | **10.76:1** | ✅ AAA |
| `#744500` on `#FFCF20` | 5.47:1 | ✅ AA |
| `#8C7212` on `#FFFFFF` | 4.63:1 | ✅ AA |
| `#222` on `#FFF6DC` | 14.75:1 | ✅ AAA |
| `#222` on `#FFFFFF` | 15.91:1 | ✅ AAA |
| `#666` on `#FFFFFF` | 5.74:1 | ✅ AA |
| `#8C7212` on `#FFCF20` | 3.13:1 | ⚠️ 仅大字 |
| `#999` on `#FFFFFF` | 2.85:1 | ⚠️ 仅占位/大字 |
| `#B59317` on `#FFCF20` | 1.99:1 | ❌ 装饰专用 |
| `#E0A504` on `#FFCF20` | 1.49:1 | ❌ 装饰专用 |
| **`#FFFFFF` on `#FFCF20`** | **1.48:1** | ❌ **绝对禁用** |

> 🚨 **黄底绝对不能用白字**（1.48:1）。这是本设计系统最容易翻车的点。
> ✅ **正确做法**：黄底一律配 `#222222`（10.76:1），这是生产站实际方案。

---

## 🧩 直接可用的 CSS 变量块

```css
:root {
  /* 🟡 Yellow 品牌主色（生产真实值）*/
  --yellow-500:#FFCF20;   /* 品牌主色 · 导航底 · 主 CTA */
  --yellow-600:#E0A504;   /* hover */
  --yellow-700:#B59317;   /* active / 黄底次要文字 */
  --yellow-800:#8C7212;   /* 黄底正文色 */
  --yellow-900:#744500;   /* 深黄 */
  --yellow-400:#FFD04E;   /* 浅黄装饰 */
  --yellow-100:#FFF6DC;   /* 浅黄底 */
  --yellow-50:#FFFAED;    /* 极浅黄底 */
  --primary-fallback:#FFC422;  /* --color-primary 的 fallback */

  /* ⚪ Neutral（生产真实值）*/
  --text:#222222;         /* 正文主色 · 最高频 */
  --text-secondary:#666666;
  --text-hint:#999999;
  --border:#DDDDDD;
  --border-light:#E6E6E6;
  --border-lighter:#E1E1E1;
  --bg:#FFFFFF;
  --bg-grey-1:#F8F8F8;    /* 浅灰底 */
  --bg-grey-2:#F5F5F5;
  --bg-grey-3:#F1F1F1;    /* hover 背景 */
  --bg-grey-4:#F0F0F0;
  --black:#000000;
  /* 🟠 状态色（生产 CSS 真实定义）*/
  --red-500:#A8071A;      /* --color-error */
  --green-500:#5CCD31;    /* --color-success */
  --orange-500:#FA4D02;   /* --color-orange */
  --red-700:#B00E16;      /* --color-warning */

  /* 语义别名 */
  --text-important:var(--text);
  --text-regular:var(--text-secondary);
  --text-aux:var(--text-hint);
  --text-on-yellow:var(--text);         /* 黄底上的正文 = #222（10.76:1）*/
  --bg-page:var(--bg);
  --bg-card:var(--bg);
  --border-divider:var(--border);
  --border-line:var(--border);
  --btn-primary:var(--yellow-500);
  --btn-primary-press:var(--yellow-700);
  --primary-500:var(--yellow-500);
  --primary-600:var(--yellow-600);
  --primary-700:var(--yellow-700);
  --primary-800:var(--yellow-800);
  --neutral-50:var(--bg);
  --neutral-200:var(--border);
  --neutral-400:var(--text-hint);
  --neutral-600:var(--text-secondary);
  --neutral-900:var(--text);

  /* ⚪ 组件库命名别名（components/ 全部用 --grey-*，勿删）
     ⚠️ 这套是 component reference 的事实变量名；上面的 --neutral-* 是语义层。
        两套并存：删掉 --grey-* 会让 8+ 个组件的 var() 失效（整条声明被丢弃） */
  --grey-50:#F8F8F8;
  --grey-100:#F1F1F1;
  --grey-200:#DDDDDD;
  --grey-300:#BBBBBB;
  --grey-400:#999999;
  --grey-600:#666666;
  --grey-700:#555555;   /* 次级正文 · 组件高频用 */
  --grey-900:#222222;
  --white:#FFFFFF;

  /* 组件库状态色别名 */
  --blue-500:#0056FA;
  --blue-50:#E6EEFF;
  --red-500:#A8071A;
  --red-50:#F6E6E8;
  --green-500:#7CB305;

  /* 组件库间距别名（4px 基数）*/
  --space-2:8px;
  --space-3:12px;
  --space-4:16px;
  --space-5:20px;
  --space-6:24px;

  /* 字体 */
  --font-sans:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --font-mono:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;

  /* 尺度 */
  --spacing:.25rem; --ui-radius:.25rem;
  --r-sm:4px; --r-md:6px; --r-lg:8px; --r-xl:12px; --r-full:9999px;
  --shadow-card:0 1px 3px rgba(0,0,0,.08);
  --header-h:56px;  /* 移动 56px / 桌面 66px */
}
```

---

# 📄 报告线 Tokens（`/auto/report/*`）· 独立产品线

> **来源**：`https://www.autocava.com.mx/auto/report/series/356/2ea7e75d9c9a4dd6b0ce75d64e6e5893`
> **权威 CSS**：`cdn.autocava.com.mx/_nuxt/asset/_reportNo_.v3.C-YtWLJM.css`（11,703 B · scoped）
> **采集**：2026-09-30 · PC（1440）+ H5（390）双视口 · `ac_ab=stable`
> **⛔ 采集时该页面【没有】反馈模块**（`report-feedback` 0 次）→ 反馈模块属 **C 档自拟**，见 §报告线未定义项

## ⚠️ 报告线 ≠ 主站（最常见的翻车点）

| 维度 | 主站（`/` `/auto/series` `/rank`） | **报告线（`/auto/report/*`）** |
|------|-------------------------------|-------------------------------|
| 品牌黄 | **`#FFCF20`** | **`#dcad00`**（暗一档，金调） |
| 第二金 | `#8C7212`（黄底文字） | **`#B59317`**（章节副标题 / VS 徽章） |
| 字体 | 系统栈（不加载 Web Font） | **Roboto + 系统栈**（加载 Roboto；CSS 里的 `MiSans` 是无 `@font-face` 的死声明）|
| 卡片圆角 | `4/6/8/12` | **`10px` 为主档** |
| 阴影 | 阴影层级多档 | **只有 1 档** `0 0 16px #0000000d` |
| 章节标题 | — | `18px`(H5) → **`32px`**(PC)，**line-height 恒为 24px** |
| 图标 | Iconify CDN | Iconify CDN（一致）|

> 🚫 **把主站 token 灌进报告 = 视觉不一致**。报告用 `#FFCF20` 会比线上明显偏亮偏冷。
> 🚫 **报告页要加载 Roboto**（主站不加载）——反了会掉字。
> 🚫 **不要加 MiSans**：它只有 `font-family` 声明、没有 `@font-face`，线上实际回退 `sans-serif`。

## 🎨 报告线真实色板（30 hex · 全部实测）

### 品牌 & 强调

| Hex | 频次 | 用途（来自选择器）|
|-----|------|------------------|
| **`#dcad00`** | x2 | **报告线品牌黄** · `.subtitle` Hero 副标题 · `.selling-bar` 卖点竖条 |
| **`#B59317`** | **x4** | 报告线第 2 金 · `.sec-sub` 章节副标题 · `.cc-box.adv` 优势标签 · `.vs-badge` VS 徽章底 |
| `#B8921A` | x1 | `.cc-bullet` 优势 bullet 文字 |
| `#FFC4221A` | x1 | 黄 10% 透明底 · `.cc-box.adv` 优势框 |
| `#0A1F33` | x1 | `.hero-pc .score-num` 深 navy 分数 |
| `#1A1F2A` | x1 | `.text-cost` 成本文字（比 `#222` 略冷）|

### 中性

| Hex | 频次 | 用途 |
|-----|------|------|
| **`#999`** | **x4** | 最高频 · `.tag-label` · `.axis-title` |
| `#222` | x3 | 正文 · `.trend-tip` |
| `#666` | x2 | 次要文字 · `.legend-item` |
| **`#F1F1F1`** | x2 | **`--color-f1` 卡片边框**（不是 `#DDD`！）|
| `#DDD` | x2 | 轮播点 · `.cava-badge` 徽章边框 |
| `#E5E8ED` | x2 | `.cc-foot` 虚线 · `.dim-track` 评分轨道底 |
| `#D1D1D1` | x1 | `.divider` header 竖分隔线 |
| `#F8F8F8` | x2 | 轮播点底 · 浅底 |
| `#FAFBFD` | x1 | `.warranty-item` 保修项底 |
| `#718096` | x1 | `.con-bullet` 劣势 bullet 灰 |

### 语义色

| Hex | 用途 |
|-----|------|
| `#059669` x3 | 绿 · `.sec-sub` · `.bar` 成本竖条 · `.card-installment` 边框（`#0596694D` = 30%）|
| `#F8FAF8` x2 | 绿底 · `.cost-inner` · `.card-installment` |
| `#00D142` x2 | 理想车型绿 · `.card.ideal` 边框（`color-mix` 30%）|
| `#1D4ED8` x2 | 蓝 · `.sec-sub` · `.bar` 口碑竖条 |
| `#0056FA` x2 | 亮蓝 · `.dec-label` 决策标签 · `.dim-fill` 评分条 |
| `#F3F8FF` | 蓝底 · `.network` · `.score-box` |
| `#FFF3F1` | 红底 · `.cc-box.con` 劣势框 |
| `#FA4D02` | 红字 · `.con-l` 劣势标签 |

### 图表 & Logo

| 值 | 用途 |
|----|------|
| `#FF7F48` | `.legend-consult` 走势图例「咨询价」|
| `#05DF72` | `.legend-avg` 走势图例「均价」|
| `linear-gradient(90deg, #0090FF -30.08%, #6000FF 4.81%, #DF00FF 48.96%, #FF007E, #FF5E00 118.03%)` | `.slogan` logo 渐变文字 |

## 🔤 报告线字体（**只加载 Roboto**，别被 MiSans 骗了）

```css
--font-report: "Roboto", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif;
```

> 🪤 **MiSans 是生产代码里的死声明** ——
> scoped CSS 里有 `font-family:MiSans,sans-serif`（`.score-num` / `.score-suffix` / `.kpi-unit`），
> 但**全站唯一的 `@font-face` 只定义了 Roboto**（`_nuxt/lib/google-fonts.css`）。
> 浏览器找不到 MiSans → **实际回退到 `sans-serif`**。
>
> ✅ **忠实复刻 = 只用 Roboto + 系统栈**。加 MiSans 会引入线上根本没有的字重和字形，比不加更不像。
> ⚠️ 看到 `font-family: X` 不等于 X 被加载了 —— **必须同时查 `@font-face`**，这是字体类 token 最常见的误判。

## 📐 报告线圆角（12 种实测 · **主档 10px**）

| 值 | 用途 |
|----|------|
| `2px` | `.selling-bar` / `.bar` 竖条 |
| `3px` | `.dim-track` / `.dim-fill` 评分轨道 |
| `4px` | `.trend-pill` 走势标签 |
| `6px` | `.warranty-item` · `.cc-img` · `.cc-box` · H5 `.big-img` |
| **`10px`** | **主档**：`.card` · `.kpi-bar` · `.cost-inner` · `.network` · `.score-box` · PC `.big-img` · PC `.cava-badge` |
| `0 10px` | `.recommend` / `.cmp-label` 右上角标签 |
| `16px` | `.share-panel`(PC) |
| `16px 16px 0 0` | 分享弹层（H5 底部弹出）|
| `50%` | `.vs-badge` · `.ch-icon` |
| `9999px` | `.dot` 轮播点 |
| `5.717px` | H5 `.cava-badge`（**生产怪值，勿抄**）|

> 📌 PC 下 `.card`（口碑卡）会 `border-top-left-radius:0; border-top-right-radius:0` 贴合上方容器。

## 🔠 报告线字号阶梯（H5 → PC）

| 角色 | H5 | PC（≥1024px）|
|------|----|------------|
| Hero 主标题 | lh 35px | **50px / 59px** |
| Hero 副标题 | lh 21px | **26px / 30px**（色 `#dcad00`）|
| **章节标题** | 18px / 24px | **32px / 24px** ⚠️ **字号变、行高不变** |
| 章节标签 | 16px / 16px | 16px |
| Hero CAVI 分 | 18px / 16px | 28px / 28px |
| 评分后缀 | 7.15px / 11px | 12.5px / 19px |
| 口碑评分 | 34px | **44px** |
| 经销商数 | 40px | 40px |
| 月供成本 | 28px / 37px | 28px / 37px |
| 价格数字 | 18px / 21px | 18px / 21px |
| 场景标题 | 20px | 26px |
| 场景描述 | 16px | 20px |
| 标签 | 13px / 15px | — |
| 走势提示 | 12px / 18px | — |
| 走势标签 | 11.5px / 13px | — |
| 方案名 / 金额 | 12px / 20px | **11px / 14px** |
| 方案后缀 | 10px / 14px | **9px** |
| 正文小字 | 10px / 14px | 10px / 14px |
| 日期 | 11px / 15px | — |
| 图例 | 10.5px / 16px | — |
| 分享标题 | 18px / 18px | — |
| 分享副文 | 12px / 16px | — |
| 渠道名 / 说明 | 12px / 14px · 10px / 12px | — |

> ⚠️ **`.sec-title` PC 行高不随字号变**（32px 字压 24px 行高）——这是生产实测值，不是笔误。

## 📐 报告线布局（PC · gap 统一 `16px`）

| 选择器 | 网格 |
|--------|------|
| `.main-grid` | `440px 1fr` |
| `.top-row` | `350px 350px 1fr` |
| `.bot-row` | `1fr 466px` |
| `.plan-row` | `repeat(3,1fr)`，`.card{max-width:237px}` |
| `.trend-card` | `min-height:345px` → PC `413px` |
| Hero | `.hero-text{width:418px}` · `.big-img{547×365}` · `.small-col{191×365, gap:10.94px}` |

## 🌑 报告线阴影（唯一一档）

```css
--shadow-report: 0 0 16px rgba(0,0,0,0.05);  /* = #0000000D，实测 .kpi-bar */
```

## 🧩 报告线 CSS 变量块（直接可用）

```css
:root {
  /* 🟡 品牌金（报告线专属，不是主站的 #FFCF20）*/
  --rp-yellow:#DCAD00;      /* 品牌黄 · Hero 副标题 · 卖点竖条 */
  --rp-gold:#B59317;        /* 第 2 金 · 章节副标题 · VS 徽章 */
  --rp-gold-text:#B8921A;   /* 优势 bullet 文字 */
  --rp-yellow-a10:#FFC4221A;/* 黄 10% 透明底 · 优势框 */

  /* ⚪ 中性 */
  --rp-text:#222;
  --rp-text-2:#666;
  --rp-text-3:#999;
  --rp-text-4:#718096;
  --rp-text-5:#1A1F2A;
  --rp-navy:#0A1F33;
  --rp-line:#F1F1F1;        /* 卡片边框（--color-f1）*/
  --rp-line-2:#E5E8ED;      /* 虚线 · 评分轨道 */
  --rp-line-3:#DDD;         /* 徽章边框 · 轮播点 */
  --rp-line-4:#D1D1D1;      /* header 竖线 */
  --rp-bg-grey:#F8F8F8;
  --rp-bg-grey-2:#FAFBFD;

  /* 🟢 绿 */
  --rp-green:#059669;
  --rp-green-soft:#F8FAF8;
  --rp-green-border:rgba(5,150,105,.3);   /* = #0596694D */
  --rp-green-ideal:#00D142;

  /* 🔵 蓝 */
  --rp-blue:#1D4ED8;
  --rp-blue-bar:#0056FA;
  --rp-blue-soft:#F3F8FF;

  /* 🔴 红（劣势）*/
  --rp-red-soft:#FFF3F1;
  --rp-red-text:#FA4D02;

  /* 📊 图表 */
  --rp-chart-consult:#FF7F48;
  --rp-chart-avg:#05DF72;

  /* 🔤 字体（只加载 Roboto；MiSans 是无 @font-face 的死声明，别加）*/
  --rp-font:"Roboto",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;

  /* 📐 尺度（主档 10px，不是主站的 4/6/8/12）*/
  --rp-r-xs:3px;  --rp-r-sm:6px;  --rp-r-md:10px;
  --rp-r-lg:16px; --rp-r-full:9999px;
  --rp-gap:16px;
  --rp-shadow:0 0 16px rgba(0,0,0,.05);
}
```

## 🚧 报告线未定义项（C 档自拟需标注）

采集时线上报告**不存在**以下模块 —— 属于本地新增，**必须显式标注为自拟**：

- ❌ 报告价值反馈模块（`report-feedback` / `helped` / `wantMore` / `freeText`）
- ❌ PC 右侧悬浮 dock / H5 粘性底栏

> 允许自拟，但 **token 必须取自上面的报告线色板**，不许借用主站 `#FFCF20` 或主站圆角档。

---

## 🔗 采集产物（可复核）

| 文件 | 内容 |
|------|------|
| `_source/production-snapshot/nuxt-ui-colors.css` | `<style id="nuxt-ui-colors">` 原始块（框架默认色板，**未启用**，仅存档）|
| `_source/production-snapshot/SOURCE.md` | 采集步骤 + 复现命令 |
| `_source/production-snapshot/oklch2hex.py` | 色彩转换脚本（供参考，本版未用到）|

### 复现方式

```bash
# 1. 抓 HTML
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..." \
  "https://www.autocava.com.mx" -o ac.html

# 2. 抓 CSS（从 HTML 里提取 link href）
grep -oE 'https://cdn\.autocava\.com\.mx/_nuxt/asset/[a-zA-Z]+\.v3\.[A-Za-z0-9]+\.css' ac.html | \
  xargs -I{} curl -s {} -o "$(basename {})"

# 3. 提取生产真实色（关键：只看 --color-<短名>）
grep -oE '\-\-color-[0-9a-f]{3,6}\s*:\s*#[0-9a-f]{3,6}' *.css

# 4. 统计真实使用频次
grep -oE '\b(bg|text)-[0-9a-f]{6}\b' ac.html | sort | uniq -c | sort -rn
```

> ⚠️ **不要用 `<style id="nuxt-ui-colors">` 里的色板** — 那是 Nuxt UI 框架预置，Autocava 未启用。

---

## 📋 维护记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-09-29 | v1.0 | 从旧 Mstar `visual-specs/` 抽取（Yellow 品牌期推测值）· 主色正确但中性色为推测 |
| 2026-09-29 | v2.0 | ❌ 误判为 Green primary（把 Nuxt UI 框架默认色板当品牌色）· 已废弃 |
| 2026-09-29 | **v3.0** | ✅ **浏览器实测 DOM class + CSS 变量** · Yellow `#FFCF20` 确认 · 15 个真实色 + 完整使用频次 · 新增 WCAG 实测表 + 复现步骤 |
| 2026-09-30 | v3.1 | ✅ **30 个组件文件批量同步** · `--yellow-600` → `#E0A504`（22 处）· 字体统一生产系统栈（22 文件）· `#E8BC1D` → `#E0A504`（7 处）· `#FFFAE9` → `#FFFAED`（14 处，生产真实值是 `fffaed` 不是 `fffae9`）· 补全生产 CSS 里另 5 个灰阶（`#F0F0F0` `#F1F1F1` `#F5F5F5` `#E1E1E1` `#E6E6E6`）+ 4 个状态色（`#A8071A` `#5CCD31` `#FA4D02` `#B00E16`）|
| 2026-09-30 | **v4.0** | 📄 **新增「报告线」独立产品线整节**（`_reportNo_.v3.C-YtWLJM.css` 11,703 B 实测）· 30 hex 色板 · 品牌黄 `#dcad00`（≠ 主站 `#FFCF20`）· 字体 Roboto + 系统栈（≠ 纯系统栈；MiSans 是死声明）· 圆角主档 `10px`（≠ 4/6/8/12）· H5→PC 字号阶梯（含 `sec-title` 32px/24px 行高不变的生产怪值）· 5 组 PC 网格 · 唯一阴影档 · 标注反馈模块为 **C 档自拟（线上无此模块）** |
