"""Slide "Neural networks": input / hidden / output layers, one layer and one weight called out,
what is actually learned, and token chips showing what goes in and comes out in a language model.

Replaces the original hand-made slide (broken "N eural Networks" heading, off-system fonts,
hard-coded page number). Placed after the Deep Learning divider; re-running replaces the slide.
"""
import design as d

MARKER = "slide-neural-network"
ANCHOR = "section-dl"
OLD_SLIDE = "Learn representations, not just a decision rule"   # original slide, removed once

# Node columns: (x, [(y center, activation value)]). Values are illustrative.
INPUT = (1.55, [(3.05, "0.90"), (3.55, "0.30"), (4.05, "0.60")])
HIDDEN1 = (2.75, [(2.90, "0.81"), (3.35, "0.24"), (3.80, "0.76"), (4.25, "0.38")])
HIDDEN2 = (3.95, [(2.90, "0.52"), (3.35, "0.91"), (3.80, "0.14"), (4.25, "0.63")])
OUTPUT = (5.15, [(3.35, "0.45"), (3.85, "0.18")])

# Weights into the first hidden neuron; the sum works out to its activation:
# 0.90 x 0.50 + 0.30 x (-0.40) + 0.60 x 0.80 = 0.81
WEIGHTS = [0.50, -0.40, 0.80]
# Weight labels placed and rotated by hand in PowerPoint (user edit): each number runs along its own
# line. (x, y, rotation in degrees).
LABEL_POS = [(2.005, 2.830, 349.8), (2.006, 3.040, 323.3), (2.015, 3.272, 309.5)]
# The weight values are shown in the colour of the weight lines.
FORMULA = [("0.90 × ", d.NAVY), ("0.50", d.MINT), ("  +  0.30 × (", d.NAVY), ("−0.40", d.MINT),
           (")  +  0.60 × ", d.NAVY), ("0.80", d.MINT), ("  =  0.81", d.NAVY)]

R = 0.17                                     # node radius

# "The cat sat" goes in, so the likely next token is "on".
IN_TOKENS = ["The", "cat", "sat"]
OUT_TOKENS = ["on", "down"]
OUT_PROBS = ["45 %", "18 %"]


def node(s, x, y, fill, value):
    """Neuron as a filled circle with its (illustrative) activation value inside."""
    d.circle(s, x - R, y - R, 2 * R, color=fill, alpha=100, line_width=0.75)
    d.text(s, value, x - R, y - 0.07, 2 * R, 0.16, font=d.MONO, size=7, color=d.WHITE,
           align=d.PP_ALIGN.CENTER)


