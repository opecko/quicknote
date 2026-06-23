# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working style (critical)

Do NOT write finished code for the user. The user writes the code themselves.
Your role: explain concepts, clarify what needs to be done, propose approaches and
designs. Help the user understand — don't hand them complete implementations.

## What this is

Quicknote — a terminal CLI for managing notes. No GUI, no database server.
Just the terminal + a JSON file at `~/.quicknote.json`.

Status: skeleton only. All `.py` files are currently empty; the architecture below
is the intended design to build toward.

## Commands (the CLI surface)

- `note add "text"`       — add a note
- `note list`             — list all notes
- `note search "foo"`     — search note text
- `note delete <pos>`     — delete by **list position** (not doc_id)
- `note done <pos>`       — mark done by **list position**

## Stack

- `click`  — CLI commands and arguments
- `rich`   — output (tables, colors)
- `tinydb` — storage to `~/.quicknote.json`

## Architecture rules

- **Layering**: `cli.py` never calls TinyDB directly. All persistence goes through `db.py`.
  - `cli.py`     — click commands
  - `db.py`      — TinyDB logic
  - `models.py`  — `Note` dataclass
  - `display.py` — rich output
- **Position vs doc_id**: delete/done operate on the note's position in the list,
  not on TinyDB's `doc_id`. `display.py` always shows positions starting at 1.
  So the user passes a 1-based position; that must be translated to the right
  record before any db operation.

## Roadmap / TODO

- Note priority
- Tags / categories
- Export to file
