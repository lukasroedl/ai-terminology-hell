#!/usr/bin/env bash
# Render the deck to PNGs in .render/ for visual checks.
# Uses the installed Microsoft PowerPoint (via AppleScript) to export a PDF, then
# PyMuPDF from .venv to rasterize it -- no global tools needed.
set -euo pipefail
cd "$(dirname "$0")/.."

DECK="${1:-ai-terminology-hell.pptx}"
case "$DECK" in /*) ;; *) DECK="$PWD/$DECK" ;; esac   # absolute path for PowerPoint
OUT="$PWD/.render"
rm -rf "$OUT" && mkdir -p "$OUT"

osascript <<EOF
tell application "Microsoft PowerPoint"
  open POSIX file "$DECK"
  set p to active presentation
  save p in (POSIX file "$OUT/deck.pdf") as save as PDF
  close p saving no
end tell
EOF

DECK="$DECK" .venv/bin/python - <<'EOF'
import os, sys
import pymupdf
from pptx import Presentation
doc = pymupdf.open(".render/deck.pdf")
for i, page in enumerate(doc, 1):
    page.get_pixmap(dpi=110).save(f".render/slide-{i:02d}.png")
print(f"Rendered {len(doc)} slides to .render/")
# PowerPoint occasionally exports a stale copy of a file that just changed on disk.
expected = len(Presentation(os.environ["DECK"]).slides)
if len(doc) != expected:
    sys.exit(f"WARNING: deck has {expected} slides but the export has {len(doc)}; "
             "PowerPoint exported a stale copy. Run the script again.")
EOF
