# Homepage build

`index.html` at the repo root is **generated** — don't hand-edit it, edit these and rebuild:

```
python3 _build/build.py
```

| file | what it holds |
|---|---|
| `data.py` | all content: bio, links, publications, projects, book chapter |
| `timeline.py` | the design (CSS + markup) |
| `common.py` | shared render helpers + page scaffolding |
| `build.py` | writes `../index.html` |

## Adding a publication

Append a dict to `SELECTED` (always visible) or `OTHER` (behind the
"Other publications" fold) in `data.py`, then rebuild. Each list is grouped by
year automatically and the per-year counts update themselves.

```python
{
    "id": "shortname",
    "title": "...",
    "authors": [ME, a("georgia")],          # ME / ME_EQ = you; a("key") = the A table
    "venue": "ICML", "year": "2026",
    "venue_short": "ICML",                   # optional, used for the badge
    "media": ("img", "images/foo.png"),      # or ("video", "images/foo.mp4")
    "href": "https://arxiv.org/abs/...",
    "links": [("paper", "https://..."), ("code", "")],   # empty url renders as disabled
    "desc": "One-sentence summary.",
}
```

The "Other publications" fold is a native `<details>`, so the page needs no
JavaScript at all.
