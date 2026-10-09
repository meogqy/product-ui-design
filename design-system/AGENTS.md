# AGENTS.md · AI Agent 入口

> **本文件是 `ui-design-system-starter/` 的 AI 自动加载入口。**
> 被 OpenCode / Codex / Cursor / Aider / Devin / Gemini CLI 等多种工具读取。
> 复制到项目根目录后，AI 会在会话开始时自动加载本文件。

---

## 🎯 本项目是什么

一个**可分发的产品 UI 设计系统 + skill 包**：

- 25 个核心组件 + 5 张内容卡（单文件 HTML reference，CSS 变量驱动）
- 60 颜色 token + 25 字体 token
- 4 个组件组合 recipe（反馈流 / 进度流 / 发现流 / 内容卡）
- Figma 588 组件名 → HTML 文件映射表
- 6 个页面级 demo（5 个抓生产真数据 + 1 个组件集成沙盘）+ `demo/index.html` 索引页

**核心原则**：`gallery.html` → `components/README.md` → `recipes/` → `FIGMA_MAP.md` → `tokens.md`

---

## ⛔ 什么时候用本设计系统

**立即加载**（命中任一）：
- 做产品页面 / 上线页面 / 真实页面 / production
- 用现有组件 / 复用组件库 / design system
- 要求接真实数据 / WCAG AA / Core Web Vitals / 响应式

**不要加载**：
- 单 feature demo / 给老板评审 / mock 数据 OK
  → 那种场景用 `product-prototype-design` skill，不适用本套硬规则

---

## ⛔ 5 步流程（不许跳步）

### Step 1 — 判断是不是真生产 UI

| 是生产 UI | 不是 |
|---------|------|
| 用户在真实产品里看到的页面 | 单 feature demo |
| 接真实数据 | mock 数据 OK |
| 必须复用本目录组件 | 可自创样式 |
| 要过 WCAG AA + Core Web Vitals | 评审通过即可 |

判断错 → 换 skill，**别混用**。

### Step 2 — 复用视觉资产（⚡ 第一步必做，5 个查表路径）

按顺序查，**不要跳**：

1. **`gallery.html`** — 一页总览所有 30 组件 + 4 recipes
2. **`components/README.md`** — 组件索引 + 场景选型表 + 优先级矩阵
3. **`recipes/`** — 4 个组合 pattern（反馈流 / 进度流 / 发现流 / 内容卡）
4. **`FIGMA_MAP.md`** — Figma 588 组件名 → HTML 文件映射
5. **`tokens.md`** — 颜色 / 字体 / 间距 / 圆角 / 阴影 变量
6. **`components/`** + **`components/cards/`** — 现成组件 class

**决策路径**：
```
需求/设计稿
  → FIGMA_MAP.md 找对应 HTML
  → recipes/ 看有没有现成组合模式
  → 复制 components/ 的 class
  → 改 tokens.md 的 5 个颜色变量适配品牌
```

❌ 禁止自创新 token / 新组件样式 / 新图标来源

### Step 2.5 — ⚠️ 做平台页面时，必须核对生产环境真实值

> **这条是 2026-09-29 踩坑后加的。** `tokens.md` 里的值**可能已过时**。

**触发条件**：任务涉及 autocava.com.mx 或其他真实生产平台的页面。

**3 步核对（10 分钟）**：

```bash
# ① 抓生产 HTML
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..." \
  "https://www.autocava.com.mx" -o /tmp/ac.html

# ② 统计真实在用的颜色（看 class，不是看 CSS 变量定义）
grep -oE '\b(bg|text|border)-[0-9a-f]{3,6}\b' /tmp/ac.html | sort | uniq -c | sort -rn | head -20

# ③ 抓 CSS 找这些色的实际定义
grep -oE 'https://cdn\.autocava\.com\.mx/_nuxt/asset/.*\.css' /tmp/ac.html | \
  xargs -I{} curl -s {} | grep -oE '\-\-color-[0-9a-f]{3,6}\s*:\s*#[0-9a-f]{3,6}'
```

