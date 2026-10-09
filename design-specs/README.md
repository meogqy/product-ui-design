# design-specs · 站点级设计规范

> **在这里改你的品牌色、字体、间距。** 组件源码在 [`../design-system/`](../design-system/)。

---

## 目录

| 子目录 | 内容 | 何时查 |
|--------|------|--------|
| [`tokens.md`](tokens.md) | **设计变量集中版** — 颜色 / 字体 / 间距 / 圆角 / 语义化命名 | **做 UI 第一步** |
| [`cards/`](cards/README.md) | 卡片类组件样式 reference（展示卡 / 价格卡 / 行动卡 / 对比卡） | 做列表或详情展示页时 |

> 通用组件库（按钮 / 输入 / 卡片 / 导航 / 弹窗 / Toast 等）不在这里，
> 在 [`../design-system/`](../design-system/)，一页总览见
> [`../design-system/gallery.html`](../design-system/gallery.html)。

---

## 🧭 决策树 · 什么时候查哪里

```
开始做 UI
  │
  ├─ 这是"卡片"吗？（列表项 / 详情展示 / 价格展示）
  │    └─ 是 → cards/README.md 查 → 有现成样式吗？
  │           ├─ 有 → 直接复用
  │           └─ 没有 → 评估是否值得新立（多次出现 → 立；一次 → 写在页面本地）
  │
  ├─ 这是"组件"吗？（按钮 / 输入 / 弹窗 / Toast / 导航…）
  │    └─ 是 → ../design-system/components/README.md 查 → 复用或改造
  │
  ├─ 需要完整色值 / 字号 / 间距
  │    └─ 是 → tokens.md（本文件的事实来源）
  │
  └─ 需要一个交互流程 pattern（提交反馈 / 多步流程 / 引导发现）
       └─ 是 → ../design-system/recipes/README.md
```

---

## 🚦 产品线分流

若你的项目有**多条产品线并存**（主站 / 报告页 / 后台等），先判定本页归属哪条：

| 产品线 | 典型路径 | 品牌色 | 字体 | 卡片圆角 | token 来源 |
|--------|---------|--------|------|---------|-----------|
| （填你的）主站 | `/` `/list/*` | `<PRIMARY_COLOR>` | `<系统栈或Web Font>` | `4/6/8/12` | `design-specs/tokens.md` |
| （填你的）报告页 | `/report/*` | `<SECONDARY_COLOR>` | `<WEB_FONT>` | `10px` | `design-specs/tokens.md` |
| （填你的）后台 | `/admin/*` | `<ADMIN_PRIMARY>` | `<系统栈>` | `6px` | `design-specs/tokens.md` |

> ⚠️ **产品线之间 token 不互通。** 跨线借用（给A 线灌 B 线的品牌色 / 圆角）会让用户
> 认不出「是不是同一个产品」。先查表，再动手。

---

## ⚠️ 按项目改写

本目录含**示例性**内容。用到自己的项目时替换：

| 内容 | 替换为 |
|------|--------|
| `tokens.md` 里的品牌色 | 你的品牌色（**实测生产页面**，别猜） |
| `cards/` 里的卡片样式 | 你的业务卡片（若业务不同） |
| 上表的产品线划分 | 你项目的实际划分 |

> 来源：原 Mstar 工作区 `visual-specs/` · 随包分发于 product-ui-design v2.0