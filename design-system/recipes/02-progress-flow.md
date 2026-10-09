# Recipe 02 · 进度流(Progress + Steps + Battery)

> **典型场景**:多步骤表单填写 / 车辆续航展示 / 加载进度可视化
> **使用组件**:18-progress (Linear/Battery/Circular/Stepper) + 20-steps

---

## 🎬 完整交互剧本

```
[用户进入"贷款申请"流程]
    ↓
① 顶部步骤条 (20-steps.html · 横排)
   5 步:选车型 → 填资料 → 信用评估 → 合同签署 → 提车
   当前:第 1 步 active / 其他灰色
    ↓ (用户进入"信用评估"页面)
② 评估进度展示 (18-progress.html · Linear + Battery)
   顶部:Linear 进度条 "评估中 65%"
   旁边:Battery 图标 "还剩约 6 小时"
    ↓ (评估完成)
③ Stepper 步骤切换到 done
   第 3 步:✓
   第 4 步:active
```

---

## 💻 实际写法

### 场景 A · 贷款申请多步骤表单

```html
<!-- 顶部步骤条 (横向) -->
<div class="steps-h">
  <div class="step-h done"><div class="step-h-icon">✓</div><div class="step-h-label">选车型</div></div>
  <div class="step-h done"><div class="step-h-icon">✓</div><div class="step-h-label">填资料</div></div>
  <div class="step-h active"><div class="step-h-icon">3</div><div class="step-h-label">信用评估</div><div class="step-h-desc">1-2 天</div></div>
  <div class="step-h"><div class="step-h-icon">4</div><div class="step-h-label">合同签署</div></div>
  <div class="step-h"><div class="step-h-icon">5</div><div class="step-h-label">提车</div></div>
</div>

<!-- 当前步骤内容 -->
<section class="step-content">
  <h2>您的资料已收到,正在评估中...</h2>
  
  <!-- 评估进度 Linear -->
  <div class="linear">
    <div class="linear-bar" style="width: 65%"></div>
  </div>
  <p>评估进度:65% · 还需约 6 小时</p>
  
  <!-- 剩余时间 Battery -->
  <div class="battery">
    <div class="battery-shell">
      <div class="battery-fill mid" style="width: 60%"></div>
    </div>
    <span class="battery-percent">6h / 10h</span>
  </div>
</section>
```

### 场景 B · 订单状态追踪

```html
<!-- 时间线(竖排) -->
<div class="timeline">
  <div class="tl-item done">
    <div class="tl-dot"></div>
    <div class="tl-content">
      <div class="tl-time">2026-09-25 10:30</div>
      <div class="tl-title">✓ 已提交贷款申请</div>
    </div>
  </div>
  <div class="tl-item done">
    <div class="tl-dot"></div>
    <div class="tl-content">
      <div class="tl-time">2026-09-25 14:20</div>
      <div class="tl-title">✓ 人工审核完成</div>
    </div>
  </div>
  <div class="tl-item active">
    <div class="tl-dot"></div>
    <div class="tl-content">
      <div class="tl-time">2026-09-26 09:00</div>
      <div class="tl-title">⏳ 信用评估中</div>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-content">
      <div class="tl-title">合同签署</div>
    </div>
  </div>
</div>
```

### 场景 C · 视频/文件上传进度

```html
<!-- 圆形进度(Circular) -->
<div class="circular">
  <svg width="120" height="120">
    <circle class="circular-track" cx="60" cy="60" r="48" stroke-width="8" fill="none"/>
    <circle class="circular-bar" cx="60" cy="60" r="48" stroke-width="8" fill="none"
      stroke-dasharray="301.59" stroke-dashoffset="120.6"/>
  </svg>
  <div class="circular-label">60%</div>
</div>
```

### 场景 D · 车辆续航展示

```html
<!-- 续航 Linear + Battery 组合 -->
<div class="vehicle-range">
  <h3>当前续航</h3>
  
  <!-- 进度条 -->
  <div class="linear">
    <div class="linear-bar success" style="width: 75%"></div>
  </div>
  
  <!-- 数字 + 单位 -->
  <div class="t-number-block">
    <span class="t-number-lg">375</span>
    <span class="t-unit">km</span>
  </div>
  
  <!-- 电池图标 -->
  <div class="battery">
    <div class="battery-shell">
      <div class="battery-fill high" style="width: 82%"></div>
    </div>
    <span class="battery-percent">82%</span>
  </div>
</div>
```

---

## 🔧 JS 动态控制

```javascript
// 步骤切换函数
function goToStep(stepNumber) {
  document.querySelectorAll('.step-h').forEach((el, i) => {
    el.classList.remove('done', 'active');
    if (i + 1 < stepNumber) el.classList.add('done');
    else if (i + 1 === stepNumber) el.classList.add('active');
  });
}

// 进度条更新
function updateProgress(percent) {
  document.querySelector('.linear-bar').style.width = percent + + '%';
  if (percent >= 80) document.querySelector('.linear-bar').classList.add('success');
  else if (percent >= 40) document.querySelector('.linear-bar').classList.add('warning');
}

// 模拟评估进度(从 0% 到 100%)
let progress = 0;
const interval = setInterval(() => {
  progress += 5;
  updateProgress(progress);
  if (progress >= 100) {
    clearInterval(interval);
    goToStep(4); // 跳到下一步
  }
}, 500);
```

---

## ⚠️ 易错点

1. **Stepper 段落条 vs 节点式**:5 步以内用段落条,5-7 步用节点式,7 步以上要拆分页面
2. **进度条颜色阈值**:
   - 0-40% → grey-100 底
   - 40-70% → yellow-500 (warning)
   - 70-100% → green-500 (success)
3. **Battery 颜色档位**:
   - ≥60% → 绿(high)
   - 30-60% → 黄(mid)
   - <30% → 红(low)
4. **Circular 进度**:仅用于"加载中/上传中"等单一数字场景,**不要在列表里**用
5. **时间线 + 当前态**:用 active + 黄色边框 + 黄色光晕,清楚区分历史节点

---

## 🎯 适用页面

| 页面 | 用此 recipe |
|------|-------------|
| 贷款申请多步骤 | ✅ Stepper + Loading + Linear |
| 订单详情 / 物流追踪 | ✅ Timeline + Battery 剩余时间 |
| 车辆续航展示 | ✅ Linear + Battery + 数字大字 |
| 文件/图片上传 | ✅ Circular 或 Linear |
| 注册/认证步骤 | ✅ Stepper 节点式 |
| 视频缓冲 / 在线播放 | ✅ Linear 缓冲条 |

---

## 📚 相关组件

- [`../components/18-progress.html`](../components/18-progress.html) ⭐ 最高频缺口
- [`../components/20-steps.html`](../components/20-steps.html)
- [`../components/19-typography.html`](../components/19-typography.html) (数字大字配套)
- [Recipe 01: 反馈流](./01-feedback-flow.md)
- [Recipe 03: 发现流程](./03-discovery-flow.md)