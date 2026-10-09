#!/usr/bin/env python3
"""构建 product-ui-design 在线文档站（Cloudflare Pages · 纯静态）

把包内 Markdown 规范转成 HTML，套统一文档壳，产出 publish 目录。
无运行时依赖：构建一次，静态托管。

用法:
    python3 scripts/build_docs.py
    python3 scripts/build_docs.py --out ../product-ui-design-docs

输出:
    <out>/index.html      入口页（Hero + 分组卡片网格）
    <out>/docs/*.html     各规范文档
    <out>/404.html
    <out>/.nojekyll
    <out>/design-system/  原始组件库（gallery 等）
"""
import argparse
import html
import pathlib
import re
import shutil
import sys

try:
    import markdown
    from pygments import highlight
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import get_lexer_by_name, TextLexer
except ImportError:
    sys.exit("缺少依赖: pip install markdown pygments")


# ── 设计 token（与 design-specs/tokens.md 同源） ──
T = {
    "y50": "#FFFAE9", "y500": "#FFCF20", "y600": "#E8BC1D",
    "b500": "#0056FA", "g500": "#7CB305", "r500": "#A8071A",
    "g50": "#F8F8F8", "g100": "#F1F1F1", "g200": "#DDDDDD",
    "g400": "#999999", "g600": "#666666", "g700": "#555555",
    "g900": "#222222", "white": "#FFFFFF",
}

ROOT = pathlib.Path(__file__).resolve().parent.parent
GH = "https://github.com/meogqy/product-ui-design"

# ── 文档注册表 ──
DOCS = [
    {"slug": "skill", "title": "Skill 主入口", "group": "核心", "icon": "skill",
     "desc": "5 步工作流 + 10 条硬规则。AI 加载这个就能按标准做页。",
     "src": "SKILL.md"},

    {"slug": "site-config", "title": "站点配置", "group": "核心", "icon": "config",
     "desc": "品牌色 / 市场 / 视口 / 数据源 / PII 策略。装完先填这个。",
     "src": "SITE-CONFIG.md"},

    {"slug": "delivery-verification", "title": "交付自检协议", "group": "规范", "icon": "checklist",
     "desc": "每次交付必附的自检报告格式。AI 说「做完了」不算数，必须出示证据。",
     "src": "rules/01-delivery-verification.mdc"},

    {"slug": "html-prototype", "title": "HTML/CSS 写法规范", "group": "规范", "icon": "code",
     "desc": "响应式 / 图标 / 品牌色 / C 端可见性 / 留资隐私等 12 节全规范。",
     "src": "rules/03-html-prototype.mdc"},

    {"slug": "platform-data", "title": "数据真实性协议", "group": "规范", "icon": "data",
     "desc": "平台已有维度禁止示意假曲线；拿不到真点位就不画图。",
     "src": "rules/07-prototype-platform-data.mdc"},

    {"slug": "constraints", "title": "市场与法规约束", "group": "规范", "icon": "gauge",
     "desc": "MX 市场专项：色彩层级 / 小屏视口 / WCAG 对比 / CAT 合规 / 性能预算。",
     "src": "DESIGN_CONSTRAINTS.md"},

    {"slug": "mx-lead-privacy", "title": "留资隐私（墨西哥）", "group": "合规", "icon": "law",
     "desc": "凡索要手机号的表单，必带 Política de Privacidad + 中介免责。",
     "src": "rules/06-mx-lead-privacy.mdc"},

    {"slug": "publishing", "title": "发布渠道协议", "group": "合规", "icon": "download",
     "desc": "静态产物唯一发布渠道：Cloudflare Pages。",
     "src": "rules/02-publishing.mdc"},

    {"slug": "tokens", "title": "设计 Token", "group": "组件", "icon": "palette",
     "desc": "颜色 / 字体 / 间距 / 圆角档位。改品牌色从这开始。",
     "src": "design-specs/tokens.md"},

    {"slug": "design-system", "title": "组件库总览", "group": "组件", "icon": "layers",
     "desc": "30 个组件源码 + 索引 + demo。",
     "src": "design-system/README.md"},

    {"slug": "icon-spec", "title": "图标映射表", "group": "组件", "icon": "icon",
     "desc": "品牌图标与功能图标的选择规则。",
     "src": "ICON_SPEC.md"},
]

