# quicknote

Quick notes in your terminal. No GUI, no database server — just the terminal and a JSON file.

Notes are stored in `~/.quicknote.json`.

## Installation

### As a package (provides the `note` command)

```bash
git clone https://github.com/opecko/quicknote.git
cd quicknote
pip install .
```

This installs a `note` command available system-wide.

### For development

```bash
git clone https://github.com/opecko/quicknote.git
cd quicknote

python -m venv venv
source venv/bin/activate        # fish: source venv/bin/activate.fish
pip install -e .
```

`-e` installs in editable mode, so code changes take effect immediately.

## Usage

```bash
note add "buy milk"            # add a note
note list                      # list all notes
note list --completed          # show only completed notes
note list --uncompleted        # show only uncompleted notes
note mark-done 2               # mark note at position 2 as done
note mark-undone 2             # mark note at position 2 as not done
note delete 2                  # delete note at position 2
```

You can write the note text without quotes — the words are joined together:

```bash
note add buy milk and bread
```

### Positions

Notes are numbered starting from `1`. The `delete`, `mark-done`, and `mark-undone`
commands take this **list position**, not any internal ID. Always take the position
from a plain `note list` — filtered views (`--completed` / `--uncompleted`) renumber
the notes, so their numbers won't match.

## Commands

| Command | Description |
|---------|-------------|
| `add <text>` | Add a new note |
| `list` | List all notes |
| `list --completed`, `-c` | Show only completed notes |
| `list --uncompleted`, `-u` | Show only uncompleted notes |
| `mark-done <position>` | Mark a note as done |
| `mark-undone <position>` | Mark a note as not done |
| `delete <position>` | Delete a note |

Help for any command:

```bash
note --help
note list --help
```

## Stack

- [click](https://click.palletsprojects.com/) — CLI commands and arguments
- [rich](https://rich.readthedocs.io/) — colored output and tables
- [tinydb](https://tinydb.readthedocs.io/) — JSON storage

## Project layout

```
quicknote/
├── quicknote/
│   ├── cli.py       # click commands
│   ├── db.py        # TinyDB logic
│   ├── models.py    # Note dataclass
│   └── display.py   # rich output
├── aur/             # AUR packaging (PKGBUILD, .SRCINFO)
├── main.py          # entry point
├── pyproject.toml
└── README.md
```

## Packaging

An `aur/PKGBUILD` is included for building an Arch package. AUR publication is
pending while account registration on the AUR is temporarily disabled. You can
still build and install locally:

```bash
cd aur
makepkg -si
```
