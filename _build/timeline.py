# -*- coding: utf-8 -*-
"""The homepage design: one column, publications grouped by year.

Everything (header, bio, section headings, cards) shares a single left and
right edge. Selected publications are always visible; the rest of each year
sits behind a native <details> fold directly beneath them, so the page needs
no JavaScript.
"""

from collections import OrderedDict

from data import PROFILE, SELECTED, OTHER, PROJECTS, BOOK
from common import (page, authors_html, links_html, media_html, venue_year,
                    profile_links, bio_paras)

PRECONNECT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
              '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
FONTS = (PRECONNECT + '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Google+Sans:wght@400;500;600;700&display=swap">')


CSS = """
:root{
  --bg:#fbfbfc; --paper:#fff; --ink:#131519; --body:#3a3f48; --dim:#5d626c; --dim2:#9ba0aa;
  --line:#e6e7ea; --card-line:#ececf0; --well:#f5f5f7;
  --acc:#5b3df5; --acc-ink:#4a30d6; --acc-soft:rgba(91,61,245,.08); --acc-line:rgba(91,61,245,.38);
  --pf:224px;
  --c-violet:#6d4bff;
}
body{background:
    radial-gradient(620px 420px at 12% -6%,rgba(109,75,255,.13),transparent 70%),
    radial-gradient(560px 380px at 58% -12%,rgba(47,124,246,.10),transparent 70%),
    radial-gradient(520px 420px at 96% 4%,rgba(232,69,124,.10),transparent 70%),
    var(--bg);
  background-repeat:no-repeat;color:var(--ink);font:400 16.5px/1.7 "Google Sans",system-ui,sans-serif;
  -webkit-font-smoothing:antialiased}
a{text-decoration:none}
.wrap{max-width:1020px;margin:0 auto;padding:0 28px 96px}

/* inline links: accent text, no underline */
.bio a,.plist a{color:var(--acc);font-weight:500;transition:color .15s}
.bio a:hover,.plist a:hover{color:var(--acc-ink)}

/* ---------- header ---------- */
header{padding:96px 0 0;display:grid;grid-template-columns:minmax(0,1fr) var(--pf);
  gap:56px;align-items:start}
.pf{width:var(--pf);height:var(--pf);object-fit:cover;border-radius:50%;background:var(--well);
  box-shadow:0 0 0 1px rgba(19,21,25,.06),0 14px 32px -20px rgba(19,21,25,.45)}
h1{font-size:clamp(34px,5.4vw,48px);font-weight:500;letter-spacing:-.02em;line-height:1.1}
.social{margin-top:28px;display:flex;flex-wrap:wrap;gap:8px}
.social a{--b:var(--c-violet);display:inline-flex;align-items:center;gap:7px;font-size:14px;font-weight:500;
  color:var(--ink);border:1px solid color-mix(in srgb,var(--b) 26%,transparent);
  background:var(--paper);border-radius:999px;padding:7px 14px;
  transition:background .15s,border-color .15s,color .15s,transform .15s}
.social a[href*="scholar.google"]{--b:#4285f4}
.social a[href*="github.com"],.social a[href*="x.com"]{--b:#1f2328;border-color:var(--line)}
.social a[href*="linkedin.com"]{--b:#0a66c2}
.social a:hover{background:var(--b);border-color:var(--b);color:#fff;transform:translateY(-1px)}
.social i{color:var(--b);font-size:14px;width:14px;text-align:center;transition:color .15s}
.social .ico{width:15px;height:15px;fill:var(--b);flex:none;transition:fill .15s}
.social a:hover i{color:#fff}
.social a:hover .ico{fill:#fff}
.bio{margin-top:20px;display:grid;gap:16px;color:var(--body)}

/* ---------- section headings ---------- */
.sec{margin:72px 0 24px;display:flex;align-items:center;gap:16px}
.sec h2{font-size:20px;font-weight:500;line-height:1.3;letter-spacing:-.01em;white-space:nowrap}
.sec .ln{flex:1;height:1px;background:var(--line)}
.note{font-size:13px;line-height:1.5;color:var(--dim2);margin:-18px 0 28px}

/* ---------- year groups ---------- */
.grp + .grp{margin-top:40px}
.yr{font-size:14px;font-weight:600;line-height:1.3;letter-spacing:.08em;color:var(--dim);margin:0 0 12px}
.cards{display:grid;gap:16px;min-width:0}

/* ---------- per-year fold ---------- */
.more>summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:8px;
  font-size:14px;font-weight:600;color:var(--dim);padding:2px 0;transition:color .15s}
.more>summary:hover{color:var(--acc)}
.more>summary .chev{font-size:9px;transition:transform .2s}
.more[open]>summary .chev{transform:rotate(180deg)}
.more>summary:focus-visible{outline:2px solid var(--acc);outline-offset:4px;border-radius:4px}
.more .lbl-open{display:none}
.more[open] .lbl-shut{display:none}
.more[open] .lbl-open{display:inline}
.more .node{margin-top:16px}
.more[open]>summary{margin-bottom:0}

/* ---------- cards ---------- */
.card{display:grid;grid-template-columns:332px minmax(0,1fr);gap:28px;align-items:start;
  background:var(--paper);border:1px solid var(--card-line);border-radius:12px;padding:20px;
  transition:border-color .2s}
.card:hover{border-color:#d9dae0}
.fig{align-self:center;display:block;overflow:hidden;background:var(--paper);border-radius:10px}
.thumb{display:block;width:100%;height:auto;max-height:300px;object-fit:contain;margin:0 auto}
.ttl{font-size:18px;font-weight:500;line-height:1.35;letter-spacing:-.005em;margin:0 0 6px}
.ttl a:hover{color:var(--acc)}
.authors{font-size:14px;color:var(--dim);line-height:1.6}
.authors a:hover{color:var(--acc)}
.me{color:var(--ink);font-weight:600}
.venue-row{display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin-top:10px}
.vbadge,.stars{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:600;
  letter-spacing:.02em;line-height:1;border-radius:6px;padding:5px 8px}
.vbadge{color:var(--acc-ink);background:var(--acc-soft)}
.stars{color:var(--dim);background:var(--well)}
.stars i{color:#e8a317;font-size:11px}
.desc{font-size:15px;line-height:1.6;color:#4b505a;margin-top:10px}
.lnks{margin-top:14px;display:flex;flex-wrap:wrap;gap:6px}
.lnk{font-size:13px;font-weight:500;color:var(--body);background:var(--paper);
  border:1px solid var(--line);border-radius:999px;padding:5px 13px;
  transition:border-color .15s,color .15s}
.lnk:hover{color:var(--acc);border-color:var(--acc)}
.lnk.off{color:var(--dim2);border-style:dashed;pointer-events:none}
.sep{display:none}

/* ---------- open-source extras ---------- */
.pi{font-size:14.5px;color:#4b505a;margin-top:16px}
.plist{margin-top:6px;display:grid;gap:6px;font-size:14.5px;color:#4b505a}
.plist li{padding-left:14px;position:relative}
.plist li::before{content:"";position:absolute;left:0;top:.65em;width:5px;height:5px;
  border-radius:50%;background:var(--dim2)}
.cite{display:block;font-size:12.5px;color:var(--dim2)}
.blogs{margin-top:14px}
.blogs>summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:8px;
  font-size:14px;font-weight:600;color:var(--dim);transition:color .15s}
.blogs>summary:hover{color:var(--acc)}
.blogs>summary .chev{font-size:9px;transition:transform .2s}
.blogs[open]>summary .chev{transform:rotate(180deg)}
.blogs .pi{margin-top:8px}

@media (max-width:980px){
  .card{grid-template-columns:280px minmax(0,1fr);gap:24px}
}
@media (max-width:760px){
  header{grid-template-columns:1fr;gap:24px;padding-top:56px}
  .pf{--pf:128px;order:-1}
  .card{grid-template-columns:minmax(0,1fr);gap:16px}
  .fig{max-width:420px;width:100%}
  .sec{margin-top:56px}
}
@media (max-width:520px){
  .wrap{padding:0 16px 72px}
  header{padding-top:40px}
  .card{padding:16px}
}
"""


