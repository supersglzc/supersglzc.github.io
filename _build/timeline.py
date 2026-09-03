# -*- coding: utf-8 -*-
"""The homepage design: one chronological timeline of publications.

Every publication sits under its own year. Selected ones are always visible;
the rest are folded away and appear directly beneath the selected papers of
the same year when unfolded. The fold is a visually hidden checkbox, so the
page needs no JavaScript.
"""

from collections import OrderedDict

from data import PROFILE, SELECTED, OTHER, PROJECTS, BOOK
from common import (page, authors_html, links_html, media_html, venue_year,
                    profile_links, bio_paras)

PRECONNECT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
              '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
FONTS = (PRECONNECT + '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Manrope:wght@400;500;600;700;800&display=swap">')


CSS = """
:root{
  --bg:#fbfbfc; --paper:#fff; --ink:#131519; --dim:#5d626c; --dim2:#9ba0aa;
  --line:#e6e7ea; --acc:#5b3df5; --acc2:#e0397a;
  --yrw:92px;       /* column 1: the year label   */
  --railw:52px;     /* column 2: the timeline rail */
  --indent:144px;   /* = yrw + railw: everything outside the timeline lines
                       up with the cards, leaving the rail its own margin */
}
body{background:var(--bg);color:var(--ink);font:400 15.5px/1.68 "Manrope",system-ui,sans-serif;
  -webkit-font-smoothing:antialiased}
a{text-decoration:none}
.wrap{max-width:1060px;margin:0 auto;padding:0 26px 100px}
.vh{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0 0 0 0);white-space:nowrap;border:0}

/* ---------- header ---------- */
header,.bio,.sec{margin-left:var(--indent)}
header{padding:76px 0 0;display:grid;grid-template-columns:1fr 212px;gap:44px;align-items:center}
.pf{width:196px;height:196px;object-fit:cover;border-radius:50%;background:var(--paper);
  border:5px solid var(--paper);box-shadow:0 10px 34px -14px rgba(19,21,25,.32);margin-left:auto}
h1{font-size:clamp(33px,6vw,47px);font-weight:800;letter-spacing:-.042em;line-height:1.05}
.social{margin-top:22px;display:flex;flex-wrap:wrap;gap:8px}
.social a{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:600;
  border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:8px 14px;
  transition:border-color .18s,color .18s,transform .18s}
.social a:hover{border-color:var(--acc);color:var(--acc);transform:translateY(-1px)}
.social i{color:var(--dim2);font-size:12.5px}
.social a:hover i{color:var(--acc)}
.bio{margin-top:34px;display:grid;gap:14px;max-width:72ch;color:#3a3f48}
.bio a{color:var(--acc);border-bottom:1px solid rgba(91,61,245,.25);font-weight:600}
.bio a:hover{color:var(--acc2);border-color:var(--acc2)}

/* ---------- section headings ---------- */
.sec{margin:74px 0 30px var(--indent);display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.sec h2{font-size:19px;font-weight:800;letter-spacing:-.028em}
.sec .ln{flex:1;height:1px;background:var(--line);min-width:20px}
.sec .cnt{font-size:12px;font-weight:700;color:var(--dim2);letter-spacing:.06em}
.note{font-size:11.5px;color:var(--dim2);margin:-22px 0 26px var(--indent);letter-spacing:.02em}

/* ---------- per-year expander ---------- */
.more{position:relative}
.more>summary{list-style:none;cursor:pointer;position:relative;padding-bottom:22px;
  display:flex;align-items:center}
.more>summary::before{content:"";position:absolute;left:calc(-1 * var(--railw)/2 - 5px);top:11px;
  width:10px;height:10px;border-radius:50%;background:var(--bg);
  border:2px solid var(--line);z-index:1;transition:border-color .18s,background .18s}
.more>summary:hover::before{border-color:var(--acc)}
.more[open]>summary::before{background:var(--acc);border-color:var(--acc)}
.moreu{display:inline-flex;align-items:center;gap:8px;background:var(--paper);
  border:1px dashed #d3d5da;border-radius:999px;padding:7px 15px;
  font-size:12.5px;font-weight:700;letter-spacing:.01em;color:var(--dim2);
  transition:border-color .18s,color .18s,border-style .18s,box-shadow .18s}
.more>summary:hover .moreu{border-style:solid;border-color:var(--acc);color:var(--acc);
  box-shadow:0 6px 18px -14px rgba(91,61,245,.7)}
.more[open]>summary .moreu{border-style:solid}
.moreu .chev{font-size:9px;transition:transform .2s}
.more[open]>summary .moreu .chev{transform:rotate(180deg)}
.more>summary:focus-visible .moreu{outline:2px solid var(--acc);outline-offset:3px}
.more .lbl-open{display:none}
.more[open] .lbl-shut{display:none}
.more[open] .lbl-open{display:inline}

/* ---------- timeline ---------- */
.tl{position:relative}
.tl::before{content:"";position:absolute;left:calc(var(--yrw) + var(--railw)/2 - 1px);
  top:12px;bottom:26px;width:2px;
  background:linear-gradient(180deg,var(--acc),rgba(91,61,245,.18) 68%,transparent)}
.grp{display:grid;grid-template-columns:var(--yrw) var(--railw) minmax(0,1fr);align-items:start}
.grp.only .yr{padding-top:5px}
.yr{grid-column:1;padding-top:19px;text-align:right;
  font-size:21px;font-weight:800;letter-spacing:-.03em;color:var(--ink)}
.yr small{display:block;font-size:10.5px;font-weight:700;letter-spacing:.1em;
  color:var(--dim2);text-transform:uppercase;margin-top:3px}
.cards{grid-column:3;min-width:0}
.node{position:relative;padding-bottom:22px}
.node::before{content:"";position:absolute;left:calc(-1 * var(--railw)/2 - 6px);top:24px;
  width:12px;height:12px;
  border-radius:50%;background:var(--acc);border:2.5px solid var(--acc);z-index:1;
  transition:box-shadow .18s}
.node.alt::before{background:var(--paper);border-color:var(--dim2)}
.node:hover::before{background:var(--acc);border-color:var(--acc);
  box-shadow:0 0 0 5px rgba(91,61,245,.14)}

.card{display:grid;grid-template-columns:262px 1fr;gap:24px;align-items:start;
  background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:16px;
  transition:box-shadow .22s,border-color .22s,transform .22s}
.card:hover{border-color:#d8d9de;box-shadow:0 14px 34px -22px rgba(19,21,25,.34);transform:translateY(-2px)}
.fig{align-self:center;display:block;overflow:hidden;background:var(--paper);border-radius:10px}
.thumb{display:block;width:100%;height:auto;max-height:250px;object-fit:contain;margin:0 auto}
.vbadge{display:inline-block;font-size:10.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--acc);background:rgba(91,61,245,.08);border-radius:6px;padding:5px 9px}
.node.alt .vbadge{color:var(--dim);background:#f1f1f4}
.ttl{font-size:17px;font-weight:750;line-height:1.3;letter-spacing:-.022em;margin:10px 0 7px}
.ttl a:hover{color:var(--acc)}
.authors{font-size:13px;color:var(--dim);line-height:1.6}
.authors a{font-weight:600}
.authors a:hover{color:var(--acc)}
.me{color:var(--ink);font-weight:800}
.desc{font-size:13.8px;color:#4b505a;margin-top:9px}
.lnks{margin-top:12px;display:flex;flex-wrap:wrap;gap:6px}
.lnk{font-size:12px;font-weight:700;letter-spacing:.02em;color:var(--acc);
  border:1px solid rgba(91,61,245,.24);border-radius:999px;padding:6px 12px}
.lnk:hover{background:var(--acc);color:#fff;border-color:var(--acc)}
.lnk.off{color:var(--dim2);border-color:var(--line);border-style:dashed;pointer-events:none}
.sep{display:none}

/* ---------- open-source extras ---------- */
.pi{font-size:13.5px;color:#4b505a;margin-top:11px;font-weight:600}
.plist{margin-top:7px;display:grid;gap:7px;font-size:13.2px;color:#4b505a}
.plist li{padding-left:15px;position:relative}
.plist li::before{content:"";position:absolute;left:0;top:.62em;width:6px;height:6px;
  border-radius:50%;background:var(--acc2)}
.plist a{color:var(--acc);font-weight:600}
.plist a:hover{color:var(--acc2)}
.cite{display:block;font-size:11.8px;color:var(--dim2);font-weight:400}


@media (max-width:960px){
  :root{--yrw:70px;--railw:42px;--indent:112px}
  .card{grid-template-columns:216px 1fr;gap:20px}
  .yr{font-size:19px}
}
@media (max-width:820px){
  :root{--indent:0px}
  header{grid-template-columns:1fr;gap:22px}
  .pf{width:132px;height:132px;order:-1;border-width:4px;margin-left:0}
  .tl::before{left:5px;top:8px}
  .grp{grid-template-columns:minmax(0,1fr)}
  .yr{grid-column:1;padding:0 0 12px 28px;text-align:left;font-size:18px;
    display:flex;align-items:baseline;gap:9px}
  .yr small{margin:0}
  .cards{grid-column:1}
  .node{padding-left:28px}
  .node::before{left:0;top:24px}
  .card{grid-template-columns:1fr;gap:14px}
  .fig{max-width:360px;width:100%}
}
@media (max-width:520px){
  .wrap{padding:0 16px 80px}
  header{padding-top:44px}
  .sec{gap:10px}
  .sec .ln{display:none}
}
"""


