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

Current arc (37 slides):
1. Title
2. **Terminology hell**: a deliberately chaotic cloud of every term the deck explains (`scripts/slide_terminology_hell.py`)
3. Five nested ideas: AI → ML → Deep Learning → GenAI → Agentic AI. Years: AI 1955 (term coined), ML 1959 (Samuel), DL 2012 (AlexNet), GenAI 2018, Agentic AI 2024 (`scripts/edit_foundations_dates.py`)
4. *Section divider · Artificial Intelligence (orientation only, no part number, no content)*
5. *Section divider · Part 1: Rule-based AI*
6. **Stream 1, explicit programming / rule-based AI** (also called symbolic AI): IF/ELSE spam flowchart, where rules break, famous examples (`scripts/slide_explicit_programming.py`)
7. *Section divider · Part 2: Machine Learning*
8. **Stream 2, machine learning**: same spam problem, learned from labelled examples; Samuel 1959 (`scripts/slide_machine_learning.py`)
9. **Statement slide**: "Both streams ran side by side. Learning took the lead from the 1990s, as data and computing power grew." Statement only (`scripts/slide_ml_outperforms.py`)
10. *Section divider · Part 3: Deep Learning*
11. **Neural networks**: input/hidden/output layers, one layer and one weight called out, what is learned, tokens in and out (`scripts/slide_neural_network.py`)
12. *Section divider · Part 4: Generative AI*
13. **Generative AI**: recognise (label in) vs. generate (new content), and the branches text/LLM · images · audio · video (`scripts/slide_generative_ai.py`)
14. **Transformer / GPT**: milestone band 2017 Google → 2018 OpenAI, decoder-only attention demo ("it" only looks back), GPT spelled out (`scripts/slide_transformer.py`)
15. **Token**: text → tokens → numbers (`scripts/slide_token.py`)
16. **Next-word prediction**: two generation steps with the same probability picture; the chosen token is boxed and carried into step 2 (`scripts/slide_next_word.py`)
17. **Pre-training**: any text → next-token guessing staircase → learning loop (loss, gradients, adjust weights) (`scripts/slide_pretraining.py`)
18. *Sub-divider · "Terms you meet when working with LLMs": Vocabulary & embeddings · Prompt · Context window · Hallucination (`scripts/slide_llm_terms_divider.py`)*
19. **Vocabulary, token, embedding**: the model's vocabulary table (ID · token · embedding) plus the three definitions (`scripts/slide_vocabulary.py`)
20. **Prompt**: the prompt inside a chat input field (parts marked by shading, attachment chip) → LLM → answer, horizontal flow; takeaway names the hidden parts (system prompt, history, attachments) (`scripts/slide_prompt.py`)
21. **Context window**: conversation strip with the window, how big windows got (`scripts/slide_context_window.py`)
22. **Hallucination**: chat app window (request → invented guideline → reality check), why it happens, what helps (`scripts/slide_hallucination.py`)
23. *Section divider · Part 5: Agentic AI*
24. **Chatbot vs. agent**: turn-by-turn exchange vs. the agent loop, both in cards (`scripts/slide_chatbot_vs_agent.py`)
25. **What an agent is made of**: formula Agent = Model + Instructions + Tools + Runtime, four cards, OpenAI definition (`scripts/slide_agent_anatomy.py`)
26. **Bridge question**: "how do we get from predicting the next token to an agent that works in Outlook?", light statement slide with the four missing pieces (`scripts/slide_bridge_question.py`)
27. **A model alone can only talk**: knowledge learned in training and frozen in the weights; four gaps in cards, each tagged "solved by" RAG / tool use (`scripts/slide_model_alone.py`)
28. **Timeline from RAG to MCP**: milestone band 2020 RAG → 2021–2023 tool use → 2023–2024 agents → Nov 2024 MCP, each tagged with the bridge question's missing piece it fills (`scripts/slide_agentic_timeline.py`)
29. **RAG**: search → add to prompt → answer flow with a toy question, why it helps / where it stops, open-book analogy, footnote on vector databases (`scripts/slide_rag.py`)
30. **Tool use**: RAG's fixed route vs. the model choosing a tool; "tool use / tool calling / function calling" are one idea (`scripts/slide_tool_use.py`)
31. **How an agent uses a tool**: four steps (tool list → tool call → the app runs the tool → next step) with the loop back; the model only writes text, the app executes (`scripts/slide_tool_calling.py`)
32. **MCP**: before (every app wired to every system) vs. after (everyone plugs into MCP), USB-C analogy (`scripts/slide_mcp.py`)
33. **Inside MCP**: host / client / server diagram (Outlook server local or in the cloud, files server on your computer) plus one card per role: what the client does, what a server offers and where it runs (`scripts/slide_mcp_architecture.py`)
34. **How the pieces fit together**: stack named like the parts on slide 25 (runtime = the agent loop · tools = RAG & tool use · MCP · model = the LLM), each mapped to what it adds (`scripts/slide_agent_stack.py`)
35. **The hard part** (navy statement): connecting a tool is easy, keeping the loop in check is not; four guardrails, the signature circle drawn as the agent loop (`scripts/slide_hard_part.py`)
36. **Closing quote** (navy): Richard Feynman, "I learned very early the difference between knowing the name of something and knowing something." (`scripts/slide_closing_quote.py`)
37. **Sources**: three intranet resources, linked titles and URLs (`scripts/slide_sources.py`)

