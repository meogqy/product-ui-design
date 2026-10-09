# Recipe 01 · 反馈流(Modal + Toast + Loading + Empty State)

> **典型场景**:用户点 CTA → 弹出 Modal 填表 → 提交 → Loading → 成功 Toast / 失败 Empty State
> **使用组件**:09-modal + 10-toast + 07-loading + 08-empty-state

---

## 🎬 完整交互剧本

```
[用户点击"立即申请"按钮]
    ↓
① Modal 弹窗打开 (09-modal.html)
   标题:"填写联系方式"
   内容:姓名输入 + 手机号输入
   主 CTA:"提交申请"
   关闭:× / 取消 / ESC
    ↓ (用户填写完成,点提交)
② Loading 状态切换 (07-loading.html)
   Modal 内部按钮 loading 中
   "正在提交..."
    ↓ (200-500ms 后)
③ 成功 → Modal 关闭 + Toast 弹出 (10-toast.html)
   Toast 类型:success
   消息:"提交成功!销售将 1 小时内联系您"
   持续:3 秒后自动消失
    ↓ (3 秒)
④ Toast 消失,用户停留在原页面
    ↓
⑤ 如果失败 → Modal 内显示 Empty State (08-empty-state.html)
   空状态文案:"网络异常,请重试"
   重试按钮
```

---

## 💻 实际写法

```html
<!-- 1. 引入 CSS 变量 + 各组件样式 -->
<style>
:root {
  --yellow-500: #FFCF20;
  --grey-100: #F1F1F1;
  --grey-600: #666666;
  --grey-900: #222222;
  /* ... */
}

/* 直接复用各组件 CSS,本文件不重写 */
</style>

<!-- 2. HTML 结构 -->
<button class="btn-primary" onclick="openApplyModal()">立即申请</button>

<!-- Modal -->
<div class="modal-overlay" id="applyModal" style="display:none">
  <div class="modal-card">
    <div class="modal-header">
      <h3>填写联系方式</h3>
      <button onclick="closeApplyModal()">×</button>
    </div>
    <div class="modal-body">
      <input class="input" placeholder="姓名" />
      <input class="input" placeholder="手机号" />
      <!-- Loading 状态(默认隐藏) -->
      <div class="loading-state" id="modalLoading" style="display:none">
        <div class="loading-spinner"></div>
        <span>正在提交...</span>
      </div>
      <!-- Empty State 失败(默认隐藏) -->
      <div class="empty-state" id="modalError" style="display:none">
        <div class="empty-icon">⚠️</div>
        <h4>网络异常,请重试</h4>
        <button class="btn-secondary" onclick="retrySubmit()">重试</button>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn-secondary" onclick="closeApplyModal()">取消</button>
      <button class="btn-primary" id="submitBtn" onclick="submitForm()">提交申请</button>
    </div>
  </div>
</div>

<!-- 3. JS 串联流程 -->
<script>
function openApplyModal() {
  document.getElementById('applyModal').style.display = 'flex';
  resetModalStates();
}

function closeApplyModal() {
  document.getElementById('applyModal').style.display = 'none';
  resetModalStates();
}

function resetModalStates() {
  document.getElementById('modalLoading').style.display = 'none';
  document.getElementById('modalError').style.display = 'none';
  document.getElementById('submitBtn').disabled = false;
}

function submitForm() {
  // 1. 切 Loading
  document.getElementById('modalLoading').style.display = 'flex';
  document.getElementById('submitBtn').disabled = true;

  // 2. 模拟 API 调用
  setTimeout(() => {
    const success = Math.random() > 0.3; // 70% 成功率
    
    if (success) {
      // 3. 成功:关 Modal + Toast
      closeApplyModal();
      showToast('提交成功!销售将 1 小时内联系您', 'success');
    } else {
      // 3. 失败:Loading → Empty State
      document.getElementById('modalLoading').style.display = 'none';
      document.getElementById('modalError').style.display = 'block';
      document.getElementById('submitBtn').disabled = false;
    }
  }, 1200);
}

function retrySubmit() {
  document.getElementById('modalError').style.display = 'none';
  submitForm();
}

function showToast(msg, type) {
  // 复用 10-toast.html 的 toast 容器
  const toast = document.getElementById('toast');
  toast.className = 'toast show ' + type;
  toast.querySelector('.toast-msg').textContent = msg;
  setTimeout(() => toast.classList.remove('show'), 3000);
}
</script>
```

---

## ⚠️ 易错点

1. **Loading 位置**:Loading 应该**在 Modal 内**,不要让整个 Modal 消失。否则用户会以为页面卡死
2. **Toast 类型**:success(✅)/ info(ℹ️)/ warning(⚠️)/ error(❌) 4 种,根据场景选
3. **Empty State 重试**:失败必须有重试按钮,不能只显示错误就完了
4. **Modal 关闭**:成功后**自动关闭**,失败保留 Modal 让用户改
5. **按钮 disabled**:Loading 时禁用提交按钮,防重复提交
6. **可访问性**:ESC 关闭 Modal + 焦点 trap + ARIA role="dialog"

---

## 🎯 适用页面

| 页面 | 用此 recipe |
|------|-------------|
| 留资表单 | ✅ 提交 + 成功 Toast |
| 申请贷款 | ✅ Modal + Loading + 成功跳转 |
| 预约试驾 | ✅ 选时间 → 提交 |
| 评价 / 评论提交 | ✅ Loading → Toast |
| 删除确认 | ✅ Modal 确认 + Toast 反馈 |

---

## 📚 相关组件

- [`../components/09-modal.html`](../components/09-modal.html)
- [`../components/10-toast.html`](../components/10-toast.html)
- [`../components/07-loading.html`](../components/07-loading.html)
- [`../components/08-empty-state.html`](../components/08-empty-state.html)
- [Recipe 02: 进度流程](./02-progress-flow.md)
- [Recipe 03: 发现流程](./03-discovery-flow.md)