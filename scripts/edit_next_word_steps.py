"""Rename the step labels on the original "Next-word prediction" slide to the deck's "STEP 1: TEXT"
pattern (edits the existing slide in place; safe to re-run)."""
import re

import design as d

ANCHOR = "Next-word prediction: probabilities become text"


def build(prs):
    slide = prs.slides[d.index_after(prs, ANCHOR) - 1]
    for sh in slide.shapes:
        if not sh.has_text_frame:
            continue
        runs = [r for p in sh.text_frame.paragraphs for r in p.runs]
        m = re.match(r"^\s*(\d+)\s*/\s*(.+)$", "".join(r.text for r in runs))
        if m:
            runs[0].text = f"STEP {m.group(1)}: {m.group(2).strip()}"
            for r in runs[1:]:
                r.text = ""
    return slide


if __name__ == "__main__":
    d.run(build)
