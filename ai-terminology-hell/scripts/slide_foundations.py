"""Slide "Five nested ideas, seventy years": AI ⊃ ML ⊃ Deep Learning ⊃ (Generative AI, Agentic AI) as
nested signature circles, next to a vertical timeline that names the milestone behind each year.

Years: AI 1955 (term coined in the Dartmouth proposal), ML 1959 (Arthur Samuel's checkers program),
Deep Learning 2012 (AlexNet), Generative AI 2018 (the first GPT), Agentic AI 2024 (agents take off).
The definitions are the ones of the original hand-made slide.

Replaces that original slide. The headline stays the same: the AI divider uses it as its anchor.
Placed after the terminology hell slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-foundations"
ANCHOR = "terminology-hell-title"
HEADLINE = "Five nested ideas, seventy years"
BOTTOM = 4.9                                   # lowest y of the circles (takeaway starts at 5.02)

# (year, milestone, name, definition, accent)
IDEAS = [
    ("1955", "term coined", "Artificial Intelligence",
     "The overarching field: machines performing tasks that require human-like intelligence.",
     d.TEAL),
    ("1959", "Arthur Samuel", "Machine Learning",
     "A subset of AI: learning from data instead of explicit programming, to predict, classify or "
     "detect patterns.", d.TEAL),
    ("2012", "AlexNet", "Deep Learning",
     "A subset of ML using many-layered neural networks to find complex patterns in large, "
     "unstructured data — text, images, audio, video.", d.TEAL),
    ("2018", "the first GPT", "Generative AI",
     "A branch of AI that creates new content — text, images, video, audio, code — by learning "
     "patterns from massive datasets.", d.TEAL),
    ("2024", "agents take off", "Agentic AI",
     "Builds on generative models by adding tool/API use, memory and planning in a closed loop, "
     "enabling autonomous goal pursuit beyond content creation.", d.MINT),
]


def build(prs):
    for slide in list(prs.slides):          # the previous version or the original hand-made slide
        if any(sh.has_text_frame and sh.text_frame.text == HEADLINE for sh in slide.shapes):
            d.delete_slide(prs, slide)
    s = d.content_slide(
        prs, "Foundations · 1955–2024", HEADLINE,
        "Each idea is a part of the one around it, not a replacement for it.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: nested circles, all touching the same bottom point ----------------------------
    cx = 2.1
    for dia, alpha, name in ((2.95, 8, "Artificial Intelligence"), (2.35, 12, "Machine Learning"),
                             (1.75, 16, "Deep Learning")):
        d.circle(s, cx - dia / 2, BOTTOM - dia, dia, color=d.TEAL, alpha=alpha)
        d.text(s, name, cx - 1.0, BOTTOM - dia + 0.2, 2.0, 0.22, font=d.HEADLINE, size=11,
               color=d.NAVY, align=d.PP_ALIGN.CENTER)
    # Two overlapping circles fully inside Deep Learning (agentic AI builds on generative models):
    # centres 0.34 in left/right of the middle and 0.18 in below the Deep Learning centre.
    small, cy = 0.74, BOTTOM - 1.75 / 2 + 0.18
    for dx, color, alpha, name in ((-0.34, d.TEAL, 35, "Generative\nAI"),
                                   (0.34, d.MINT, 40, "Agentic\nAI")):
        x, y = cx + dx - small / 2, cy - small / 2
        d.circle(s, x, y, small, color=color, alpha=alpha)
        d.text(s, name, x, y, small, small, font=d.HEADLINE, size=9, color=d.NAVY,
               align=d.PP_ALIGN.CENTER, anchor=d.MSO_ANCHOR.MIDDLE)

    # --- Right: vertical timeline, oldest on top ----------------------------------------------
    line_x, tx, top, row_h = 4.3, 4.55, 1.95, 0.6
    d.line(s, line_x, top + 0.2, line_x, top + 4 * row_h + 0.2, color=d.BORDER, width=1.5)
    for i, (year, milestone, name, definition, accent) in enumerate(IDEAS):
        y = top + i * row_h
        d.circle(s, line_x - 0.07, y + 0.13, 0.14, color=accent, alpha=100)
        d.rich_text(s, [(year, accent), (f"  ·  {milestone}".upper(), d.MUTED)], tx, y + 0.02,
                    1.65, 0.16, font=d.MONO, size=8, spacing=100)
        d.text(s, name, tx, y + 0.2, 1.6, 0.3, font=d.HEADLINE, size=13, color=d.NAVY)
        # The original definitions are longer: they start level with the year and take 3 lines.
        d.text(s, definition, 6.2, y + 0.03, 3.32, 0.55, size=9, color=d.MUTED)

    d.takeaway(s, "Deep learning is a method within machine learning, not a synonym for all of AI.")
    return s


if __name__ == "__main__":
    d.run(build)
