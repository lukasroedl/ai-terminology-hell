"""Slide "Prompt": the prompt shown inside a chat input field, flowing left to right into the model
and out as an answer. The parts of a good prompt are marked by background shading inside the field.

Placed after the vocabulary slide. Re-running replaces the slide.
"""
import design as d

MARKER = "slide-prompt"
ANCHOR = "slide-vocabulary"

# (part, shading colour, example line as typed into the chat box)
ANSWER = ["• 2,400 employees surveyed", "• Productivity up 13%", "• Fewer sick days",
          "• Weaker team communication", "• Hybrid work recommended"]

PARTS = [
    ("Role", d.TEAL_TINT, "You are an experienced science writer."),
    ("Task", d.MINT_TINT, "Summarize the attached study report"),
    ("Context", d.TEAL_TINT, "for colleagues without a medical background"),
    ("Format", d.MINT_TINT, "in five short bullet points."),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Prompt", "The prompt: what you give the model",
        "A prompt is the input you provide to the model, mostly a question or instruction plus "
        "some context. A good prompt nudges the generation process of the model in the right "
        "direction. Better input means better output.",
        index=d.index_after(prs, ANCHOR), marker=MARKER, subtitle_size=12.5)

    mid = 3.35                                        # the flow runs horizontally at this height

    # --- The chat input field ---------------------------------------------------------------------
    fx, fw, fy, fh = d.LEFT, 4.5, 2.05, 2.6
    d.rect(s, fx, fy, fw, fh, fill=d.WHITE, line=d.BORDER, radius=0.12)
    d.label(s, "Chat input", fx + 0.22, fy + 0.14, w=2.0)

    y = fy + 0.46
    for part, shade, line in PARTS:
        d.rect(s, fx + 0.22, y, fw - 0.44, 0.32, fill=shade, radius=0.05)   # shaded part
        d.text(s, line, fx + 0.32, y + 0.06, fw - 1.25, 0.22, size=10.5, color=d.NAVY)
        d.text(s, part.upper(), fx + fw - 1.0, y + 0.08, 0.75, 0.18, font=d.MONO, size=7.5,
               color=d.MUTED, align=d.PP_ALIGN.RIGHT)
        y += 0.38

    # Attachment and send button, as in a chat app. The attachment is where the numbers in the
    # answer come from — without it the example would show an invented summary.
    ay = fy + fh - 0.45
    d.rect(s, fx + 0.22, ay, 1.75, 0.26, fill=d.LIGHT_BG, line=d.BORDER, radius=0.05)
    d.rect(s, fx + 0.3, ay + 0.05, 0.12, 0.16, fill=d.WHITE, line=d.MUTED)      # tiny document
    d.rect(s, fx + 0.32, ay + 0.09, 0.08, 0.02, fill=d.MUTED)
    d.rect(s, fx + 0.32, ay + 0.13, 0.08, 0.02, fill=d.MUTED)
    d.text(s, "study-report.pdf", fx + 0.48, ay + 0.04, 1.4, 0.2, size=9, color=d.TEXT_DARK)
    d.chip(s, "↑", fx + fw - 0.55, fy + fh - 0.5, 0.34, h=0.34, fill=d.NAVY, color=d.WHITE,
           size=12)

    # --- Flow: field -> model -> answer -----------------------------------------------------------
    cx, r = 6.05, 0.55
    d.line(s, fx + fw + 0.08, mid, cx - r - 0.08, mid, color=d.TEAL, width=1.75, arrow=True)
    d.circle(s, cx - r, mid - r, 2 * r, color=d.TEAL, alpha=18)
    d.text(s, "LLM", cx - r, mid - 0.2, 2 * r, 0.4, font=d.HEADLINE, size=19, color=d.NAVY,
           align=d.PP_ALIGN.CENTER)
    d.line(s, cx + r + 0.08, mid, 6.95, mid, color=d.TEAL, width=1.75, arrow=True)

    ax, aw = 7.03, d.LEFT + d.CONTENT_W - 7.03
    d.rect(s, ax, 2.3, aw, 2.1, fill=d.NAVY, radius=0.1)
    d.label(s, "Answer", ax + 0.22, 2.45, color=d.MINT)
    for i, line in enumerate(ANSWER):
        d.text(s, line, ax + 0.22, 2.76 + i * 0.28, aw - 0.4, 0.24, size=10,
               color=d.SOFT_ON_DARK)

    d.takeaway(s, "Same model, different prompt, different answer. The chat tool also sends along "
                  "things you never type: a system prompt, the conversation so far and "
                  "attachments — together they fill the context window.", y=5.0, size=11.5, h=0.44)
    return s


if __name__ == "__main__":
    d.run(build)
