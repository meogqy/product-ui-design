# UI Design System Starter · 可分发的产品 UI 设计技能包

> **Version**: 1.1 (2026-09-29)
> **Type**: Project / Personal Skill + Design System Template
> **License**: MIT

---

## 📦 这是什么？

一个**即开即用**的产品 UI 设计 skill 包，包含：

- ✅ **SKILL.md** — AI 工具可加载的产品 UI 设计 skill（v1.1 自动触发）
- ✅ **gallery.html** — 一页总览所有 30 组件 + 4 recipes · **从这里开始**
- ✅ **principles.md** — 7 条跨产品线硬规则（任何 UI 工作通用）
- ✅ **tokens.md** — 设计变量集中版（颜色 / 字体 / 间距）+ CSS 变量映射
- ✅ **components/** — 25 个核心组件的完整 HTML reference
- ✅ **components/cards/** — 5 张内容卡
- ✅ **recipes/** — 4 个组合模式(反馈流/进度流/发现流/内容卡组合)
- ✅ **FIGMA_MAP.md** — Figma 588 组件名 → HTML 文件映射表
- ✅ **demo/** — 6 个页面级 demo（5 个生产真数据 + 1 个组件集成沙盘），另有 `demo/index.html` 索引页

---

## 🚀 3 分钟安装

### 步骤 1：复制整个 `ui-design-system-starter/` 到你的项目

```bash
# 复制到你项目根目录
cp -r ui-design-system-starter /path/to/your-project/

# 或者在已 clone 的项目里拉取
cd /path/to/your-project
# 把 ui-design-system-starter/ 这个目录放进来
```

### 步骤 2：（可选）让 AI 工具自动发现

### 步骤 2：让 AI 工具自动发现

本包提供 **4 个工具入口文件**，按你用的工具复制对应的：

| 工具 | 复制这个 | 生效方式 |
|------|---------|---------|
| **Cursor / Cline / Roo Code / Continue / Windsurf** | `.cursorrules` | 放项目根，自动生效 |
| **Claude Code** | `CLAUDE.md` | 放项目根，自动生效 |
| **Codex / OpenCode / Devin / Gemini CLI / Aider** | `AGENTS.md` | 放项目根，自动生效 |
| **想作为独立 skill 用** | `SKILL.md` | 复制到 skills 目录 |

```bash
# 一行装完（Cursor + Claude Code + 通用工具）
cp ui-design-system-starter/.cursorrules /path/to/your-project/
cp ui-design-system-starter/CLAUDE.md     /path/to/your-project/
cp ui-design-system-starter/AGENTS.md     /path/to/your-project/

# 或者作为独立 skill（Cursor / Codex / Claude Code）
mkdir -p your-project/.cursor/skills
cp ui-design-system-starter/SKILL.md your-project/.cursor/skills/product-ui-design.md
```

> 装好后直接在 AI 里说「帮我做一个 XX 页面」，它会自动按 `AGENTS.md` 的 5 步流程走。

### 步骤 3：自定义品牌色

打开 `tokens.md`，找到 `:root {` CSS 变量块，把 `--yellow-500` 等颜色**改成你的品牌色**。

```css
:root {
  /* 改这里 ↓ */
  --yellow-500: #YOUR_BRAND_PRIMARY;
  --yellow-600: #YOUR_PRIMARY_DARK;
  
  /* 下面是自动算出来的辅助色（10 档梯度） */
  /* ... */
}
```

### 步骤 4：开始使用

#### 选项 1 — 让 AI 加载 skill

在 AI 工具里说：

```
请用 product-ui-design skill 帮我设计 XXX 页面
```

AI 会自动加载 SKILL.md，按决策树走，引用 `tokens.md` 和 `components/` 里的资源。

#### 选项 2 — 自己动手

不一定要 AI 加载：

1. **先打开 `gallery.html`** → 浏览所有 30 组件 + 4 recipes，点感兴趣的卡片
2. 打开 `recipes/0X-*.md` → 看组合模式（反馈流 / 进度流 / 发现流 / 内容卡），复制剧本
3. 打开 `FIGMA_MAP.md` → 看到 Figma 组件名 → 找到 HTML 文件
4. 打开 `tokens.md` → 复制 CSS 变量到你的项目
5. 打开 `components/0X-*.html` → 找现成组件，**直接复制 class**
6. 打开 `demo/01-autocava-news-home.html` → 生产真数据首页示例，从这里 fork 修改

---

## 🎨 自定义清单

每个团队 / 项目都应该改这些：

| 项 | 在哪 | 改什么 |
|----|------|--------|
| **品牌主色** | `tokens.md` CSS 变量块 | `--yellow-500` |
| **品牌色梯度** | `tokens.md` 颜色家族 | 10 档 Yellow / Blue / Red / Green |
| **字体家族** | `tokens.md` `--font-sans` | Roboto / Inter / 系统字体 |
| **触达工具** | `principles.md` §1 | MX = WhatsApp · 国内 = 微信 · 其他市场 = 适配 |
| **隐私合规** | `principles.md` §5 | MX = Política de Privacidad · 国内 = 隐私协议 · EU = GDPR |
| **留资表单字段** | `principles.md` §5 | 市场法规决定 |
| **产品线映射** | `SKILL.md` 产品线路由表 | 改 4 条产品线为你项目的 |

---

## 📂 完整结构

```
ui-design-system-starter/
├── README.md                       ← 你正在看
├── .cursorrules                    ← ⭐ Cursor / Cline / Roo Code / Continue 入口
├── AGENTS.md                       ← ⭐ Codex / OpenCode / Devin / Gemini CLI 入口
├── CLAUDE.md                       ← Claude Code 入口（指向 AGENTS.md）
├── SKILL.md                        ← 完整 skill 定义
├── gallery.html                    ← 一页总览 30 组件 + 4 recipes
├── FIGMA_MAP.md                    ← Figma 588 → HTML 映射表
├── principles.md                   ← 7 条跨线硬规则
├── tokens.md                       ← 设计变量集中版
├── recipes/
│   ├── README.md                   ← 4 个组合 pattern 索引
│   ├── 01-feedback-flow.md         ← Modal+Toast+Loading+Empty
│   ├── 02-progress-flow.md         ← Progress+Steps+Battery
│   ├── 03-discovery-flow.md        ← Brand Grid+Ranking+Filter+Favorite
│   └── 04-card-composition.md      ← Content+Article+Product Card
├── components/
│   ├── README.md                   ← 组件库索引 (25+5)
│   ├── 01-17-*.html                ← P0 基础交互 11 个 + P1 反馈场景
│   ├── 18-progress.html            ← 电量条/进度条 ⭐ Figma 342 次
│   ├── 19-typography.html          ← 字体层级 14+
│   ├── 20-steps.html               ← 流程步骤 3 视图
│   ├── 21-filter.html              ← 筛选 Chip/Sheet/Modal
│   ├── 22-brand-grid.html          ← 品牌 Logo 网格
│   ├── 23-ranking.html             ← 排行榜 3 视图
│   ├── 24-favorite.html            ← 收藏切换 4 视图
│   ├── 25-footer.html              ← 页面底部 4 视图
│   └── cards/
│       ├── 01-content-card.html    ← 通用内容卡
│       ├── 02-simple-card.html     ← 简洁卡
│       ├── 03-brand-card.html      ← 品牌入口卡
│       ├── 04-article-card.html    ← 文章/资讯卡 🆕
│       └── 05-product-card.html    ← 商品/车型卡 🆕
└── demo/
    ├── index.html                     ← demo 索引页
    ├── 01-autocava-news-home.html    ← 首页（真数据）
    │                                    ⚠️ 02 号位空缺（原「价格详情」demo 未做，勿当漏文件）
    ├── 03-series-detail-captiva.html ← 车系页（真数据）
    ├── 04-cavi-lead-report.html      ← CAVI 留资页（真数据）
    ├── 05-car-list-filter.html       ← 车型列表页（真数据）
    ├── 06-rank-ventas.html            ← 排行榜页（真数据）
    └── product-detail-page.html      ← 组件集成沙盘（mock）
