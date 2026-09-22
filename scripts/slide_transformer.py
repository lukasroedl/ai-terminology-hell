"""Slide "Transformer / GPT": attention as a fan of lines, plus the GPT acronym spelled out.

Placed right after the GenAI/LLM slide. Re-running replaces the slide.
"""
import design as d

MARKER = "slide-transformer"
ANCHOR = "From recognizing content to creating it"  # GenAI/LLM slide

# Sentence for the attention demo: (word, attention weight from "it"). Illustrative weights.
WORDS = [("The", 0.5), ("cat", 4.5), ("sat", 1.0), ("on", 0.5), ("the", 0.5), ("mat", 1.5),
         ("because", 0.75), ("it", None), ("was", 1.0), ("tired", 2.0)]

GPT = [
    ("G", "Generative", "Creates new text, not just labels or scores."),
    ("P", "Pre-trained", "First learned from huge amounts of text, before anyone uses it."),
    ("T", "Transformer", "Built on the attention design shown above."),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Generative AI · 2017–2018", "The engine inside every LLM: the Transformer",
        "A 2017 neural-network design from Google. Nearly every language model today is built on it.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Attention demo -------------------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, d.CONTENT_W, 1.78)
    d.label(s, "Attention · how a Transformer reads a sentence", 0.85, 2.07, w=6)

    row_y, node_y = 2.4, 3.28
    x, centers = 0.85, {}
    for word, _ in WORDS:
        w = 0.16 + 0.1 * len(word)
        if word == "it":
            d.chip(s, word, x, row_y, w, fill=d.NAVY, color=d.WHITE)
        elif word == "cat":
            d.chip(s, word, x, row_y, w, fill=d.MINT, color=d.NAVY)
        else:
            d.chip(s, word, x, row_y, w, fill=d.TEAL_TINT, color=d.NAVY)
        centers[word] = x + w / 2
        x += w + 0.08

    # "it" asks the question; every other word answers with a line whose thickness = attention.
    node_x = (centers["The"] + centers["tired"]) / 2
    for word, weight in WORDS:
        if weight is None:
            continue
        color = d.MINT if word == "cat" else (d.TEAL if weight >= 1.5 else d.DIM_ON_DARK)
        d.line(s, node_x, node_y, centers[word], row_y + 0.34, color=color, width=weight * 1.4)
    d.chip(s, "“it” = ?", node_x - 0.45, node_y, 0.9, h=0.32, fill=d.NAVY, color=d.WHITE, size=10)

    d.text(s, "To understand “it”, the model weighs every other word, and “cat” matters most.",
           6.85, 2.38, 2.45, 0.7, size=11, color=d.TEXT_DARK)
    d.text(s, "Thicker line = more attention. This is what made Transformers so good at language.",
           6.85, 2.98, 2.45, 0.7, size=11, color=d.MUTED)

    # --- GPT spelled out ------------------------------------------------------------------------
    gap, top, h = 0.15, 3.9, 1.42
    w = (d.CONTENT_W - 3 * gap) / 4
    for i, (letter, name, desc) in enumerate(GPT):
        x = d.LEFT + i * (w + gap)
        d.card(s, x, top, w, h)
        d.text(s, letter, x + 0.22, top + 0.08, 0.5, 0.5, font=d.HEADLINE, size=26, color=d.TEAL)
        d.text(s, name, x + 0.62, top + 0.2, w - 0.7, 0.3, font=d.HEADLINE, size=15, color=d.NAVY)
        d.text(s, desc, x + 0.22, top + 0.62, w - 0.38, 0.65, size=10.5, color=d.MUTED)

    x = d.LEFT + 3 * (w + gap)
    d.rect(s, x, top, w, h, fill=d.NAVY)
    d.text(s, "GPT", x + 0.22, top + 0.08, 1.0, 0.5, font=d.HEADLINE, size=26, color=d.MINT)
    d.text(s, "OpenAI's models behind ChatGPT. Claude, Gemini and Llama are Transformers too.", x + 0.22, top + 0.62, w - 0.38, 0.65, size=10.5,
           color=d.SOFT_ON_DARK)
    return s


if __name__ == "__main__":
    d.run(build)
