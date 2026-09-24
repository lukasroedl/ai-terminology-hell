"""Slide "RAG: look it up before answering": the three RAG steps (search, add to prompt, answer) as a
left-to-right flow with a toy example, then why it helps and where it stops.

Replaces the original hand-made RAG slide ("The first admission") in plain language. Placed after
the timeline; re-running replaces the slide.
"""
import design as d

MARKER = "slide-rag"
ANCHOR = "slide-agentic-timeline"
OLD_SLIDE = "The first admission"

QUESTION = "What does our travel policy say about train travel?"


def doc_icon(s, x, y, highlight=False):
    """Tiny document: white page with three text lines; the best match is outlined in mint."""
    d.rect(s, x, y, 0.36, 0.46, fill=d.MINT_TINT if highlight else d.WHITE,
           line=d.MINT if highlight else d.BORDER, line_width=1.25 if highlight else 0.75)
    for i, lw in enumerate((0.22, 0.24, 0.16)):
        d.rect(s, x + 0.06, y + 0.1 + i * 0.1, lw, 0.035, fill=d.TEAL if highlight else d.BORDER)


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "2020 · RAG", "RAG: look it up before answering",
        "RAG (Retrieval-Augmented Generation): search the documents first, then answer from them.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- The flow: question, then three steps ----------------------------------------------------
    d.card(s, d.LEFT, 1.95, d.CONTENT_W, 2.05, accent=d.TEAL)
    d.label(s, "Your question", 0.85, 2.1, w=1.5, color=d.MUTED, size=8)
    d.chip(s, QUESTION, 2.1, 2.05, 3.6, h=0.3, size=9.5, fill=d.MINT_TINT, color=d.NAVY, font=d.BODY)

    bw, bh, by, gap = 2.52, 1.4, 2.48, 0.44
    xs = [0.85 + i * (bw + gap) for i in range(3)]
    for i, (title, caption) in enumerate((
            ("Search", "Finds the passages that match best in your documents."),
            ("Add to prompt", "Puts these passages into the prompt, next to your question."),
            ("Answer", "The LLM answers from the passages and names its source."))):
        x = xs[i]
        d.step_box(s, x, by, bw, bh)
        d.step_label(s, i + 1, title, x + 0.12, by + 0.1, w=bw - 0.2)
        d.text(s, caption, x + 0.12, by + 0.98, bw - 0.24, 0.38, size=9, color=d.TEXT_DARK)
        if i < 2:
            d.line(s, x + bw + 0.06, by + bh / 2, x + bw + gap - 0.06, by + bh / 2, color=d.TEAL,
                   arrow=True)

    # Step 1: a shelf of documents, the best match highlighted.
    for j in range(5):
        doc_icon(s, xs[0] + 0.14 + j * 0.46, by + 0.4, highlight=(j == 1))
    # Step 2: the prompt holds the question plus the found passage.
    px = xs[1] + 0.12
    d.rect(s, px, by + 0.36, bw - 0.24, 0.56, fill=d.WHITE, line=d.BORDER, radius=0.06)
    d.chip(s, "Your question", px + 0.08, by + 0.42, 1.0, h=0.2, size=7.5, fill=d.MINT_TINT,
           color=d.NAVY, font=d.BODY)
    d.chip(s, "Passage from the travel policy", px + 0.08, by + 0.66, 1.9, h=0.2, size=7.5,
           fill=d.TEAL_TINT, color=d.NAVY, font=d.BODY)
    # Step 3: LLM -> answer with source.
    ax = xs[2] + 0.12
    d.chip(s, "LLM", ax, by + 0.5, 0.5, h=0.3, size=9, fill=d.NAVY, color=d.WHITE)
    d.line(s, ax + 0.54, by + 0.65, ax + 0.78, by + 0.65, color=d.TEAL, arrow=True)
    d.rect(s, ax + 0.82, by + 0.4, 1.46, 0.5, fill=d.TEAL_TINT, radius=0.06)
    d.text(s, "Answer …", ax + 0.9, by + 0.45, 1.3, 0.18, size=8.5, color=d.NAVY)
    d.text(s, "Source: Travel policy, p. 3", ax + 0.9, by + 0.66, 1.34, 0.18, size=7.5,
           color=d.TEAL)

    # --- Why it helps / where it stops -----------------------------------------------------------
    w = 4.38
    for x, accent, title, body in (
            (d.LEFT, d.MINT, "Why it helps",
             "It stays up to date. It knows your company’s documents. It shows sources you can "
             "check. That means fewer hallucinations."),
            (d.LEFT + w + 0.14, d.NAVY, "Where it stops",
             "It can only read, not act. And the search always runs first, as a fixed step: "
             "the model does not decide when to look something up.")):
        d.card(s, x, 4.1, w, 0.82, accent=accent)
        d.text(s, title, x + 0.23, 4.17, 1.4, 0.25, font=d.HEADLINE, size=13, color=d.NAVY)
        d.text(s, body, x + 1.45, 4.19, w - 1.6, 0.68, size=9.5, color=d.MUTED)

    d.takeaway(s, "Like an open-book exam: instead of answering from memory, the model looks it up "
                  "first.")
    # Footnote: what "search your documents" means in practice.
    d.text(s, "Note: RAG usually doesn’t search the files directly, but a vector database that "
              "stores each passage as an embedding and finds it by meaning.",
           d.LEFT, 5.36, d.CONTENT_W, 0.16, size=8, color=d.MUTED)
    return s


if __name__ == "__main__":
    d.run(build)
