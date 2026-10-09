---
name: product-ui-design
description: 设计任何产品页面的 UI（首页 / 详情页 / 列表页 / 表单页 / 看板 等真实生产页面，不是演示原型）。本 skill 强制使用 tokens 设计变量、复用已有组件、复用真实平台数据、生产可达性（WCAG AA / Core Web Vitals）、响应式断点（≥1024px PC / <1024px H5）。区别于 product-prototype-design（演示原型 skill / 单 feature 测试用 / mock 数据 OK / 评审通过即可）。当用户给出"做产品页 / 上线页 / 用现有组件库 / 接真实数据 / WCAG / Core Web Vitals"任一信号时自动加载。
version: 1.1
disable-model-invocation: false
triggers:
  - "设计产品页面"
  - "上线页面"
  - "真实页面"
  - "production"
  - "用现有组件"
  - "复用组件库"
  - "组件库"
  - "ui-design-system"
  - "ui-design-system-starter"
  - "做 UI"
  - "做产品 UI"
source_documents:
  - ./tokens.md
  - ./principles.md
  - ./components/README.md
  - ./components/cards/README.md
  - ./recipes/README.md
  - ./FIGMA_MAP.md
  - ./gallery.html
related_skills:
  - product-prototype-design
entry_points:
  - ./gallery.html          # 一页总览所有 30 组件 + 4 recipes
  - ./components/README.md  # 组件索引 + 场景选型表
  - ./recipes/README.md  # 4 个组合 pattern
  - ./FIGMA_MAP.md        # Figma 588 → HTML 映射
---

# 产品页面 UI 设计 Skill v1.0

> **本 skill 用于设计要真实上线给用户用的产品页面**，不是演示原型。
>
> | 用途 | 用哪个 skill |
> |------|-------------|
> | 单 feature 演示 / 老板评审 / mock 数据 | `product-prototype-design`（演示原型 skill） |
> | 真实生产页面 / 平台组件集成 / 上线 | **本 skill**（产品页面 UI 设计 skill） |

---

## ⛔ 加载后第一步：判断这次是不是真的生产 UI

| 是生产 UI（用本 skill） | 不是生产 UI（用 `product-prototype-design`） |
|------------------------|------------------------------------------|
| 用户在真实产品里看到的页面 | 单 feature demo 给老板 / PM 评审 |
| 需要接真实数据 | mock / lorem / 占位数据 OK |
| 必须复用本目录已有组件 | 可以自创新样式 |
| 要过 WCAG AA + Core Web Vitals | demo 评审通过即可 |
| 走真实环境分流 | 不强制环境分流 |

> 判断错了 → 重新选 skill，**别混用**。

---

## 🧭 生产 UI 设计 5 步

### Step 1：定位是哪个真实页面

- 是首页 / 详情页 / 列表页 / 表单页 / 后台看板 …？
- **确认页面归属的产品线 → 决定走哪份 token**（见下表，**走错会整页返工**）
- 写下"入口 → 交付 → 闭环"（参考 [`principles.md` §产物方法论](./principles.md)）

#### 🚦 产品线分流（必查，选错直接翻车）

| 页面路径 | 产品线 | 品牌黄 | 字体 | 卡片圆角 | token 来源 |
|---------|--------|--------|------|---------|-----------|
| `/` · `/auto/series/*` · `/auto/library` · `/rank` · `/finance/*` | **主站** | **`#FFCF20`** | 系统栈（不加载 Web Font）| `4/6/8/12` | [`tokens.md` §真实色板](./tokens.md) |
| **`/auto/report/*`**（购车指南报告）| **报告线** | **`#dcad00`** | **MiSans + Roboto** | **`10px`** 主档 | [`tokens.md` §报告线 Tokens](./tokens.md) |

**判断方法**：路径里有没有 `/auto/report/`。
- 有 → 报告线，走 `--rp-*` 变量
- 没有 → 主站，走 `--yellow-*` / `--text-*` 变量

> ⛔ **跨线借用 = 视觉不一致**。给报告页灌 `#FFCF20` 会明显偏亮偏冷；给主站灌 `10px` 圆角会偏圆。
> ⛔ **主站不加载 Web Font，报告线要加载** —— 反过来做会导致中文掉字回退。

