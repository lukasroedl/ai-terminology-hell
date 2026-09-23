"""Slide "2017 the architecture, 2018 the first GPT": milestone band, attention demo and GPT spelled
out, tied together by the two year tags.

The attention demo follows a decoder-only model: "it" attends only to the words before it; the words
after it are dimmed. Placed after the Generative AI slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-transformer"
ANCHOR = "From recognizing content to creating it"  # GenAI/LLM slide

# Sentence for the attention demo (wording and weights as set by the user in PowerPoint).
# kind: "mint"/"teal"/"dim" = attended with that colour, "self" = "it" attending to itself,
# None = comes after "it", so a text generator cannot see it yet.
WORDS = [("The", "dim"), ("cat", "mint"), ("sat", "teal"), ("because", "dim"), ("it", "self"),
         ("was", None), ("tired", None)]
LINE_COLOR = {"mint": "MINT", "teal": "TEAL", "dim": "DIM_ON_DARK", "self": "DIM_ON_DARK"}

GPT = [
    ("G", "enerative", "Creates new text, not just labels or scores."),
    ("P", "re-trained", "Learn from huge amounts of text, before anyone uses it."),
    ("T", "ransformer", "Built on the transformer architecture."),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · 2017–2018", "The engine for every LLM: Transformer Architecture",
        "A 2017 published neural-network architecture from Google lead to the first GPT model "
        "in 2018.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    left_x, left_w = d.LEFT, 4.38                     # the 2017 column
    right_x = left_x + left_w + 0.14                  # the 2018 column
    right_w = d.LEFT + d.CONTENT_W - right_x

    # --- Two columns, each headed by its milestone ------------------------------------------------
    for x, w, accent, label, text in (
            (left_x, left_w, d.MINT, "2017 · Google",
             "“Attention Is All You Need” introduces Transformer Architecture."),
            (right_x, right_w, d.NAVY, "2018 · OpenAI",
             "GPT-1: the first Generative Pre-trained Transformer.")):
        d.card(s, x, 1.95, w, 3.0, accent=accent)
        d.label(s, label, x + 0.23, 2.1, w=2.5, color=accent)
        d.text(s, text, x + 0.23, 2.46, w - 0.23, 0.17, size=10, color=d.TEXT_DARK)

    # --- Left column: what the 2017 architecture does ---------------------------------------------
    d.label(s, "Attention: the core idea", left_x + 0.23, 2.88, w=3.0)

    row_y, node_y = 3.16, 3.70
    x, centers, attended = left_x + 0.23, {}, []
    for word, kind in WORDS:
        w = 0.12 + 0.09 * len(word)
        if kind == "self":
            d.chip(s, word, x, row_y, w, h=0.3, size=10, fill=d.NAVY, color=d.WHITE)
        elif kind is None:                     # not visible to "it" yet
            d.chip(s, word, x, row_y, w, h=0.3, size=10, fill=d.LIGHT_BG, color=d.DIM_ON_DARK,
                   line=d.BORDER)
        else:
            fill = d.MINT if kind == "mint" else d.TEAL_TINT
            d.chip(s, word, x, row_y, w, h=0.3, size=10, fill=fill, color=d.NAVY)
            attended.append(word)
        centers[word] = x + w / 2
        x += w + 0.06

    # The question node sits under the words before "it"; "it" also attends to itself.
    node_x = (centers[attended[0]] + centers[attended[-1]]) / 2
    for word, kind in WORDS:
        if kind is None:
            continue
        d.line(s, node_x, node_y, centers[word], row_y + 0.3, color=getattr(d, LINE_COLOR[kind]),
               width=1.5 if kind == "mint" else 0.75)
    d.chip(s, "“it” = ?", node_x - 0.42, node_y, 0.84, h=0.3, fill=d.NAVY, color=d.WHITE, size=9.5)

    d.text(s, "The model perceives “it” as a weighted combination of itself and all of the words "
              "before it. A thicker line means more attention, so the word “cat” matters most for "
              "the word “it” — the mechanism that made Transformers so good at language.",
           left_x + 0.23, 4.12, left_w - 0.45, 0.64, size=9.5, color=d.TEXT_DARK)

    # --- Right column: GPT spelled out, one card per letter ---------------------------------------
    h, gap = 0.53, 0.14
    for i, (letter, rest, desc) in enumerate(GPT):
        top = 2.84 + i * (h + gap)
        d.rect(s, right_x + 0.23, top, right_w - 0.46, h, fill=d.LIGHT_BG, radius=0.07)
        d.rect(s, right_x + 0.23, top, 0.04, h, fill=d.TEAL)          # thin accent edge
        d.rect(s, right_x + 0.37, top + 0.09, 0.35, 0.35, fill=d.WHITE, radius=0.07)
        d.text(s, letter, right_x + 0.37, top + 0.09, 0.35, 0.33, font=d.HEADLINE, size=19,
               color=d.TEAL, align=d.PP_ALIGN.CENTER, anchor=d.MSO_ANCHOR.MIDDLE)
        d.rich_text(s, [(letter + rest, d.NAVY)], right_x + 0.84, top + 0.07, 2.4, 0.22,
                    font=d.HEADLINE, size=12)
        d.text(s, desc, right_x + 0.84, top + 0.28, right_w - 1.2, 0.2, size=9, color=d.MUTED)

    # One timeline across both columns, drawn last so it runs over the cards and the gap between
    # them instead of being cut by the column accent bars.
    d.line(s, left_x + 0.23, 2.36, d.LEFT + d.CONTENT_W - 0.23, 2.36, color=d.BORDER, width=1.5)
    for dot_x, accent in ((left_x + 0.27, d.MINT), (right_x + 0.27, d.NAVY)):
        d.circle(s, dot_x, 2.29, 0.14, color=accent, alpha=100, line_width=0.75)

    d.rect(s, d.LEFT, 5.07, 0.05, 0.24, fill=d.TEAL)
    d.text(s, "Nearly every language model today is built on this architecture — ChatGPT, Claude, "
              "Gemini, Llama and more.", 0.78, 5.05, 8.74, 0.2, size=12, color=d.NAVY)
    return s


if __name__ == "__main__":
    d.run(build)
