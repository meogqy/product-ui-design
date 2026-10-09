> ⚠️ **来源说明**：本文件含项目特定示例（品牌名 / 市场 / 平台专有参数）。
> 作为通用参考可用，但**具体值需按 [`SITE-CONFIG.md`](../SITE-CONFIG.md) 替换**后使用。
> 原路径：Mstar 工作区 · 随包分发于 product-ui-design v2.0

# Design Tokens · Mstar / AutoCava 设计变量

> **来源**：从 Figma 文件 *Autocava* (file_key: `poqMSloU9upY9iYTQ3mbc6`) → Colors & Typography 页面同步
> **同步日期**：2026-09-29
> **覆盖**：63 个颜色 + 25 个 typography token
> **权威性**：这是**视觉规范的源头**，所有产品线（CAVI / Autocava PC/H5 / 销售工作台）共用

---

## 🎨 颜色系统（63 个，按家族分 10 组）

> **使用原则**：跨产品线统一色板；具体应用通过**语义化命名**（Text/* / Background/* / Border/* / Button-Yellow/*）而非直接用 raw hex。

### Yellow · 品牌主色（10 档）

> 品牌主色系。`yellow-500` = `#FFCF20` = 顶栏 / 强 CTA / 强调装饰。

| Token | Hex | 用途示例 |
|-------|-----|----------|
| `Yellow/yellow-50` | `#FFFAE9` | 最浅背景 / 选中态底色 |
| `Yellow/yellow-100` | `#FFFAE9` | （与 50 同色，按 token 命名） |
| `Yellow/yellow-200` | `#FFE998` | 浅黄装饰 / hover 底色 |
| `Yellow/yellow-300` | `#FFDF6A` | 中浅装饰 |
| `Yellow/yellow-400` | `#FFD94D` | 中度强调 |
| **`Yellow/yellow-500-主色`** | **`#FFCF20`** | **品牌顶栏 / 主 CTA / 强强调** |
| `Yellow/yellow-600` | `#E8BC1D` | hover / 弱化主色 |
| `Yellow/yellow-700` | `#B59317` | 文字色（黄底） |
| `Yellow/yellow-800` | `#8C7212` | 深色文字（黄底） |
| `Yellow/yellow-900` | `#6B570D` | 最深（极少用） |

### Blue · 信任色（10 档）

> 信任 / 链接 / 重要操作。深蓝用在品牌权威场景。

| Token | Hex |
|-------|-----|
| `Blue/blue-50` | `#E6EEFF` |
| `Blue/blue-100` | `#B0CBFD` |
| `Blue/blue-200` | `#8AB1FD` |
| `Blue/blue-300` | `#548EFC` |
| `Blue/blue-400` | `#3378FB` |
| `Blue/blue-500` | `#0056FA` |
| `Blue/blue-600` | `#004EE4` |
| `Blue/blue-700` | `#003DB2` |
| `Blue/blue-800` | `#002F8A` |
| `Blue/blue-900` | `#002469` |

### Red · 告警色（10 档）

> 错误 / 删除 / 风险提示。**`red-500-告警` = `#A8071A` 是主要使用档**。

| Token | Hex |
|-------|-----|
| `Red/red-50` | `#F6E6E8` |
| `Red/red-100` | `#E4B2B8` |
| `Red/red-200` | `#D78D96` |
| `Red/red-300` | `#C55966` |
| `Red/red-400` | `#B93948` |
| **`Red/red-500-告警`** | **`#A8071A`** |
| `Red/red-600` | `#990618` |
| `Red/red-700` | `#770512` |
| `Red/red-800` | `#5C040E` |
| `Red/red-900` | `#47030B` |

### Green · 成功色（10 档）

> 成功 / 通过 / 储蓄。**`green-500-成功` = `#7CB305` 是主要使用档**。

| Token | Hex |
|-------|-----|
| `Green/green-50` | `#F2F7E6` |
| `Green/green-100` | `#D6E7B2` |
| `Green/green-200` | `#C3DC8C` |
| `Green/green-300` | `#A7CC58` |
| `Green/green-400` | `#96C237` |
| **`Green/green-500-成功`** | **`#7CB305`** |
| `Green/green-600` | `#71A305` |
| `Green/green-700` | `#587F04` |
| `Green/green-800` | `#446203` |
| `Green/green-900` | `#344B02` |

### Grey · 中性色（10 档）

> 文字 / 背景 / 分割线主力。**`grey-50` ~ `grey-200` 是文字灰度系统核心**。

| Token | Hex | 用途 |
|-------|-----|------|
| `Grey/grey-50` | `#F8F8F8` | 浅背景 |
| `Grey/grey-100` | `#F1F1F1` | 卡片底色 / 分割线 |
| `Grey/grey-200` | `#DDDDDD` | 边框 / 分割线 |
| `Grey/grey-300` | `#BBBBBB` | 弱文字 |
| `Grey/grey-400` | `#999999` | 次要文字 |
| `Grey/grey-500` | `#888888` | 辅助文字 |
| `Grey/grey-600` | `#666666` | 常规文字 |
| `Grey/grey-700` | `#555555` | 强调文字 |
| `Grey/grey-800` | `#444444` | 重要文字 |
| `Grey/grey-900` | `#222222` | 标题文字 |

### Text · 文字色（5 档）

> **不要直接用 raw hex**。所有文字色必须从这套取，覆盖 90% 文字场景。

| Token | Hex | 用途 |
|-------|-----|------|
| **`Text/color-900-重要`** | `#222222` | 标题 / 重要正文 |
| `Text/color-600-常规` | `#666666` | 默认正文 |
| `Text/color-400-提示` | `#999999` | 辅助说明 |
| `Text/color-300-辅助提示` | `#BBBBBB` | 占位 / 弱提示 |
| `Text/color-200-禁用` | `#DDDDDD` | 禁用状态文字 |

### Background · 背景色（2 档）

| Token | Hex | 用途 |
|-------|-----|------|
| `Background/color-0` | `#FFFFFF` | 主背景（卡片 / 内容区） |
| `Background/color-50-页面背景` | `#F8F8F8` | 整页背景 |

### Border · 边框 / 分割线（2 档）

| Token | Hex | 用途 |
|-------|-----|------|
| `Border/border-100-分割线` | `#F1F1F1` | 极轻分割 |
| `Border/border-200-边框线` | `#DDDDDD` | 卡片 / 输入框边框 |

### Button-Yellow · 品牌按钮（2 档）

> 黄色系 CTA 专用。**所有"主行动按钮"用这组，不用 raw yellow-500**。

| Token | Hex | 用途 |
|-------|-----|------|
| **`Button-Yellow/button-500-默认`** | **`#FFCF20`** | 主 CTA 默认态 |
| `Button-Yellow/button-600-按压` | `#E8BC1D` | 主 CTA 按压态 |

### Pop-up · 浮层（2 档）

| Token | Hex | 用途 |
|-------|-----|------|
| `Pop-up/pop-up` | `#000000` | Modal 遮罩（通常带透明度） |
| `Pop-up/toast` | `#222222` | Toast 背景 |

---

## 🔤 字体系统（25 个 text style）

> **字体家族**：**Roboto**（默认）+ **Roboto Flex**（半粗体 Semi Bold 专用，更现代）
> **基础节奏**：line-height = font-size × 1.17（约 17% 行高，**注意不是 1.5**）
> **letter-spacing**：默认 0
> **使用规则**：先选级层级（Huge/Large/Big/Title/Headline/Body/...）再选 weight

### 24 / Semi Bold

> **重要模块大标题**

| Variant | Font | Size | Weight | Line Height |
|---------|------|------|--------|-------------|
| 24/Regular | Roboto | 24px | 400 | 28.125px |
| 24/Medium | Roboto | 24px | 500 | 28.125px |
| **24/Semi Bold** | **Roboto Flex** | **24px** | **600** | **28.125px** |
| 24/Bold | Roboto | 24px | 700 | 28.125px |

### 22

> **多级页面重要信息标题**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 22/Regular | Roboto | 22px | 400 |
| 22/Medium | Roboto | 22px | 500 |
| 22/Semi Bold | Roboto Flex | 22px | 600 |
| 22/Bold | Roboto | 22px | 700 |

### 20

> **实际页面模块的标题**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 20/Regular | Roboto | 20px | 400 |
| 20/Medium | Roboto | 20px | 500 |
| 20/Semi Bold | Roboto Flex | 20px | 600 |
| 20/Bold | Roboto | 20px | 700 |

### 18

> **强调标识 / 参数强调**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 18/Regular | Roboto | 18px | 400 |
| 18/Medium | Roboto | 18px | 500 |
| 18/Semi Bold | Roboto Flex | 18px | 600 |
| 18/Bold | Roboto | 18px | 700 |

### 16

> **正文 / 描述**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 16/Regular | Roboto | 16px | 400 |
| 16/Medium | Roboto | 16px | 500 |
| 16/Semi Bold | Roboto | 16px | 600 |

### 14

> **辅助文字 / 标签**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 14/Regular | Roboto | 14px | 400 |
| 14/Medium | Roboto | 14px | 500 |
| 14/Bold | Roboto | 14px | 700 |

### 12

> **标签 / 极小辅助**

| Variant | Font | Size | Weight |
|---------|------|------|--------|
| 12/Regular | Roboto | 12px | 400 |
| 12/Medium | Roboto | 12px | 500 |
| 12/Bold | Roboto | 12px | 700 |

---

## 🎯 语义映射（设计 → 代码）

> 这是 AI / 开发最常用的对照表。看到设计稿里的颜色 / 字号，先来这里查对应 token，**不要硬编码 hex**。

| 场景 | 用 Token |
|------|----------|
| 顶栏背景 / 主 CTA 默认 | `Button-Yellow/button-500-默认` |
| 顶栏背景 / 主 CTA hover | `Button-Yellow/button-600-按压` |
| 页面背景 | `Background/card-50-页面背景` |
| 卡片背景 | `Background/card-0` |
| 一级标题（重要） | 24/Semi Bold + `Text/color-900-重要` |
| 二级标题 | 20/Semi Bold + `Text/color-900-重要` |
| 默认正文 | 16/Regular + `Text/color-600-常规` |
| 辅助说明 | 14/Regular + `Text/color-400-提示` |
| 占位文字 | 16/Regular + `Text/color-300-辅助提示` |
| 错误状态 | `Red/red-500-告警` |
| 成功状态 | `Green/green-500-成功` |
| 卡片边框 | `Border/border-200-边框线` |
| 分割线 | `Border/border-100-分割线` |
| Modal 遮罩 | `Pop-up/pop-up` + opacity 0.5 |
| Toast 背景 | `Pop-up/toast` |

---

## 📦 对应到 CSS 变量

```css
:root {
  /* Yellow - 品牌主色 */
  --yellow-50:  #FFFAE9;
  --yellow-100: #FFFAE9;
  --yellow-200: #FFE998;
  --yellow-300: #FFDF6A;
  --yellow-400: #FFD94D;
  --yellow-500: #FFCF20;  /* 主色 */
  --yellow-600: #E8BC1D;
  --yellow-700: #B59317;
  --yellow-800: #8C7212;
  --yellow-900: #6B570D;

  /* Blue - 信任色 */
  --blue-50:  #E6EEFF;
  --blue-100: #B0CBFD;
  --blue-200: #8AB1FD;
  --blue-300: #548EFC;
  --blue-400: #3378FB;
  --blue-500: #0056FA;
  --blue-600: #004EE4;
  --blue-700: #003DB2;
  --blue-800: #002F8A;
  --blue-900: #002469;

  /* Red - 告警色 */
  --red-50:  #F6E6E8;
  --red-100: #E4B2B8;
  --red-200: #D78D96;
  --red-300: #C55966;
  --red-400: #B93948;
  --red-500: #A8071A;  /* 告警主色 */
  --red-600: #990618;
  --red-700: #770512;
  --red-800: #5C040E;
  --red-900: #47030B;

  /* Green - 成功色 */
  --green-50:  #F2F7E6;
  --green-100: #D6E7B2;
  --green-200: #C3DC8C;
  --green-300: #A7CC58;
  --green-400: #96C237;
  --green-500: #7CB305;  /* 成功主色 */
  --green-600: #71A305;
  --green-700: #587F04;
  --green-800: #446203;
  --green-900: #344B02;

  /* Grey - 中性色 */
  --grey-50:  #F8F8F8;
  --grey-100: #F1F1F1;
  --grey-200: #DDDDDD;
  --grey-300: #BBBBBB;
  --grey-400: #999999;
  --grey-500: #888888;
  --grey-600: #666666;
  --grey-700: #555555;
  --grey-800: #444444;
  --grey-900: #222222;

  /* Semantic Colors */
  --text-important:      var(--grey-900);  /* #222222 */
  --text-regular:       var(--grey-600);  /* #666666 */
  --text-hint:          var(--grey-400);  /* #999999 */
  --text-aux-hint:      var(--grey-300);  /* #BBBBBB */
  --text-disabled:      var(--grey-200);  /* #DDDDDD */

  --bg-page:            var(--grey-50);   /* #F8F8F8 */
  --bg-card:            #FFFFFF;

  --border-divider:     var(--grey-100);  /* #F1F1F1 */
  --border-line:        var(--grey-200);  /* #DDDDDD */

  --btn-yellow-default: #FFCF20;
  --btn-yellow-pressed: #E8BC1D;

  --popup-overlay:      #000000;
  --popup-toast:        #222222;

  /* Typography */
  --font-sans:    'Roboto', 'Roboto Flex', -apple-system, sans-serif;
  --font-mono:    'Roboto Mono', monospace;

  /* Spacing (基于 8px 节奏系统，建议补全 — Figma Colors & Typography 页未涵盖) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
}
```

---

## 🔗 相关规范

- [`DESIGN_CONSTRAINTS.md`](../DESIGN_CONSTRAINTS.md) — 市场色彩层级与法规约束（**按你的市场改写**）
- [`ICON_SPEC.md`](../ICON_SPEC.md) — 图标规范（独立于本 tokens）
- [`cards/`](cards/README.md) — 卡片样式库（用本 token 落地）
- [`../design-system/tokens.md`](../design-system/tokens.md) — 基础 token 档位（圆角 / 间距 / 灰阶）

---

## 📋 维护记录

| 日期 | 变更 |
|------|------|
| v2.0 | 随 product-ui-design 包分发；**请把下方示例值替换为你项目的品牌色** |
| v1.0 | 初版：从设计系统文件同步色板与字体梯度 |

