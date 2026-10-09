---
name: product-ui-design
description: 设计要真实上线的产品页面 UI（首页 / 详情页 / 列表页 / 表单页 / 落地页 / 后台看板等生产页面），不是演示原型。强制复用包内设计 token 与已有组件、接真实平台数据、生产级可达性（WCAG AA / 触控热区 / 响应式断点 / 性能预算）。当用户说「做产品页 / 上线页 / 用现有组件库 / 接真实数据 / 要过 WCAG / 要能上线」时使用。本包完全自包含，不依赖任何外部文件。
version: 2.0
license: MIT
disable-model-invocation: false
triggers:
  - "设计产品页面"
  - "做产品页"
  - "上线页面"
  - "真实页面"
  - "production page"
  - "用现有组件"
  - "复用组件库"
  - "组件库"
  - "设计系统"
  - "做 UI"
  - "做产品 UI"
entry_points:
  - ./design-system/gallery.html      # 一页总览全部组件 + recipes + 生产页 demo
  - ./design-system/components/README.md  # 组件索引 + 场景选型表
  - ./design-system/recipes/README.md      # 组合 pattern（反馈流 / 进度流 / 发现流…）
  - ./design-system/FIGMA_MAP.md            # Figma 组件名 → HTML 文件映射
  - ./design-specs/tokens.md                 # 站点级设计 token（改品牌色从这里开始）
  - ./SITE-CONFIG.md# 配置你的站点与市场
  - ./LICENSE
---

# 产品页面 UI 设计 Skill v2.0

> 用于设计**要真实上线给终端用户**的产品页面，不是给老板评审的演示 demo。

| 用途 | 用哪个 skill |
|------|-------------|
| 单feature 演示 / 评审 / mock 数据 | 演示原型 skill（可自创样式） |
| **真实生产页面 / 上线 / 接真实数据** | **本 skill** |

---

## ⛔ 第0 步：先配置你的站点（必做，跳过必翻车）

本 skill 是**通用**的，不预设任何品牌和市场。动手前先读 [`SITE-CONFIG.md`](./SITE-CONFIG.md)，确认下面 5 件事：

| # | 要确认什么 | 填在哪 |
|---|-----------|--------|
| 1 | **品牌主色**是什么（不要凭印象猜，见 Step 2.5） | `design-specs/tokens.md` |
| 2 | **目标市场**在哪（决定触达工具 / 法规 / 视口下限） | `SITE-CONFIG.md` |
| 3 | **最低端机型视口**（移动优先，别按 iPhone 大屏设计） | `SITE-CONFIG.md` |
| 4 | **数据来源**与**环境分流参数**（多环境时必填） | `SITE-CONFIG.md` |
| 5 | 是否**采集用户信息**（采集则隐私脚注是硬要求） | `SITE-CONFIG.md` |

> ⚠️ **未配置就开工 = 必返工**。本文所有涉及品牌色 / 触达工具 / 法规 / 视口的具体值都写成占位符
> （如 `<PRIMARY_COLOR>`、`<CONTACT_CHANNEL>`、`<LOW_END_VIEWPORT>`），**必须**替换为 `SITE-CONFIG.md` 里的实际值。

---

## 🚦 Step 1：定位页面与产品线

- 这是什么页面？（首页 / 详情 / 列表 / 表单 / 落地页 / 后台看板）
- 属于哪条产品线？**一个项目常有多套并存的视觉体系**（如主站 / 报告页 / 后台），
  各自有独立 token 与圆角档位。
- **产品线之间 token 不互通**：给 A 线灌 B 线的品牌色/圆角，会明显视觉不一致。
- 判定方法：先列出项目里所有产品线各自的**品牌色 + 字体 + 卡片圆角 + token 文件位置**，
  再决定本页归属。**查不到就去真实页面量，不要凭印象。**

### 写下「入口 → 交付 → 闭环」

任何页面设计开工前必须明确三件事，否则做完用户找不到入口、流程断在半路：

| | 要回答 |
|---|---|
| **入口** | 用户从哪个已有页面/触点看到它？进入条件？带什么上下文过来？ |
| **交付** | 用户实际得到什么？（内容 / 状态 / 服务）承诺时效？ |
| **闭环** | 拿到后下一步做什么？失败怎么兜底？产生什么数据给谁看？ |

---

## Step 2：复用已有资产，不要造轮子