The five parts are Rule-based AI, Machine Learning, Deep Learning, Generative AI and Agentic AI. The AI divider
before them only orients the audience. All dividers (`scripts/slide_sections.py`) show a family tree
AI → (Rule-based AI | Machine Learning) → Deep Learning → (Generative AI | Agentic AI). The current node is
filled mint, and its line of ancestors is highlighted in teal. Unnamed dashed "•••" branches (both on the right)
show that AI and ML have more children than drawn. Each part divider also has an "In this part" list. Update that
list when slides are added to or removed from a part.

Inside Part 4 a lighter **sub-divider** (light background, no family tree) opens the block of term slides
(`scripts/slide_llm_terms_divider.py`). Its chip list must match the slides that follow it.

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
| Dim text on dark | `#8FA6B2` | Secondary/small text on navy (use this, not `#6B7B8C`, when text sits over circles) |
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
Use **as many visual explanation aids as possible**. The neural network on slide 11 (input/hidden/output layers, callouts for one layer and one weight,
tokens in and out) is the reference example. Every concept should have a picture where possible:
- Diagrams built from native PowerPoint shapes (ellipses, lines, arrows, rectangles) in the palette. Don't use
  stock images or clip art.
- Flows (left → right), nested sets, timelines, before/after comparisons, simple toy examples (e.g. the next-word
  probability bars on slide 16).
- **Numbered steps** are labelled "STEP 1: TEXT" (`d.step_label`), never "1 / text". When several steps share one
  card, give each step its own light box (`d.step_box`: light background, thin border, small fixed corner radius).
  Sub-steps inside a step use letters (a, b, c) so they don't clash with the step numbers.
- Diagrams must be simplified and labelled in plain language. They illustrate the idea and are not an exact
  technical reproduction.

### Format
- 16:9, slide size 9144000 × 5143500 EMU (10 × 5.625 in).
- Title and section/bridge slides: navy background. Content slides: `#F4F7F8` light background.

## Where the work stands (2026-09-24)

All 37 slides have been reworked and are built by scripts (except slide 3, which is edited in place).
Part 5 follows the four missing pieces named on the bridge question (knowledge → RAG, hands → tool
use, one common plug → MCP, a loop kept in check → the hard part); keep that thread when editing it.