**判断主色的唯一正确方法**：
- ✅ 看**渲染 DOM 的 class**（`bg-ffcf20` = 黄色主色）
- ✅ 看**使用频次**（主色一定排在最前）
- ❌ **不要**看框架预置的色板变量

> 🚨 **真实翻车案例（2026-09-29）**：Autocava 用 Nuxt UI 框架，框架预置了完整的
> `--color-green-*` 色板，但**实际启用的是 Tailwind utility class 直写 hex（`bg-ffcf20` 黄色）**。
> AI 看到 green 色板就断定"主色是绿"，把整站改成绿色 —— **完全错了**。
> 用户反馈"主色明明是黄色"后，浏览器实测 DOM 才拿到真相。
>
> **教训**：框架默认色板 ≠ 品牌色。**永远看真实渲染结果，别看变量定义。**

#### 补充坑位（2026-09-30 抓 6 个 demo 时踩出）：车系图 ID 空间不统一

生产站有 **3 套** 车图路径，且**图 ID 与 `/auto/series/{id}` 不是同一套编号**：

| 路径 | 规则 | 备注 |
|------|------|------|
| `cdn.autocava.com.mx/car/series/{hash32}.png` | hash，与 seriesId 无关 | **当前主路径**（首屏 preload 用它） |
| `cdn.autocava.com.mx/series/white/{NNNN}.png` | 4 位编号，**独立 ID 空间** | 旧路径，部分车系有、部分 403 |
| `cdn.autocava.com.mx/car/serial/{2字母}/{hash}.jpg` | 街景图 | 车系页大图 |

**反例（别再犯）**：`/auto/series/510`（Toyota Hilux）的白底图是 `series/white/0113.png`，
而 `113` 在榜单里是 Chevrolet S10 Max —— **编号不对应车系**。
同理用 `/series/white/{seriesId}.png` 去拼会得到 403 或错车。

**正确取图方法**（按此顺序，勿跳）：
```bash
# ① 抓该车系自己的页面
curl -s "https://www.autocava.com.mx/auto/series/{id}" -o /tmp/s.html
# ② 取 payload 中【第一个】出现的车图 URL —— 那是本车系的，之后的是交叉推荐位
grep -oE 'https://cdn\.autocava\.com\.mx/(car/series/[a-f0-9]{32}\.png|series/white/[0-9]+\.png)' /tmp/s.html | head -1
# ③ 校验唯一性：20 台车批量抓完后，去重数量应等于车数
```
> ⚠️ 千万不要用 `sort -u` 再取第一个 —— 排序会打乱文档顺序，
> 导致 Captiva/CX-30/Groove/Magnite/CRETA 全指向同一张 `0031.png`。
> 必须用 `grep -oE ... | head -1`（**保序**）。

**图片内容必须核对车名**：抓完 20 台后，用每个车系页 `<title>` 的真实名
与榜单名逐一比对，全部对上才算数（本轮 20/20 ✅）。

### Step 3 — 接真实数据

- 数据从真实平台取（SSR / API / CMS）
- **环境分流**：stable（基础）· canary（灰度）· experiment（实验）
- ❌ 禁止用示意曲线 / 假序列冒充真点位
- ❌ 拿不到真数据 → 标 `[待PM确认]` 留空，**不要编**

### Step 4 — 生产级质量

| 项 | 要求 |
|----|------|
| 可达性 | WCAG AA（普通文字 4.5:1 / 大字 3:1）|
| 视口 | 按目标市场最低端机型压测（MX 360×800）|
| 性能 | LCP < 2.5s / FID < 100ms / CLS < 0.1 |
| 响应式 | 单文件自适应，断点 **1024px**（PC ≥1024 / H5 <1024）|

### Step 5 — 上线前自检

- [ ] 入口 → 交付 → 闭环 写了吗
- [ ] 7 条跨线硬规则全过（`principles.md`）
- [ ] 每个数字字段有数据溯源注释
- [ ] 0 个硬编码 hex（必须 CSS 变量）
- [ ] ICON 全走 Iconify 单源

