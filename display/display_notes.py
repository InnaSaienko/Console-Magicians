from rich.console import Console
from rich.table import Table

from book.fields_type import Note

console = Console(record=True)


def show_notes(name, notes: list[Note]):

    table = Table(title=f"Notes for {name}")
    table.add_column("Note", style="yellow")
    table.add_column("Tags", style="magenta")

    for note in notes:
        tags = ", ".join(note.tags) if note.tags else "-"
        table.add_row(note.value, tags)

    console.print(table)
