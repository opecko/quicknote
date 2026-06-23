from rich.console import Console
from rich.table import Table

console = Console()


def show_notes(notes):
    if not notes:
        console.print("[dim]No notes.[/dim]")
        return

    table = Table()
    table.add_column("#", justify="right")
    table.add_column("Text")
    table.add_column("State", justify="center")

    for i, note in enumerate(notes, start=1):
        text = f"[strike]{note.text}[/strike]" if note.done else note.text
        state = "[green]☑[/green]" if note.done else "[dim]☐[/dim]"
        table.add_row(str(i), text, state)

    console.print(table)