GROUPS = ["核心", "规范", "合规", "组件"]
GROUP_DESC = {
    "核心": "装完先读这 2 篇 · AI 工具会自动加载",
    "规范": "AI 做页时必须过的硬约束",
    "合规": "按你的目标市场改写",
    "组件": "复用优先，造轮子违法",
}

ICONS = {
    "skill": '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>',
    "config": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "palette": '<path d="M12 2a10 10 0 0 0 0 20 2.5 2.5 0 0 0 2.5-2.5 2.5 2.5 0 0 1 2.5-2.5H19a3 3 0 0 0 3-3 10 10 0 0 0-10-10z"/><circle cx="7.5" cy="10.5" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="16.5" cy="10.5" r="1"/>',
    "checklist": '<path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 14l2 2 4-4"/>',
    "law": '<path d="M12 3v18M5 21h14M7 7l-4 7h8zM17 7l-4 7h8z"/>',
    "data": '<path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 5-8"/>',
    "layers": '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v4"/><path d="M7 10l5 5 5-5M12 5v10"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/>',
    "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "gauge": '<circle cx="12" cy="12" r="10"/><path d="M12 12l4-4"/><path d="M6 18h12"/>',
    "icon": '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
}

CSS = """
:root {
  --y50:%(y50)s; --y500:%(y500)s; --y600:%(y600)s;
  --b500:%(b500)s; --g500:%(g500)s; --r500:%(r500)s;
  --g50:%(g50)s; --g100:%(g100)s; --g200:%(g200)s;
  --g400:%(g400)s; --g600:%(g600)s; --g700:%(g700)s;
  --g900:%(g900)s; --white:%(white)s;
  --r-sm:6px; --r-md:8px; --r-lg:12px; --r-xl:16px;
  --shadow:0 4px 16px rgba(10,25,41,.06);
  --shadow-h:0 8px 24px rgba(10,25,41,.12);
  --font:'Inter',-apple-system,'PingFang SC','Helvetica Neue',sans-serif;
  --mono:'SF Mono','Menlo','Consolas',monospace;
}
* { box-sizing:border-box; margin:0; padding:0; }
html { scroll-behavior:smooth; }
body { font-family:var(--font); background:var(--g50); color:var(--g900);
       line-height:1.6; font-size:15px; -webkit-font-smoothing:antialiased; }
a { color:var(--b500); text-decoration:none; }
a:hover { text-decoration:underline; }

.topbar { position:sticky; top:0; z-index:100; background:var(--g900);
  color:var(--white); padding:0 24px; min-height:56px;
  display:flex; align-items:center; gap:16px; }
.topbar .brand { display:flex; align-items:center; gap:10px;
  font-weight:800; font-size:15px; color:var(--white); text-decoration:none; }
.topbar .brand:hover { text-decoration:none; }
.topbar .brand svg { width:26px; height:26px; }
.topbar .spacer { flex:1; }
.topbar .nav { display:flex; gap:4px; align-items:center; }
.topbar .nav a { color:rgba(255,255,255,.82); font-size:13px; font-weight:600;
  padding:8px 12px; border-radius:var(--r-sm); min-height:36px;
  display:inline-flex; align-items:center; gap:6px; }
.topbar .nav a:hover { background:rgba(255,255,255,.12); color:var(--white); text-decoration:none; }
.topbar .nav a.on { background:var(--y500); color:var(--g900); }
.topbar .gh { background:var(--y500); color:var(--g900)!important; font-weight:700; }

.wrap { max-width:1180px; margin:0 auto; padding:0 24px; }
.doc { padding:36px 0 72px; }

.hero { background:linear-gradient(135deg,var(--y50) 0%%,var(--white) 55%%,var(--g50) 100%%);
  border-bottom:1px solid var(--g200); padding:56px 0 48px; }
.hero .badge { display:inline-flex; align-items:center; gap:8px;
  background:var(--g900); color:var(--white); font-size:12px; font-weight:700;
  padding:6px 14px; border-radius:999px; margin-bottom:18px; }
.hero .badge svg { width:14px; height:14px; }
.hero h1 { font-size:40px; font-weight:800; letter-spacing:-.02em; margin-bottom:12px; }
.hero .sub { font-size:17px; color:var(--g600); max-width:720px; }
.hero .cta { display:flex; gap:12px; margin-top:28px; flex-wrap:wrap; }
.hero .cta a { display:inline-flex; align-items:center; gap:8px; font-weight:700;
  font-size:14px; padding:14px 24px; min-height:48px; border-radius:var(--r-md);
  transition:transform .15s, box-shadow .15s; }
.hero .cta a:hover { text-decoration:none; transform:translateY(-2px); }
.hero .cta a svg { width:17px; height:17px; }
.hero .cta .p { background:var(--g900); color:var(--white); box-shadow:var(--shadow-h); }
.hero .cta .p:hover { background:#111; }
.hero .cta .s { background:var(--white); color:var(--g900);
  border:1px solid var(--g200); box-shadow:var(--shadow); }
.hero .cta a:focus-visible, .topbar a:focus-visible, .card:focus-visible {
  outline:3px solid var(--y500); outline-offset:2px; }

.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
  gap:20px; margin-top:24px; }
.card { background:var(--white); border:1px solid var(--g200); border-radius:var(--r-lg);
  padding:24px; box-shadow:var(--shadow); display:block;
  transition:transform .18s, box-shadow .18s, border-color .18s; }
.card:hover { text-decoration:none; transform:translateY(-3px);
  box-shadow:var(--shadow-h); border-color:var(--y600); }
.card .ic { width:44px; height:44px; border-radius:var(--r-md);
  display:flex; align-items:center; justify-content:center; margin-bottom:16px;
  background:var(--y50); color:var(--g900); }
.card .ic svg { width:22px; height:22px; }
.card h3 { font-size:17px; font-weight:800; margin-bottom:8px; }
.card p { font-size:13.5px; color:var(--g600); line-height:1.55; }
.card .go { margin-top:14px; font-size:13px; font-weight:700; color:var(--b500);
  display:inline-flex; align-items:center; gap:5px; }
.card .go svg { width:15px; height:15px; }

.sec-h { margin:52px 0 6px; font-size:26px; font-weight:800; }
.sec-d { font-size:14px; color:var(--g600); }

.md { background:var(--white); border:1px solid var(--g200); border-radius:var(--r-lg);
  padding:36px; box-shadow:var(--shadow); }
.md h1 { font-size:30px; font-weight:800; margin:0 0 20px; letter-spacing:-.01em; }
.md h2 { font-size:21px; font-weight:800; margin:40px 0 14px;
  padding-top:20px; border-top:1px solid var(--g200); }
.md h2:first-of-type { border-top:0; padding-top:0; margin-top:28px; }
.md h3 { font-size:16px; font-weight:700; margin:26px 0 10px; }
.md p { margin:10px 0; }
.md ul,.md ol { margin:12px 0; padding-left:26px; }
.md li { margin:6px 0; }
.md table { border-collapse:collapse; width:100%%; margin:18px 0; font-size:13.5px; }
.md table th { background:var(--g100); text-align:left; font-weight:700;
  padding:10px 12px; border:1px solid var(--g200); }
.md table td { padding:10px 12px; border:1px solid var(--g200); vertical-align:top; }
.md blockquote { border-left:3px solid var(--y500); background:var(--y50);
  padding:14px 18px; margin:18px 0; color:var(--g700);
  border-radius:0 var(--r-sm) var(--r-sm) 0; }
.md blockquote p { margin:6px 0; }
.md code { font-family:var(--mono); font-size:12.5px; background:var(--g100);
  padding:2px 6px; border-radius:4px; color:var(--r500); }
.md pre { background:var(--g900); color:#E6EDF3; padding:18px;
  border-radius:var(--r-md); overflow-x:auto; margin:16px 0; line-height:1.5; }
.md pre code { background:none; padding:0; color:inherit; font-size:12.5px; }
.md hr { border:0; border-top:1px solid var(--g200); margin:32px 0; }

.src-note { margin-top:24px; font-size:13px; color:var(--g600); text-align:center; }
.src-note code { font-family:var(--mono); background:var(--g100);
  padding:2px 6px; border-radius:4px; }
.md svg.em { width:1.05em; height:1.05em; vertical-align:-0.16em; margin-right:2px; }
.md td svg.em:first-child { margin-right:5px; }

.foot { background:var(--g900); color:rgba(255,255,255,.72); padding:32px 0;
  font-size:13px; border-top:4px solid var(--y500); }
.foot .w { display:flex; justify-content:space-between; align-items:center;
  gap:16px; flex-wrap:wrap; }
.foot a { color:var(--white); font-weight:600; }

@media (min-width:1024px) {
  .md { padding:44px; }
  .hero h1 { font-size:44px; }
}
@media (max-width:720px) {
  .topbar .nav a:not(.gh) { display:none; }
  .hero h1 { font-size:30px; }
  .md { padding:20px; }
  .grid { grid-template-columns:1fr; }
  .foot .w { flex-direction:column; text-align:center; }
}
@media (prefers-reduced-motion:reduce) {
  * { animation:none!important; transition:none!important; }
}
""" % T