### Step 2：复用视觉资产，不要造轮子

**⚡ 第一步必做（5 个查表路径））**：
- 查 [`gallery.html`](./gallery.html) — 一页总览所有 30 组件 + 4 recipes,快速定位用什么
- 查 [`components/README.md`](./components/README.md) — 组件索引 + 场景选型表 + 优先级矩阵
- 查 [`recipes/`](./recipes/README.md) — 4 个组合 pattern(反馈流 / 进度流 / 发现流 / 内容卡)
- 查 [`FIGMA_MAP.md`](./FIGMA_MAP.md) — Figma 588 组件名 → HTML 文件映射
- 查 [`tokens.md`](./tokens.md) — 颜色 / 字体 / 间距 / 圆角 / 阴影 是否有现成变量
- 查 [`components/`](./components/) + [`cards/`](./components/cards/) — 按钮 / 输入 / 卡片 / 导航 是否有现成组件

**决策顺序**:
```
设计稿/需求 → 扫 FIGMA_MAP.md 找到对应 HTML
            → 查 recipes/ 看有没有现成组合模式
            → 找 components/ 对应组件文件复制样式
            → 改 tokens.md 5 个颜色变量适配品牌
```
- ❌ 禁止自创新设计 token / 新组件样式 / 新图标来源

### Step 2.5：⚠️ 做平台页面时，必须核对生产环境真实值

> **`tokens.md` 的值可能已过时。** 2026-09-29 真实翻车案例：

Autocava 用了 Nuxt UI 框架，框架预置完整的 `--color-green-*` 色板，但**实际启用的是 Tailwind utility class 直写 hex（`bg-ffcf20` 黄色）**。AI 看到 green 色板就断定"主色是绿"，把整站改成绿色 —— **完全错了**。

**判断主色的唯一正确方法**：

```bash
# ① 抓生产 HTML
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..." \
  "https://www.autocava.com.mx" -o /tmp/ac.html

# ② 统计真实在用的颜色（看 class，不是看 CSS 变量定义）
grep -oE '\b(bg|text|border)-[0-9a-f]{3,6}\b' /tmp/ac.html | sort | uniq -c | sort -rn | head -20
```

| ✅ 正确 | ❌ 错误 |
|---------|--------|
| 看渲染 DOM 的 class（`bg-ffcf20`） | 看框架预置色板变量（`--color-green-*`）|
| 看使用频次（主色排最前） | 看 CSS 里"定义了"就认为"启用了" |
| 浏览器截图确认 | 只读 HTML 源码推测 |

> **铁律**：框架默认色板 ≠ 品牌色。**永远看真实渲染结果。**


### Step 3：接真实数据（环境分流）

- 数据从你的真实平台取（SSR / API / CMS）
- **环境分流硬规则**：
  - 基础数据 = 默认环境
  - 新功能 / 灰度 = canary / beta
  - 实验性功能 = experiment / A/B
- ❌ 禁止用示意曲线 / 假序列冒充真点位
- 详见 `principles.md §4 数据真实性` 和 `§7 环境分流`

### Step 4：满足生产级质量

- **可达性**：WCAG AA 对比度（4.5:1 普通文字 / 3:1 大字）
- **视口**：移动端压测（按目标市场最低端机型，如 MX 360×800）
- **性能**：Core Web Vitals（LCP < 2.5s / FID < 100ms / CLS < 0.1）
- **响应式**：单文件自适应，断点 **1024px**（PC ≥1024px / H5 <1024px）

### Step 5：上线前自检

- 入口 → 交付 → 闭环 写了吗？
- 跨产品线硬规则全过？（[`principles.md`](./principles.md) 7 条）
- 数据溯源注释（每个数字字段都有 source）

---

## 🔒 本 skill 专属硬规则（跟 prototype-design 不同的地方）

