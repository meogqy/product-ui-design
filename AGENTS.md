# AGENTS.md · 产品页面 UI 设计（Codex / Claude Code / OpenCode / Devin / Aider 等）

>本文件供不支持 skill 机制的 AI 工具使用。**开始任何 UI 设计任务前，先读
> [`SKILL.md`](./SKILL.md)，再填[`SITE-CONFIG.md`](./SITE-CONFIG.md)。**

---

## 这个包是什么

设计**要真实上线**的产品页面 UI 的规范包。自包含，复制整个目录即用。

---

## 开工前必做（顺序不可跳）

### 1. 读 `SKILL.md`

完整工作流（5 步）+ 10 条硬规则在那里。

### 2. 填 `SITE-CONFIG.md`

本包是**通用**的，不预设品牌色 / 市场 / 视口 / 触达工具。
**未配置就开工 = 必返工**（文档里所有 `<PRIMARY_COLOR>` 这类占位符会直接进你的页面）。

### 3. 确认产品线归属

若项目有多套视觉体系（主站/ 报告页 / 后台），**各自 token 不互通**。
先查 [`design-specs/tokens.md`](./design-specs/tokens.md)，不要凭印象套色。

---

## 10 条硬规则（不可协商）

| # | 规则 |
|---|------|
| 1 | **数据必须真实**。生产页面禁止 mock / 示意曲线 / 假序列 |
| 2 | **组件必须复用**。先查 `design-system/components/`，禁止自创新样式 |
| 3 | **token 不跨线借用**。主站色 ≠ 报告页色 ≠ 后台色 |
| 4 | **多环境必须分流**，交付物标注用了哪个环境 |
| 5 | **WCAG AA**：正文对比度 ≥4.5:1，控件边框 ≥3:1（**实测**，不目测） |
| 6 | **触控热区** ≥44×44px；主 CTA 高度 ≥48px（**实测**，不目测） |
| 7 | **每个可聚焦元素都要有 `:focus-visible`**（禁止 `outline: none` 了事） |
| 8 | **单文件响应式**，断点 1024px，禁止拆 PC/移动两个文件 |
| 9 | **按最低端机型压测**（见 `SITE-CONFIG.md`），不用你的开发机视口 |
| 10 | **图标走 Iconify 单源**；禁止 emoji 当图标，禁止混用多个图标库 |

---

## 数据真实性（最高优先级）

- 数据优先取页面 SSR 或公开接口
- ⚠️ SSR 未必是 JSON 对象：Nuxt 等用 **devalue扁平数组**，形如 `"price":93` 里的
  `93` 是**数组下标不是价格**。正则直取会拿到垃圾数
- ⚠️ 页面常混入推荐位其他条目的数据，必须与目标对象**名称比对**后再采信
- 拿不到真实点位 → **不画曲线**，只展示已确认的真实字段 + 链回平台
- 每处数据标注来源（注释或说明）

详见 [`rules/07-prototype-platform-data.mdc`](./rules/07-prototype-platform-data.mdc)。

---

## 技术范围

✅ **只产出静态产物**

- 单文件 HTML（Vanilla + CSS + 少量 JS）
- 静态资源（CDN 图 / SVG / CSS 变量）
- 跳转链接（`href` / 营销号直达链接）
- 模拟交互（hover / 点击高亮 / 前端校验 / 弹窗）

❌ **不做**

- 后端 API / 数据库 /鉴权 / 服务端逻辑
- 部署脚本（Docker / CI/CD / Nginx）
- 支付 / 订单 / 库存等真实业务逻辑
- **在页面里写假 `fetch('/api/...')` 假装真后端**

---

## 交付要求

每次交付必须附**自检报告**，含：

1. **数据溯源表** —— 每个数字/价格/评分的值与来源
2. **约束合规证据** —— 逐条勾选，指明在文件哪一行
3. **视觉对比**（复刻类任务）—— 目标值 vs 交付值逐项对比

格式见 [`rules/01-delivery-verification.mdc`](./rules/01-delivery-verification.mdc)。

**没有自检报告 = 交付未完成。**

---

## 采集用户信息时

只要采集手机号 / 邮箱 / 任何联系方式，CTA 下方**必须**有：

1. 隐私政策链接（用你所在市场的法规条款）
2. 中介/平台角色免责

> `rules/06-mx-lead-privacy.mdc` 是**墨西哥市场示例**，用到别的市场请改写。

---

## 常用入口

| 我要做什么 | 看哪里 |
|-----------|--------|
| 查有哪些组件 | [`design-system/components/README.md`](./design-system/components/README.md) |
| 一页扫完所有组件 | [`design-system/gallery.html`](./design-system/gallery.html) |
| 要个交互流程 pattern | [`design-system/recipes/README.md`](./design-system/recipes/README.md) |
| 改品牌色 | [`design-specs/tokens.md`](./design-specs/tokens.md) |
| 查图标 | [`ICON_SPEC.md`](./ICON_SPEC.md) |
| 查市场法规 | [`DESIGN_CONSTRAINTS.md`](./DESIGN_CONSTRAINTS.md) |
| 写 HTML 拿不准 | [`rules/03-html-prototype.mdc`](./rules/03-html-prototype.mdc) |

---

## License

MIT。见 [`LICENSE`](./LICENSE)。