To rework or add a slide: build it with `d.content_slide(...)` (kicker → headline → one-line
subtitle), cards or a diagram in the deck's colours, and a takeaway line at the bottom. When it
replaces a hand-made slide, delete the original by a distinctive text of its own
(`d.delete_slides_with_text(prs, OLD_SLIDE)`).

## Keeping the deck consistent
- If a term is added to or removed from the deck, update the term cloud on slide 2 (`TERMS` in
  `scripts/slide_terminology_hell.py`). Every term in the cloud must be explained somewhere.

## Working with the deck
- **The user also edits slides by hand in PowerPoint. Never overwrite those edits.** Before re-running any slide
  script, run `.venv/bin/python scripts/check_drift.py scripts/slide_<name>.py`. If it reports drift, port the
  manual edits into the script first, rerun the check until it reports "No drift", and only then rebuild.
  Hand-tuned values in scripts are marked with a "user edit" comment; keep them unless asked to change them.
  The check compares position, size, text, font sizes and colours — it cannot see everything, so read the
  rendered slide as well before rebuilding one the user has touched.
- While the deck is open in PowerPoint (a `~$ai-terminology-hell.pptx` lock file exists), script edits and a
  later save in PowerPoint overwrite each other. Ask the user to save and close the deck before scripts write to it.
- The `.pptx` is the source of truth. Edit it programmatically (python-pptx in `.venv`, or direct OOXML edits);
  `python-pptx` 1.0.2 is installed in `.venv`; run scripts with `.venv/bin/python`.
- To preview changes while the deck is open in PowerPoint, build into a temporary copy in `.preview/` (ignored by
  git) and run `scripts/render.sh .preview/deck.pptx`. Write to the real deck only after the user has closed it,
  then delete `.preview/`.
- **Always check your edits visually:** run `scripts/render.sh` (optionally with a deck path) and then look at
  `.render/slide-NN.png`. It exports a PDF with the installed Microsoft PowerPoint through AppleScript, then
  converts it to PNGs with PyMuPDF from `.venv`. Check for text overflow, overlaps, off-slide elements and circles
  colliding with content.
- Don't install tools globally (no Homebrew / LibreOffice / poppler). Python dependencies go into `.venv` only.
  PowerPoint's direct "save as PNG" silently produces nothing, and files inside PowerPoint's sandbox container
  can't be read, so always export into the project folder.
  PowerPoint sometimes exports a stale copy of a file that just changed; `render.sh` then fails with a
  slide-count warning. Simply run it again.
- Keep a backup / commit before big structural edits. The `.pptx` is binary, so git diffs are not readable.
- The sources slide links to internal Merck intranet (evarooms) pages. Don't remove or alter those URLs without
  asking.
- Images the user inserts (e.g. PowerPoint stock icons, which are SVGs) are extracted to `assets/` and
  re-inserted by the slide script with `d.svg_picture(...)`, so a rebuild keeps them.
- `check_drift.py` matches shapes by content, so a changed z-order is reported as one line instead of a
  long diff. Reproduce the user's drawing order with `d.send_to_back(...)` or by creating shapes later.
- **Slides are built by scripts:** `scripts/design.py` holds the design system (colors, fonts, `new_slide`,
  `kicker`, `text`, `accent_bar`, `circle`), and each new or rebuilt slide has its own
  `scripts/slide_<name>.py`. A slide script replaces its previous version when re-run (it finds the slide by a
  marker shape name), so you can run it repeatedly. Run with `.venv/bin/python scripts/slide_<name>.py`, then
  `scripts/render.sh`. Slide scripts insert themselves after an anchor slide (`d.index_after`, by headline
  text or another script's marker) instead of a fixed index, so they stay in place when slides are added.
  Content slides use `d.content_slide(...)` plus `card`, `chip`, `label`, `line`, `takeaway`. Keep subtitles
  to one line (about 90 characters).
- Speaker notes can't be added yet: the deck's notes master has no body placeholder, so python-pptx returns no
  notes text frame. This needs fixing before notes can be written.