| # | 规则 | `product-prototype-design`（demo） | 本 skill（生产） |
|---|------|-----------------------------------|---------------------------|
| 1 | **数据来源** | mock / 占位 OK | **必须真实数据**，无数据 = 标 `[待PM确认]` 留空 |
| 2 | **组件复用** | 自创样式 OK | **必须查 `components/` 复用**，禁止新立 |
| 3 | **颜色 token** | 默认 brand color | 按页面归属选（前台 vs 后台 vs 浮层） |
| 4 | **环境分流** | 不强制 | **必须分流**（stable / canary / experiment，注明） |
| 5 | **可达性** | 评审通过即可 | **WCAG AA 必达** |
| 6 | **性能** | 评审通过即可 | **Core Web Vitals 必达** |
| 7 | **触达工具** | 市场合规通道 | 市场合规通道（一致） |
| 8 | **留资隐私** | 必带隐私脚注 | 必带（一致） |
| 9 | **ICON** | 单一图标 CDN | 单一图标 CDN（一致） |
| 10 | **单文件自适应** | 强制 | 强制（一致） |

> **共识**（跟 prototype-design 一致）：7 / 8 / 9 / 10 四条不重复。
> **差异**（本 skill 独有）：1 / 2 / 3 / 4 / 5 / 6 六条比 demo 更严。

---

## 📦 复用资源（先查再写）

| 资源 | 何时用 | 在哪 |
|------|--------|------|
| **🎨 Gallery** | 第一次接触 — 一页看全部 30 组件 + 4 recipes | [`gallery.html`](./gallery.html) |
| **Design Tokens**（颜色 / 字体 / 间距 / 语义化映射 + CSS 变量） | **所有 UI 设计的第一步** | [`tokens.md`](./tokens.md) |
| **组件库**（25 个核心组件） | 复用已有组件样式 | [`components/`](./components/) |
| **内容卡库**（5 张卡） | 列表/详情/搜索场景 | [`components/cards/`](./components/cards/) |
| **Recipes**（4 个组合 pattern） | 真实页面流程（反馈/进度/发现/卡组合） | [`recipes/`](./recipes/) |
| **Figma 映射表** | 看到 Figma 组件名 → 立刻知道对应 HTML | [`FIGMA_MAP.md`](./FIGMA_MAP.md) |
| **完整生产页 demo** | 看整体怎么落地 | [`demo/`](./demo/) |
| **7 条硬规则** | 跨产品线底线 | [`principles.md`](./principles.md) |

> ❌ **禁止**在生产页面里立"新一套卡片样式 / 新颜色 token / 新图标来源"。
> ✅ **第一步永远是查 `gallery.html` + `tokens.md`**——这两个是事实来源。

---

## 🚫 本 skill 明确不做的事

- ❌ **不做演示 / 单 feature demo**（走 `product-prototype-design`）
- ❌ **不复制 `tokens.md` / `components/` 全文**（按需查）
- ❌ **不修改共享资源**而不更新对应引用
- ❌ **不写后端 / API / 数据库**
- ❌ **不写绝对颜色 / 字号**（必须用 CSS 变量）

---

## 🔗 与 `product-prototype-design` 的协作关系

```
[产品想法]
    ↓
product-prototype-design  ← 单 feature 演示 / mock / 老板评审
    ↓ 验证通过
product-ui-design（本 skill）← 真实数据 / 复用组件 / 上线
    ↓ 发布
线上环境 / 静态托管
```

- **`product-prototype-design`** = demo skill（单 feature / mock 数据 / 评审通过即可）
- **`product-ui-design`** = 生产 skill（要上线 / 真实数据 / 复用现有组件 / 满足 WCAG + Core Web Vitals）

> 一个功能的完整链路通常会**两个 skill 都过**：先 prototype 验证，再 product-ui 落地。

---

## 🛠️ 适配你的项目

| 你的项目 | 怎么改 |
|----------|--------|
| **品牌色** | 编辑 `tokens.md` CSS 变量块 |
| **字体家族** | 改 `tokens.md` `--font-sans` |
| **触达工具** | 改 `principles.md` §1 + `components/*.html` 里的链接 |
| **隐私合规** | 改 `principles.md` §5 + 链接 |
| **组件 / 页面** | 直接编辑 `components/` `demo/` |

---

## 📋 维护记录

| 日期 | 变更 | 作者 |
|------|------|------|
| 2026-09-29 | v1.0 初版：从生产工作流抽出，去除 Mstar 专属引用 | AI 起草，待 PM 审 |
| 2026-09-29 | v1.1 升级为完整 skill 包：新增 8 组件 + 2 卡 + 4 recipes + gallery + FIGMA_MAP.md | Figma 588 盘点后增量 |