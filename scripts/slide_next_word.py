"""Slide "Generation process: next-word prediction": two generation steps, each with the same
probability picture. The token chosen in step 1 is boxed and an arrow carries it into the input
sequence of step 2.

Replaces the original hand-made slide. Placed after the tokens slide; re-running replaces it.
"""
import design as d

MARKER = "slide-next-word"
ANCHOR = "slide-token"
OLD_SLIDE = "A toy example of an autoregressive language model"

# (context tokens, appended token, [(token, probability, chosen)])
STEPS = [
    (["The", "cat", "sat", "on", "the"], None,
     [("mat", 45, True), ("chair", 25, False), ("floor", 20, False), ("other", 10, False)]),
    (["The", "cat", "sat", "on", "the"], "mat",
     [(".", 70, False), ("today", 15, False), ("quietly", 10, False), ("other", 5, False)]),
]
BAR_X, BAR_MAX = 5.55, 2.2          # probability bars: left edge and full-scale width


def sequence(s, tokens, appended, x, y):
    """Context chips followed by the appended token (mint) and the open slot."""
    boxes = {}
    for token in tokens:
        w = 0.14 + 0.09 * len(token)
        d.chip(s, token, x, y, w, h=0.3, size=10, fill=d.TEAL_TINT, color=d.NAVY)
        x += w + 0.06
    if appended:
        w = 0.14 + 0.09 * len(appended)
        boxes["appended"] = d.chip(s, appended, x, y, w, h=0.3, size=10, fill=d.MINT, color=d.NAVY)
        boxes["appended_box"] = (x, y, w)
        x += w + 0.06
    d.chip(s, "?", x, y, 0.3, h=0.3, size=10, fill=d.WHITE, color=d.TEAL, line=d.TEAL)
    return boxes


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · Generation", "Generation process: next-word prediction",
        "A toy example of an autoregressive language model. All probabilities are illustrative.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    chosen_box = None
    for step, (tokens, appended, options) in enumerate(STEPS):
        top = 1.95 + step * 1.55
        d.card(s, d.LEFT, top, d.CONTENT_W, 1.45)
        d.step_label(s, step + 1, "Score the possible next tokens" if step == 0
                     else "Append it and score again", 0.85, top + 0.1, w=4.0)
        seq = sequence(s, tokens, appended, 0.85, top + 0.38)

        for i, (token, prob, chosen) in enumerate(options):
            y = top + 0.34 + i * 0.26
            d.text(s, token, 4.75, y, 0.75, 0.22, font=d.MONO, size=9.5, color=d.NAVY)
            d.rect(s, BAR_X, y + 0.06, BAR_MAX, 0.1, fill=d.BORDER)          # scale
            d.rect(s, BAR_X, y + 0.06, BAR_MAX * prob / 100, 0.1,
                   fill=d.MINT if chosen else d.TEAL)
            d.text(s, f"{prob}%", BAR_X + BAR_MAX + 0.18, y, 0.5, 0.22, font=d.MONO, size=9.5,
                   color=d.NAVY if chosen else d.MUTED)
            if chosen:                                                        # mark the pick
                d.rect(s, 4.66, y - 0.04, BAR_X + BAR_MAX + 0.06 - 4.66, 0.3, line=d.MINT,
                       line_width=1.25, radius=0.06)
                d.text(s, "chosen", BAR_X + BAR_MAX + 0.72, y, 0.7, 0.22, font=d.MONO, size=8,
                       color=d.MINT)
                chosen_box = (4.66, y + 0.11)                                 # left edge, middle

        if step == 1 and chosen_box and "appended_box" in seq:
            # Carry the chosen token down into the next input sequence, routed around the labels.
            ax, ay = chosen_box
            bx, by, bw = seq["appended_box"]
            lane, mid = 4.5, 3.45          # free column left of the labels, gap between the cards
            d.line(s, ax, ay, lane, ay, color=d.MINT, width=1.25)
            d.line(s, lane, ay, lane, mid, color=d.MINT, width=1.25)
            d.line(s, lane, mid, bx + bw / 2, mid, color=d.MINT, width=1.25)
            d.line(s, bx + bw / 2, mid, bx + bw / 2, by - 0.03, color=d.MINT, width=1.25,
                   arrow=True)

    d.takeaway(s, "Likely continuation does not mean verified fact. Real models predict tokens, "
                  "not always words.", y=5.1)
    return s


if __name__ == "__main__":
    import sys
    deck = sys.argv[1] if len(sys.argv) > 1 else "ai-terminology-hell.pptx"
    prs = __import__("pptx").Presentation(deck)
    for slide in list(prs.slides):          # drop the original hand-made slide once
        if any(sh.has_text_frame and OLD_SLIDE in sh.text_frame.text for sh in slide.shapes):
            d.delete_slide(prs, slide)
    build(prs)
    prs.save(deck)
    print("Next-word slide rebuilt")