```

---

## 🌐 与 Mstar / AutoCava 的关系

本 starter 来自 [Mstar](https://github.com/) 工作区的 `visual-specs/`，经过：

- **去除 Mstar 专属引用**（autocava.com.mx CDN / 子项目路径 / AGENTS.md 等）
- **抽象通用方法论**（7 条硬规则 = 任何 UI 工作通用）
- **保留具体实现**（token 值 / 组件样式 = 真实可用的参考）

如果你在 Mstar / AutoCava 工作，**优先使用**项目内的：

- `Mstar/visual-specs/`（**项目源** · 含 Mstar 专属引用 + 与 `product-prototype-design` skill 的集成）
- `Mstar/.cursor/skills/product-ui-design/`（**项目 skill**，自动可用）

---

## 🛠️ 适配你的项目

### 场景 1：你是产品经理（无代码项目）

1. 复制整个目录到项目根
2. 打开 `tokens.md` → 改你的品牌色 → 复制 CSS 给前端
3. 打开 `components/0X-*.html` 在浏览器看 → 把要用的组件截图给设计师 / 前端
4. **不要**复制 `SKILL.md` 到 `.cursor/skills/`（除非你用 AI 辅助）

### 场景 2：你是设计师（Figma / Sketch）

1. 复制整个目录作为**设计规范参考**
2. 用 `tokens.md` 的 CSS 变量 → 在 Figma 里建对应 Variables
3. 用 `components/` 的 HTML → 截图后丢到 Figma Library
4. 不用 `SKILL.md`（设计师不需要 AI 工具加载）

### 场景 3：你是 AI 开发者 / AI 辅助 UI

1. 复制整个目录到项目根
2. 把 `SKILL.md` 复制到 `.cursor/skills/`（让 Cursor / Codex 自动发现）
3. 改 `tokens.md` 品牌色
4. 对 AI 说"用 product-ui-design skill 设计 XXX"
5. AI 会自动引用 `tokens.md` + `components/` 里的资源

### 场景 4：开源贡献 / 公开分发：

- 把 starter 单独建一个 GitHub repo
- 在 README 加你的品牌信息
- 给 `tokens.md` 改通用化（去品牌色，让用户自己配）

---

## 🤝 反馈 / 贡献

发现 bug / 想加组件？直接在本目录改 `tokens.md` / `components/` / `demo/`，保持：

- 数据真实（P0）
- 触达工具合规
- 单文件自适应（PC ≥1024px / H5 <1024px）
- 0 个硬编码 hex（必须 CSS 变量）

---

## 🌐 部署到公网（可选）

本包是纯静态文件，**无构建步骤**，可直接托管到任何静态托管平台。

### Cloudflare Pages

```bash
# 1. 准备（Cloudflare Pages 要求根目录有 index.html）
cp gallery.html index.html

