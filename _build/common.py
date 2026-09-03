# -*- coding: utf-8 -*-
"""Shared render helpers used by every design template."""

from data import PROFILE, GA_ID, FOOTER_CREDIT

# ---------------------------------------------------------------------------
# Small atoms
# ---------------------------------------------------------------------------

def authors_html(pub, me_cls="me", sep=", "):
    parts = []
    for name, url, is_me in pub["authors"]:
        if is_me:
            parts.append('<span class="%s">%s</span>' % (me_cls, name))
        elif url:
            parts.append('<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, name))
        else:
            parts.append('<span class="au">%s</span>' % name)
    return sep.join(parts)


def links_html(pub, sep=None, cls="lnk"):
    if sep is None:
        sep = '<span class="sep">/</span>'
    out = []
    for label, url in pub.get("links", []):
        if url:
            out.append('<a class="%s" href="%s" target="_blank" rel="noopener">%s</a>' % (cls, url, label))
        else:
            out.append('<span class="%s off" title="coming soon">%s</span>' % (cls, label))
    return sep.join(out)


def media_html(pub, base, cls="thumb"):
    kind, src = pub["media"]
    src = base + src
    if kind == "video":
        return ('<video class="%s" src="%s" autoplay muted loop playsinline '
                'preload="metadata"></video>' % (cls, src))
    alt = pub["title"].split(":")[0]
    return '<img class="%s" src="%s" alt="%s" loading="lazy" decoding="async">' % (cls, src, alt)


def venue(pub, short=False):
    if short:
        return pub.get("venue_short", pub["venue"])
    return pub["venue"]


def venue_year(pub, short=False):
    return "%s %s" % (venue(pub, short), pub["year"])


def profile_links(sep=None, cls="lnk", icons=False):
    if sep is None:
        sep = '<span class="sep">/</span>'
    out = []
    for label, url, icon in PROFILE["links"]:
        ic = '<i class="%s" aria-hidden="true"></i> ' % icon if icons else ""
        out.append('<a class="%s" href="%s"%s>%s%s</a>'
                   % (cls, url, '' if url.startswith("mailto:") else ' target="_blank" rel="noopener"', ic, label))
    return sep.join(out)


def bio_paras(cls="bio"):
    return "\n".join('<p class="%s">%s</p>' % (cls, p) for p in PROFILE["bio"])


# ---------------------------------------------------------------------------
# Page scaffolding
# ---------------------------------------------------------------------------

RESET = """
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0}
img,video{max-width:100%;height:auto;display:block}
a{color:inherit}
h1,h2,h3,h4,p,ul,ol,figure{margin:0}
ul{padding:0;list-style:none}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
details summary::-webkit-details-marker{display:none}
:focus-visible{outline:2px solid currentColor;outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
"""

GA = """
<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '%s');
</script>
""" % (GA_ID, GA_ID)

FA = ('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" '
      'crossorigin="anonymous" referrerpolicy="no-referrer">\n'
      '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.4/css/academicons.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">')


def page(css, body, base, fonts="", extra_head="", theme="#ffffff", icons=False,
         preview=None, body_class=""):
    """Assemble a complete standalone HTML document."""
    bar = ""
    if preview:
        bar = ('<a class="__gallery" href="index.html">&#8592; all designs '
               '<b>%s</b></a>' % preview)
        css += """
.__gallery{position:fixed;z-index:9999;left:50%;transform:translateX(-50%);bottom:14px;
  font:600 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.04em;
  background:#111;color:#fff;padding:9px 14px;border-radius:999px;text-decoration:none;
  box-shadow:0 6px 24px rgba(0,0,0,.28);opacity:.55;transition:opacity .15s}
.__gallery:hover{opacity:1;color:#fff}
.__gallery b{font-weight:400;opacity:.6;margin-left:2px}
@media print{.__gallery{display:none}}
"""
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="%(theme)s">
<title>%(name)s</title>
<meta name="description" content="Zechu (Steven) Li — PhD student at PEARL Lab. Reinforcement learning, robotics, and scalable systems.">
<link rel="icon" href="%(base)s%(photo)s">
%(fonts)s
%(icons)s
%(extra)s
<style>%(reset)s%(css)s</style>
</head>
<body%(bodyclass)s>
%(body)s
%(bar)s
%(ga)s
</body>
</html>
""" % {
        "theme": theme,
        "name": PROFILE["name"],
        "base": base,
        "photo": PROFILE["photo"],
        "fonts": fonts,
        "icons": FA if icons else "",
        "extra": extra_head,
        "reset": RESET,
        "css": css,
        "body": body,
        "bar": bar,
        "ga": GA,
        "bodyclass": ' class="%s"' % body_class if body_class else "",
        }


def footer_html(cls="foot"):
    return ('<footer class="%s"><p>%s</p></footer>' % (cls, FOOTER_CREDIT))


# ---------------------------------------------------------------------------
# Shared JS: scroll-spy for designs with in-page navigation
# ---------------------------------------------------------------------------

SCROLLSPY = """
<script>
(function(){
  var links = [].slice.call(document.querySelectorAll('[data-spy] a[href^="#"]'));
  if(!links.length) return;
  var map = {};
  links.forEach(function(a){
    var el = document.getElementById(a.getAttribute('href').slice(1));
    if(el) map[el.id] = a;
  });
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        links.forEach(function(a){a.classList.remove('on');});
        if(map[e.target.id]) map[e.target.id].classList.add('on');
      }
    });
  }, {rootMargin:'-25% 0px -70% 0px'});
  Object.keys(map).forEach(function(id){obs.observe(document.getElementById(id));});
})();
</script>
"""
