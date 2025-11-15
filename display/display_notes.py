from rich.console import Console
from rich.table import Table

console = Console(record=True)


def show_notes_for_record(record):
    if not record.notes:
        console.print(f"[yellow]{record.name.value} has no notes.[/yellow]")
        return

    table = Table(title=f"Notes for {record.name.value}")
    table.add_column("Contact name", style="cyan", no_wrap=True)
    table.add_column("Note", style="yellow")
    table.add_column("Tags", style="magenta")

    for note in record.notes:
        tags = ", ".join(note.tags) if note.tags else "-"
        table.add_row(record.name.value, note.value, tags)

    console.print(table)