def esc(s):
    return html.escape(str(s), quote=True)


def icon(name):
    body = ICONS.get(name, ICONS["skill"])
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>' % body)


def head(title, desc):
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
           "viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' "
           "fill='%23222222'/%3E%3Cpath d='M50 18L18 34l32 16 32-16-32-16z' "
           "fill='%23FFCF20'/%3E%3Cpath d='M18 50l32 16 32-16M18 66l32 16 32-16' "
           "stroke='%23FFCF20' stroke-width='6' fill='none' stroke-linecap='round' "
           "%2F%3E%3C%2Fsvg%3E")
    return """<!DOCTYPE html>
<!--
  product-ui-design 在线文档站
  由 scripts/build_docs.py 从包内 Markdown 静态生成
  源仓库: %s
-->
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" href="%s">
<style>%s</style>
</head>
<body>""" % (GH, esc(title), esc(desc), fav, CSS)


def topbar(active=""):
    """顶栏。base 按页面深度修正相对路径（根='' /docs/='../'）"""
    base = "../" if active.startswith("docs/") else ""
    items = []
    for href, label in [("index.html", "首页"),
                        ("docs/skill.html", "Skill"),
                        ("docs/tokens.html", "Tokens"),
                        ("design-system/gallery.html", "Gallery")]:
        on = ' class="on"' if href == active else ""
        items.append('<a href="%s%s"%s>%s</a>' % (base, href, on, esc(label)))
    items.append('<a class="gh" href="%s" target="_blank" rel="noopener">%sGitHub</a>'
                 % (GH, icon("arrow")))
    return ('<header class="topbar">\n'
            '  <a class="brand" href="%sindex.html">%sproduct-ui-design</a>\n'
            '  <span class="spacer"></span>\n'
            '  <nav class="nav">%s</nav>\n'
            '</header>' % (base, icon("skill"), "".join(items)))


