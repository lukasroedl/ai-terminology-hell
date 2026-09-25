"""Slide "Passive response, active problem-solving": chatbot exchange vs. agent loop, side by side.

Replaces the original hand-made slide, keeping its content but using the deck's card language.
Placed after the Agentic AI divider; re-running replaces the slide.
"""
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.shapes import MSO_SHAPE

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
RESULTS = ["✓  Draft email written in Outlook", "✓  Schedule follow-up meetings"]
CONFIRMATION = "I have executed all tasks. The draft email is waiting for your approval."
AVATAR_USER = "assets/avatar-user.svg"
AVATAR_AI = "assets/avatar-ai.svg"

# Chat windows (left and right): the user's window from the left card, taller so both sides fit.
WINDOW_X = [0.85, 5.37]
WINDOW_Y, WINDOW_W, WINDOW_H, BAR_H = 2.529, 3.92, 2.03, 0.32


def chat_window(s, x):
    """Chat app window with a title bar (rounded top corners), AI icon and label; outline and corner
    radius as set by the user in PowerPoint."""
    window = d.rect(s, x, WINDOW_Y, WINDOW_W, WINDOW_H, fill=d.WHITE, line=d.NAVY, radius=0.1)
    window.adjustments[0] = 0.06172
    bar = s.shapes.add_shape(MSO_SHAPE.ROUND_2_SAME_RECTANGLE, d.Inches(x), d.Inches(WINDOW_Y),
                             d.Inches(WINDOW_W), d.Inches(BAR_H))
    bar.adjustments[0], bar.adjustments[1] = 0.25934, 0.0
    bar.fill.solid()
    bar.fill.fore_color.rgb = d.LIGHT_BG
    bar.shadow.inherit = False
    for shape in (window, bar):
        shape.line.color.theme_color = MSO_THEME_COLOR.TEXT_1    # near-black outline, 0.75 pt
        shape.line.color.brightness = 0.05
        shape.line.width = d.Pt(0.75)
    d.circle(s, x + 0.1, 2.6, 0.18, color=d.TEAL, alpha=100, line_width=0.5)
    d.text(s, "AI", x + 0.1, 2.63, 0.18, 0.14, font=d.MONO, size=6, color=d.WHITE,
           align=d.PP_ALIGN.CENTER)
    d.text(s, "AI assistant", x + 0.34, 2.61, 1.6, 0.18, font=d.HEADLINE, size=9, color=d.NAVY)
    return window, bar


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
    cards, backs = [], []
    for x, accent, title in ((lx, d.TEAL, "Generative AI chatbot"), (rx, d.MINT, "Agentic AI")):
        d.card(s, x, top, w, height, accent=accent)
        cards.append(s.shapes[-2])                 # the card itself (the last shape is its accent)
        d.text(s, title, x + 0.23, top + 0.1, 3.98, 0.3, font=d.HEADLINE, size=15, color=d.NAVY)

    # --- Two identical chat windows: same app, different behaviour -------------------------------
    for i, x in enumerate(WINDOW_X):
        window, bar = chat_window(s, x)
        backs.extend([cards[i], window, bar])
    d.send_to_back(s, *backs)                    # cards, windows and title bars at the back

    # --- Left: one turn at a time ------------------------------------------------------------------
    avatars = []
    for i, (line, from_user) in enumerate(CHAT):
        y = 3.0 + i * 0.44
        if from_user:
            d.chip(s, line, 1.47, y, 2.85, h=0.32, size=8.5, fill=d.MINT_TINT, color=d.NAVY,
                   font=d.BODY)
            avatars.append((AVATAR_USER, 4.39, y - 0.01))
        else:
            d.chip(s, line, 1.29, y, 2.85, h=0.32, size=8.5, fill=d.TEAL_TINT, color=d.NAVY,
                   font=d.BODY)
            avatars.append((AVATAR_AI, 0.93, y - 0.01))
    d.text(s, "Every step waits for you.", 0.95, 4.3, 2.5, 0.2, size=9, color=d.MUTED)

    # --- Right: one goal, then the agent's own loop ------------------------------------------------
    d.chip(s, GOAL, 6.3, 2.92, 2.44, h=0.27, size=8.5, fill=d.MINT_TINT, color=d.NAVY, font=d.BODY)
    avatars.append((AVATAR_USER, 8.82, 2.88))

    # The loop and its arrows carry the colour of the AI icon.
    lx0, ly0, lw = 5.8, 3.24, 3.4
    d.rect(s, lx0, ly0, lw, 0.6, fill=d.LIGHT_BG, line=d.ICON_TEAL, radius=0.08)
    d.text(s, "↻  the agent repeats on its own", lx0 + 0.06, ly0 + 0.03, 2.6, 0.13, font=d.MONO,
           size=6.5, color=d.ICON_TEAL, spacing=100)
    for i, step in enumerate(LOOP):
        sx = lx0 + 0.06 + i * 1.14
        d.chip(s, step, sx, ly0 + 0.18, 0.96, h=0.21, size=7, fill=d.WHITE, color=d.NAVY,
               font=d.BODY, line=d.BORDER)
        if i < len(LOOP) - 1:
            # Moved behind the next step by the user (the visible arrows are drawn at the end).
            d.line(s, sx + 1.15, ly0 + 0.2945, sx + 1.27, ly0 + 0.2945, color=d.ICON_TEAL, width=1,
                   arrow=True)
    for i, tool in enumerate(TOOLS):             # under "Uses tools"
        d.chip(s, tool, lx0 + 1.0305 + i * 0.445, ly0 + 0.4295, 0.4, h=0.13,  # user edit
                size=5.5 if i < 2 else 7,
               fill=d.TEAL_TINT, color=d.NAVY, font=d.BODY)
    avatars.append((AVATAR_AI, 5.43, 3.4))

    # The executed tasks, shown the way a chat interface lists them: an expanded dropdown.
    dx, dw, dy = lx0, 1.93, 3.9
    d.rect(s, dx, dy, dw, 0.4, fill=d.WHITE, line=d.ICON_TEAL, radius=0.06)
    d.text(s, "▾", dx + 0.04, dy + 0.01, 0.2, 0.16, font=d.BODY, size=8, color=d.ICON_TEAL)
    d.text(s, f"Executed {len(RESULTS)} tasks", dx + 0.22, dy + 0.025, 1.6, 0.12, font=d.MONO,
           size=7, color=d.ICON_TEAL, spacing=100)
    d.line(s, dx, dy + 0.15, dx + dw - 0.01, dy + 0.15, color=d.BORDER, width=0.75)
    for i, result in enumerate(RESULTS):
        d.text(s, result, dx + 0.14, dy + 0.18 + i * 0.11, 1.7, 0.1, size=6, color=d.ICON_TEAL)
    # The agent's closing message, once the tasks are done.
    d.chip(s, CONFIRMATION, lx0, 4.34, lw, h=0.18, size=7, fill=d.TEAL_TINT, color=d.NAVY,
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
    for x in WINDOW_X:                           # window buttons in each title bar: user edit
        for dot_x in (x + 3.432, x + 3.572, x + 3.712):
            d.circle(s, dot_x, 2.679, 0.07, color=d.DIM_ON_DARK, alpha=100, line_width=0.5)
    for arrow_x in (6.82, 7.96):                 # thicker loop arrows: user edit 2026-09-25
        d.line(s, arrow_x, 3.525, arrow_x + 0.18, 3.525, color=d.ICON_TEAL, width=1.75, arrow=True)
    return s


if __name__ == "__main__":
    import sys
    deck = sys.argv[1] if len(sys.argv) > 1 else d.DECK
    prs = __import__("pptx").Presentation(deck)
    for slide in list(prs.slides):          # drop the original hand-made slide once
        if any(sh.has_text_frame and OLD_SLIDE in sh.text_frame.text for sh in slide.shapes):
            d.delete_slide(prs, slide)
    build(prs)
    prs.save(deck)
    print("Chatbot vs agent slide rebuilt")
