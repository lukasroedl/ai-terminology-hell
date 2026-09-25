# CLAUDE.md

## What this repository is

`ai-classroom`: educational material that explains AI, built by the user. Each project folder teaches one topic
to a specific audience, and together they show the user's hands-on experience with AI.

The audience and rules differ per project, so each project folder has its own `CLAUDE.md`. Its rules apply only
inside that folder. For work outside a project folder (this file, the root README, shared setup), write clearly
for readers who want to learn about AI; technical terms are fine when they are explained.

## Projects

| Folder | What it is |
|---|---|
| `ai-terminology-hell/` | The slide deck "A Short History of AI: From Generative AI to Agentic AI" for a **non-technical corporate audience**, plus the scripts that build it. |

Add a row here, and to the root `README.md`, when a new project folder is added.

## Shared setup

- Python: one virtual environment for the whole repo in `.venv` (dependencies in `requirements.txt`). Run
  Python with `.venv/bin/python` from the repo root. Don't install tools globally; add Python dependencies to
  `.venv` and `requirements.txt`.
- Generated or temporary files (`.render/`, `.preview/`, PowerPoint lock files `~$*`) are ignored by git.
