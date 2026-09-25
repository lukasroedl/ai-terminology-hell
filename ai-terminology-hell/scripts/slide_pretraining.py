"""Slide "Pre-training": any text -> next-token guessing staircase -> high-level learning loop.

Placed right after the next-word prediction slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-pretraining"
ANCHOR = "Generation process: next-word prediction"   # headline as edited by the user

SENTENCE = ["The", "cat", "sat", "on", "the", "mat"]
# For each step: the model's guess for the next token. Wrong guesses show the real token.
GUESSES = ["dog", "sat", "down", "the", "floor"]

# (activity, what happens, term for it — shown in brackets under the description)
LOOP = [
    ("Compare", "How wrong was the guess?", "(Calculate Loss)"),
    ("Trace back", "In which direction should each weight move?", "(Calculate Gradients)"),
    ("Adjust", "Update the weights of the neural network a tiny bit.", None),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    # Layout moved up by the user: the cards start right under the headline, and the long
    # explanation sits at the bottom of the slide instead of under the title.
    s = d.content_slide(
        prs, "Generative AI · Pre-training", "Pre-training: guess the next token, trillions of times",
        None, index=d.index_after(prs, ANCHOR), marker=MARKER)
    top, h = 1.45, 3.0

    # --- 1: any text is training material ---------------------------------------------------------
    d.card(s, d.LEFT, top, 2.2, h)
    d.step_label(s, 1, "Any text", 0.85, top + 0.13, w=1.9)
    d.rect(s, 0.85, top + 0.45, 1.75, 1.85, fill=d.WHITE, line=d.BORDER)
    widths = [1.45, 1.3, 1.45, None, 1.2, 1.45, 0.9]
    for i, w in enumerate(widths):
        y = top + 0.63 + i * 0.22
        if w is None:  # the highlighted sentence
            d.rect(s, 0.97, y - 0.06, 1.5, 0.2, fill=d.MINT_TINT, line=d.MINT)
            d.text(s, "The cat sat on the mat.", 1.02, y - 0.05, 1.45, 0.18, size=8, color=d.NAVY)
        else:
            d.rect(s, 0.99, y, w, 0.06, fill=d.BORDER)
    d.text(s, "Books, articles and large parts of the public internet. No labels needed.",
           0.85, top + 2.37, 1.9, 0.48, size=9.5, color=d.MUTED)
    d.line(s, 2.5, top + 1.29, 3.1, top + 1.29, color=d.MINT, width=1.5, arrow=True)

    # --- 2: the staircase ---------------------------------------------------------------------------
    x0 = 2.97
    d.card(s, x0, top, 4.0, h)
    d.step_label(s, 2, "Guess the next token", x0 + 0.23, top + 0.13, w=3.6)
    guess_x, mark_x, real_x = 5.58, 6.1, 6.35
    d.label(s, "What the model sees", x0 + 0.23, top + 0.41, color=d.MUTED, size=8)
    d.label(s, "Guess", guess_x, top + 0.41, color=d.MUTED, size=8)
    d.label(s, "Real", real_x + 0.05, top + 0.41, color=d.MUTED, size=8)

    for step, guess in enumerate(GUESSES):
        y = top + 0.67 + step * 0.44
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
    d.step_label(s, 3, "Learn & adjust", x0 + 0.23, top + 0.13, w=2.1)
    for i, (activity, desc, term) in enumerate(LOOP):
        y = top + 0.45 + i * 0.85
        d.chip(s, "abc"[i], x0 + 0.23, y, 0.3, h=0.3, fill=d.NAVY, color=d.WHITE, size=10)
        if i < len(LOOP) - 1:
            d.line(s, x0 + 0.38, y + 0.38, x0 + 0.38, y + 0.83, color=d.TEAL, width=1.25,
                   arrow=True)
        # Activity large, what happens below it, the technical term smallest of all.
        d.text(s, activity, x0 + 0.6, y + 0.01, 1.65, 0.28, font=d.HEADLINE, size=15, color=d.NAVY)
        d.text(s, desc, x0 + 0.6, y + 0.34, 1.8, 0.32, size=9.5, color=d.MUTED)
        if term:
            d.text(s, term, x0 + 0.6, y + (0.46 if i == 0 else 0.66), 1.7, 0.14, font=d.MONO,
                   size=8.5, color=d.TEAL)
    d.text(s, "↻  Repeat with the next batch of text", x0 + 0.23, 4.26, w - 0.3, 0.25,
           font=d.MONO, size=9, color=d.TEAL)

    # The explanation at the bottom of the slide (user edit).
    d.rect(s, 0.63, 4.7, 0.06, 0.5, fill=d.TEAL)
    d.text(s, "The model reads huge amounts of text and practices predicting what comes next. "
              "Repeated over trillions of tokens, this simple game teaches the model grammar, "
              "facts and style.", 0.76, 4.7, 8.9, 0.5, size=14, color=d.TEXT_DARK)
    return s


if __name__ == "__main__":
    d.run(build)
