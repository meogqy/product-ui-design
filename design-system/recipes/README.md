# Recipes · 组件组合模式

> **目的**：把 25 个组件 + 5 张卡 **组合起来**完成真实页面流程,不只单组件 demo
> **每个 recipe = 一个完整交互剧本 + HTML/JS 代码模板 + 易错点**

---

## 📦 4 个常用模式

| # | Recipe | 典型场景 | 使用组件 |
|---|--------|---------|---------|
| 01 | [反馈流](./01-feedback-flow.md) | 用户点 CTA → Modal → Loading → Toast / Empty State | Modal + Toast + Loading + Empty State |
| 02 | [进度流](./02-progress-flow.md) | 多步骤表单 / 续航 / 上传 / 订单追踪 | Progress (Linear/Battery/Circular/Stepper) + Steps |
| 03 | [发现流](./03-discovery-flow.md) | 选车 → 看榜 → 筛选 → 收藏 | Brand Grid + Ranking + Filter + Favorite + Product Card |
| 04 | [内容卡组合](./04-card-composition.md) | 首页 / 列表 / 详情 / 搜索结果的卡片混排 | Content + Article + Product + Brand Card |

---

## 🎬 Recipe 选择决策树

```
[新页面需求]
    ↓
是否有"提交/操作反馈"? ─→ 是 → Recipe 01 (反馈流)
    ↓ 否
是否有"多步骤/进度展示"? ─→ 是 → Recipe 02 (进度流)
    ↓ 否
是否有"浏览/筛选/收藏"? ─→ 是 → Recipe 03 (发现流)
    ↓ 否
是否有"卡片混排展示"? ─→ 是 → Recipe 04 (内容卡组合)
    ↓ 否
单组件 demo 即可 (参考 components/ 各 HTML 文件)
```

---

## 🚦 实战页面映射

| 页面类型 | 用哪些 Recipe |
|---------|--------------|
| 首页 | Recipe 04 + Recipe 03 |
| 选车 / 车型库 | Recipe 03 + Recipe 04 |
| 车型详情页 | Recipe 04 + Recipe 01 (留资) |
| 列表页(车型/资讯) | Recipe 03 + Recipe 04 |
| 文章详情页 | Recipe 04 + Recipe 02 (视频) |
| 贷款申请 | Recipe 02 + Recipe 01 |
| 表单页(留资/预约) | Recipe 01 + Recipe 02 |
| 搜索结果 | Recipe 03 |
| 个人中心 | Recipe 04 (我的收藏 = Product + Article) |
| 排行榜页 | Recipe 03 + Recipe 04 |

---

## 📚 相关资源

- [`../components/`](../components/) — 25 个组件单独 demo
- [`../components/cards/`](../components/cards/) — 5 张内容卡
- [`../demo/`](../demo/) — 完整生产页 demo(product-detail-page.html)
- [`../FIGMA_MAP.md`](../FIGMA_MAP.md) — Figma 组件名 → HTML 文件映射表
- [`../SKILL.md`](../SKILL.md) — AI skill 入口