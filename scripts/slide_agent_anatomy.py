"""Slide "What an agent is made of": the four parts as a formula and as cards, plus the definition.

Replaces the original hand-made slide, keeping its content. Placed after the chatbot/agent slide;
re-running replaces the slide.
"""
import design as d

MARKER = "slide-agent-anatomy"
ANCHOR = "slide-chatbot-vs-agent"
OLD_SLIDE = "An AI application consisting of a"

PARTS = [
    ("Model", "Usually an LLM. Core capabilities: observing, understanding, planning, "
               "deciding."),
    ("Instructions", "Define the goals and behaviour that steer actions toward the intended "
                     "outcome."),
    ("Tools", "Extend capability beyond the model: browsing, calling APIs, operating software."),
    ("Runtime", "Manages the execution loop — plan, act, observe, iterate toward the objective."),
]
QUOTE = ("“An AI application consisting of a model equipped with instructions that guide its "
         "behavior, access to tools that extend its capabilities, encapsulated in a runtime with "
         "a dynamic lifecycle.”")


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · Anatomy", "What an agent is made of", QUOTE + "   — OpenAI definition",
        index=d.index_after(prs, ANCHOR), marker=MARKER, subtitle_size=11.5)

    # --- The formula ------------------------------------------------------------------------------
    x = d.LEFT
    d.chip(s, "Agent", x, 1.95, 1.0, h=0.42, size=13, font=d.HEADLINE, fill=d.NAVY, color=d.WHITE)
    x += 1.0
    for i, (part, _) in enumerate(PARTS):
        d.text(s, "=" if i == 0 else "+", x + 0.06, 2.0, 0.3, 0.3, font=d.HEADLINE, size=15,
               color=d.MUTED, align=d.PP_ALIGN.CENTER)
        x += 0.42
        w = 0.42 + 0.1 * len(part)
        d.chip(s, part, x, 1.95, w, h=0.42, size=12, font=d.HEADLINE, fill=d.TEAL_TINT,
               color=d.NAVY)
        x += w

    # --- The four parts as cards ------------------------------------------------------------------
    cw, ch, gap = 4.38, 1.06, 0.18
    for i, (part, desc) in enumerate(PARTS):
        cx = d.LEFT + (i % 2) * (cw + gap)
        cy = 2.66 + (i // 2) * (ch + gap)
        d.card(s, cx, cy, cw, ch, accent=d.MINT if i % 2 else d.TEAL)
        d.text(s, part, cx + 0.23, cy + 0.12, cw - 0.45, 0.3, font=d.HEADLINE, size=15,
               color=d.NAVY)
        d.text(s, desc, cx + 0.23, cy + 0.44, cw - 0.45, 0.4, size=10, color=d.MUTED)

    d.takeaway(s, "A model alone is not an agent: instructions, tools and a runtime make it one.",
               y=5.1)
    return s


if __name__ == "__main__":
    prs = __import__("pptx").Presentation("ai-terminology-hell.pptx")
    for slide in list(prs.slides):          # drop the original hand-made slide once
        if any(sh.has_text_frame and OLD_SLIDE in sh.text_frame.text for sh in slide.shapes):
            d.delete_slide(prs, slide)
    build(prs)
    prs.save("ai-terminology-hell.pptx")
    print("Agent anatomy slide rebuilt")
