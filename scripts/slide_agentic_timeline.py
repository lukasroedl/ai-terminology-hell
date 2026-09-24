"""Slide "From RAG to MCP": the four steps from a talking model to a working agent as one milestone
band (in the style of the Transformer slide), each step tagged with the missing piece it fills
(the chips of the bridge question).

Replaces the original hand-made chronology ("Evolution of Agentic"). Placed after the "model alone"
slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-agentic-timeline"
ANCHOR = "slide-model-alone"
OLD_SLIDE = "Evolution of Agentic"

# (years, name, spelled out / other names, what it does, milestone, missing piece it fills, accent)
STEPS = [
    ("2020", "RAG", "Retrieval-Augmented Generation",
     "The model looks things up in documents before it answers.",
     "2020: a paper by Facebook AI (today Meta) names the method.",
     "Knowledge it never learned", d.TEAL),
    ("2021–2023", "Tool use", "also: tool calling, function calling",
     "The model decides to use a tool, e.g. search, calendar or email.",
     "2023: OpenAI adds function calling to its developer platform.",
     "Hands to act with", d.TEAL),
    ("2023–2024", "Agents", "Agentic AI",
     "The model works in a loop: plan, use tools, check, repeat.",
     "2023: first experiments like AutoGPT. 2024: “agentic AI” takes off.",
     "A loop kept in check", d.TEAL),
    ("Nov 2024", "MCP", "Model Context Protocol",
     "One standard way to plug any tool into any AI app.",
     "Published by Anthropic, adopted by OpenAI, Google and Microsoft in 2025.",
     "One common plug", d.MINT),
]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · 2020–2024", "From RAG to MCP: four steps to an agent",
        "Each step filled one gap. Together they turn a model that talks into an agent that "
        "works.", index=d.index_after(prs, ANCHOR), marker=MARKER)

    gap = 0.14
    w = (d.CONTENT_W - 3 * gap) / 4
    top, h = 1.95, 2.92
    for i, (years, name, spelled, does, milestone, piece, accent) in enumerate(STEPS):
        x = d.LEFT + i * (w + gap)
        d.card(s, x, top, w, h, accent=accent)
        d.label(s, years, x + 0.23, top + 0.15, w=w - 0.3, color=accent)
        d.text(s, name, x + 0.23, top + 0.55, w - 0.35, 0.4, font=d.HEADLINE, size=22, color=d.NAVY)
        d.text(s, spelled, x + 0.23, top + 0.97, w - 0.35, 0.2, size=8.5, color=d.MUTED)
        d.text(s, does, x + 0.23, top + 1.24, w - 0.4, 0.6, size=10, color=d.TEXT_DARK)
        d.text(s, milestone, x + 0.23, top + 1.88, w - 0.4, 0.45, size=8.5, color=d.MUTED)
        d.label(s, "Fills", x + 0.23, top + 2.33, w=1.0, color=d.MUTED, size=7.5)
        d.chip(s, piece, x + 0.23, top + 2.52, w - 0.42, h=0.26, size=8.5, fill=d.MINT_TINT,
               color=d.NAVY, font=d.BODY)

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
