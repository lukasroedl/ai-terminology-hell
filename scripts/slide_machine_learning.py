"""Slide "Stream 2: machine learning": same spam problem, solved by learning from labelled examples.

Placed right after the explicit-programming slide. Re-running replaces the slide.
"""
import design as d

MARKER = "slide-machine-learning"
ANCHOR = "section-ml"  # after the "Machine Learning" section divider

EXAMPLES = [("Free money now!", True), ("Meeting at 3 pm", False),
            ("You won a prize!", True), ("Minutes from Monday", False)]

# Learned signals: (word, strength 0..1, points to spam?)
PATTERNS = [("prize", 0.95, True), ("free", 0.85, True), ("claim", 0.6, True),
            ("meeting", 0.75, False), ("minutes", 0.6, False)]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Foundations · Stream 2 · since 1959", "Machine learning: the computer finds the rules",
        "Instead of writing rules, show the computer many examples together with the right answer.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    top, h = 1.95, 2.3
    d.card(s, d.LEFT, top, d.CONTENT_W, h)

    # Four steps, each in its own light box: (left, width). Arrows run between the boxes.
    by, bh, cy = 2.03, 2.14, 3.1
    B = [(0.75, 2.4), (3.38, 1.6), (5.2, 2.2), (7.62, 1.81)]
    for bx, bw in B:
        d.step_box(s, bx, by, bw, bh)
    for (ax, aw), (bx, _) in zip(B, B[1:]):
        d.line(s, ax + aw, cy, bx - 0.02, cy, color=d.TEAL, width=1.5, arrow=True)

    # --- Step 1: labelled examples ------------------------------------------------------------------
    x = B[0][0] + 0.12
    d.step_label(s, 1, "Labelled examples", x, 2.1, w=2.3)
    for i, (mail, spam) in enumerate(EXAMPLES):
        y = 2.42 + i * 0.36
        d.chip(s, mail, x, y, 1.6, h=0.28, fill=d.WHITE, color=d.NAVY, size=9, font=d.BODY,
               line=d.BORDER)
        d.chip(s, "SPAM" if spam else "OK", x + 1.65, y, 0.55, h=0.28,
               fill=d.NAVY if spam else d.TEAL_TINT, color=d.MINT if spam else d.NAVY, size=8.5)
    d.text(s, "… plus thousands more", x, 3.86, 2.2, 0.25, size=9.5, color=d.MUTED)

    # --- Step 2: training ---------------------------------------------------------------------------
    x = B[1][0] + 0.12
    d.step_label(s, 2, "Training", x, 2.1, w=1.5)
    cx, r = B[1][0] + B[1][1] / 2, 0.5
    d.circle(s, cx - r, cy - r, 2 * r, color=d.TEAL, alpha=18)
    d.text(s, "Learn", cx - r, cy - 0.17, 2 * r, 0.35, font=d.HEADLINE, size=15, color=d.NAVY,
           align=d.PP_ALIGN.CENTER)

    # --- Step 3: learned patterns as a tug of war --------------------------------------------------
    # Spam words pull right (mint), normal words pull left (teal); bar length = signal strength.
    # The word sits on the opposite side of the centre line from its bar.
    x = B[2][0] + 0.1
    d.step_label(s, 3, "Learned patterns", x, 2.1, w=2.2)
    mid = B[2][0] + B[2][1] / 2
    # End tags styled like the answers in step 1, so the colours connect.
    d.chip(s, "◄ OK", B[2][0] + 0.12, 2.38, 0.62, h=0.24, fill=d.TEAL_TINT, color=d.NAVY, size=8)
    d.chip(s, "SPAM ►", B[2][0] + B[2][1] - 0.74, 2.38, 0.62, h=0.24, fill=d.NAVY, color=d.MINT,
           size=8)
    d.line(s, mid, 2.66, mid, 3.86, color=d.DIM_ON_DARK, width=1)
    for i, (word, strength, spammy) in enumerate(PATTERNS):
        y = 2.68 + i * 0.24
        length = 0.9 * strength
        if spammy:
            d.rect(s, mid, y + 0.04, length, 0.14, fill=d.MINT)
            d.text(s, word, mid - 0.88, y, 0.8, 0.22, font=d.MONO, size=9, color=d.NAVY,
                   align=d.PP_ALIGN.RIGHT)
        else:
            d.rect(s, mid - length, y + 0.04, length, 0.14, fill=d.TEAL)
            d.text(s, word, mid + 0.08, y, 0.8, 0.22, font=d.MONO, size=9, color=d.NAVY)

    # --- Step 4: classification of a new email --------------------------------------------------------------------------
    x, w = B[3][0] + 0.1, B[3][1] - 0.2
    d.step_label(s, 4, "Classification", x, 2.1, w=1.7)
    d.chip(s, "“Claim your prize today!”", x, 2.62, w, h=0.46, fill=d.WHITE, color=d.NAVY,
           size=9, font=d.BODY, line=d.BORDER)
    d.line(s, x + w / 2, 3.12, x + w / 2, 3.38, color=d.TEAL, width=1.25, arrow=True)
    d.chip(s, "SPAM · 94%", x, 3.42, w, h=0.36, fill=d.NAVY, color=d.MINT, size=10)
    d.text(s, "Caught, with no new rule", x, 3.86, w + 0.1, 0.25, size=9.5, color=d.TEAL)

    # --- Bottom: history (the "learning pulls ahead" statement has its own slide next) -------------
    y, hh = 4.38, 0.52
    d.card(s, d.LEFT, y, d.CONTENT_W, hh)
    d.text(s, "1959: Arthur Samuel's checkers program learns by playing against itself and gives "
              "“machine learning” its name.", d.LEFT + 0.23, y + 0.14, d.CONTENT_W - 0.35, 0.3, size=10.5,
           color=d.TEXT_DARK)

    d.takeaway(s, "Data + answers → rules. The more good examples, the better the learned rules.",
               y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
