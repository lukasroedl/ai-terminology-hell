"""Sub-divider inside the Generative AI part: the block of terms you meet when working with LLMs.

Lighter than the five part dividers (light background instead of navy), because it opens a group
inside a part rather than a new part. Placed after the Transformer slide, before the tokens slide.
Re-running replaces the slide.
"""
import design as d

MARKER = "slide-llm-terms-divider"
ANCHOR = "slide-pretraining"   # after the mechanics block, before the practical terms

TERMS = ["Vocabulary & embeddings", "Prompt", "Context window", "Hallucination"]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.new_slide(prs, background=d.LIGHT_BG, index=d.index_after(prs, ANCHOR))
    d.rect(s, 0, 0, 0.22, 5.625, fill=d.NAVY)
    d.circle(s, 7.1, 2.6, 3.6, color=d.TEAL, alpha=10)          # signature circles, corner only
    d.circle(s, 8.6, 1.75, 2.3, color=d.MINT, alpha=8)

    d.kicker(s, "Part 4 · Generative AI", 0.9, 1.5, w=4.0, color=d.TEAL)
    title = d.text(s, "Terms you meet when\nworking with LLMs", 0.9, 1.85, 5.4, 1.5,
                   font=d.HEADLINE, size=40, color=d.NAVY)
    title.name = MARKER
    d.accent_bar(s, 0.9, 3.5)

    x, y = 0.9, 3.78
    for term in TERMS:
        w = 0.34 + 0.085 * len(term)
        d.chip(s, term, x, y, w, h=0.36, fill=d.WHITE, color=d.NAVY, size=10, font=d.BODY,
               line=d.BORDER)
        x += w + 0.12
    d.text(s, "The next few slides explain each of them in plain language.", 0.9, 4.4, 6.0, 0.25,
           size=11, color=d.MUTED)
    return s


if __name__ == "__main__":
    d.run(build)
