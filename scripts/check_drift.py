"""Detect manual edits: does the deck still match what a slide script would build?

Usage: .venv/bin/python scripts/check_drift.py scripts/slide_<name>.py [deck]

Runs the slide script on a temporary copy of the deck and compares every script-built slide (slides that
carry a marker shape named "slide-*", "section-*" or "terminology-hell-title") shape by shape: type,
position, size, text and font sizes. Exit code 1 and a list of differences if the deck was edited by
hand, e.g. in PowerPoint. Port those edits into the script before re-running it, or they are lost.
"""
import importlib.util
import os
import shutil
import sys
import tempfile

from pptx import Presentation
from pptx.util import Emu

TOLERANCE = 0.02  # inches


def is_marker(name):
    return name.startswith(("slide-", "section-")) or name == "terminology-hell-title"


def marked_slides(prs):
    out = {}
    for slide in prs.slides:
        for sh in slide.shapes:
            if is_marker(sh.name):
                out[sh.name] = slide
    return out


def shape_colors(sh):
    """(fill, line) colour as hex, or None where it isn't a plain solid colour."""
    out = []
    line = getattr(sh, "line", None)          # connectors have a line but no fill
    for part in (getattr(sh, "fill", None), getattr(line, "fill", None)):
        value = None
        try:
            if part is not None and part.type == 1:
                value = str(part.fore_color.rgb)
        except Exception:
            value = None
        out.append(value)
    return tuple(out)


def describe(sh):
    text, sizes = "", []
    if sh.has_text_frame:
        text = " ".join(sh.text_frame.text.split())
        # Distinct sizes of non-blank runs: PowerPoint splits runs when text is edited by hand.
        sizes = sorted({r.font.size.pt for p in sh.text_frame.paragraphs for r in p.runs
                        if r.font.size and r.text.strip()})
    geo = [Emu(v).inches for v in (sh.left, sh.top, sh.width, sh.height)]
    geo.append(round(sh.rotation, 1) / 100)        # rotation, scaled into the same tolerance
    colors = shape_colors(sh)
    try:                                   # line width, so thickness changes count as drift too
        colors += (round(sh.line.width.pt, 2) if sh.line.width else None,)
    except Exception:
        pass
    if sh.has_text_frame:
        # Distinct colours of non-blank runs (PowerPoint splits runs when text is edited by hand).
        run_colors = set()
        for p in sh.text_frame.paragraphs:
            for r in p.runs:
                if not r.text.strip():
                    continue
                try:
                    run_colors.add(str(r.font.color.rgb))
                except Exception:
                    pass
        colors += tuple(sorted(run_colors))
    return str(sh.shape_type), geo, text, sizes, colors


def compare(a, b):
    diffs = []
    sa, sb = list(a.shapes), list(b.shapes)
    if len(sa) != len(sb):
        diffs.append(f"shape count: deck {len(sa)} vs script {len(sb)}")
    for i, (x, y) in enumerate(zip(sa, sb)):
        tx, gx, textx, szx, cx = describe(x)
        ty, gy, texty, szy, cy = describe(y)
        label = textx or texty or tx
        if tx != ty:
            diffs.append(f"#{i} type: deck {tx} vs script {ty}")
        if any(abs(p - q) > TOLERANCE for p, q in zip(gx, gy)):
            fmt = lambda g: "x{:.2f} y{:.2f} w{:.2f} h{:.2f}".format(*g)
            diffs.append(f"#{i} '{label[:40]}' geometry: deck {fmt(gx)} vs script {fmt(gy)}")
        if textx != texty:
            diffs.append(f"#{i} text: deck '{textx[:50]}' vs script '{texty[:50]}'")
        if szx != szy:
            diffs.append(f"#{i} '{label[:40]}' font sizes: deck {szx} vs script {szy}")
        if cx != cy:
            diffs.append(f"#{i} '{label[:40]}' colours: deck {cx} vs script {cy}")
    return diffs


def main():
    script = sys.argv[1]
    deck = sys.argv[2] if len(sys.argv) > 2 else "ai-terminology-hell.pptx"
    sys.path.insert(0, os.path.dirname(os.path.abspath(script)))
    spec = importlib.util.spec_from_file_location("slide_script", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, "deck.pptx")
        shutil.copy(deck, copy)
        prs = Presentation(copy)
        module.build(prs)
        prs.save(copy)
        rebuilt = marked_slides(Presentation(copy))
    current = marked_slides(Presentation(deck))

    drift = False
    for name, slide in rebuilt.items():
        if name not in current:
            print(f"{name}: not in the deck yet (new slide)")
            continue
        diffs = compare(current[name], slide)
        if diffs:
            drift = True
            print(f"{name}: deck differs from script output (manual edits?)")
            for line in diffs:
                print("   ", line)
    if not drift:
        print("No drift: the deck matches the script output.")
    sys.exit(1 if drift else 0)


if __name__ == "__main__":
    main()
