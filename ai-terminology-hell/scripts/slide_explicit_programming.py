"""Slide "Stream 1: explicit programming": an IF/ELSE spam flowchart, where it breaks, famous examples.

Placed right after the "Five nested ideas" slide; paired with slide_machine_learning.py, which solves
the same spam problem by learning. Re-running replaces the slide.
"""
import design as d

MARKER = "slide-explicit-programming"
ANCHOR = "section-rulebased"  # after the "Rule-based AI" section divider

EXAMPLES = [("1956", "Logic Theorist proves theorems"),
            ("1966", "ELIZA, a scripted chatbot"),
            ("1970s–80s", "Expert systems, e.g. MYCIN")]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Foundations · Stream 1 · 1950s–1980s", "Early AI: humans write the rules",
        "Rule-based AI (also called symbolic AI) captures knowledge in hand-written IF–THEN rules.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: the decision logic -------------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, 5.5, 3.0)
    d.label(s, "Example · Is this email spam?", 0.85, 2.08)

    # Top-to-bottom flow: email -> RULES container (IF, ELSE IF; "yes" exits right to SPAM) -> NOT SPAM.
    # All flowchart boxes share one size. Layout fine-tuned by hand in PowerPoint (user edits, 2026-09-22)
    # and ported back here: keep these numbers unless the user asks for a change.
    bw, bh = 2.1, 0.38                             # box width / height
    cx = 2.05                                      # center of the decision column
    ox = 3.725                                     # left edge of the outcome column
    email_y = 2.28                                 # "New email" top
    d1, d2 = 3.052, 3.74                           # decision box tops
    # Container around the two decisions only; drawn first so arrows sit on top.
    d.rect(s, cx - bw / 2 - 0.15, 2.75, bw + 0.48, 1.62, fill=d.LIGHT_BG, line=d.BORDER, rounded=True)
    d.label(s, "Rules written by hand", cx - bw / 2, 2.789, w=1.02, size=7)   # wraps to two lines

    d.chip(s, "New email", cx - bw / 2, email_y, bw, h=bh, fill=d.NAVY, color=d.WHITE, size=10)
    d.line(s, cx, email_y + bh, cx, d1, color=d.TEAL, width=1.5, arrow=True)

    for top, keyword, condition in ((d1, "IF", "it says “free money”"),
                                    (d2, "ELSE IF", "unknown sender + link")):
        d.decision(s, keyword, condition, cx - bw / 2, top, bw, h=bh, keyword_size=10,
                   condition_size=10)
    for top, yes_dy in ((d1, 0.195), (d2, 0.215)):
        mid = top + bh / 2
        d.line(s, cx + bw / 2, mid, ox, mid, color=d.TEAL, width=1.5, arrow=True)
        d.text(s, "yes", cx + bw / 2 + 0.08, mid - yes_dy, 0.4, 0.2, font=d.MONO, size=9, color=d.TEAL)
        d.chip(s, "SPAM", ox, top, bw, h=bh, fill=d.NAVY, color=d.MINT, size=10)

    d.line(s, cx, d1 + bh, cx, d2, color=d.TEAL, width=1.5, arrow=True)
    d.line(s, cx, d2 + bh, cx, 4.52, color=d.TEAL, width=1.5, arrow=True)
    for top in (d1 + bh + 0.054, d2 + bh + 0.017):
        d.text(s, "no", cx + 0.065, top, 0.4, 0.2, font=d.MONO, size=9, color=d.TEAL)
    d.chip(s, "NOT SPAM", cx - bw / 2, 4.52, bw, h=bh, fill=d.TEAL_TINT, color=d.NAVY, size=10)

    # --- Right top: where it breaks -----------------------------------------------------------------
    x, w = 6.3, d.LEFT + d.CONTENT_W - 6.3
    d.card(s, x, 1.95, w, 1.42, accent=d.MINT)
    d.label(s, "Where it breaks", x + 0.23, 2.08)
    d.chip(s, "“Claim your prize today!”", x + 0.23, 2.36, 2.15, h=0.32, fill=d.LIGHT_BG,
           color=d.NAVY, size=9.5, font=d.BODY, line=d.BORDER)
    d.text(s, "✗", x + 2.45, 2.36, 0.25, 0.32, size=13, color=d.MUTED, anchor=d.MSO_ANCHOR.MIDDLE)
    d.text(s, "No rule matches, so it lands in the inbox. Every new trick needs a new rule.",
           x + 0.23, 2.78, w - 0.4, 0.5, size=10, color=d.TEXT_DARK)

    # --- Right bottom: famous examples --------------------------------------------------------------
    d.card(s, x, 3.53, w, 1.42)
    d.label(s, "Famous examples", x + 0.23, 3.66)
    for i, (year, desc) in enumerate(EXAMPLES):
        y = 3.94 + i * 0.32
        d.text(s, year, x + 0.23, y, 0.8, 0.3, font=d.MONO, size=9, color=d.TEAL)
        d.text(s, desc, x + 1.0, y - 0.02, w - 1.1, 0.3, size=10, color=d.TEXT_DARK)

    d.takeaway(s, "Rules + data → answers. Works for clear-cut problems, breaks on messy reality.",
               y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
