"""Slide "Vocabulary, token, embedding": how the three relate, shown as the model's vocabulary table.

First slide of the "Terms you meet when working with LLMs" block. Re-running replaces it.
"""
import design as d

MARKER = "slide-vocabulary"
ANCHOR = "slide-llm-terms-divider"

# (id, token, first embedding numbers) — illustrative, as on the tokens slide. The values are
# rendered in square brackets and spread across the column.
ROWS = [("15836", "AI", ["0.31", "−0.02", "0.77"]),
        ("3872", "makes", ["−0.14", "0.62", "0.08"]),
        ("27291", "pharmac", ["0.12", "−0.48", "0.91"]),
        ("9013", "easier", ["0.55", "0.27", "−0.36"]),
        ("13", ".", ["0.04", "−0.11", "0.19"])]
EMB_X, EMB_W = 3.2, 3.0                        # embedding column: left edge and width
HIGHLIGHT = 2                                  # the row carried over from the tokens slide

TERMS = [("Vocabulary", d.TEAL,
          "The fixed list of all tokens a model knows — typically 50,000 to 200,000 entries."),
         ("Token", d.MINT,
          "One entry in that list: a word, part of a word or a punctuation mark."),
         ("Embedding", d.NAVY,
          "The list of numbers stored for each entry, learned during training.")]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Vocabulary", "Vocabulary, token, embedding: one table, three terms",
        "Every model carries a fixed list of tokens. Each entry has a number and a list of numbers.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: the vocabulary table ---------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, 5.6, 3.0)
    d.label(s, "The model's vocabulary", 0.85, 2.07, w=3.0)

    cols = ((0.92, 0.85, "ID"), (1.85, 1.35, "Token"), (3.3, 2.9, "Embedding"))
    for x, w, name in cols:
        d.label(s, name, x, 2.42, w=w, color=d.MUTED, size=8)
    d.line(s, 0.92, 2.64, 6.2, 2.64, color=d.BORDER, width=0.75)

    for i, (tid, token, values) in enumerate(ROWS):
        y = 2.74 + i * 0.36
        if i == HIGHLIGHT:
            d.rect(s, 0.86, y - 0.04, 5.4, 0.36, fill=d.LIGHT_BG, radius=0.05)
        d.chip(s, tid, 0.92, y, 0.85, h=0.28, size=9, fill=d.WHITE, color=d.NAVY,
               line=d.TEAL if i == HIGHLIGHT else d.BORDER)
        d.chip(s, token, 1.85, y, 1.0, h=0.28, size=9,
               fill=d.MINT if i == HIGHLIGHT else d.TEAL_TINT, color=d.NAVY)
        # Bracketed, with the values and the "…" spread evenly between the brackets.
        d.text(s, "[", EMB_X, y + 0.04, 0.2, 0.22, font=d.MONO, size=9, color=d.MUTED)
        inner_x, inner_w = EMB_X + 0.18, EMB_W - 0.36
        slot = inner_w / (len(values) + 1)
        for k, value in enumerate(values + ["…"]):
            d.text(s, value, inner_x + k * slot, y + 0.04, slot, 0.22, font=d.MONO, size=9,
                   color=d.MUTED if value == "…" else d.NAVY, align=d.PP_ALIGN.CENTER)
        d.text(s, "]", EMB_X + EMB_W - 0.12, y + 0.04, 0.2, 0.22, font=d.MONO, size=9,
               color=d.MUTED)

    d.text(s, "… and roughly 100,000 more rows.", 0.92, 4.6, 3.5, 0.22, size=9.5, color=d.MUTED)

    # --- Right: the three terms -------------------------------------------------------------------
    x, w = 6.45, 3.07
    for i, (term, color, desc) in enumerate(TERMS):
        top = 1.95 + i * 1.04
        d.card(s, x, top, w, 0.94, accent=color)
        d.text(s, term, x + 0.23, top + 0.12, w - 0.4, 0.28, font=d.HEADLINE, size=15, color=color)
        d.text(s, desc, x + 0.23, top + 0.42, w - 0.4, 0.45, size=10, color=d.TEXT_DARK)

    d.takeaway(s, "Same text, different model, different vocabulary — which is why token counts and "
                  "prices differ.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