def foot():
    return ('<footer class="foot">\n  <div class="wrap w">\n'
            '    <span>product-ui-design · 通用 UI 设计 Skill · MIT License</span>\n'
            '    <span>由包内 Markdown 静态生成</span>\n'
            '  </div>\n</footer>')


def render_md(src_path, base="../"):
    """Markdown → HTML：剥 frontmatter + 修相对链接 + 代码高亮"""
    text = src_path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)

    # 相对 .md/.mdc 链接 → 已生成的文档页， 否则 → GitHub 源文件
    by_src = {d["src"]: d["slug"] for d in DOCS}

    def fix(m):
        tgt = m.group(1)
        if tgt.startswith(("http", "#", "mailto:", "/")):
            return m.group(0)
        norm = tgt.lstrip("./")
        if norm in by_src:
            return "](%s)" % (base + "docs/" + by_src[norm] + ".html")
        # 其它包内 Markdown → 指向 GitHub 源（保证链接不失效）
        if norm.endswith((".md", ".mdc")):
            return "](%s/blob/main/%s" % (GH, norm)
        # 目录链接 → 对应目录的 README
        if norm.endswith("/"):
            return "](%s/tree/main/%s" % (GH, norm)
        # 包内 HTML（gallery 等已随站点发布）→ 站点内路径
        if norm.endswith(".html"):
            depth = base.count("../")
            return "](%s%s" % ("../" * depth, norm)
        return m.group(0)

    text = re.sub(r"\]\(([^)\s]+)\)", fix, text)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    body = md.convert(text)

    fmt = HtmlFormatter(nowrap=True)

    def hl(m):
        lang, code = m.group(1), html.unescape(m.group(2))
        try:
            lexer = get_lexer_by_name(lang) if lang else TextLexer()
        except Exception:
            lexer = TextLexer()
        return highlight(code, lexer, fmt)

    body = re.sub(r'<pre><code class="language-([\w+#-]*)">(.*?)</code></pre>',
                  lambda m: "<pre><code>%s</code></pre>" % hl(m), body, flags=re.S)
    return emoji_to_svg(body)


