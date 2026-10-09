# CLAUDE.md · 产品页面 UI 设计

> 本文件供 Claude Code 自动加载。

## 必读（按顺序，不可跳）

1. **读 `SKILL.md`** —— 完整工作流（5 步）与 10 条硬规则
2. **填 `SITE-CONFIG.md`** —— 品牌色 / 市场 / 视口 / 触达工具 / 数据来源

> ⚠️ **未填 SITE-CONFIG 就开工 = 必返工。** 规范里所有 `<PRIMARY_COLOR>` 这类占位符会直接进你的页面。

## 10 条硬规则

1. **数据必须真实** —— 生产页面禁止 mock / 示意曲线 / 假序列
2. **组件必须复用** —— 先查 `design-system/components/`，禁止自创新样式
3. **token 不跨线借用** —— 主站色 ≠ 报告页色 ≠ 后台色
4. **多环境必须分流** —— 交付物标注用了哪个环境
5. **WCAG AA** —— 正文对比度 ≥4.5:1，控件边框 ≥3:1（**实测**不目测）
6. **触控热区 ≥44×44px** —— 主 CTA ≥48px（**实测**不目测）
7. **每个可聚焦元素都要有 `:focus-visible`** —— 禁止 `outline: none` 了事
8. **单文件响应式** —— 断点 1024px，禁止拆 PC/移动两个文件
9. **按最低端机型压测** —— 不用你的开发机视口
10. **图标走 Iconify 单源** —— 禁止 emoji 当图标，禁止混用多个图标库

## 动手前先查

| 我要做什么 | 看哪里 |
|-----------|--------|
| 有哪些组件 | `design-system/components/README.md` |
| 一页扫完所有组件 | `design-system/gallery.html` |
| 交互流程 pattern | `design-system/recipes/README.md` |
| 改品牌色 / 查色值 | `design-specs/tokens.md` |
| 查图标 | `ICON_SPEC.md` |
| 写 HTML 拿不准 | `rules/03-html-prototype.mdc` |
| 交付前自检 | `rules/01-delivery-verification.mdc` |

## 技术范围

✅ 静态产物：单文件 HTML（Vanilla + CSS + 少量 JS）、静态资源、跳转链接、模拟交互。

❌ 不写后端 API / 数据库 / 鉴权 / 服务端逻辑 / 部署脚本 / 真实业务逻辑。
❌ 禁止写假 `fetch('/api/...')` 假装真后端。

## 交付要求

每次交付**必须附自检报告**（数据溯源表 + 约束合规证据，逐条指明行号）。
格式见 `rules/01-delivery-verification.mdc`。**没有自检报告 = 交付未完成。**