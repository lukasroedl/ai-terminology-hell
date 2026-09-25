"""Slide "Hallucination": a chat where the model confidently invents a study, plus why and what helps.

Placed right after the context window slide. Re-running replaces it.
"""
import design as d

MARKER = "slide-hallucination"
ANCHOR = "slide-context-window"

# A request, the invented answer, and the check that exposes it. Invented for illustration.
REQUEST = "Which internal guideline covers data retention in clinical trials?"
ANSWER = ["Guideline SOP-4711 “Clinical Data Retention”,", "version 3.2 from March 2021, section 5.4:",
          "records are kept for 15 years after study end."]
CHECK = ("No SOP-4711 in the document system. No version 3.2, no section 5.4. "
         "The 15 years are invented too")
AVATAR_USER = "assets/avatar-user.svg"      # stock icons the user placed on the slide
AVATAR_AI = "assets/avatar-ai.svg"


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Working with LLMs · Hallucination", "Hallucination: fluent, confident and wrong",
        "An LLM writes likely-sounding text, not checked facts. When it doesn't know, it may make things up.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Left: a chat app window (layout fine-tuned by the user in PowerPoint) ---------------------
    card = d.rect(s, d.LEFT, 1.94, 5.73, 3.0, fill=d.WHITE, line=d.BORDER)

    wx, ww, wy, wh = 0.75, 5.49, 2.05, 2.15                # the chat window
    window = d.rect(s, wx, wy, ww, wh, fill=d.WHITE, radius=0.12)
    title_bar = d.rect(s, wx, wy, ww, 0.37, fill=d.LIGHT_BG, radius=0.12)
    d.circle(s, 0.89, 2.13, 0.24, color=d.TEAL, alpha=100, line_width=0.5)
    d.text(s, "AI", 0.89, 2.17, 0.24, 0.17, font=d.MONO, size=10, color=d.WHITE,
           align=d.PP_ALIGN.CENTER)
    title = d.text(s, "AI assistant", 1.21, 2.15, 2.0, 0.22, font=d.HEADLINE, size=11,
                   color=d.NAVY)
    # The window sits behind the slide furniture, as the user arranged it.
    d.send_to_back(s, card, window, title_bar, title)
    for i in range(3):                                             # window dots
        d.circle(s, 5.69 + i * 0.14, 2.21, 0.07, color=d.DIM_ON_DARK, alpha=100, line_width=0.5)

    # User message: the bubble and both avatars are added at the very end (user's arrangement)
    d.text(s, "09:41", 4.88, 3.12, 0.70, 0.16, font=d.MONO, size=7, color=d.MUTED,
           align=d.PP_ALIGN.RIGHT)

    # Assistant message
    d.rect(s, 1.26, 3.25, 3.90, 0.72, fill=d.TEAL_TINT, radius=0.14)
    for i, line in enumerate(ANSWER):
        d.text(s, line, 1.42, 3.31 + i * 0.21, 3.60, 0.20, size=9, color=d.NAVY)
    d.text(s, "09:42", 1.36, 4.01, 0.70, 0.12, font=d.MONO, size=7, color=d.MUTED)

    # The reality check sits under the conversation
    d.line(s, 2.61, 3.99, 2.61, 4.31, color=d.MINT, width=1, arrow=True)
    d.rect(s, 1.26, 4.32, 3.90, 0.55, fill=d.NAVY, radius=0.1)
    d.text(s, "REALITY CHECK", 1.37, 4.38, 1.60, 0.16, font=d.MONO, size=7.5, color=d.MINT,
           spacing=100)
    d.text(s, CHECK, 1.37, 4.54, 3.73, 0.29, size=8.5, color=d.SOFT_ON_DARK)

    # --- Right: why + what helps ------------------------------------------------------------------
    x, w = 6.50, 3.14
    d.card(s, x, 1.95, w, 1.42)
    d.label(s, "Why it happens", x + 0.25, 2.08)
    d.text(s, "The model always writes the most likely next token. It has no built-in fact check, "
              "and plausible is not the same as true.", x + 0.25, 2.35, 2.77, 0.56, size=11,
           color=d.TEXT_DARK)

    d.card(s, x, 3.53, w, 1.42, accent=d.MINT)
    d.label(s, "What helps", x + 0.25, 3.66)
    d.text(s, "• Give it the source documents (RAG, later in this talk)\n"
              "• Ask for sources, then check them\n"
              "• Treat every answer as a first draft", x + 0.25, 3.93, 2.63, 0.74, size=11,
           color=d.TEXT_DARK)

    d.takeaway(s, "You stay responsible for the facts, especially names, numbers and sources.",
               y=5.1)

    d.chip(s, REQUEST, 1.72, 2.60, 3.95, h=0.48, size=10, fill=d.MINT_TINT, color=d.NAVY,
           font=d.BODY)
    d.svg_picture(s, AVATAR_USER, 5.73, 2.61, 0.46, 0.46)
    d.svg_picture(s, AVATAR_AI, 0.78, 3.38, 0.46, 0.46)
    return s


if __name__ == "__main__":
    d.run(build)