def _node(p, base, alt=False, badge=None):
    """One card hanging off the timeline spine."""
    return """
<div class="node%(alt)s">
  <article class="card">
    <a class="fig" href="%(href)s" target="_blank" rel="noopener">%(media)s</a>
    <div>
      <span class="vbadge">%(v)s</span>
      <h3 class="ttl"><a href="%(href)s" target="_blank" rel="noopener">%(title)s</a></h3>
      %(authors)s
      <p class="desc">%(desc)s</p>
      <div class="lnks">%(links)s</div>
      %(extra)s
    </div>
  </article>
</div>""" % {
        "alt": " alt" if alt else "",
        "href": p["href"], "media": media_html(p, base),
        "v": badge or venue_year(p, short=True),
        "title": p["title"],
        "authors": '<p class="authors">%s</p>' % authors_html(p) if p.get("authors") else "",
        "desc": p["desc"], "links": links_html(p, ""), "extra": _project_extra(p),
    }


def _project_extra(p):
    if "contrib" not in p:
        return ""
    out = ['<p class="pi">%s</p>' % p["contrib_intro"], '<ul class="plist">']
    out += ['<li>%s</li>' % c for c in p["contrib"]]
    out.append('</ul>')
    out.append('<p class="pi">%s</p>' % p["blog_intro"])
    out.append('<ul class="plist">')
    for title, url, outlet, date in p["blog"]:
        out.append('<li><a href="%s" target="_blank" rel="noopener">%s</a>'
                   '<span class="cite"><em>%s</em>, %s</span></li>' % (url, title, outlet, date))
    out.append('</ul>')
    return "\n".join(out)


