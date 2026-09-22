"""Slide "Hallucination": a chat where the model confidently invents a study, plus why and what helps.

Placed right after the context window slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-hallucination"
ANCHOR = "slide-context-window"


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Hallucination", "Hallucination: fluent, confident and wrong",
        "An LLM writes likely-sounding text, not checked facts. When it doesn't know, it may make things up.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: chat mock-up -----------------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, 5.3, 3.0, accent=None)
    d.label(s, "Example (invented for illustration)", 0.85, 2.08, w=4.5, color=d.MUTED)

    d.rect(s, 2.55, 2.4, 3.15, 0.55, fill=d.NAVY_LIGHT, rounded=True)
    d.text(s, "Summarize the 2019 Hartmann & Lindqvist study on remote work.",
           2.72, 2.46, 2.85, 0.45, size=10.5, color=d.WHITE, anchor=d.MSO_ANCHOR.MIDDLE)

    d.rect(s, 0.85, 3.1, 3.9, 1.05, fill=d.TEAL_TINT, rounded=True)
    d.text(s, "Hartmann & Lindqvist (2019) surveyed 2,400 employees and found that productivity "
              "rose by 13% when working from home …", 1.02, 3.18, 3.6, 0.9, size=10.5,
           color=d.NAVY, anchor=d.MSO_ANCHOR.MIDDLE)

    d.chip(s, "This study does not exist", 2.9, 4.3, 2.55, h=0.34, fill=d.NAVY, color=d.MINT,
           size=10)
    d.text(s, "Names, numbers, sources:\nall made up.", 0.85, 4.28, 1.95, 0.5, size=10,
           color=d.MUTED)

    # --- Right: why + what helps ------------------------------------------------------------------
    x, w = 6.15, 3.37
    d.card(s, x, 1.95, w, 1.42)
    d.label(s, "Why it happens", x + 0.25, 2.08)
    d.text(s, "The model always writes the most likely next token. It has no built-in fact check, "
              "and plausible is not the same as true.", x + 0.25, 2.35, w - 0.4, 0.95, size=11,
           color=d.TEXT_DARK)

    d.card(s, x, 3.53, w, 1.42, accent=d.MINT)
    d.label(s, "What helps", x + 0.25, 3.66)
    d.text(s, "• Give it the source documents (RAG, later in this talk)\n"
              "• Ask for sources, then check them\n"
              "• Treat every answer as a first draft", x + 0.25, 3.93, w - 0.4, 0.95, size=11,
           color=d.TEXT_DARK)

    d.takeaway(s, "You stay responsible for the facts, especially names, numbers and sources.",
               y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