# 2. 部署（首次会要求登录 Cloudflare）
npx wrangler pages deploy . --project-name=ui-design-system-starter

# 3. 拿到 URL，形如：
#    https://ui-design-system-starter.pages.dev
#    → 打开就是 gallery.html（组件总览页）
```

**部署后建议**：
- 把 `gallery.html` 改名成 `index.html`（当首页）
- README.md / SKILL.md 等 .md 文件浏览器直接看原始文本，可接受

### 其他平台

| 平台 | 做法 |
|------|------|
| Vercel | `npx vercel deploy`（同样需要 index.html）|
| Netlify | 拖整个文件夹到 app.netlify.com/drop |
| GitHub Pages | push 到 repo，Settings → Pages 选根目录 |
| 内网共享 | 起个 `python3 -m http.server 8000`，团队访问 `http://<你的IP>:8000/gallery.html` |

> ⚠️ **部署前确认**：公网 URL 任何拿到链接的人都能访问。如果组件里有内部数据 / 未发布设计，**不要部署**。

---

## 🌐 在线预览（已发布）

**🌍 https://ui-design-system-starter.pages.dev**

打开即是 `gallery.html`（30 组件 + 4 recipes 总览页），可直接点进每个组件。

| 在线直达 | 内容 |
|---------|------|
| `/` · `/gallery.html` | 组件总览 |
| `/components/01-25-*.html` | 25 个组件单页 |
| `/components/cards/01-05-*.html` | 5 张内容卡 |
| `/demo/01-autocava-news-home.html` | 生产真数据首页 demo |
| `/SKILL.md` · `/AGENTS.md` · `/.cursorrules` | AI 入口文件 |
| `/FIGMA_MAP.md` · `/tokens.md` · `/recipes/*.md` | 文档 |

> 重新部署：`wrangler pages deploy . --project-name=ui-design-system-starter --branch=main`
> 下线：`wrangler pages deployment list --project-name=ui-design-system-starter` 拿到 deployment id 后删除，或在 dashboard 停用项目

---

## 📜 License

MIT — 你可以自由使用、修改、分发。

> 灵感来自真实的产品设计工作流（2026-09 Mstar / AutoCava）