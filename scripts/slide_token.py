"""Slide "Token": text -> tokens -> numbers, plus rule of thumb and why it matters.

Placed right after the Transformer slide (before next-word prediction). Re-running replaces it.
"""
import design as d

MARKER = "slide-token"
ANCHOR = "slide-transformer"

# Illustrative split and IDs for "AI makes pharmacovigilance easier." Real tokenizers differ per
# model: common words stay whole, long or rare words break apart, punctuation is its own token.
TOKENS = [("AI", "15836"), ("makes", "3872"), ("pharmac", "27291"), ("ovig", "9014"),
          ("ilance", "5188"), ("easier", "9013"), (".", "13")]
# What the model really computes with: the first numbers of one token's embedding.
EMBEDDING = ["0.12", "−0.48", "0.91", "0.05"]
FOCUS = 2                     # the token whose ID is followed into its embedding ("pharmac")


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · Tokens", "Tokens: Models read tokens, not words",
        "Text is cut into tokens: small pieces, often a whole word, sometimes just part of one.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: from text down to what the model computes with -------------------------------------
    d.card(s, d.LEFT, 1.95, 5.6, 3.0)
    bx, bw, bh = 0.78, 5.3, 0.6
    tops = (2.05, 2.72, 3.39, 4.06)
    for top in tops:
        d.step_box(s, bx, top, bw, bh)

    d.step_label(s, 1, "Your text", 0.92, tops[0] + 0.06)
    d.text(s, "AI makes pharmacovigilance easier.", 0.92, tops[0] + 0.25, 5.0, 0.3, size=15,
           color=d.NAVY)
    d.step_label(s, 2, "Cut into tokens", 0.92, tops[1] + 0.06)
    d.step_label(s, 3, "Each token is translated into its vocabulary ID", 0.92, tops[2] + 0.06,
                 w=4.0)
    x = 0.92
    for i, (tok, tid) in enumerate(TOKENS):
        w = 0.20 + 0.09 * len(tok)
        d.chip(s, tok, x, tops[1] + 0.26, w, h=0.28, size=10,
               fill=d.TEAL_TINT if i % 2 == 0 else d.MINT_TINT, color=d.NAVY)
        d.chip(s, tid, x, tops[2] + 0.26, w, h=0.28, size=9, fill=d.WHITE, color=d.NAVY,
               line=d.TEAL if i == FOCUS else d.BORDER)      # the ID followed in step 4
        x += w + 0.08

    # Step 4: follow one vocabulary ID down into its embedding.
    d.step_label(s, 4, "Each vocabulary ID is translated into its embedding", 0.92,
                 tops[3] + 0.06, w=4.2)
    tok, tid = TOKENS[FOCUS]
    w = 0.20 + 0.09 * len(tok)
    d.chip(s, tid, 0.92, tops[3] + 0.26, w, h=0.28, size=9, fill=d.WHITE, color=d.NAVY,
           line=d.TEAL)
    x = 0.92 + w
    d.line(s, x + 0.04, tops[3] + 0.4, x + 0.3, tops[3] + 0.4, color=d.TEAL, width=1, arrow=True)
    x += 0.38
    for value in EMBEDDING:
        d.chip(s, value, x, tops[3] + 0.26, 0.52, h=0.28, size=9, fill=d.NAVY, color=d.WHITE)
        x += 0.56
    d.text(s, "… hundreds more", x + 0.04, tops[3] + 0.31, 1.3, 0.22, size=9, color=d.MUTED)

    note = d.text(s, "Embedding = Numbers the model actually computes with (what we feed into the "
                     "neural network).", 0.92, 4.7, 5.2, 0.22, size=9, color=d.MUTED)
    note.left, note.top, note.width, note.height = (d.Emu(713232), d.Emu(4319147), d.Emu(5010912),
                                                    d.Emu(138499))          # user edit 2026-09-25

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

    d.takeaway(s, "The model never sees letters or words, only numbers.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
