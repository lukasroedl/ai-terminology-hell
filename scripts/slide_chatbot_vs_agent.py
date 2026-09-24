"""Slide "Passive response, active problem-solving": chatbot exchange vs. agent loop, side by side.

Replaces the original hand-made slide, keeping its content but using the deck's card language.
Placed after the Agentic AI divider; re-running replaces the slide.
"""
import design as d

MARKER = "slide-chatbot-vs-agent"
ANCHOR = "section-agentic"
OLD_SLIDE = "A structured exchange that needs a human"

# Left: a short chat, in the style of the hallucination slide.
CHAT = [("Summarize these meeting notes.", True), ("Here are the five key points …", False),
        ("Now draft the text for an email from it.", True)]
# Right: the same task, carried through by the agent.
GOAL = "Turn these notes into follow-ups."
LOOP = ["Plans the steps", "Uses tools", "Checks the result"]
TOOLS = ["Outlook", "File Sys.", "…"]
RESULTS = ["✓  Draft email written in Outlook", "✓  Schedule follow-up meetings",
           "✓  Store meeting notes on sharepoint"]
CONFIRMATION = "I have executed all tasks. The draft email is waiting for your approval."
AVATAR_USER = "assets/avatar-user.svg"
AVATAR_AI = "assets/avatar-ai.svg"


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "The shift", "From just answering to actually doing",
        "LLMs generate text and answer queries. AI Agents can set or interpret goals, plan and "
        "sequence actions, use tools (like web browsers, code, or APIs), make decisions based on "
        "feedback and adapt over time to complete tasks.",
        index=d.index_after(prs, ANCHOR), marker=MARKER, subtitle_size=11.5)

    lx, rx, w = d.LEFT, 5.14, 4.38
    top, height = 2.1, 2.85
    for x, accent, title in ((lx, d.TEAL, "Generative AI chatbot"), (rx, d.MINT, "Agentic AI")):
        d.card(s, x, top, w, height, accent=accent)
        d.text(s, title, x + 0.23, top + 0.1, 3.98, 0.3, font=d.HEADLINE, size=15, color=d.NAVY)

    # --- Left: a chat window, one turn at a time --------------------------------------------------
    wx, ww, wy, wh = 0.85, 3.92, 2.52, 1.62
    d.rect(s, wx, wy, ww, wh, fill=d.WHITE, line=d.BORDER, radius=0.1)
    d.rect(s, wx, wy, ww, 0.3, fill=d.LIGHT_BG, radius=0.1)              # title bar
    d.rect(s, wx, wy + 0.2, ww, 0.1, fill=d.LIGHT_BG)
    d.circle(s, 0.95, 2.58, 0.18, color=d.TEAL, alpha=100, line_width=0.5)
    d.text(s, "AI", 0.95, 2.61, 0.18, 0.14, font=d.MONO, size=6, color=d.WHITE,
           align=d.PP_ALIGN.CENTER)
    d.text(s, "AI assistant", 1.19, 2.59, 1.6, 0.18, font=d.HEADLINE, size=9, color=d.NAVY)

    avatars = []
    for i, (line, from_user) in enumerate(CHAT):
        y = 2.94 + i * 0.4
        if from_user:
            d.chip(s, line, 1.47, y, 2.85, h=0.32, size=8.5, fill=d.MINT_TINT, color=d.NAVY,
                   font=d.BODY)
            avatars.append((AVATAR_USER, 4.39, y - 0.01))
        else:
            d.chip(s, line, 1.29, y, 2.85, h=0.32, size=8.5, fill=d.TEAL_TINT, color=d.NAVY,
                   font=d.BODY)
            avatars.append((AVATAR_AI, 0.93, y - 0.01))
    d.text(s, "Every step waits for you.", 0.85, 4.2, 2.5, 0.2, size=9.5, color=d.MUTED)

    # --- Right: one goal, then the agent's own loop (positions fine-tuned by the user) ----------
    d.chip(s, GOAL, 6.55, 2.48, 2.44, h=0.32, size=8.5, fill=d.MINT_TINT, color=d.NAVY,
           font=d.BODY)
    avatars.append((AVATAR_USER, 9.04, 2.47))

    # The loop and its arrows carry the colour of the AI icon.
    d.rect(s, 5.67, 2.86, 3.69, 0.82, fill=d.LIGHT_BG, line=d.ICON_TEAL, radius=0.08)
    d.text(s, "↻  the agent repeats on its own", 5.72, 2.91, 2.6, 0.2, font=d.MONO, size=8,
           color=d.ICON_TEAL, spacing=100)
    for i, step in enumerate(LOOP):
        sx = 5.72 + i * 1.29
        d.chip(s, step, sx, 3.11, 1.01, h=0.3, size=8.5, fill=d.WHITE, color=d.NAVY, font=d.BODY,
               line=d.BORDER)
        if i < len(LOOP) - 1:
            d.line(s, sx + 1.05, 3.26, sx + 1.24, 3.26, color=d.ICON_TEAL, width=1, arrow=True)
    for i, tool in enumerate(TOOLS):
        d.chip(s, tool, 6.89 + i * 0.445, 3.44, 0.4, h=0.2, size=6 if i < 2 else 8.5,
               fill=d.TEAL_TINT, color=d.NAVY, font=d.BODY)

    avatars.append((AVATAR_AI, 5.31, 3.52))
    # The executed tasks, shown the way a chat interface lists them: an expanded dropdown.
    dx, dw, dy = 5.67, 1.93, 3.72
    d.rect(s, dx, dy, dw, 0.6, fill=d.WHITE, line=d.ICON_TEAL, radius=0.06)
    d.text(s, "▾", dx + 0.04, dy + 0.02, 0.2, 0.18, font=d.BODY, size=8, color=d.ICON_TEAL)
    d.text(s, f"Executed {len(RESULTS)} tasks", dx + 0.22, dy + 0.03, 1.6, 0.12, font=d.MONO,
           size=7, color=d.ICON_TEAL, spacing=100)
    d.line(s, dx, dy + 0.15, dx + dw - 0.01, dy + 0.15, color=d.BORDER, width=0.75)
    for i, result in enumerate(RESULTS):
        d.text(s, result, dx + 0.14, dy + 0.18 + i * 0.15, 1.6, 0.1, size=6, color=d.ICON_TEAL)

    # The agent's closing message, once the tasks are done
    d.chip(s, CONFIRMATION, 5.67, 4.36, 3.69, h=0.23, size=7, fill=d.TEAL_TINT, color=d.NAVY,
           font=d.BODY)

    # --- Bottom of each card: what it is, and a typical request -----------------------------------
    for x, desc in (
            (lx, "A structured exchange that needs a human for every decision."),
            (rx, "An autonomous system that pursues a goal on its own.")):
        d.line(s, x + 0.23, 4.68, x + w - 0.23, 4.68, color=d.BORDER, width=0.75)
        d.text(s, desc, x + 0.23, 4.74, 3.93, 0.2, size=9, color=d.TEXT_DARK)

    d.takeaway(s, "The chatbot waits for your next instruction. The agent decides the next step "
                  "itself.", y=5.1)

    for path, ax, ay in avatars:                 # drawn last, like on the hallucination slide
        d.svg_picture(s, path, ax, ay, 0.34, 0.34)
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
    print("Chatbot vs agent slide rebuilt")
