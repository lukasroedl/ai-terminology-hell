"""Statement slide after the machine-learning slide: only the statement that learning took the lead.

Light background with the signature circles in the corner. Re-running replaces the slide.
"""
import design as d

MARKER = "slide-ml-outperforms"
ANCHOR = "slide-machine-learning"
STATEMENT = ("Both streams ran side by side. Learning took the lead from the 1990s, as data and "
             "computing power grew.")


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.new_slide(prs, background=d.LIGHT_BG, index=d.index_after(prs, ANCHOR))
    d.rect(s, 0, 0, 0.22, 5.625, fill=d.NAVY)                        # side bar, as on content slides
    d.circle(s, 6.9, 2.75, 3.8, color=d.TEAL, alpha=12)               # signature circles, corner only
    d.circle(s, 8.5, 1.9, 2.4, color=d.MINT, alpha=10)

    d.accent_bar(s, 0.9, 1.75)
    statement = d.text(s, STATEMENT, 0.9, 1.95, 6.6, 2.0, font=d.HEADLINE, size=36, color=d.NAVY)
    statement.name = MARKER
    return s


if __name__ == "__main__":
    d.run(build)