def _stars(n):
    if n is None:
        return ""
    label = "%.1fk" % (n / 1000.0) if n >= 1000 else str(n)
    return ('<span class="stars" title="%s GitHub stars">'
            '<i class="fas fa-star" aria-hidden="true"></i>%s</span>' % ("{:,}".format(n), label))


def _node(p, base, badge=None):
    """One publication / project card."""
    return """
<div class="node">
  <article class="card">
    <a class="fig" href="%(href)s" target="_blank" rel="noopener">%(media)s</a>
    <div>
      <h3 class="ttl"><a href="%(href)s" target="_blank" rel="noopener">%(title)s</a></h3>
      %(authors)s
      <div class="venue-row"><span class="vbadge">%(v)s</span>%(stars)s</div>
      <p class="desc">%(desc)s</p>
      <div class="lnks">%(links)s</div>
      %(extra)s
    </div>
  </article>
</div>""" % {
        "href": p["href"], "media": media_html(p, base),
        "v": badge or venue_year(p, short=True), "stars": _stars(p.get("stars")),
        "title": p["title"],
        "authors": '<p class="authors">%s</p>' % authors_html(p) if p.get("authors") else "",
        "desc": p["desc"], "links": links_html(p, ""), "extra": _project_extra(p),
    }


CHEV = '<i class="chev fas fa-chevron-down" aria-hidden="true"></i>'


