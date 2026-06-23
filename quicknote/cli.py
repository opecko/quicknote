import click
from click.decorators import argument

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
@click.option("--completed", "-c", is_flag=True, help="Shows already completed notes")
@click.option(
    "--all", "-a", is_flag=True, help="Shows all tasks (completed and uncompleted)"
)
def list_notes(all, completed):
    """Lists completed notes (see more by at 'notes list --help')"""
    notes = db.get_all()

    if completed:
        notes = [n for n in notes if n.done]

    if not all:
        notes = [n for n in notes if not n.done]

    # když all=true tak to nic nedela (projde to se vším)

    show_notes(notes)


@cli.command()
@click.argument("id")
def delete(id):
    """Deletes a note"""
    db.delete_by_position(id)
    click.echo(f"Deleted note {id}")


@cli.command(name="mark-done")
@click.argument("id")
def mark_done(id):
    """Marks note as done"""
    db.mark_done(id)
    click.echo(f"Note {id} marked as done!")


@cli.command(name="mark-undone")
@click.argument("id")
def mark_undone(id):
    """Marks note as undone"""
    db.mark_undone(id)
    click.echo(f"Note {id} marked as undone!")
