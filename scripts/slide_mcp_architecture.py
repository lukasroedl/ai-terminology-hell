"""Slide "Inside MCP: host, client and server": the three MCP roles as a diagram (the AI app holds
one client per server, each server opens up one system; one server runs in the cloud, one on your
computer), then one plain-language card per role: what the client does, and what a server offers
and where it can run.

Replaces the original hand-made architecture slide ("One host, many capabilities"), which used
off-system fonts. Placed after the MCP slide; re-running replaces the slide.
"""
import design as d
from pptx.util import Emu

MARKER = "slide-mcp-architecture"
ANCHOR = "slide-mcp"
OLD_SLIDE = "One host, many capabilities"
TAG_W, TAG_H = 2023607, 100027          # size of the Outlook server tag (EMU): user edit

# (server, system behind it, where the server runs)
SERVERS = [("Outlook", "Mailbox & calendar", "runs on your computer or in the cloud"),  # user edit
           ("Files", "Files on your laptop", "runs on your computer")]
OFFERS = [("Tools", "actions"), ("Resources", "data to read"), ("Prompts", "ready-made instructions")]
CLIENT_TASKS = ["connects to its server", "asks what the server offers",
                "forwards tool calls and results", "keeps the line running"]
RUNS = [("On your computer", "a small local program"), ("In the cloud", "a service, e.g. run by IT")]


def bullets(s, parts_list, x, y, w, step=0.17):
    """Short list lines (one rich_text line each) inside a role card."""
    for i, parts in enumerate(parts_list):
        d.rich_text(s, parts, x, y + i * step, w, 0.16, size=8.5)


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(prs, "MCP · How it works", "Inside MCP: host, client and server",
                        index=d.index_after(prs, ANCHOR), marker=MARKER)

    # --- Diagram ---------------------------------------------------------------------------------
    d.card(s, d.LEFT, 1.5, d.CONTENT_W, 1.62, accent=None)
    col = {"host": 0.85, "server": 4.95, "system": 7.55}
    for key, text in (("host", "Host"), ("server", "MCP servers"), ("system", "Your systems")):
        d.label(s, text, col[key], 1.6, w=2.0, color=d.MUTED, size=8)

    # Host: the AI app, holding the model and one client per server.
    d.rect(s, 0.85, 1.85, 3.25, 1.12, fill=d.LIGHT_BG, line=d.TEAL, radius=0.08)
    d.text(s, "The AI app", 0.97, 1.91, 1.5, 0.22, font=d.HEADLINE, size=11, color=d.NAVY)
    d.chip(s, "LLM", 1.0, 2.35, 0.62, h=0.3, size=9, fill=d.NAVY, color=d.WHITE)
    for i, (name, system, where) in enumerate(SERVERS):
        y = 2.05 + i * 0.52
        d.line(s, 1.64, 2.5, 2.58, y + 0.14, color=d.BORDER, width=1)
        d.chip(s, f"MCP Client {i + 1}", 2.6, y,  # "MCP": user edit
                1.3, h=0.28, size=8.5, fill=d.TEAL_TINT, color=d.NAVY)
        d.line(s, 3.92, y + 0.14, col["server"] - 0.02, y + 0.14, color=d.TEAL, width=1.25)
        d.text(s, "MCP", 4.2, y - 0.08, 0.5, 0.14, font=d.MONO, size=7, color=d.TEAL,
               align=d.PP_ALIGN.CENTER)
        tag = d.label(s, where, col["server"], y - 0.17, w=2.05, color=d.TEAL, size=6.5)
        if i == 0:                                   # longer tag, box resized by the user
            tag.width, tag.height = Emu(TAG_W), Emu(TAG_H)
        d.chip(s, f"MCP server: {name}", col["server"], y, 2.05, h=0.28, size=8.5, font=d.BODY,
               fill=d.WHITE, color=d.NAVY, line=d.TEAL)
        d.line(s, col["server"] + 2.07, y + 0.14, col["system"] - 0.02, y + 0.14, color=d.BORDER,
               width=1)
        d.chip(s, system, col["system"], y, 1.7, h=0.28, size=8.5, font=d.BODY, fill=d.LIGHT_BG,
               color=d.NAVY, line=d.BORDER)

    # --- One card per role -----------------------------------------------------------------------
    gap = 0.14
    w = (d.CONTENT_W - 2 * gap) / 3
    top, h = 3.22, 1.74
    roles = [
        ("Host", "The AI app you work with, e.g. a chat assistant or an agent. It holds the model, "
                 "asks you for permission and hands each tool call to the right client.", d.NAVY),
        ("Client", "The go-between, one per server. It:", d.TEAL),
        ("Server", "Opens up one system to AI and offers:", d.MINT),
    ]
    xs = [d.LEFT + i * (w + gap) for i in range(3)]
    for x, (name, body, accent) in zip(xs, roles):
        d.card(s, x, top, w, h, accent=accent)
        d.text(s, name, x + 0.23, top + 0.1, w - 0.4, 0.28, font=d.HEADLINE, size=14, color=d.NAVY)
        d.text(s, body, x + 0.23, top + 0.42, w - 0.4, 0.75, size=9.5, color=d.MUTED)

    bullets(s, [[("·  " + task, d.TEXT_DARK)] for task in CLIENT_TASKS],
            xs[1] + 0.23, top + 0.64, w - 0.4)
    d.text(s, "It decides nothing and runs no tool itself.", xs[1] + 0.23, top + 1.36, w - 0.4, 0.2,
           size=8.5, color=d.MUTED)

    bullets(s, [[(offer, d.TEAL), (f"  {meaning}", d.TEXT_DARK)] for offer, meaning in OFFERS],
            xs[2] + 0.23, top + 0.64, w - 0.4)
    d.label(s, "Runs either", xs[2] + 0.23, top + 1.16, w=1.5, color=d.MUTED, size=7.5)
    bullets(s, [[(where, d.TEAL), (f"  {what}", d.TEXT_DARK)] for where, what in RUNS],
            xs[2] + 0.23, top + 1.32, w - 0.4, step=0.16)

    d.takeaway(s, "Build an MCP server for a system once, and every MCP-compatible AI app can use it.")
    return s


if __name__ == "__main__":
    d.run(build)
