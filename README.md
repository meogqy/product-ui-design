# product-ui-design · 产品页面 UI 设计 Skill

> 一个**自包含**的 AI skill，用于设计**要真实上线**的产品页面 UI。
> 强制复用包内组件与token、接真实数据、过生产级可达性与响应式标准。
>
> **MIT License · 复制整个目录即用，零外部依赖**

---

## 这是什么

大多数 UI skill 让AI「自由发挥」出一个能看的页面。本 skill 走相反的路：

|约束 | 说明 |
|------|------|
| **不许造轮子** | 必须先查包内组件库和 token，禁止自创新样式 |
| **不许假数据** | 生产页面禁止用示意曲线 / 假序列冒充真实数据 |
| **不许小热区** | 所有可点元素 ≥44×44px，主 CTA ≥48px |
| **不许假对比度** | 正文 ≥4.5:1，控件边框 ≥3:1，必须实测不目测 |
| **不许假焦点态** | 每个可聚焦元素都要有 `:focus-visible` |
| **不许大屏思维** | 按目标市场**最低端机型**压测，不是你的开发机 |

---

## 🚀 3 分钟安装

### 步骤 1：复制到你的项目

```bash
cp -r product-ui-design /path/to/your-project/
```

>整个目录是自包含的，**不需要**其他任何文件。

### 步骤 2：让 AI 工具自动发现

按你用的工具复制对应入口文件到项目根目录：

| 工具 | 复制这个 | 生效方式 |
|------|---------|---------|
| **Cursor / Cline / Roo Code / Continue / Windsurf** | `.cursorrules` | 放项目根，自动生效 |
| **Claude Code** | `CLAUDE.md` | 放项目根，自动生效 |
| **Codex / OpenCode / Devin / Gemini CLI / Aider** | `AGENTS.md` | 放项目根，自动生效 |
| **想作为独立 skill** | `SKILL.md` | 复制到skills 目录 |

```bash
# 作为独立 skill（Cursor / Codex / Claude Code）
mkdir -p your-project/.cursor/skills
cp product-ui-design/SKILL.md your-project/.cursor/skills/product-ui-design.md

# 包内文件也要一起复制，否则 SKILL.md 里的相对链接会失效
cp -r product-ui-design/design-system your-project/.cursor/skills/
cp -r product-ui-design/design-specs  your-project/.cursor/skills/
cp -r product-ui-design/rules        your-project/.cursor/skills/
```

### 步骤 3：配置你的站点（**必做**）

打开 [`SITE-CONFIG.md`](./SITE-CONFIG.md)，填 5 件事：

1. **品牌主色 + 产品线**（实测生产页面得来，别猜）
2. **目标市场** → 决定触达工具与法规
3. **最低端机型视口** → 决定响应式基线
4. **数据来源与环境分流** → 决定怎么取数
5. **是否采集用户信息** → 决定隐私合规要求

### 步骤 4：改品牌色

打开 [`design-specs/tokens.md`](./design-specs/tokens.md)，把 `--yellow-500` 等改成你的品牌色。
包内默认色仅作占位，**必须替换**。

### 步骤 5：开始用

```
请用 product-ui-design skill 帮我设计 XXX 页面
```

AI 会加载 SKILL.md，按 5 步流程走，并优先查包内组件与 token。

---

## 📦 包内容

```
product-ui-design/
├── SKILL.md                    ← 主入口 · 5 步工作流 + 10 条硬规则
├── SITE-CONFIG.md              ← 你的站点配置（先填这个）
├── README.md                   ← 本文件
├── LICENSE                     ← MIT
│
├── design-system/              ← 通用组件库
│   ├── tokens.md               ←   基础 token（颜色/字体/间距/圆角档位）
│   ├── components/             ←   组件源码 + 索引
│   ├── recipes/                ←   组合 pattern（反馈流/进度流/发现流…）
│   ├── gallery.html            ←   一页总览所有组件
│   ├── FIGMA_MAP.md            ←   Figma 组件名 → HTML 映射
│   ├── demo/                   ←   页面级 demo
│   └── principles.md           ←   设计原则
│
├── design-specs/               ← 站点级 token（改品牌色在这）
│   ├── tokens.md               ←   你的品牌色 / 字体 / 间距
│   └── cards/                  ←   卡片库（商品/价格/行动/对比）
│
├── rules/                      ← 规范文件
│   ├── 01-delivery-verification.mdc  ←   交付自检报告格式
│   ├── 02-publishing.mdc             ←   发布渠道
│   ├── 03-html-prototype.mdc         ←   HTML/CSS 写法全规范
│   ├── 06-mx-lead-privacy.mdc        ←   留资隐私（墨西哥示例，按你市场改）
│   └── 07-prototype-platform-data.mdc←   数据真实性 + 环境分流
│
├── DESIGN_CONSTRAINTS.md       ← 市场与法规约束
├── ICON_SPEC.md                ← 图标映射表
├── knowledge/                  ← 领域知识
└── reference/                  ← 参考资料
```

> **自包含**：不依赖包外任何文件。复制整个目录即可用。

---

## 🎯 什么时候用/ 不用

| 场景 | 用这个吗 |
|------|---------|
| 真实上线的产品页（首页/详情/列表/表单/落地页/后台） | ✅ |
| 要接真实数据 | ✅ |
| 要复用现有组件库与设计系统 | ✅ |
| 要过 WCAG AA / 性能预算 | ✅ |
| 单 feature 演示给老板评审 | ❌ 用演示原型 skill |
| mock 数据 / 自创样式 | ❌ 用演示原型 skill |

---

## ⚠️ 按市场改写的地方

本包是**通用**的，以下文件含**特定市场示例**，用到时请按你的实际情况替换：

| 文件 | 需替换内容 |
|------|-----------|
| `SITE-CONFIG.md` | 全部占位符（品牌色/市场/视口/触达工具…） |
| `rules/06-mx-lead-privacy.mdc` | **墨西哥市场**隐私法规 → 换成你所在市场的 |
| `rules/03-html-prototype.mdc` | 部分约束按 Mstar 实践写的，按你的项目调整 |
| `design-specs/tokens.md` | 默认品牌色是占位值，**必须替换** |

---

## 🧭 一页速查：5 步工作流

1. **定位页面与产品线** —— 判定归属，写「入口→交付→闭环」
2. **复用已有资产** —— 查组件库 / token / 卡片库，禁止造轮子
   - **2.5 核对生产真实值** —— 品牌色实测，不信文档
3. **接真实数据** —— 注意 SSR 扁平数组陷阱 / 环境分流
4. **生产级质量** —— WCAG AA + 44px 热区 + 1024px 响应式 + 性能预算
5. **上线前自检** —— 出交付自检报告

---

## 📄 License

MIT — 自由使用、修改、分发。见 [`LICENSE`](./LICENSE)。