def _project_extra(p):
    if "contrib" not in p:
        return ""
    out = ['<p class="pi">%s</p>' % p["contrib_intro"], '<ul class="plist">']
    out += ['<li>%s</li>' % c for c in p["contrib"]]
    out.append('</ul>')
    out.append('<details class="blogs"><summary>Tutorial blogs (%d) %s</summary>'
               % (len(p["blog"]), CHEV))
    out.append('<p class="pi">%s</p>' % p["blog_intro"])
    out.append('<ul class="plist">')
    for title, url, outlet, date in p["blog"]:
        out.append('<li><a href="%s" target="_blank" rel="noopener">%s</a>'
                   '<span class="cite"><em>%s</em>, %s</span></li>' % (url, title, outlet, date))
    out.append('</ul></details>')
    return "\n".join(out)


def _plural(n):
    return "paper" if n == 1 else "papers"


def publications(base):
    """Grouped by year: each year's selected papers, then its folded ones."""
    groups = OrderedDict()
    for p in SELECTED:
        groups.setdefault(p["year"], {"sel": [], "alt": []})["sel"].append(p)
    for p in OTHER:
        groups.setdefault(p["year"], {"sel": [], "alt": []})["alt"].append(p)

    out = []
    for year in sorted(groups, reverse=True):
        g = groups[year]
        cards = [_node(p, base) for p in g["sel"]]
        if g["alt"]:
            # "N more" only reads right when something is already shown above it
            n = len(g["alt"])
            shut = ('%d more from %s' % (n, year) if g["sel"]
                    else 'Show %d %s' % (n, _plural(n)))
            cards.append(
                '<details class="more">'
                '<summary><span class="lbl-shut">%s</span>'
                '<span class="lbl-open">Show fewer</span>%s</summary>%s</details>'
                % (shut, CHEV, "".join(_node(p, base) for p in g["alt"])))
        out.append('<section class="grp"><h3 class="yr">%s</h3><div class="cards">%s</div></section>'
                   % (year, "".join(cards)))
    return "\n".join(out)


def build(base=""):
    prj = '<div class="cards">%s</div>' % "".join(_node(p, base, badge="GitHub") for p in PROJECTS)
    bk = '<div class="cards">%s</div>' % "".join(_node(p, base) for p in BOOK)

    body = """
<div class="wrap">
<header>
  <div>
    <h1>%(name)s</h1>
    <div class="bio">%(bio)s</div>
    <nav class="social">%(links)s</nav>
  </div>
  <img class="pf" src="%(base)s%(photo)s" alt="Zechu (Steven) Li" width="256" height="256">
</header>

<main>
  <div class="sec"><h2>Publications</h2><span class="ln"></span></div>
  <p class="note">* equal contribution</p>
  %(tl)s

  <div class="sec"><h2>Open Source Projects</h2><span class="ln"></span></div>
  %(prj)s

  <div class="sec"><h2>Book Chapter</h2><span class="ln"></span></div>
  %(bk)s
</main>
</div>
""" % {"base": base, "name": PROFILE["name"], "photo": PROFILE["photo"],
       "links": profile_links("", "", icons=True), "bio": bio_paras("bio-p"),
       "tl": publications(base), "prj": prj, "bk": bk}

    return page(CSS, body, base, fonts=FONTS, theme="#fbfbfc", icons=True)