def _plural(n):
    return "paper" if n == 1 else "papers"


def publications(base):
    """One spine, grouped by year: each year's selected papers, then its folded ones."""
    groups = OrderedDict()
    for p in SELECTED:
        groups.setdefault(p["year"], {"sel": [], "alt": []})["sel"].append(p)
    for p in OTHER:
        groups.setdefault(p["year"], {"sel": [], "alt": []})["alt"].append(p)

    out = ['<div class="tl">']
    for year in sorted(groups, reverse=True):
        g = groups[year]
        n_all = len(g["sel"]) + len(g["alt"])
        cards = [_node(p, base) for p in g["sel"]]
        if g["alt"]:
            # "N more" only reads right when something is already shown above it
            shut = ('%d more from %s' % (len(g["alt"]), year) if g["sel"]
                    else 'Show %d %s' % (len(g["alt"]), _plural(len(g["alt"]))))
            cards.append(
                '<details class="more">'
                '<summary><span class="moreu">'
                '<span class="lbl-shut">%s</span>'
                '<span class="lbl-open">Show fewer</span>'
                '<i class="chev fas fa-chevron-down" aria-hidden="true"></i>'
                '</span></summary>%s</details>'
                % (shut, "".join(_node(p, base, alt=True) for p in g["alt"])))
        out.append(
            '<div class="grp%s">'
            '<div class="yr">%s<small>%d %s</small></div>'
            '<div class="cards">%s</div>'
            '</div>'
            % ("" if g["sel"] else " only", year, n_all, _plural(n_all), "".join(cards)))
    out.append('</div>')
    return "\n".join(out)


def build(base=""):
    prj = ('<div class="tl"><div class="grp"><div class="yr"></div><div class="cards">%s'
           '</div></div></div>' % "".join(_node(p, base, badge="GitHub") for p in PROJECTS))
    bk = ('<div class="tl"><div class="grp"><div class="yr"></div><div class="cards">%s'
          '</div></div></div>' % "".join(_node(p, base) for p in BOOK))

    body = """
<div class="wrap">
<header>
  <div>
    <h1>%(name)s</h1>
    <nav class="social">%(links)s</nav>
  </div>
  <img class="pf" src="%(base)s%(photo)s" alt="Zechu (Steven) Li" width="256" height="256">
</header>
<div class="bio">%(bio)s</div>

<main>
  <div class="sec"><h2>Publications</h2><span class="ln"></span><span class="cnt">%(npub)d</span></div>
  <p class="note">* equal contribution</p>
  %(tl)s

  <div class="sec"><h2>Open Source Projects</h2><span class="ln"></span><span class="cnt">%(nprj)d</span></div>
  %(prj)s

  <div class="sec"><h2>Book Chapter</h2><span class="ln"></span><span class="cnt">1</span></div>
  %(bk)s
</main>
</div>
""" % {"base": base, "name": PROFILE["name"], "photo": PROFILE["photo"],
       "links": profile_links("", "", icons=True), "bio": bio_paras("bio-p"),
       "tl": publications(base), "prj": prj, "bk": bk,
       "npub": len(SELECTED) + len(OTHER), "nprj": len(PROJECTS)}

    return page(CSS, body, base, fonts=FONTS, theme="#fbfbfc", icons=True)
