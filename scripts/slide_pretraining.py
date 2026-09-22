"""Slide "Pre-training": any text -> next-token guessing staircase -> high-level learning loop.

Placed right after the next-word prediction slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-pretraining"
ANCHOR = "Next-word prediction: probabilities become text"

SENTENCE = ["The", "cat", "sat", "on", "the", "mat"]
# For each step: the model's guess for the next token. Wrong guesses show the real token.
GUESSES = ["dog", "sat", "down", "the", "floor"]

LOOP = [
    ("Compare", "How wrong was the guess?", "loss"),
    ("Trace back", "Which way should each weight move?", "gradients"),
    ("Adjust", "Nudge all weights a tiny step.", None),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · Pre-training", "Pre-training: guess the next token, trillions of times",
        "The model reads huge amounts of text and practices predicting what comes next.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)
    top, h = 1.95, 3.0

    # --- 1: any text is training material ---------------------------------------------------------
    d.card(s, d.LEFT, top, 2.2, h)
    d.step_label(s, 1, "Any text", 0.85, 2.08, w=1.9)
    d.rect(s, 0.85, 2.4, 1.75, 1.85, fill=d.WHITE, line=d.BORDER)
    widths = [1.45, 1.3, 1.45, None, 1.2, 1.45, 0.9]
    for i, w in enumerate(widths):
        y = 2.58 + i * 0.22
        if w is None:  # the highlighted sentence
            d.rect(s, 0.97, y - 0.06, 1.5, 0.2, fill=d.MINT_TINT, line=d.MINT)
            d.text(s, "The cat sat on the mat.", 1.02, y - 0.05, 1.45, 0.18, size=8, color=d.NAVY)
        else:
            d.rect(s, 0.99, y, w, 0.06, fill=d.BORDER)
    d.text(s, "Books, websites, articles: every sentence is practice. No labels needed.",
           0.85, 4.32, 1.9, 0.6, size=9.5, color=d.MUTED)
    d.line(s, 2.5, 3.24, 3.1, 3.24, color=d.MINT, width=1.5, arrow=True)

    # --- 2: the staircase ---------------------------------------------------------------------------
    x0 = 2.97
    d.card(s, x0, top, 4.0, h)
    d.step_label(s, 2, "Guess the next token", x0 + 0.23, 2.08, w=3.6)
    guess_x, mark_x, real_x = 5.58, 6.1, 6.35
    d.label(s, "What the model sees", x0 + 0.23, 2.36, color=d.MUTED, size=8)
    d.label(s, "Guess", guess_x, 2.36, color=d.MUTED, size=8)
    d.label(s, "Real", real_x, 2.36, color=d.MUTED, size=8)

    for step, guess in enumerate(GUESSES):
        y = 2.62 + step * 0.44
        x = x0 + 0.23
        for tok in SENTENCE[:step + 1]:
            w = 0.12 + 0.08 * len(tok)
            d.chip(s, tok, x, y, w, h=0.3, fill=d.TEAL_TINT, color=d.NAVY, size=9.5)
            x += w + 0.05
        d.chip(s, "?", x, y, 0.3, h=0.3, fill=d.WHITE, color=d.TEAL, size=10, line=d.TEAL)

        real = SENTENCE[step + 1]
        right = guess == real
        d.chip(s, guess, guess_x, y, 0.5, h=0.3, fill=d.LIGHT_BG, color=d.NAVY, size=9.5,
               line=d.BORDER)
        d.text(s, "✓" if right else "✗", mark_x, y + 0.02, 0.2, 0.28, size=12,
               color=d.TEAL if right else d.MUTED, align=d.PP_ALIGN.CENTER)
        if not right:
            d.chip(s, real, real_x, y, 0.5, h=0.3, fill=d.MINT, color=d.NAVY, size=9.5)

    # --- 3: learning loop ---------------------------------------------------------------------------
    x0 = 7.12
    w = d.LEFT + d.CONTENT_W - x0
    d.card(s, x0, top, w, h, accent=d.MINT)
    d.step_label(s, 3, "Learn & adjust", x0 + 0.23, 2.08, w=2.1)
    for i, (title, desc, term) in enumerate(LOOP):
        y = 2.45 + i * 0.7
        d.chip(s, "abc"[i], x0 + 0.23, y, 0.3, h=0.3, fill=d.NAVY, color=d.WHITE, size=10)  # sub-steps of step 3
        if i < len(LOOP) - 1:
            d.line(s, x0 + 0.38, y + 0.33, x0 + 0.38, y + 0.67, color=d.TEAL, width=1.25, arrow=True)
        head = f"{title}  ·  {term}" if term else title
        d.text(s, head, x0 + 0.65, y - 0.02, w - 0.75, 0.25, font=d.HEADLINE, size=13, color=d.NAVY)
        d.text(s, desc, x0 + 0.65, y + 0.24, w - 0.75, 0.4, size=9.5, color=d.MUTED)
    d.text(s, "↻  Repeat with the next batch of text", x0 + 0.23, 4.55, w - 0.3, 0.25,
           font=d.MONO, size=9, color=d.TEAL)

    d.takeaway(s, "Repeated over trillions of tokens, this simple game teaches the model grammar, "
                  "facts and style.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
