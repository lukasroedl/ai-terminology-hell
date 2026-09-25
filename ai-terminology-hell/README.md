# ai-terminology-hell

The slide deck "A Short History of AI: From Generative AI to Agentic AI, Welcome to terminology hell"
(`ai-terminology-hell.pptx`). It explains the most important AI terms to a non-technical audience by telling the
story of how AI evolved.

Each slide is built by its own script in `scripts/` (design system in `scripts/design.py`). From this folder:

```bash
../.venv/bin/python scripts/check_drift.py scripts/slide_<name>.py   # hand edits in PowerPoint?
../.venv/bin/python scripts/slide_<name>.py                          # rebuild one slide
scripts/render.sh                                                    # export PNGs to .render/
```
