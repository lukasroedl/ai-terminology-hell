"""Sources slide "Continue the conversation": three internal Merck resources, each a card with a
linked title, a description and the full (linked) URL.

The URLs are intranet (evarooms) links: keep them exactly as they are. Replaces the original
hand-made slide; placed after the closing quote; re-running replaces the slide.
"""
import design as d

MARKER = "slide-sources"
ANCHOR = "slide-closing-quote"
OLD_SLIDE = "Continue the conversation"

SOURCES = [
    ("AI Glossary for LE Teams · Q4 2024",
     "Legal & Compliance knowledge base · terminology and definitions",
     "https://evarooms.merckgroup.com/Organization/Legal-Compliance/PublishingImages/"
     "le-knowledge-base/le-expert-groups/digital-data-economy/AI%20Glossary%20for%20LE%20Teams"
     "%20Q4%2024.pdf"),
    ("AI Microlesson Series",
     "MGF Data · learning and development · practical AI concepts",
     "https://evarooms.merckgroup.com/Topic/MGF-Data/learning-development/ai-microlesson-series"),
    ("Merck Data and AI – Learning Hub",
     "Merck Data · learning resource",
     "https://evarooms.merckgroup.com/Topic/MerckData/learn"),
]


def build(prs):
    d.delete_slides_with_text(prs, OLD_SLIDE)
    d.replace_slide(prs, MARKER)
    s = d.content_slide(prs, "Sources", "Continue the conversation",
                        "Internal resources to go deeper into the terms from this talk.",
                        index=d.index_after(prs, ANCHOR), marker=MARKER)

    h, gap = 0.86, 0.14
    for i, (title, desc, url) in enumerate(SOURCES):
        y = 2.0 + i * (h + gap)
        d.card(s, d.LEFT, y, d.CONTENT_W, h, accent=d.TEAL)
        d.link(d.text(s, title, d.LEFT + 0.25, y + 0.14, 4.4, 0.3, font=d.HEADLINE, size=16,
                      color=d.NAVY), url)
        d.text(s, desc, d.LEFT + 0.25, y + 0.5, 4.4, 0.25, size=10, color=d.MUTED)
        d.link(d.text(s, url, 5.3, y + 0.14, 4.0, h - 0.24, font=d.MONO, size=7, color=d.TEAL,
                      anchor=d.MSO_ANCHOR.MIDDLE), url)
    return s


if __name__ == "__main__":
    d.run(build)
