import click

from quicknote import db
from quicknote.display import show_notes


@click.group()
def cli():
    """Quicknote - notes in the terminal"""
    pass


@cli.command()
@click.argument("text", nargs=-1)
def add(text):
    """Add a new note"""

    text = " ".join(text)
    if not text:
        click.echo("No note provided.")
        return

    db.add_note(text)
    click.echo(f"Note added: {text}")


@cli.command(name="list")
@click.option("--completed", "-c", is_flag=True, help="Shows only completed notes")
@click.option("--uncompleted", "-u", is_flag=True, help="Shows only uncompleted notes")
def list_notes(uncompleted, completed):
    """Lists all notes (see more at 'notes list --help')"""

    notes = db.get_all()

    if completed:
        notes = [n for n in notes if n.done]
    elif uncompleted:
        notes = [n for n in notes if not n.done]

    show_notes(notes)


@cli.command()
@click.argument("position", type=int)
def delete(position):
    """Delete a note by its position in the list.

    Position is the number shown in `list`. After a delete the
    remaining notes are renumbered, and filtered views
    (--completed / --uncompleted) renumber too — so take the
    position from a plain `list`.
    """

    try:
        db.delete_by_position(position)
    except IndexError:
        click.echo(f"Note {position} doesn't exist!")
        return

    click.echo(f"Deleted note {position}")


@cli.command(name="mark-done")
@click.argument("position", type=int)
def mark_done(position):
    """Mark a note as done, by its position in the list.

    Position is the number shown in a plain `list`. Filtered
    views may renumber notes, so use the position from `list`
    without filters.
    """

    try:
        db.mark_done(position)
    except IndexError:
        click.echo(f"Note {position} doesn't exist!")
        return

    click.echo(f"Note {position} marked as done!")


@cli.command(name="mark-undone")
@click.argument("position", type=int)
def mark_undone(position):
    """Mark a note as not done, by its position in the list.

    Position is the number shown in a plain `list`. Filtered
    views may renumber notes, so use the position from `list`
    without filters.
    """

    try:
        db.mark_undone(position)
    except IndexError:
        click.echo(f"Note {position} doesn't exist!")
        return

    click.echo(f"Note {position} marked as undone!")