def connect(s, left, right, highlight=None, weights=None):
    """All-to-all connections. `highlight` is the (left, right) pair drawn as the example weight;
    `weights` labels the connections into the first neuron of the right column with their values."""
    lx, lys = left[0], [y for y, _ in left[1]]
    rx, rys = right[0], [y for y, _ in right[1]]
    for i, ly in enumerate(lys):
        for j, ry in enumerate(rys):
            if highlight == (i, j) or (weights and j == 0):
                continue
            d.line(s, lx + R, ly, rx - R, ry, color=d.BORDER, width=0.75)
    if weights:  # the connections into the first neuron of the right column, with their values
        for i, (ly, w) in enumerate(zip(lys, weights)):
            # All three the same fine width (user edit); the numbers carry the emphasis.
            d.line(s, lx + R, ly, rx - R, rys[0], color=d.MINT, width=0.75)
            # Label positions placed by hand in PowerPoint (user edit): each number sits on its own
            # line. Colour matches the weight lines and the weights in the formula.
            fx, fy, rot = LABEL_POS[i]
            d.text(s, f"{w:.2f}".replace("-", "−"), fx, fy, 0.36, 0.16, font=d.MONO,
                   size=7, color=d.MINT, align=d.PP_ALIGN.CENTER, rotation=rot)


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 3 · Deep learning", "Neural networks: many layers, many adjustable weights",
        "Deep learning uses neural networks with many layers to learn complex patterns.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Diagram (geometry fine-tuned by hand in PowerPoint; keep unless asked) ------------------
    d.card(s, d.LEFT, 1.95, 5.78, 3.0)

    connect(s, INPUT, HIDDEN1, highlight=(0, 0), weights=WEIGHTS)
    connect(s, HIDDEN1, HIDDEN2)
    connect(s, HIDDEN2, OUTPUT)
    for column, fill in ((INPUT, d.NAVY), (HIDDEN1, d.TEAL), (HIDDEN2, d.TEAL), (OUTPUT, d.NAVY)):
        for y, value in column[1]:
            node(s, column[0], y, fill, value)
    d.rich_text(s, FORMULA, 0.85, 2.05, 3.6, 0.22, font=d.MONO, size=8)

    # Callouts: caption in the colour of the thing it points at (user edit).
    d.rect(s, HIDDEN2[0] - 0.24, 2.66, 0.48, 1.84, line=d.TEAL, line_width=0.75, radius=0.06)
    d.text(s, "Layer", 4.40, 2.31, 0.60, 0.17, size=10, color=d.TEAL)
    d.line(s, 4.45, 2.52, 4.26, 2.77, color=d.TEAL, width=1, arrow=True)

    d.text(s, "Weights", 1.55, 2.31, 0.60, 0.17, size=10, color=d.MINT)
    d.line(s, 1.96, 2.56, 2.12, 2.813, color=d.MINT, width=1, arrow=True)

    d.text(s, "Neuron", 3.02, 2.31, 0.48, 0.17, size=10, color=d.TEAL)
    d.line(s, 3.05, 2.52, 2.88, 2.75, color=d.TEAL, width=1, arrow=True)

    # Layer names
    mid_hidden = (HIDDEN1[0] + HIDDEN2[0]) / 2
    for x, name, w in ((INPUT[0], "Input layer", 1.6), (mid_hidden, "Hidden layers", 2.0),
                       (OUTPUT[0], "Output layer", 1.6)):
        d.text(s, name.upper(), x - w / 2, 4.60, w, 0.22, font=d.MONO, size=9.5, color=d.MUTED,
               spacing=100, align=d.PP_ALIGN.CENTER)

    # Tokens in, tokens out (probability next to the chip, user edit)
    for (y, _), tok in zip(INPUT[1], IN_TOKENS):
        d.chip(s, tok, 0.72, y - 0.14, 0.60, h=0.28, fill=d.TEAL_TINT, color=d.NAVY, size=9)
        d.line(s, 1.34, y, INPUT[0] - R - 0.02, y, color=d.DIM_ON_DARK, width=0.75, arrow=True)
    for (y, _), tok, prob in zip(OUTPUT[1], OUT_TOKENS, OUT_PROBS):
        d.line(s, OUTPUT[0] + R + 0.02, y, 5.55, y, color=d.DIM_ON_DARK, width=0.75, arrow=True)
        d.chip(s, tok, 5.60, y - 0.14, 0.39, h=0.28, fill=d.MINT_TINT, color=d.NAVY, size=9)
        d.text(s, prob, 6.04, y - 0.07, 0.30, 0.135, font=d.MONO, size=8, color=d.NAVY,
               anchor=d.MSO_ANCHOR.MIDDLE)     # position fine-tuned by hand (user edit)

    # --- Right: three cards, evenly distributed between y=1.95 and the takeaway -------------------
    x, w, tw = 6.53, 3.14, 2.75          # card left, card width, text width
    for top, height, accent, title, body in (
            (1.95, 1.15, d.MINT, "WHAT THE MODEL LEARNS",
             ["Training adjusts the weights on every connection — millions to billions of "
              "numbers. Those weights are the model's knowledge; nothing else is stored."]),
            (3.19, 0.72, d.NAVY, "INPUTS AND OUTPUTS",
             ["In a language model, what goes in and comes out are tokens."]),
            (4.00, 0.95, d.TEAL, "SIMPLIFIED ON PURPOSE",
             ["· One token = many numbers",
              "· Output is calculated across the whole vocabulary",
              "· Each neuron also has a bias",
              "· A real LLM is a Transformer"])):
        d.rect(s, x, top, w, height, fill=d.WHITE, line=d.BORDER)
        d.rect(s, x, top, 0.05, height, fill=accent)
        d.text(s, title, x + 0.19, top + 0.10, 2.4, 0.17, font=d.MONO, size=9.5, color=accent,
               spacing=100)
        if len(body) == 1:
            d.text(s, body[0], x + 0.20, top + 0.32, tw, height - 0.4, size=10, color=d.TEXT_DARK)
        else:
            for i, item in enumerate(body):
                d.text(s, item, x + 0.17, top + 0.28 + i * 0.16, 2.85, 0.16, size=9,
                       color=d.TEXT_DARK)

    d.takeaway(s, "Deep learning is a method within machine learning, not a synonym for all AI.",
               y=5.1)
    return s


if __name__ == "__main__":
    prs = __import__("pptx").Presentation("ai-terminology-hell.pptx")
    for slide in list(prs.slides):                  # drop the original hand-made slide once
        if any(sh.has_text_frame and OLD_SLIDE in sh.text_frame.text for sh in slide.shapes):
            d.delete_slide(prs, slide)
    build(prs)
    prs.save("ai-terminology-hell.pptx")
    print("Neural network slide rebuilt")
