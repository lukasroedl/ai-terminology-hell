"""Correct the milestone years on the "Five nested ideas" slide (edits the existing slide in place).

ML 1997 -> 1959: Arthur Samuel's self-learning checkers program, which named "machine learning".
Deep Learning 2017 -> 2012: AlexNet, the image-recognition breakthrough (2017 is the Transformer).
AI stays 1955 (term coined in the Dartmouth proposal). Safe to re-run.
"""
import design as d

ANCHOR = "Five nested ideas, seventy years"
YEARS = {"1997": "1959", "2017": "2012"}


def build(prs):
    slide = prs.slides[d.index_after(prs, ANCHOR) - 1]
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.text.strip() in YEARS:
                        r.text = YEARS[r.text.strip()]
    return slide


if __name__ == "__main__":
    d.run(build)
