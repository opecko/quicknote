from pathlib import Path

from tinydb import TinyDB

from quicknote.models import Note

DB_PATH = Path.home() / ".quicknote.json"
db = TinyDB(DB_PATH)


def add_note(text):
    note = Note(text)
    db.insert(note.to_dict())


def get_all():
    return [Note.from_dict(row) for row in db.all()]


def delete_by_position(pos):
    rows = db.all()
    if pos < 1 or pos > len(rows):
        raise IndexError
    target = rows[pos - 1]
    db.remove(doc_ids=[target.doc_id])


def mark_done(pos):
    rows = db.all()
    if pos < 1 or pos > len(rows):
        raise IndexError
    target = rows[pos - 1]
    db.update({"done": True}, doc_ids=[target.doc_id])


def mark_undone(pos):
    rows = db.all()
    if pos < 1 or pos > len(rows):
        raise IndexError
    target = rows[pos - 1]
    db.update({"done": False}, doc_ids=[target.doc_id])
