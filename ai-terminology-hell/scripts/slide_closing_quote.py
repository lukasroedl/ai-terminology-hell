"""Closing quote slide: Richard Feynman on knowing the name of something vs. knowing something, which
sums up the idea of the whole talk. Navy statement slide with the signature circles of slide 1.

Source: R. P. Feynman, "What Do You Care What Other People Think?" (1988), chapter "The Making of a
Scientist". Placed after the "hard part" slide, before the sources; re-running replaces the slide.
"""
import design as d

MARKER = "slide-closing-quote"
ANCHOR = "slide-hard-part"

QUOTE = ("I learned very early the difference between knowing the name of something and knowing "
         "something.")


def build(prs):
    d.replace_slide(prs, MARKER)
    s = d.new_slide(prs, background=d.NAVY, index=d.index_after(prs, ANCHOR))

    # Signature circles in the top-right corner, bleeding off the slide as on the title slide.
    d.circle(s, 7.0, -1.3, 3.8, color=d.TEAL, alpha=18)
    d.circle(s, 8.5, 0.6, 2.4, color=d.MINT, alpha=12)

    d.kicker(s, "Before you go", 0.8, 1.2, w=4.0)
    d.text(s, "“", 0.8, 1.64, 0.8, 0.9, font=d.HEADLINE, size=72, color=d.MINT)   # user edit
    title = d.text(s, QUOTE, 1.2, 1.93, 6.6, 1.5, font=d.HEADLINE, size=32)       # user edit
    title.name = MARKER
    d.accent_bar(s, 0.8, 3.8)
    d.text(s, "RICHARD FEYNMAN", 0.8, 3.98, 4.0, 0.3, font=d.MONO, size=12, color=d.MINT,
           spacing=300)
    # Closing mark after the quote (user edit 2026-09-25; the user removed the subtitle line).
    d.text(s, "“", 5.14, 2.83, 0.8, 0.9, font=d.HEADLINE, size=72, color=d.MINT)
    return s


if __name__ == "__main__":
    d.run(build)
