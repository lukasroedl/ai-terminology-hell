"""Slide "How an agent actually uses a tool": one request walked through the four steps of a tool
call (tool list, tool call, the app (runtime) runs the tool, the model decides what's next), with the loop
back that makes it an agent.

The key message: the model only writes text (a tool call is text in a fixed format, still next-token
prediction); the app it runs in executes the tool. Placed after the tool use slide; re-running
replaces the slide.
"""
import design as d

MARKER = "slide-tool-calling"
ANCHOR = "slide-tool-use"

REQUEST = "Turn these notes into follow-ups."          # same task as on the chatbot-vs-agent slide
AVATAR_USER = "assets/avatar-user.svg"

# (label, who does it + what, explanation)
STEPS = [
    ("Tool list", "The app (runtime) lists tools",
     "Name, description and required parameters {in braces}."),
    ("Tool call", "The model writes a tool call",
     "Fills in the parameters: still next-token prediction."),
    ("Run the tool", "The app (runtime) runs the tool",
     "It opens the file and hands the result back to the model."),
    ("Next step", "The model decides what’s next",
     "Another tool call, or the final answer to you."),
]


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "Part 5 · Tool use, step by step", "How an agent actually uses a tool",
        "The model (LLM) cannot press any buttons. Instead, it writes the tool call as text in a "
        "fixed format, through the usual next-token prediction, and the app (runtime) reads the "
        "tool call and acts on it.", index=d.index_after(prs, ANCHOR), marker=MARKER,
        subtitle_size=12.5)

    d.card(s, d.LEFT, 2.06, d.CONTENT_W, 2.87, accent=d.TEAL)
    d.label(s, "Your request", 0.85, 2.22, w=1.5, color=d.MUTED, size=8)
    d.chip(s, REQUEST, 2.1, 2.16, 2.75, h=0.3, size=9.5, fill=d.MINT_TINT, color=d.NAVY, font=d.BODY)
    d.svg_picture(s, AVATAR_USER, 4.92, 2.15, 0.3, 0.3)

    bw, gap, by, bh = 1.93, 0.24, 2.58, 1.8
    xs = [0.85 + i * (bw + gap) for i in range(4)]
    for i, (lab, title, caption) in enumerate(STEPS):
        x = xs[i]
        d.step_box(s, x, by, bw, bh)
        d.step_label(s, i + 1, lab, x + 0.1, by + 0.1, w=bw - 0.15)
        d.text(s, title, x + 0.1, by + 0.32, bw - 0.2, 0.36, font=d.HEADLINE, size=11, color=d.NAVY)
        d.text(s, caption, x + 0.1, by + 1.37, bw - 0.2, 0.46, size=8.5, color=d.MUTED)
        if i < 3:
            d.line(s, x + bw + 0.04, by + 0.95, x + bw + gap - 0.04, by + 0.95, color=d.TEAL,
                   arrow=True)

    # Step 1: two tools, each with its description and the parameters it needs.
    x = xs[0] + 0.1
    for j, (name, params, desc) in enumerate((("read_file", "{file, folder}", "opens a file"),
                                              ("draft_email", "{to, text}", "writes a draft"))):
        y = by + 0.68 + j * 0.33
        d.rect(s, x, y, bw - 0.2, 0.3, fill=d.WHITE, line=d.BORDER, radius=0.05)
        d.rich_text(s, [(name + " ", d.TEAL), (params, d.NAVY)], x + 0.06, y + 0.04, bw - 0.3,
                    0.12, font=d.MONO, size=6.5)
        d.text(s, desc, x + 0.06, y + 0.16, bw - 0.3, 0.12, size=6.5, color=d.MUTED)

    # Step 2: the tool call: the same tool, its parameters filled in.
    x = xs[1] + 0.1
    d.rect(s, x, by + 0.68, bw - 0.2, 0.63, fill=d.WHITE, line=d.TEAL, radius=0.05)
    for j, parts in enumerate(([("read_file {", d.TEAL)],
                               [("  file: ", d.MUTED), ("meeting-notes.docx", d.NAVY)],
                               [("  folder: ", d.MUTED), ("Meetings", d.NAVY)],
                               [("}", d.TEAL)])):
        d.rich_text(s, parts, x + 0.08, by + 0.73 + j * 0.135, bw - 0.3, 0.13, font=d.MONO, size=7)

    # Step 3: the counterpart of step 2: the opened file, and the result that goes back.
    x = xs[2] + 0.1
    d.rect(s, x + 0.04, by + 0.74, 0.36, 0.46, fill=d.WHITE, line=d.BORDER)       # the file
    for k, lw in enumerate((0.22, 0.24, 0.16)):
        d.rect(s, x + 0.1, by + 0.84 + k * 0.1, lw, 0.035, fill=d.TEAL)
    d.text(s, "meeting-notes", x - 0.08, by + 1.21, 0.6, 0.1, size=5.5, color=d.MUTED,
           align=d.PP_ALIGN.CENTER)
    d.line(s, x + 0.44, by + 0.97, x + 0.54, by + 0.97, color=d.TEAL, arrow=True)
    rx = x + 0.58
    d.rect(s, rx, by + 0.68, bw - 0.2 - 0.58, 0.63, fill=d.WHITE, line=d.MINT, radius=0.05)
    for j, (value, color) in enumerate((("result", d.MINT), ("1. Send slides", d.NAVY),
                                        ("2. Schedule follow-up", d.NAVY), ("3. …", d.NAVY))):
        d.text(s, value, rx + 0.06, by + 0.73 + j * 0.135, 1.08, 0.13, font=d.MONO,
               size=6.5 if j == 0 else 6, color=color, wrap=False)

    # Step 4: two possible next moves, spread over the same height as the boxes in steps 2 and 3.
    x = xs[3] + 0.1
    d.chip(s, "draft_email …", x, by + 0.68, bw - 0.2, h=0.22, size=7, fill=d.WHITE, color=d.TEAL,
           line=d.TEAL)
    d.text(s, "or", x, by + 0.935, bw - 0.2, 0.12, size=7, color=d.MUTED, align=d.PP_ALIGN.CENTER)
    d.chip(s, "“Please review the email draft.”",  # user edit
           x, by + 1.09, bw - 0.2, h=0.22, size=7.5,
           font=d.BODY, fill=d.MINT_TINT, color=d.NAVY)

    # The loop: from step 4 back to step 2.
    ly = by + bh + 0.18
    d.line(s, xs[3] + bw / 2, by + bh, xs[3] + bw / 2, ly, color=d.ICON_TEAL, dashed=True)
    d.line(s, xs[3] + bw / 2, ly, xs[1] + bw / 2, ly, color=d.ICON_TEAL, dashed=True)
    d.line(s, xs[1] + bw / 2, ly, xs[1] + bw / 2, by + bh + 0.02, color=d.ICON_TEAL, dashed=True,
           arrow=True)
    mid = (xs[1] + xs[3] + bw) / 2
    d.rect(s, mid - 1.25, ly - 0.1, 2.5, 0.2, fill=d.WHITE)
    d.text(s, "↻  repeats until done: the agent loop", mid - 1.2, ly - 0.08, 2.4, 0.16,
           font=d.MONO, size=7.5, color=d.ICON_TEAL, spacing=50, align=d.PP_ALIGN.CENTER)

    d.takeaway(s, "Because the app (runtime) runs every tool, it can check permissions and ask you before "
                  "anything is sent.")
    return s


if __name__ == "__main__":
    d.run(build)
