"""Slide "MCP: one common plug for every tool": before/after picture of the integration problem
(every app wired to every system vs. everyone plugging into one standard).

Replaces the original hand-made MCP slide ("An integration problem, not a model one") in plain
language. Placed after the tool call slide; re-running replaces the slide.
"""
import design as d

MARKER = "slide-mcp"
ANCHOR = "slide-tool-calling"
OLD_SLIDE = "An integration problem, not a model one"

APPS = ["AI app 1", "AI app 2", "AI app 3"]
SYSTEMS = ["Outlook", "SharePoint", "Database", "HR system"]


def nodes(s, x, w):
    """Draw the apps (left) and systems (right) of one card; return their connection points."""
    app_pts, sys_pts = [], []
    for i, app in enumerate(APPS):
        y = 2.7 + i * 0.4
        d.chip(s, app, x + 0.25, y, 0.95, h=0.28, size=8.5, fill=d.NAVY, color=d.WHITE)
        app_pts.append((x + 1.22, y + 0.14))
    for i, system in enumerate(SYSTEMS):
        y = 2.5 + i * 0.4
        d.chip(s, system, x + w - 1.25, y, 1.0, h=0.28, size=8.5, fill=d.WHITE, color=d.NAVY,
               font=d.BODY, line=d.BORDER)
        sys_pts.append((x + w - 1.27, y + 0.14))
    return app_pts, sys_pts


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(
        prs, "2024 · MCP", "MCP: one common plug for every tool",
        "MCP (Model Context Protocol): an open standard for connecting AI apps to tools and data.",
        index=d.index_after(prs, ANCHOR), marker=MARKER)

    w, top, h = 4.38, 1.95, 2.5
    lx, rx = d.LEFT, d.LEFT + w + 0.14
    for x, accent, title, caption in (
            (lx, d.NAVY, "Before: a custom connection for every pair",
             "3 apps × 4 systems = 12 connections, each built and maintained on its own."),
            (rx, d.MINT, "With MCP: everyone plugs into one standard",
             "Each app and each system connects once: 3 + 4 = 7.")):
        d.card(s, x, top, w, h, accent=accent)
        d.text(s, title, x + 0.23, top + 0.12, w - 0.4, 0.3, font=d.HEADLINE, size=14, color=d.NAVY)
        d.text(s, caption, x + 0.23, top + h - 0.36, w - 0.4, 0.25, size=9.5, color=d.MUTED)

    # Before: every app wired to every system.
    app_pts, sys_pts = nodes(s, lx, w)
    for ax, ay in app_pts:
        for sx, sy in sys_pts:
            d.line(s, ax, ay, sx, sy, color=d.MUTED, width=0.75)

    # After: every app and every system wired once to the MCP standard in the middle.
    app_pts, sys_pts = nodes(s, rx, w)
    hub_x, hub_y, hub_w, hub_h = rx + 1.72, 2.92, 0.7, 0.42
    for ax, ay in app_pts:
        d.line(s, ax, ay, hub_x - 0.02, hub_y + hub_h / 2, color=d.TEAL, width=1.25)
    for sx, sy in sys_pts:
        d.line(s, hub_x + hub_w + 0.02, hub_y + hub_h / 2, sx, sy, color=d.TEAL, width=1.25)
    d.chip(s, "MCP", hub_x, hub_y, hub_w, h=hub_h, size=14, font=d.HEADLINE, fill=d.MINT,
           color=d.NAVY)

    # Analogy and adoption.
    d.card(s, d.LEFT, 4.55, d.CONTENT_W, 0.38, accent=None)
    d.rich_text(s, [("Like USB-C: ", d.NAVY), ("one plug shape, so any device fits any charger.   ",
                                                d.TEXT_DARK),
                    ("Published by Anthropic in Nov 2024, adopted by OpenAI, Google and Microsoft "
                     "in 2025.", d.MUTED)], 0.85, 4.65, 8.5, 0.2, size=9.5)

    d.takeaway(s, "MCP doesn’t make the model smarter. It makes connecting it to your systems much "
                  "easier.")
    return s


if __name__ == "__main__":
    d.run(build)
