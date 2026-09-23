"""Slide "Context window": a conversation strip with a window frame, plus how big windows got.

Placed right after the prompt slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-context-window"
ANCHOR = "slide-prompt"

# (block, width in). The first FADED blocks are outside the window.
BLOCKS = [("Instructions", 0.95), ("Document", 1.2), ("Question 1", 0.9), ("Answer 1", 1.0),
          ("Question 2", 0.9), ("Answer 2", 1.0), ("Question 3", 0.9), ("New answer", 1.0)]
FADED = 3

# (year, bar length in, description). Bars grow but are not to scale. Figures: GPT-3.5 at
# ChatGPT launch (4,096), GPT-4 Turbo (128k), Gemini 1.5 Pro (1M); ~670 tokens per page.
SIZES = [("2022", 0.25, "~4,000 tokens  ≈  6 pages"),
         ("2023", 1.3, "~128,000 tokens  ≈  a 200-page book"),
         ("2024", 3.0, "1,000,000+ tokens  ≈  1,500 pages")]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Context window", "The context window: the model's working memory",
        "A model can only “see” a limited amount of text at once, and everything has to fit.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Top: conversation strip with the window ---------------------------------------------------
    d.card(s, d.LEFT, 1.95, d.CONTENT_W, 1.78)
    d.label(s, "A long conversation", 0.85, 2.08)
    x, y, h, gap = 0.95, 2.5, 0.48, 0.07
    window_x = None
    for i, (name, w) in enumerate(BLOCKS):
        if i < FADED:
            d.chip(s, name, x, y, w, h=h, fill=d.LIGHT_BG, color=d.DIM_ON_DARK, size=10,
                   font=d.BODY, line=d.BORDER)
        else:
            window_x = window_x or x
            fill = d.NAVY if name == "New answer" else (d.TEAL_TINT if "Question" in name else d.MINT_TINT)
            d.chip(s, name, x, y, w, h=h, fill=fill, color=d.WHITE if fill == d.NAVY else d.NAVY,
                   size=10, font=d.BODY)
        x += w + gap
    window_end = x - gap
    d.rect(s, window_x - 0.08, y - 0.1, window_end - window_x + 0.16, h + 0.2, line=d.MINT,
           line_width=2.25, rounded=True)
    d.text(s, "CONTEXT WINDOW = HOW MUCH THE MODEL CAN TAKE INTO ACCOUNT AT ONCE",
           window_x - 0.08, 2.19, 5.39, 0.15, font=d.MONO, size=9, color=d.NAVY, spacing=100)

    # Time axis under the conversation: it runs left to right, the window sits at its end.
    axis_y = 3.18
    d.line(s, 0.95, axis_y, window_end + 0.1, axis_y, color=d.DIM_ON_DARK, width=1, arrow=True)
    for tick in (0.95, window_end + 0.1):        # only the two ends carry a tick (user edit)
        d.line(s, tick, axis_y - 0.05, tick, axis_y + 0.05, color=d.DIM_ON_DARK, width=1)
    d.text(s, "start of the conversation", 0.95, axis_y + 0.1, 0.75, 0.3, size=9, color=d.MUTED)
    d.text(s, "now", window_end - 0.7, axis_y + 0.1, 0.8, 0.2, size=9, color=d.MUTED,
           align=d.PP_ALIGN.RIGHT)
    d.text(s, "When the window is full, the oldest parts are dropped or shortened.",
           2.57, axis_y + 0.3, 5.0, 0.3, size=10.5, color=d.MUTED)

    # --- Bottom: how big are windows? -----------------------------------------------------------
    d.card(s, d.LEFT, 3.82, d.CONTENT_W, 1.14)
    d.label(s, "How much fits? (approximate, bars not to scale)", 0.85, 3.93, w=6)
    for i, (year, length, desc) in enumerate(SIZES):
        ry = 4.22 + i * 0.24
        d.text(s, year, 0.85, ry, 0.5, 0.2, font=d.MONO, size=10, color=d.MUTED)
        d.rect(s, 1.45, ry + 0.04, length, 0.13, fill=d.TEAL if i < 2 else d.MINT)
        d.text(s, desc, 1.45 + length + 0.15, ry, 4.5, 0.2, size=10.5, color=d.NAVY)

    d.takeaway(s, "Bigger windows help, but details buried deep in very long inputs can still be "
                  "overlooked.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