| 资产 | 何时查 | 位置 |
|------|--------|------|
| **组件库**（按钮/输入/卡片/导航/弹窗/Toast…） | 任何页面 | [`design-system/components/README.md`](./design-system/components/README.md) |
| **一页总览**（全部组件 + recipes + 生产页 demo） | 选型时快速扫 | [`design-system/gallery.html`](./design-system/gallery.html) |
| **组合 pattern**（反馈流 / 进度流 / 发现流） | 有交互流程的页面 | [`design-system/recipes/`](./design-system/recipes/README.md) |
| **基础 token**（颜色/字体/间距/圆角档位） | 所有页面的第一步 | [`design-system/tokens.md`](./design-system/tokens.md) |
| **站点 token**（你的品牌色在此覆盖） | 改品牌色 | [`design-specs/tokens.md`](./design-specs/tokens.md) |
| **卡片库**（商品/价格/行动/对比类） | 任何列表或详情展示 | [`design-specs/cards/`](./design-specs/cards/) |
| **图标规范** | 所有图标决策 | [`ICON_SPEC.md`](./ICON_SPEC.md) |
| **市场/法规约束** | 面向特定市场 | [`DESIGN_CONSTRAINTS.md`](./DESIGN_CONSTRAINTS.md) |
| **HTML/CSS 写法规范** | 写代码时 | [`rules/03-html-prototype.mdc`](./rules/03-html-prototype.mdc) |

> ❌ **禁止**自创新设计 token / 新卡片样式 / 新图标来源。
> ✅ **第一步永远是查 token 文件**——那是颜色/字体的事实来源。

---

### Step 2.5：⚠️ 核对生产环境真实值，不要相信文档

> **token 文件和设计文档里的值都可能已过时。** 真实翻车案例：某项目用了 UI 框架，
> 框架预置完整的绿色色板，但**实际启用的是 utility class 直写十六进制色值**。
> AI 看到绿色色板就断定「主色是绿」，把整站改成绿色 —— **完全错了**。

**判定主色的唯一正确方法：看真实渲染结果，不看 CSS 里「定义了」什么。**

```bash
# ① 抓生产 HTML（用桌面 UA，标注环境参数）
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..." \
  "<目标页面 URL>" -o /tmp/page.html

# ② 统计真实在用的颜色（看 class / style，不看变量定义）
grep -oE '\b(bg|text|border)-[0-9a-f]{3,6}\b' /tmp/page.html | sort | uniq -c | sort -rn | head -20

# ③ 浏览器截图确认（最可靠）
```

| ✅ 正确 | ❌ 错误 |
|--------|--------|
| 看渲染 DOM 的 class | 看框架预置色板变量 |
| 看使用频次（主色排最前） | 「CSS 里定义了」就认为「启用了」 |
| 截图确认 | 只读源码推测 |

> **铁律：框架默认色板 ≠ 品牌色。永远看真实渲染结果。**

#### 静态资源 ID 空间可能不统一

很多站点同一类资源有**多套路径**，且**ID 与页面 URL 里的 ID 不是同一套编号**（如
`cdn/xxx/{hash}.png` 与 `/series/{NNNN}` 并存）。取图时：

```bash
# 保序取第一个，不要 sort -u（排序会打乱文档顺序，导致多张图指向同一资源）
grep -oE 'https?://cdn\.[^"]+\.(png|jpg|webp)' /tmp/page.html | head -1
```

> ⚠️ 抓完必须与页面真实名称**逐一比对**，全部对上才算数。

---

## Step 3：接真实数据

- 数据优先取**页面 SSR 数据**或公开接口；原型/原型演示可用 mock，但**生产页面不可**。
- ⚠️ **SSR 未必是 JSON 对象**：Nuxt 等框架用 devalue **扁平数组**序列化，形如
  `"price":93` 里的 `93` 是**数组下标**不是价格。正则直取会拿到垃圾数。两种正确做法：
  - 按下标回查扁平数组（严谨，适合写脚本）
  - 取页面可见金额（快，适合原型取价）
- ⚠️ 页面常混入**推荐位/广告位的其他条目数据**，必须与目标对象**名称比对**后再采信。
- **多环境必须分流**（如 stable / canary / experiment）：
  - 在交付物顶部注释里写明用了哪个环境
  - 不同维度归属不同环境时，按维度分别标注
  - 拿不到真实点位就**不要画曲线**，只展示已确认的真实字段 + 链路回平台
- ❌ 禁止用示意曲线 / 假序列 / 「示例数据」冒充真实点位
- 详见 [`rules/07-prototype-platform-data.mdc`](./rules/07-prototype-platform-data.mdc)

---

## Step 4：生产级质量

### 可达性（硬要求）

