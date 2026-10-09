> ⚠️ **来源说明**：本文件含项目特定示例（品牌名 / 市场 / 平台专有参数）。
> 作为通用参考可用，但**具体值需按 [`SITE-CONFIG.md`](./SITE-CONFIG.md) 替换**后使用。
> 原路径：Mstar 工作区 · 随包分发于 product-ui-design v2.0

# AutoCava 图标规范

## 图标来源

所有项目图标统一使用 **Simple Icons** (https://simpleicons.org/)

## 使用方法

### 1. CDN 引用
```html
<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
```

### 2. 图标格式
```html
<span class="iconify" data-icon="simple-icons:[品牌名称]" data-width="20" data-height="20"></span>
```

## 常用图标映射

| 图标名称 | Simple Icons 标识 | 用途 |
|---------|------------------|------|
| WhatsApp | `simple-icons:whatsapp` | WhatsApp 联系方式 |
| Facebook | `simple-icons:facebook` | Facebook 分享 |
| Twitter/X | `simple-icons:x` | Twitter 分享 |
| Email | `simple-icons:microsoftoutlook` | 邮件分享 |
| Link | `simple-icons:linktree` | 复制链接 |
| Phone | `simple-icons:googlephone` | 电话咨询 |
| Share | `simple-icons:addthis` | 分享按钮 |
| Copy | `simple-icons:copy` | 复制链接 |

## 示例代码

### WhatsApp 按钮
```html
<button class="btn-whatsapp">
  <span class="iconify" data-icon="simple-icons:whatsapp" data-width="20" data-height="20"></span>
  WhatsApp
</button>
```

### 分享图标
```html
<span class="iconify" data-icon="simple-icons:addthis" data-width="24" data-height="24"></span>
```

### 复制链接
```html
<span class="iconify" data-icon="simple-icons:copy" data-width="20" data-height="20"></span>
```

## 颜色

图标默认颜色继承父元素颜色，如需指定：
```html
<span class="iconify" data-icon="simple-icons:whatsapp" style="color: #25D366;"></span>
```

## 常用品牌颜色

| 品牌 | 颜色代码 |
|-----|---------|
| WhatsApp | `#25D366` |
| Facebook | `#1877F2` |
| X (Twitter) | `#000000` |
| Gmail | `#EA4335` |

