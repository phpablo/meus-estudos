# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal **study monorepo** — not a single application. It collects coursework, challenges, and projects across many languages and stacks. There is no global build, test, or lint at the root; each subproject is self-contained and uses the toolchain native to its language. Always determine the stack from the local folder before running anything.

## Layout (top-level)

- `eng-soft-uniamerica/` — UniAmérica Software Engineering degree, organized by `semestre-N/` then discipline.
- `ads-ufca/` — UFCA ADS degree, same `semestre-N/` structure.
- `cursos/` — course material (Curso em Vídeo Python/Java/JS/HTML-CSS, SQL, etc.). Python course is split into `mundo-01/02/03` with an `exercicios/` folder (`exNN.py` per exercise).
- `desafios/` — coding challenges: `leet-code/`, `code-wars/`, `frontend-mentor/`.
- `projetos/` — numbered mini-projects (`NNN-name/`), each with its own README and toolchain (PHP CRUD, Spring Boot + React, Python ETL/Airflow, etc.).
- `resumos/` — theory notes and study summaries.

## Running code

Per-subproject. Common cases:
- **Python exercises** (`cursos/.../exercicios/exNN.py`): run directly, `python exNN.py`. A repo-root `.venv/` exists — activate it (`.venv\Scripts\Activate.ps1` on PowerShell) for projects needing dependencies.
- **Numbered projects** (`projetos/NNN-*`): check that folder's own README/package manifest (`requirements.txt`, `package.json`, `pom.xml`, etc.) for build/run steps.

## Commit convention

Conventional Commits with a leading gitmoji (see README). Used in practice:
- `:sparkles: feat` — new feature or exercise
- `:bug: fix` — bug fix
- `:pencil: docs` — documentation / resumos (also used for adding exercises)
- `:recycle: refactor`, `:white_check_mark: test`, `:zap: perf`, `:wrench: chore`

Keep commits scoped to one exercise/file where the existing history does (e.g. one commit per `exNN.py`).