| 项 | 标准 |
|---|---|
| 文字对比度 | ≥ **4.5:1**（大字 ≥ 3:1） |
| 可交互控件边框 | ≥ **3:1**（非文本对比度） |
| **触控热区** | 所有可点元素 ≥ **44×44 CSS px**；主CTA 高度 ≥ 48px |
| **焦点可见** | 每个可聚焦元素必须有 `:focus-visible` 样式（禁止 `outline: none` 了事） |
| 表单标签 | 输入框必须有可关联的 `<label>` |

> **触控热区是最常被漏掉的一条**——小圆角chip 常做到 36px，在移动端难点中。
> 用浏览器实测高度，别目测。

### 响应式（硬要求）

- **单文件自适应**，禁止拆成 PC 版 + 移动版两个文件
- 断点统一 **1024px**（PC ≥1024px / 移动 <1024px）
- **按目标市场最低端机型压测**（见 `SITE-CONFIG.md`），再退一档验证
- 验证项：无横向滚动、无元素溢出视口、无内容被裁切

### 性能预算

| 指标 | 目标 |
|------|------|
| LCP | < 2.5s |
| FID | < 100ms |
| CLS | < 0.1 |

### 文案压测

- 用**最长真实名称**做布局压测（如某站最长的车系名 `Hyundai GRAND i10 HATCHBACK`）
- 名称不能截断成无意义片段，也不能撑破布局

---

## Step 5：上线前自检

- [ ] 「入口 → 交付 → 闭环」写了吗？
- [ ] 产品线 token 用对了？（没跨线借用）
- [ ] 数据全部来自真实来源？每处都标了来源与环境？
- [ ] 可达性实测过（对比度 / 触控热区 / 焦点态 / label）？
- [ ] 响应式在最低端机型视口验证过？
- [ ] 采集用户信息的话，隐私脚注 + 免责齐吗？（见 [`rules/06-mx-lead-privacy.mdc`](./rules/06-mx-lead-privacy.mdc)，**按你的市场替换法规**）
- [ ] 出具交付自检报告（见 [`rules/01-delivery-verification.mdc`](./rules/01-delivery-verification.mdc)）

---

## 🔒 本 skill 的硬规则

| # | 规则 | 演示原型 | 本 skill（生产） |
|---|------|---------|------------------|
| 1 | **数据来源** | mock / 占位 OK | **必须真实**，无数据则留空并标注待确认 |
| 2 | **组件复用** | 自创样式 OK | **必须查组件库**，禁止新立 |
| 3 | **token** | 随意 | 按产品线选，禁止跨线借用 |
| 4 | **环境分流** | 不强制 | 多环境必须分流并注明 |
| 5 | **可达性** | 评审通过即可 | **WCAG AA 必达** |
| 6 | **触控热区** | 随意 | **≥44px 必达** |
| 7 | **响应式** | 强制 | 强制 + 最低端机型压测 |
| 8 | **数据真实性** | 允许示意 | **禁止示意曲线冒充真点位** |

---

## 📦 包内文件清单

```
product-ui-design/
├── SKILL.md                  ← 本文件（主入口）
├── SITE-CONFIG.md            ← 你要先填的配置
├── README.md                 ← 安装说明
├── LICENSE                   ← MIT
├── design-system/            ← 通用组件库（tokens + 组件 + recipes + demo）
├── design-specs/             ← 站点级 token + 卡片库（在这里改品牌色）
├── rules/                    ← 交付/发布/HTML/隐私/数据规范
├── reference/                ← 参考资料
├── DESIGN_CONSTRAINTS.md     ← 市场与法规约束
├── ICON_SPEC.md              ← 图标映射表
└── knowledge/                ← 领域知识（按项目需要增删）
```

> **本包自包含**：除本目录外不依赖任何文件。复制整个目录即可使用。

---

## 🚫 本 skill 明确不做

- ❌ 不做演示/ 单feature demo
- ❌ 不写后端 / API / 数据库（纯静态 HTML + CSS + 少量 JS）
- ❌ 不复制规范文件全文（按需查）
- ❌ 不在生产页面里立「新一套」组件样式 / token / 图标来源

---

## 📚 按需加载（不要全塞进 context）

- [`rules/01-delivery-verification.mdc`](./rules/01-delivery-verification.mdc) — 交付自检报告
- [`rules/02-publishing.mdc`](./rules/02-publishing.mdc) — 发布渠道
- [`rules/03-html-prototype.mdc`](./rules/03-html-prototype.mdc) — HTML/CSS 写法全规范
- [`rules/06-mx-lead-privacy.mdc`](./rules/06-mx-lead-privacy.mdc) — 留资隐私（**按你的市场替换**）
- [`rules/07-prototype-platform-data.mdc`](./rules/07-prototype-platform-data.mdc) — 数据真实性 + 环境分流
- [`design-system/principles.md`](./design-system/principles.md) — 设计原则