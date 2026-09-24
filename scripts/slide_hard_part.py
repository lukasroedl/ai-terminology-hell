"""Closing statement "Connecting a tool is easy. Keeping the loop in check is not.": navy slide with
the four guardrails an agent needs; the signature circle doubles as the agent loop, with a dashed
mint ring as the guardrails around it.

Replaces the original hand-made slide ("Constraining a loop is not."), without its authoring note.
Placed after the stack slide; re-running replaces the slide.
"""
from pptx.enum.dml import MSO_LINE

import design as d

MARKER = "slide-hard-part"
ANCHOR = "slide-agent-stack"
OLD_SLIDE = "Constraining a loop is not"

GUARDRAILS = ["Knows when to stop", "Copes with errors", "Asks before irreversible steps",
              "Leaves a trail you can check"]
LOOP = [("Plan", 0.0), ("Act", 1.0), ("Check", 2.0)]          # thirds around the circle


def build(prs):
    import math
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.new_slide(prs, background=d.NAVY, index=d.index_after(prs, ANCHOR))

    # --- Right: the loop (signature circle) inside a dashed ring of guardrails -----------------
    cx, cy, r = 7.95, 2.95, 1.2
    ring = d.circle(s, cx - r - 0.35, cy - r - 0.35, 2 * r + 0.7, color=d.MINT, alpha=0,
                    line_color=d.MINT)
    ring.line.dash_style = MSO_LINE.DASH
    d.circle(s, cx - r, cy - r, 2 * r, color=d.TEAL, alpha=18)
    d.text(s, "The agent loop", cx - 0.9, cy - 0.2, 1.8, 0.3, font=d.HEADLINE, size=15,
           color=d.WHITE, align=d.PP_ALIGN.CENTER)
    d.text(s, "runs on its own", cx - 0.9, cy + 0.1, 1.8, 0.2, font=d.MONO, size=8,
           color=d.DIM_ON_DARK, align=d.PP_ALIGN.CENTER)
    for name, third in LOOP:
        a = math.radians(-90 + third * 120)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        d.chip(s, name, px - 0.35, py - 0.14, 0.7, h=0.28, size=9, fill=d.NAVY_LIGHT,
               color=d.WHITE, line=d.TEAL)
    d.text(s, "guardrails", cx + 0.55, cy + r + 0.42, 1.2, 0.2, font=d.MONO, size=8,
           color=d.MINT, spacing=100)

    # --- Left: statement and the four guardrails --------------------------------------------------
    d.kicker(s, "Part 5 · The hard part", 0.8, 0.85, w=4.5)
    title = d.text(s, "Connecting a tool is easy.\nKeeping the loop in check is not.", 0.8, 1.15,
                   5.7, 1.2, font=d.HEADLINE, size=30)
    title.name = MARKER
    d.text(s, "An agent acts on its own, so it needs guardrails:", 0.8, 2.5, 5.2, 0.3, size=13,
           color=d.SOFT_ON_DARK)
    for i, rail in enumerate(GUARDRAILS):
        x, y = 0.8 + (i % 2) * 2.62, 2.92 + (i // 2) * 0.44
        d.chip(s, rail, x, y, 2.5, h=0.34, size=10, font=d.BODY, fill=d.NAVY_LIGHT, color=d.WHITE,
               line=d.TEAL)
    d.accent_bar(s, 0.8, 4.0)
    d.text(s, "In a regulated company, each guardrail also means governance work: approvals, logs "
              "and clear responsibility.", 0.8, 4.15, 5.2, 0.5, size=11, color=d.DIM_ON_DARK)
    return s


if __name__ == "__main__":
    d.run(build)