# 功能性状态 emoji → 内联 SVG（规范：不用 emoji 当界面图标）
EMOJI_SVG = {
    "✅": ("#7CB305", '<polyline points="20 6 9 17 4 12"/>'),
    "✔️": ("#7CB305", '<polyline points="20 6 9 17 4 12"/>'),
    "❌": ("#A8071A", '<path d="M18 6L6 18M6 6l12 12"/>'),
    "✖️": ("#A8071A", '<path d="M18 6L6 18M6 6l12 12"/>'),
    "⚠️": ("#E8BC1D", '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    "⚠": ("#E8BC1D", '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    "⛔": ("#A8071A", '<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>'),
    "🚫": ("#A8071A", '<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>'),
}

# 章节标题里的装饰性 emoji → 内联 SVG（同一套图标，不新增依赖）
DECOR_SVG = {
    "📦": "layers", "🚀": "arrow", "🎨": "palette", "🔤": "code",
    "🎯": "target", "🔗": "arrow", "📋": "checklist", "🚦": "target",
    "🔒": "shield", "📚": "book", "📂": "layers", "🛠": "config",
    "🤝": "checklist", "🌍": "target", "📜": "book", "⭐": "icon",
    "🌐": "target", "📐": "ruler", "📄": "book", "🔍": "target",
    "📊": "data", "💡": "icon", "⚡": "gauge", "🧭": "target",
    "🔧": "config", "📊": "data",
}
DECOR_RE = re.compile("|".join(
    re.escape(k) for k in sorted(DECOR_SVG, key=len, reverse=True)) + "|️")


def emoji_to_svg(s):
    """功能性状态 emoji → 语义色 SVG；章节装饰 emoji → 中性 SVG"""
    def rep(m):
        ch = m.group(0)
        if ch in EMOJI_SVG:
            color, body = EMOJI_SVG[ch]
        elif ch in DECOR_SVG:
            name = DECOR_SVG[ch]
            color, body = "#999999", ICONS.get(name, ICONS["skill"])
        else:
            return ""
        return ('<svg class="em" viewBox="0 0 24 24" fill="none" stroke="%s" '
                'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                'aria-hidden="true">%s</svg>' % (color, body))
    return DECOR_RE.sub(rep, s)


def doc_page(d):
    src = ROOT / d["src"]
    if not src.exists():
        print("  ! 缺失源文件: %s" % d["src"])
        return None
    body = render_md(src, base="../")
    return """%s
%s
<main class="wrap doc">
  <article class="md">%s</article>
  <p class="src-note">源文件 <code>%s</code> · <a href="%s" target="_blank" rel="noopener">GitHub 源码</a></p>
</main>
%s
</body>
</html>""" % (
        head("%s · product-ui-design" % d["title"], d["desc"]),
        topbar(active="docs/%s.html" % d["slug"]),
        body, esc(d["src"]), GH, foot())


def index_page():
    blocks = []
    for g in GROUPS:
        entries = [d for d in DOCS if d["group"] == g]
        if not entries:
            continue
        cards = []
        for d in entries:
            cards.append("""      <a class="card" href="docs/%s.html">
        <div class="ic">%s</div>
        <h3>%s</h3>
        <p>%s</p>
        <span class="go">%s访问页面</span>
      </a>""" % (d["slug"], icon(d["icon"]), esc(d["title"]),
                 esc(d["desc"]), icon("arrow")))
        blocks.append("""    <h2 class="sec-h">%s</h2>
    <p class="sec-d">%s</p>
    <div class="grid">
%s
    </div>""" % (esc(g), esc(GROUP_DESC[g]), "\n".join(cards)))

    return """%s
%s
<main>
  <section class="hero">
    <div class="wrap">
      <span class="badge">%sMIT License · 复制整个目录即用</span>
      <h1>product-ui-design</h1>
      <p class="sub">一个自包含的 AI skill，用于设计要真实上线的产品页面 UI。强制复用包内组件与 token，接真实数据，过生产级可达性与响应式标准。</p>
      <div class="cta">
        <a class="p" href="%s/releases/tag/v2.0.0" target="_blank" rel="noopener">%s下载 v2.0.0</a>
        <a class="s" href="docs/skill.html">%s在线读文档</a>
        <a class="s" href="design-system/gallery.html">%s组件 Gallery</a>
      </div>
    </div>
  </section>

  <section class="wrap" style="padding:8px 0 72px">
%s
  </section>
</main>
%s
</body>
</html>""" % (
        head("product-ui-design · 通用 UI 设计 Skill",
             "自包含 AI skill：设计 tokens、WCAG AA 可达性、响应式规范、30 个组件。零外部依赖。"),
        topbar(active="index.html"),
        icon("shield"), GH, icon("download"), icon("book"), icon("layers"),
        "\n".join(blocks), foot())


def not_found_page():
    return """%s
%s
<main class="wrap doc">
  <div class="md">
    <h1>404</h1>
    <p>页面不存在。</p>
    <p><a href="index.html">回到首页</a> · <a href="docs/skill.html">读 Skill 文档</a></p>
  </div>
</main>
%s
</body>
</html>""" % (head("404 · product-ui-design", "页面不存在"), topbar(), foot())


def main():
    ap = argparse.ArgumentParser(description="构建 product-ui-design 文档站")
    ap.add_argument("--out", default=str(ROOT.parent / "product-ui-design-docs"))
    args = ap.parse_args()

    out = pathlib.Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / "docs").mkdir()

    # 1) 文档页
    n = 0
    for d in DOCS:
        page = doc_page(d)
        if page:
            (out / "docs" / ("%s.html" % d["slug"])).write_text(page, encoding="utf-8")
            n += 1
    print("✓ %d 篇文档页" % n)

    # 2) 原始静态资源（组件库 demo / gallery 等）
    for rel in ["design-system", "design-specs", "rules", "knowledge"]:
        s = ROOT / rel
        if s.exists():
            shutil.copytree(s, out / rel, dirs_exist_ok=True)
            cnt = sum(1 for f in (out / rel).rglob("*") if f.is_file())
            print("✓ %-16s %d 个文件" % (rel + "/", cnt))

    # 3) 入口 + 404 + nojekyll
    (out / "index.html").write_text(index_page(), encoding="utf-8")
    (out / "404.html").write_text(not_found_page(), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print("✓ index.html / 404.html / .nojekyll")

    # 4) 自检：失效链接 + emoji + 外部资源
    broken, emoji, ext = [], [], []
    for f in out.rglob("*.html"):
        s = f.read_text(encoding="utf-8", errors="ignore")
        if f.relative_to(out).parts[0] in ("design-system", "design-specs"):
            continue  # 原始组件库自带 demo，不在文档站校验范围
        for u in re.findall(r'href="([^"#][^"]*)"', s):
            if u.startswith(("http", "mailto:", "data:", "//")):
                continue
            u2 = u.split("#")[0].split("?")[0]
            if u2 and not (f.parent / u2).exists():
                broken.append((f.name, u2))
        for e in re.findall(r'[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]', s):
            if e not in EMOJI_SVG and e not in DECOR_SVG and e != "️":
                emoji.append((f.name, e))
        for u in re.findall(r'(?:href|src)="(https?://[^"]+)"', s):
            ext.append((f.name, u))

    total = sum(1 for f in out.rglob("*") if f.is_file())
    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    print("\n=== 构建自检 ===")
    print("  输出文件   : %d  (%.1f MB)" % (total, size / 1024 / 1024))
    print("  失效链接   : %d" % len(broken))
    for b in broken[:10]:
        print("      x %s -> %s" % b)
    print("  emoji 图标 : %d" % len(emoji))
    for e in emoji[:5]:
        print("      x %s %r" % e)
    print("  外部资源   : %d" % len(ext))
    for e in ext[:5]:
        print("      ! %s -> %s" % e)
    print()
    ok = not broken and not emoji
    print("✓ 通过 — 可部署" if ok else "x 存在问题，见上")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())