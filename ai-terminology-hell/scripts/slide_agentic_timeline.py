"""Slide "From RAG to MCP": the four steps from a talking model to a working agent as one milestone
band (in the style of the Transformer slide), each step tagged with the problems it solves (for
RAG and tool use: the gaps of the "model alone" slide).

Replaces the original hand-made chronology ("Evolution of Agentic"). Placed after the "model alone"
slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-agentic-timeline"
ANCHOR = "slide-model-alone"
OLD_SLIDE = "Evolution of Agentic"

# (years, name, spelled out / other names, what it does, problems it solves, accent). The problems
# of RAG and tool use are the gaps named on the "model alone" slide.
STEPS = [
    ("2020", "RAG", "Retrieval-Augmented Generation",
     "The model looks things up in documents before it answers.",
     ["Its facts are approximate", "Its knowledge stops at a date",
      "It has never seen proprietary data"], d.TEAL),
    ("2021–2023", "Tool use", "also: tool calling, function calling",
     "The model decides to use a tool, e.g. search, calendar or email.",
     ["It cannot act"], d.TEAL),
    ("2023–2024", "Agents", "Agentic AI",
     "The model works in a loop: plan, use tools, check, repeat.",
     ["It cannot do multi-step tasks"], d.TEAL),
    ("Nov 2024", "MCP", "Model Context Protocol",
     "One standard way to plug any tool into any AI app.",
     ["Every tool needs its own connection"], d.MINT),
]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · 2020–2024", "From RAG to MCP: four steps to an agent",
        "Each step solved a problem. Together they turn a model that talks into an agent that "
        "works.", index=d.index_after(prs, ANCHOR), marker=MARKER)

    gap = 0.14
    w = (d.CONTENT_W - 3 * gap) / 4
    top, h = 1.95, 2.92
    for i, (years, name, spelled, does, solves, accent) in enumerate(STEPS):
        x = d.LEFT + i * (w + gap)
        d.card(s, x, top, w, h, accent=accent)
        d.label(s, years, x + 0.23, top + 0.15, w=w - 0.3, color=accent)
        d.text(s, name, x + 0.23, top + 0.55, w - 0.35, 0.4, font=d.HEADLINE, size=22, color=d.NAVY)
        d.text(s, spelled, x + 0.23, top + 0.97, w - 0.35, 0.2, size=8.5, color=d.MUTED)
        d.text(s, does, x + 0.23, top + 1.24, w - 0.4, 0.6, size=10, color=d.TEXT_DARK)
        d.label(s, "Solves", x + 0.23, top + 1.86, w=1.0, color=d.MUTED, size=7.5)
        for j, problem in enumerate(solves):
            d.chip(s, problem, x + 0.18, top + 2.05 + j * 0.29, w - 0.32, h=0.25, size=7.5,
                   fill=d.MINT_TINT, color=d.NAVY, font=d.BODY)

    # One timeline across all cards, drawn last so it runs over the gaps and accent bars.
    band_y = top + 0.45
    d.line(s, d.LEFT + 0.23, band_y, d.LEFT + d.CONTENT_W - 0.23, band_y, color=d.BORDER,
           width=1.5, arrow=True)
    for i, step in enumerate(STEPS):
        x = d.LEFT + i * (w + gap)
        d.circle(s, x + 0.23, band_y - 0.07, 0.14, color=step[-1], alpha=100)

    d.takeaway(s, "Each step builds on the one before: an agent uses RAG and tools, and MCP "
                  "connects them.")
    return s


if __name__ == "__main__":
    d.run(build)
