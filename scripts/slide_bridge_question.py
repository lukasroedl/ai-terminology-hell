"""Bridge slide: the question that opens the second half — how does next-token prediction become an
agent that operates applications?

Light statement slide, in the style of the other dividers. Replaces the original hand-made bridge
slide. Placed after the agent anatomy slide; re-running replaces it.
"""
import design as d

MARKER = "slide-bridge-question"
ANCHOR = "slide-agent-anatomy"
OLD_SLIDE = "get hands and eyes"

QUESTION = ("Wait — how do we get from\npredicting the next token to an\n"
            "agent that operates Outlook?")          # user edit 2026-09-24
PIECES = ["Knowledge it never learned", "Hands to act with", "One common plug", "A loop kept in check"]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.new_slide(prs, background=d.LIGHT_BG, index=d.index_after(prs, ANCHOR))
    d.rect(s, 0, 0, 0.22, 5.625, fill=d.NAVY)
    d.circle(s, 7.1, 2.6, 3.6, color=d.TEAL, alpha=10)          # signature circles, corner only
    d.circle(s, 8.6, 1.75, 2.3, color=d.MINT, alpha=8)

    d.kicker(s, "Part 5 · The question", 0.9, 1.25, w=4.0, color=d.TEAL)
    title = d.text(s, QUESTION, 0.9, 1.6, 6.2, 1.72,  # height: user edit
                   font=d.HEADLINE, size=34, color=d.NAVY)
    title.name = MARKER
    d.accent_bar(s, 0.9, 3.85)

    d.text(s, "Four pieces are still missing:", 0.9, 4.05, 3.0, 0.22, size=11, color=d.MUTED)
    x = 0.9
    for piece in PIECES:
        w = 0.34 + 0.075 * len(piece)
        d.chip(s, piece, x, 4.34, w, h=0.34, fill=d.WHITE, color=d.NAVY, size=10, font=d.BODY,
               line=d.BORDER)
        x += w + 0.12
    return s


if __name__ == "__main__":
    import sys
    deck = sys.argv[1] if len(sys.argv) > 1 else "ai-terminology-hell.pptx"
    prs = __import__("pptx").Presentation(deck)
    for slide in list(prs.slides):          # drop the original hand-made slide once
        if any(sh.has_text_frame and OLD_SLIDE in sh.text_frame.text for sh in slide.shapes):
            d.delete_slide(prs, slide)
    build(prs)
    prs.save(deck)
    print("Bridge question slide rebuilt")
