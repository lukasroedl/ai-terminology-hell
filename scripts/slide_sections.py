"""Section divider slides: an AI orientation divider, then one divider for each of the five parts
(Rule-based AI, Machine Learning, Deep Learning, Generative AI, Agentic AI).

Each divider: navy background like the title slide; left: part number, name, one-line definition and
what the part covers (the AI divider only orients: no part number, no content list); right: a family tree AI -> (Rule-based AI | ML) -> Deep Learning -> (GenAI |
Agentic AI) with the current node in mint and its line of ancestors highlighted. Dashed "•••" stubs
hint that AI and ML have more children than shown. Re-running replaces all dividers.
"""
import design as d

# (key, kicker, headline, definition, covers, anchor = slide the divider is inserted after).
# covers=None marks the orientation-only divider.
SECTIONS = [
    ("ai", "The big picture · since 1955", "Artificial\nIntelligence",
     "The big umbrella: machines doing tasks that normally need human intelligence.",
     None,
     "Five nested ideas, seventy years"),
    ("rulebased", "Part 1 of 5 · since the 1950s", "Rule-based AI",  # one line: user edit 2026-09-22
     "People write down their knowledge as rules, and the computer follows them.",
     "Early AI: humans write the rules",
     "section-ai"),
    ("ml", "Part 2 of 5 · since 1959", "Machine\nLearning",
     "Instead of following hand-written rules, the computer learns from examples.",
     "The computer finds the rules itself · Why learning pulled ahead",
     "slide-explicit-programming"),
    ("dl", "Part 3 of 5 · since 2012", "Deep\nLearning",
     "Machine learning with many-layered neural networks that spot complex patterns.",
     "Neural networks",
     "slide-ml-outperforms"),
    ("genai", "Part 4 of 5 · since 2018", "Generative\nAI",
     "AI that creates new content: text, images, audio and code.",
     "LLMs · Transformer & GPT · Tokens · Next-word prediction · Pre-training · Prompt · "
     "Context window · Hallucination",
     "slide-neural-network"),
    ("agentic", "Part 5 of 5 · since 2024", "Agentic\nAI",
     "AI that doesn't just answer, but plans, uses tools and acts toward a goal.",
     "Chatbot vs. agent · What an agent is made of · RAG · Tool use · MCP",
     "slide-hallucination"),
]

# Family tree: key -> (label, year, center x, top y, parent key).
NODE_W, NODE_H = 1.75, 0.6
TREE = {
    "ai":       ("Artificial Intelligence", "1955", 6.9, 0.75, None),
    "rulebased": ("Rule-based AI",          "1950s", 5.85, 1.9, "ai"),
    "ml":       ("Machine Learning",        "1959", 7.95, 1.9, "ai"),
    "dl":       ("Deep Learning",           "2012", 7.2, 3.05, "ml"),
    "genai":    ("Generative AI",           "2018", 6.25, 4.2, "dl"),
    "agentic":  ("Agentic AI",              "2024", 8.15, 4.2, "dl"),
}


def marker(key):
    return f"section-{key}"


# "More children" stubs: (parent key, x of the unnamed branch). Dashed, dim, ending in dots.
STUBS = [("ai", 9.3), ("ml", 9.3)]  # both on the right side


def lineage(key):
    """The node and all its ancestors."""
    path = []
    while key:
        path.append(key)
        key = TREE[key][4]
    return path


def family_tree(s, current):
    path = lineage(current)
    # Faint signature circle behind the tree.
    d.circle(s, 5.0, 0.35, 5.0, color=d.TEAL, alpha=6, line_width=0.5)

    # Elbow connectors parent -> child; on the highlighted path they are teal and thicker.
    for key, (_, _, x, y, parent) in TREE.items():
        if parent is None:
            continue
        px, py = TREE[parent][2], TREE[parent][3] + NODE_H
        mid = (py + y) / 2
        on_path = key in path
        color, width = (d.TEAL, 2.0) if on_path else (d.DIM_ON_DARK, 0.75)
        d.line(s, px, py, px, mid, color=color, width=width)
        d.line(s, px, mid, x, mid, color=color, width=width)
        d.line(s, x, mid, x, y, color=color, width=width)

    for parent, sx in STUBS:
        px, py = TREE[parent][2], TREE[parent][3] + NODE_H
        child_top = min(node[3] for node in TREE.values() if node[4] == parent)
        mid = (py + child_top) / 2
        d.line(s, px, mid, sx, mid, color=d.DIM_ON_DARK, width=0.75, dashed=True)
        d.line(s, sx, mid, sx, child_top + 0.08, color=d.DIM_ON_DARK, width=0.75, dashed=True)
        for i in (-1, 0, 1):
            d.circle(s, sx + i * 0.14 - 0.035, child_top + 0.2, 0.07, color=d.DIM_ON_DARK, alpha=100,
                     line_width=0.5)

    for key, (label, year, x, y, _) in TREE.items():
        if key == current:
            fill, line, name_color, year_color = d.MINT, d.MINT, d.NAVY, d.NAVY
        elif key in path:
            fill, line, name_color, year_color = d.NAVY_LIGHT, d.TEAL, d.WHITE, d.TEAL
        else:
            fill, line, name_color, year_color = d.NAVY, d.DIM_ON_DARK, d.DIM_ON_DARK, d.DIM_ON_DARK
        d.rect(s, x - NODE_W / 2, y, NODE_W, NODE_H, fill=fill, line=line, rounded=True,
               line_width=1.5 if key in path else 0.75)
        d.text(s, label, x - NODE_W / 2, y + 0.07, NODE_W, 0.3, font=d.HEADLINE, size=13,
               color=name_color, align=d.PP_ALIGN.CENTER)
        d.text(s, year, x - NODE_W / 2, y + 0.36, NODE_W, 0.2, font=d.MONO, size=8.5,
               color=year_color, align=d.PP_ALIGN.CENTER, spacing=100)


def build_section(prs, key, kicker, headline, definition, covers, anchor):
    d.replace_slide(prs, marker(key))
    s = d.new_slide(prs, background=d.NAVY, index=d.index_after(prs, anchor))
    family_tree(s, key)

    d.kicker(s, kicker, 0.8, 1.05, w=4.0)
    title = d.text(s, headline, 0.8, 1.35, 4.0, 1.7 if "\n" in headline else 0.81, font=d.HEADLINE,
                   size=48)
    title.name = marker(key)
    d.text(s, definition, 0.8, 3.1, 3.9, 0.55, size=14, color=d.SOFT_ON_DARK)
    d.accent_bar(s, 0.8, 3.85)
    if covers is None:  # orientation divider
        d.label(s, "The family tree", 0.8, 4.02, w=3.0, color=d.DIM_ON_DARK, size=9)
        d.text(s, "Each part of this talk is one branch of AI. The highlighted box shows where we are.",
               0.8, 4.27, 3.9, 0.7, size=11, color=d.SOFT_ON_DARK)
        return s
    d.label(s, "In this part", 0.8, 4.02, w=3.0, color=d.DIM_ON_DARK, size=9)
    # Non-breaking spaces inside each item, so lines only break between items.
    covers = " · ".join(item.replace(" ", "\u00a0").replace("-", "\u2011") for item in covers.split(" · "))
    d.text(s, covers, 0.8, 4.27, 3.9, 0.7, size=11, color=d.SOFT_ON_DARK)
    return s


def build(prs):
    for section in SECTIONS:
        s = build_section(prs, *section)
    return s


if __name__ == "__main__":
    d.run(build)
