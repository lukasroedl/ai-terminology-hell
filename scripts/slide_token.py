"""Slide "Token": text -> tokens -> numbers, plus rule of thumb and why it matters.

Placed right after the Transformer slide (before next-word prediction). Re-running replaces it.
"""
import design as d

MARKER = "slide-token"
ANCHOR = "slide-transformer"

# Illustrative split and IDs. Real tokenizers differ per model.
TOKENS = [("Pharm", "47312"), ("aco", "7904"), ("vig", "29015"), ("ilance", "5818"),
          ("matters", "13121"), ("!", "0")]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · Tokens", "Models read tokens, not words",
        "Text is cut into tokens: small pieces, often a whole word, sometimes just part of one.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: the three steps ------------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, 5.6, 3.0)
    # Each step sits in its own light box: (top of box) for steps 1-3.
    bx, bw, bh = 0.78, 5.3, 0.72
    tops = (2.07, 2.87, 3.67)
    for top in tops:
        d.step_box(s, bx, top, bw, bh)
    d.step_label(s, 1, "Your text", 0.92, tops[0] + 0.07)
    d.text(s, "Pharmacovigilance matters!", 0.92, tops[0] + 0.29, 5.0, 0.4, size=18, color=d.NAVY)
    d.step_label(s, 2, "Cut into tokens", 0.92, tops[1] + 0.07)
    d.step_label(s, 3, "Each token becomes a number", 0.92, tops[2] + 0.07)
    x = 0.92
    for i, (tok, tid) in enumerate(TOKENS):
        w = 0.24 + 0.1 * len(tok)
        d.chip(s, tok, x, tops[1] + 0.31, w, fill=d.TEAL_TINT if i % 2 == 0 else d.MINT_TINT,
               color=d.NAVY)
        d.chip(s, tid, x, tops[2] + 0.31, w, fill=d.WHITE, color=d.NAVY, size=10, line=d.BORDER)
        x += w + 0.1
    d.text(s, "Illustrative split: every model has its own token vocabulary.",
           0.92, 4.53, 5.2, 0.25, size=10, color=d.MUTED)

    # --- Right: rule of thumb + why it matters --------------------------------------------------
    x, w = 6.45, 3.07
    d.card(s, x, 1.95, w, 1.42)
    d.label(s, "Rule of thumb", x + 0.25, 2.08)
    d.text(s, "1 token ≈ ¾ of a word", x + 0.25, 2.35, w - 0.4, 0.4, font=d.HEADLINE, size=20,
           color=d.NAVY)
    d.text(s, "100 tokens ≈ 75 English words", x + 0.25, 2.9, w - 0.4, 0.3, size=11, color=d.MUTED)

    d.card(s, x, 3.53, w, 1.42)
    d.label(s, "Why it matters", x + 0.25, 3.66)
    d.text(s, "Limits, speed and prices of AI tools are counted in tokens. German text usually "
              "needs more tokens than English.", x + 0.25, 3.93, w - 0.4, 0.95, size=11,
           color=d.TEXT_DARK)

    d.takeaway(s, "The model never sees letters or words, only numbered tokens.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
