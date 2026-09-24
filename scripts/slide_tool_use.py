"""Slide "Tool use: the model gets hands": RAG's fixed route vs. the model choosing from a set of
tools, plus the names the idea goes by.

Replaces the original hand-made tool use slide ("From knowledge to capability") in plain language.
Placed after the RAG slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-tool-use"
ANCHOR = "slide-rag"
OLD_SLIDE = "From knowledge to capability"

ROUTE = ["Question", "Search", "LLM", "Answer"]
TOOLS = ["Search documents", "Calculator", "Calendar", "Send email"]
CHOSEN = "Calendar"
NAMES = ["Tool use", "Tool calling", "Function calling"]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "2021–2023 · Tool use", "Tool use: the model gets hands",
        "Now the model decides by itself when to use a tool, and tools can also do things, not "
        "just read.", index=d.index_after(prs, ANCHOR), marker=MARKER)

    w, top, h = 4.38, 1.95, 2.12
    lx, rx = d.LEFT, d.LEFT + w + 0.14
    for x, accent, title in ((lx, d.TEAL, "RAG: a fixed route"),
                             (rx, d.MINT, "Tool use: the model chooses")):
        d.card(s, x, top, w, h, accent=accent)
        d.text(s, title, x + 0.23, top + 0.12, w - 0.4, 0.3, font=d.HEADLINE, size=15, color=d.NAVY)

    # --- Left: always the same four stops ------------------------------------------------------
    cw, cg = 0.78, 0.28
    y = 2.95
    for i, stop in enumerate(ROUTE):
        x = lx + 0.26 + i * (cw + cg)
        if stop == "LLM":
            d.chip(s, stop, x, y, cw, h=0.32, size=9.5, fill=d.NAVY, color=d.WHITE)
        else:
            d.chip(s, stop, x, y, cw, h=0.32, size=9, fill=d.WHITE, color=d.NAVY, font=d.BODY,
                   line=d.BORDER)
        if stop == "Search":
            d.label(s, "always", x, y - 0.25, w=cw, color=d.TEAL, size=7.5)
        if i < len(ROUTE) - 1:
            d.line(s, x + cw + 0.03, y + 0.16, x + cw + cg - 0.03, y + 0.16, color=d.TEAL, arrow=True)
    d.text(s, "The developers fixed the route: search always runs first, and the model can only "
              "read.", lx + 0.23, 3.62, w - 0.45, 0.4, size=9.5, color=d.MUTED)

    # --- Right: the model picks one tool from the toolbox ---------------------------------------
    llm_x, llm_y = rx + 0.3, 2.9
    d.chip(s, "LLM", llm_x, llm_y, 0.7, h=0.32, size=9.5, fill=d.NAVY, color=d.WHITE)
    tx, tw, th = rx + 1.9, 1.5, 0.2
    d.label(s, "Tools", tx, 2.38, w=1.0, color=d.MUTED, size=7.5)
    for i, tool in enumerate(TOOLS):
        ty = 2.6 + i * 0.24
        chosen = tool == CHOSEN
        d.line(s, llm_x + 0.72, llm_y + 0.16, tx - 0.03, ty + th / 2,
               color=d.MINT if chosen else d.BORDER, width=1.75 if chosen else 0.75, arrow=chosen)
        d.chip(s, tool, tx, ty, tw, h=th, size=8, font=d.BODY, color=d.NAVY,
               fill=d.MINT_TINT if chosen else d.WHITE, line=d.MINT if chosen else d.BORDER)
    d.text(s, "It picks the tool it needs, or none. Tools can read (search) and act (send an "
              "email). Search is now just one tool among many.", rx + 0.23, 3.62, w - 0.45, 0.4,
           size=9.5, color=d.MUTED)

    # --- Names ------------------------------------------------------------------------------------
    d.card(s, d.LEFT, 4.2, d.CONTENT_W, 0.68, accent=None)
    d.label(s, "Same idea, three names", 0.85, 4.28, w=3.0, color=d.MUTED, size=8)
    x = 0.85
    for i, name in enumerate(NAMES):
        cw = 0.3 + 0.07 * len(name)
        d.chip(s, name, x, 4.5, cw, h=0.26, size=9, font=d.BODY,
               fill=d.TEAL if i == 0 else d.TEAL_TINT, color=d.WHITE if i == 0 else d.NAVY)
        x += cw + 0.1
    d.text(s, "“Tool use” is the general term. “Function calling” is the name in some developer "
              "platforms, e.g. OpenAI’s.", 5.0, 4.35, 4.35, 0.45, size=9.5, color=d.TEXT_DARK)

    d.takeaway(s, "RAG gave the model something to read. Tool use gives it something to do.")
    return s


if __name__ == "__main__":
    d.run(build)
