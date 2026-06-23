# quicknote

Quick notes in your terminal. No GUI, no database server — just the terminal and a JSON file.

Notes are stored in `~/.quicknote.json`.

## Installation

```bash
git clone <repo-url> quicknote
cd quicknote

python -m venv venv
source venv/bin/activate        # fish: source venv/bin/activate.fish
pip install -r requirements.txt
```

## Usage

```bash
python main.py add "buy milk"          # add a note
python main.py list                    # list unfinished notes
python main.py list --all              # list everything, including done
python main.py search "milk"           # search note text
python main.py done 2                  # mark note #2 as done
python main.py delete 2                # delete note #2
```

You can write the note text without quotes — the words are joined together:

```bash
python main.py add buy milk and bread
```

### Positions vs. quotes

Notes in `list` are numbered starting from `1`. The `done` and `delete` commands
take this **list position**, not any internal ID. After a delete, the remaining
notes are renumbered, so the position always matches what you see in `list`.

## Commands

| Command | Description |
|---------|-------------|
| `add <text>` | Add a new note |
| `list` | List notes (unfinished by default) |
| `list --all`, `-a` | List everything, including done |
| `search <query>` | Search note text |
| `done <position>` | Mark a note as done |
| `delete <position>` | Delete a note |

Help for any command:

```bash
python main.py --help
python main.py list --help
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
├── main.py          # entry point
├── requirements.txt
└── README.md
```
