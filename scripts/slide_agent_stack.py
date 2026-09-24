"""Slide "How the pieces fit together": the terms of Part 5 as one stack, named like the parts on the
agent anatomy slide (runtime = the agent loop, tools = RAG & tool use, MCP, model = the LLM), each
mapped back to the piece it adds, which answers the bridge question.

Replaces the original hand-made stack slide ("Four layers, one direction of travel") in plain
language. Placed after the MCP architecture slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-agent-stack"
ANCHOR = "slide-mcp-architecture"
OLD_SLIDE = "Four layers, one direction"

# (name as on the agent anatomy slide, what it is in this part, what it does, what it adds, accent);
# top layer first.
LAYERS = [
    ("Runtime", "the agent loop",
     "Follows the instructions: plans, uses tools, checks the result and repeats until the goal "
     "is reached.", "A loop kept in check", d.MINT),
    ("Tools", "RAG & tool use", "The eyes and hands: read your documents, act in your systems.",
     "Knowledge · hands", d.TEAL),
    ("MCP", "the common plug", "Connects the tools to the app in one standard way.",
     "One common plug", d.MUTED),
    ("Model", "the LLM", "The base: understands your request and writes text, including tool "
     "calls.", "Next-token prediction", d.DIM_ON_DARK),
]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · Putting it together", "How the pieces fit together",
        index=d.index_after(prs, ANCHOR), marker=MARKER)   # no subtitle: user edit 2026-09-25

    h, gap = 0.62, 0.1
    for i, (name, alias, does, adds, accent) in enumerate(LAYERS):
        y = 1.54 + i * (h + gap)          # stack moved up: user edit
        top = i == 0
        d.rect(s, d.LEFT, y, d.CONTENT_W, h, fill=d.NAVY if top else d.WHITE,
               line=None if top else d.BORDER)
        d.rect(s, d.LEFT, y, 0.06, h, fill=accent)
        d.text(s, name, d.LEFT + 0.25, y + 0.07, 2.1, 0.32, font=d.HEADLINE, size=17,
               color=d.WHITE if top else d.NAVY)
        d.label(s, alias, d.LEFT + 0.25, y + 0.4, w=2.0, color=d.MINT if top else d.TEAL, size=7.5)
        d.text(s, does, 2.85, y, 4.35, h, size=10.5, color=d.SOFT_ON_DARK if top else d.MUTED,
               anchor=d.MSO_ANCHOR.MIDDLE)
        d.chip(s, adds, 7.35, y + 0.17, 1.95, h=0.28, size=8.5, font=d.BODY,
               fill=d.NAVY_LIGHT if top else d.MINT_TINT, color=d.MINT if top else d.NAVY)

    d.takeaway(s, "The model is the same next-token predictor as before. Everything built around it "
                  "makes it an agent.", y=4.61)                      # position: user edit
    return s


if __name__ == "__main__":
    d.run(build)
