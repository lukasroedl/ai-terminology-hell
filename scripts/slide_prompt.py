"""Slide "Prompt": anatomy of a good prompt flowing into the LLM and out as an answer.

Placed right after the next-word prediction slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-prompt"
ANCHOR = "slide-pretraining"

# (part, chip fill, chip text color, example text)
PARTS = [
    ("Role",    d.TEAL,      d.WHITE, "You are an experienced science writer."),
    ("Task",    d.NAVY,      d.WHITE, "Summarize the attached study report"),
    ("Context", d.MINT,      d.NAVY,  "for colleagues without a medical background"),
    ("Format",  d.TEAL_TINT, d.NAVY,  "in five short bullet points."),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Prompt", "The prompt: everything you give the model",
        "Your input: a question or instruction plus any context. Better input means better output.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: anatomy of a prompt ----------------------------------------------------------------
    d.card(s, d.LEFT, 1.95, 5.45, 3.0)
    d.label(s, "Anatomy of a good prompt", 0.85, 2.08)
    for i, (part, fill, color, example) in enumerate(PARTS):
        y = 2.45 + i * 0.6
        d.chip(s, part.upper(), 0.85, y, 1.05, h=0.36, fill=fill, color=color, size=10)
        d.text(s, example, 2.1, y + 0.06, 3.85, 0.3, size=12.5, color=d.NAVY)

    # --- Right: prompt -> LLM -> answer --------------------------------------------------------
    cx, cy, r = 7.95, 2.6, 0.58
    d.line(s, 6.15, cy, cx - r - 0.05, cy, color=d.TEAL, width=1.75, arrow=True)
    d.circle(s, cx - r, cy - r, 2 * r, color=d.TEAL, alpha=18)
    d.text(s, "LLM", cx - r, cy - 0.22, 2 * r, 0.45, font=d.HEADLINE, size=20, color=d.NAVY,
           align=d.PP_ALIGN.CENTER)
    d.line(s, cx, cy + r + 0.03, cx, 3.55, color=d.TEAL, width=1.75, arrow=True)

    d.rect(s, 6.4, 3.6, 3.12, 1.35, fill=d.NAVY)
    d.label(s, "Answer", 6.62, 3.73, color=d.MINT)
    d.text(s, "Five plain-language bullet points, written for exactly this audience.",
           6.62, 4.0, 2.75, 0.8, size=11.5, color=d.SOFT_ON_DARK)

    d.takeaway(s, "Same model, different prompt, different answer.", y=5.1)
    return s


if __name__ == "__main__":
    d.run(build)
