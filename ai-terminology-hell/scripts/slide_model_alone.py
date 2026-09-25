"""Slide "A model alone can only talk": the four gaps of a bare LLM, each tagged with the later step
that solves it (RAG, tool use), so the rest of Part 5 reads as the story of closing them.

Replaces the original hand-made slide ("Weights are lossy" …) in plain language. Placed after the
bridge question; re-running replaces the slide.
"""
import design as d

MARKER = "slide-model-alone"
ANCHOR = "slide-bridge-question"
OLD_SLIDE = "Weights are lossy"

# (title, explanation, solved by)
GAPS = [
    ("Its facts are approximate",
     "Facts are compressed into the weights, not stored word for word. It cannot look them up "
     "or say where they came from.", "RAG"),
    ("Its knowledge stops at a date",
     "It knows nothing that happened after its training. Updating it means training it again.",
     "RAG"),
    ("It has never seen proprietary data",
     "Internal documents, policies and systems were not part of its training text.",
     "RAG · Tool use"),
    ("It cannot act",
     "Writing text never sends an email, books a room or updates a database.", "Tool use"),
]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · The starting point", "A model alone can only talk",
        "Its knowledge is learned in training and frozen in the model’s weights. All it produces "
        "is text.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    w, h, gap = 4.38, 1.4, 0.14
    for i, (title, body, fix) in enumerate(GAPS):
        x = d.LEFT + (i % 2) * (w + gap)
        y = 1.95 + (i // 2) * (h + gap)
        d.card(s, x, y, w, h, accent=d.TEAL)
        d.text(s, title, x + 0.23, y + 0.14, w - 0.4, 0.3, font=d.HEADLINE, size=15, color=d.NAVY)
        d.text(s, body, x + 0.23, y + 0.5, w - 0.45, 0.45, size=10.5, color=d.MUTED)
        d.label(s, "Solved by", x + 0.23, y + h - 0.35, w=0.9, color=d.MUTED, size=8)
        d.chip(s, fix, x + 1.1, y + h - 0.4, 0.3 + 0.085 * len(fix), h=0.26, size=9,
               fill=d.MINT_TINT, color=d.NAVY)

    d.takeaway(s, "The next steps in the story fill these gaps, mostly by building around the model, "
                  "not by changing it.")
    return s


if __name__ == "__main__":
    d.run(build)