---

## 🔒 10 条专属硬规则

| # | 规则 | 要求 |
|---|------|------|
| 1 | **数据来源** | 必须真实；无数据 = `[待PM确认]` |
| 2 | **组件复用** | 必须查 `components/`，禁止新立 |
| 3 | **颜色 token** | 按页面归属选（前台 / 后台 / 浮层）|
| 4 | **环境分流** | stable / canary / experiment，注明 |
| 5 | **可达性** | WCAG AA 必达 |
| 6 | **性能** | Core Web Vitals 必达 |
| 7 | **触达工具** | 目标市场合规通道（MX = WhatsApp，**禁微信**）|
| 8 | **留资隐私** | 留资表单必带隐私政策 + 中介免责 |
| 9 | **ICON** | 单一图标 CDN（Iconify）|
| 10 | **单文件自适应** | 一份 HTML 覆盖 PC + H5 |

---

## 📐 技术边界（不可越界）

**只写**：
- 单文件 HTML（Vanilla + CSS + 极少 JS）
- CDN 图 / SVG / CSS 变量
- 跳转链接（`href` / `wa.me/...`）
- 模拟交互（hover / 点击高亮 / 前端校验 / 弹窗）

**绝对不写**：
- ❌ 数据库 / 后端 API / 鉴权登录态 / SSR / server 目录
- ❌ Docker / K8s / CI/CD / Nginx
- ❌ 支付 / 订单 / 库存 / 退款逻辑
- ❌ Webhook / 定时任务 / 消息队列
- ❌ `fetch('/api/...')` 假装真接口
- ❌ `package.json` / `prisma` / `.vue` / `tailwind` / `nuxt`

**危险信号**（出现立即打断）：
`package.json` · `mongoose.connect()` · `app.get('/api/...')` · `useSession()` · `fetch('https://api.xxx.com/...')` · `prisma` · `nuxt`

---

## 📂 资源索引

| 资源 | 何时用 |
|------|--------|
| `gallery.html` | 第一次接触 — 一页看全部 |
| `tokens.md` | 所有 UI 设计第一步 |
| `components/` | 复用已有组件（25 个）|
| `components/cards/` | 列表/详情/搜索（5 张卡）|
| `recipes/` | 真实页面流程（4 个 pattern）|
| `FIGMA_MAP.md` | 看到 Figma 组件名 → 找 HTML |
| **真实页面 demo**（抓 autocava.com.mx 生产数据，2026-09-30） | 页面级落地参照（⚠️ `02` 号位空缺，原「价格详情」demo 未做） |
| `demo/index.html` | demo 索引页（从这找所有页面级 demo）|
| `demo/01-autocava-news-home.html` | 首页：32 车系 / 72 品牌 / 5 篇真实资讯 |
| `demo/03-series-detail-captiva.html` | 车系页：真实价格区间 / 4 版本 / 5 条真实评价 |
| `demo/04-cavi-lead-report.html` | CAVI 报告留资页：真实 WhatsApp + 表单校验 + 隐私脚注 |
| `demo/05-car-list-filter.html` | 车型列表页：20 台真实车系 + INEGI 分榜 + 可用筛选 |
| `demo/06-rank-ventas.html` | 排行榜页：INEGI 2026-08 Top 20 真实销量 |
| `demo/product-detail-page.html` | 组件集成沙盘（mock 文案，**非生产页**）|
| `principles.md` | 7 条跨线硬规则 |
| `SKILL.md` | 本文件完整版 |

---

## 🛠️ 适配你的项目

| 你的项目 | 改哪 |
|----------|------|
| 品牌色 | `tokens.md` `--yellow-500` |
| 字体家族 | `tokens.md` `--font-sans` |
| 触达工具 | `principles.md` §1 + 组件里的链接 |
| 隐私合规 | `principles.md` §5 + 链接 |
| 组件/页面 | 直接编辑 `components/` `demo/` |

---

**同规则的其他入口**：`.cursorrules`（Cursor/Cline）· `CLAUDE.md`（Claude Code）
