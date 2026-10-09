# 生产环境采集产物 · 可复核

> 采集时间：2026-09-29 · 环境：`https://www.autocava.com.mx?ac_ab=stable` · Desktop UA
> 用途：证明 `tokens.md` v2 每个值都来自真实渲染，非推测

## 文件

| 文件 | 内容 | 大小 |
|------|------|------|
| `nuxt-ui-colors.css` | `<style id="nuxt-ui-colors">` 原始块 · 77 个色阶的原始 oklch 值 | 6,533 B |
| `oklch2hex.py` | oklch → sRGB hex 转换脚本（可复跑验证）| 1.4 KB |

## 复现方式

```bash
# 1. 抓页面
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..." \
  "https://www.autocava.com.mx?ac_ab=stable" -o ac_real.html

# 2. 提取 nuxt-ui-colors 块
python3 -c "
h=open('ac_real.html',encoding='utf-8',errors='ignore').read()
i=h.find('<style id=\"nuxt-ui-colors\">'); j=h.find('</style>',i)
open('nuxt_ui_colors.txt','w').write(h[i:j])"

# 3. 转 hex
python3 oklch2hex.py
```

## 关键发现

- **主色是绿色不是黄色** — v1 token 记录的是旧品牌期
- **框架是 Nuxt UI v3**（`--ui-*` 体系），不是 shadcn/ui
- **色彩空间是 oklch**，不是 sRGB
- **中性色是 Slate**（冷灰），不是自定义暖灰
- **字体是系统栈**，Roboto 非首选
- `--color-primary: #ffc422`（黄）仍在 CSS 里但仅 1 处引用 = 迁移期遗留

## 引用来源（生产 CSS）

```
https://cdn.autocava.com.mx/_nuxt/asset/entry.v3.B2FGwc4U.css
https://cdn.autocava.com.mx/_nuxt/asset/main.v3.Q2DHlO0l.css      (269 KB)
https://cdn.autocava.com.mx/_nuxt/asset/common.v3.D4Yo3P9Y.css
https://cdn.autocava.com.mx/_nuxt/asset/PageFooter.v3.Cwklbi1i.css
... 共 9 个
```
