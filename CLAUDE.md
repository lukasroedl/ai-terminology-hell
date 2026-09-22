# CLAUDE.md

## Project purpose

AI moves fast, and the abbreviations and concepts around it (AI, ML, LLM, GenAI, RAG, MCP, agents, …) leave
non-technical people, and many technical ones, feeling overwhelmed. This repo exists to make the most important
terms and concepts understandable.

- **Now:** the slide deck `ai-terminology-hell.pptx` ("A Short History of AI: From Generative AI to Agentic AI,
  Welcome to terminology hell").
- **Later:** the whole repo grows into a broader explainer resource. Possible additions include a glossary,
  handouts and extra decks. Keep the content reusable beyond the deck.

## Audience

A **corporate audience with no IT background** (context: Merck KGaA, Darmstadt, Germany · myGPT Suite).

- Assume no prior knowledge. No math, no code and no unexplained jargon.
- Explain in plain language. Prefer everyday analogies over technical precision, but never say anything that is
  wrong.
- Keep text short. The audience should understand a slide from its visual, with the text only supporting it.
- Tell people why a concept matters to them, not just what it is.

## Storytelling principle

The deck tells **the story of how AI evolved**. Each concept and abbreviation is introduced **at the point in the
story where it appeared**, so the terms are learned alongside the history and not as a separate glossary.

Current arc (18 slides):
1. Title
2. Five nested ideas: AI → ML → Deep Learning → GenAI → Agentic AI (1955–2024)
3. Rules vs. learning from data (AI vs. ML)
4. Neural networks / deep learning
5. Recognizing vs. creating (GenAI, LLM)
6. Next-word prediction
7. Chatbot vs. agent
8. What an agent is made of (model + instructions + tools + runtime)
9. Bridge slide: from foundations to mechanics
10. Why a model alone is not enough
11. Timeline: RAG → tool use → agents → MCP
12. RAG
13. Tool use (and which name to use for it)
14. MCP: the integration problem
15. The four-layer stack
16. MCP architecture (host / client / server)
17. The hard part: constraining the loop
18. Sources

Rules for content:
- **Spell out every abbreviation the first time it appears** (e.g. "LLM (Large Language Model)"), then use the short form.
- One core idea per slide.
- When two terms are often confused, say explicitly how they relate (e.g. "Deep learning is a method within ML,
  not a synonym for all AI"). This is the heart of "terminology hell".
- Dates and facts must be accurate and defensible. If a year marks a specific milestone and not the origin of a
  term, say which milestone (e.g. "2017: Transformer paper").

## Visual design system

The **title slide (slide 1) defines the design**. Every slide must follow it.

### Colors
| Role | Hex | Use |
|---|---|---|
| Navy (dark background / primary text) | `#0D1B2A` | Title & section slides background; main text on light slides |
| Navy, lighter | `#14293D` | Alternate dark background (bridge/section slides), dark panels |
| Teal (primary accent) | `#1B9AAA` | Key shapes, lines, highlights |
| Mint (secondary accent) | `#06D6A0` | Kicker labels, accent bars, emphasis |
| Light background | `#F4F7F8` | Content slide background |
| Light grey (borders, dividers) | `#DDE5E9` | Card borders, separators |
| Muted text | `#6B7B8C` | Captions, footers, secondary text |
| Soft text on dark | `#AFC2CE` | Subtitles on navy backgrounds |
| White | `#FFFFFF` | Headlines on dark, card fills on light |

Don't introduce new accent colors. If more categories are needed, use tints of teal/mint/navy.

### Typography
| Role | Font | Notes |
|---|---|---|
| Headlines | **Oswald** | e.g. 44 pt on the title slide |
| Body text | **Roboto** | e.g. 16 pt subtitle |
| Kicker labels / meta / code-like tokens | **JetBrains Mono** | small (10–11 pt), UPPERCASE, wide letter spacing, usually mint |

Slide pattern: mint mono kicker (e.g. `FOUNDATIONS · 1955–2024`) → Oswald headline → Roboto body. The title slide
also uses a short mint accent bar and a muted mono footer.

### Circles as a signature element
Slide 1 uses large, overlapping circles in the top-right corner, partially bleeding off the slide:
- Circle 1: teal `#1B9AAA` fill at **18% opacity**, thin (0.75 pt) solid teal outline.
- Circle 2: mint `#06D6A0` fill at **12% opacity**, thin mint outline, smaller and overlapping the first.

Reuse this motif on other slides **where there is enough space**, e.g. section/bridge slides, sparse slides,
corners of content slides. It must never compete with or overlap the content. Circles can also be meaningful,
e.g. nested circles for "AI ⊃ ML ⊃ DL".

### Visual explanations first
Use **as many visual explanation aids as possible**. The simplified neural network on slide 4 (input nodes → hidden
layers → output, connected by lines) is the reference example. Every concept should have a picture where possible:
- Diagrams built from native PowerPoint shapes (ellipses, lines, arrows, rectangles) in the palette. Don't use
  stock images or clip art.
- Flows (left → right), nested sets, timelines, before/after comparisons, simple toy examples (e.g. the next-word
  probability bars on slide 6).
- Diagrams must be simplified and labelled in plain language. They illustrate the idea and are not an exact
  technical reproduction.

### Format
- 16:9, slide size 9144000 × 5143500 EMU (10 × 5.625 in).
- Title and section/bridge slides: navy background. Content slides: `#F4F7F8` light background.

## Known issues in the current deck (fix when touching those slides)
- Slides **3, 4, 5, 6, 16** use off-system fonts (Arial, Bahnschrift Condensed, Consolas, Courier New). Change
  them to Oswald / Roboto / JetBrains Mono. Some also lack the explicit slide background.
- Slide 4: headline is split as "N eural  Networks", and the hard-coded page number in the bottom right says "06" (wrong for slide 4).
- Slide 11: headline "Evolution of Agentic" looks truncated.
- Slide 2: years are debatable (ML 1997, but the term dates to 1959; Deep Learning 2017, but the usual
  breakthrough is 2012 (AlexNet), and 2017 is the Transformer). Clarify or correct them.
- Slides 12–17 are written for a technical audience ("parametric memory", "top-k", "M×N connectors", "LSP",
  "control layer"). Rewrite them for non-IT readers.
- Slide 17 contains a note about Claude's knowledge cutoff. This is an authoring note and must not appear on a slide.

## Working with the deck
- The `.pptx` is the source of truth. Edit it programmatically (python-pptx in `.venv`, or direct OOXML edits);
  `python-pptx` 1.0.2 is installed in `.venv`; run scripts with `.venv/bin/python`.
- **Always check your edits visually:** run `scripts/render.sh` (optionally with a deck path) and then look at
  `.render/slide-NN.png`. It exports a PDF with the installed Microsoft PowerPoint through AppleScript, then
  converts it to PNGs with PyMuPDF from `.venv`. Check for text overflow, overlaps, off-slide elements and circles
  colliding with content.
- Don't install tools globally (no Homebrew / LibreOffice / poppler). Python dependencies go into `.venv` only.
  PowerPoint's direct "save as PNG" silently produces nothing, and files inside PowerPoint's sandbox container
  can't be read, so always export into the project folder.
- Keep a backup / commit before big structural edits. The `.pptx` is binary, so git diffs are not readable.
- The sources slide links to internal Merck intranet (evarooms) pages. Don't remove or alter those URLs without
  asking.
