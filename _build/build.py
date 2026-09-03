# -*- coding: utf-8 -*-
"""Regenerate the homepage.

    python3 _build/build.py

Content lives in _build/data.py; the design lives in _build/timeline.py.
Edit those, re-run this, and index.html is rewritten.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import timeline

if __name__ == "__main__":
    html = timeline.build(base="")
    dst = os.path.join(ROOT, "index.html")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote %s (%.1f KB)" % (dst, os.path.getsize(dst) / 1024))
