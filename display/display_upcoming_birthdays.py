from rich.console import Console
from rich.table import Table

console = Console(record=True)


def show_birthdays(records, title="Upcoming Birthdays"):
    if not records:
        console.print("[yellow]No upcoming birthdays found[/yellow]")
        return

    table = Table(title=title)
    table.add_column("Contact name", style="cyan", no_wrap=True)
    table.add_column("Congratulation date", style="magenta")

    for record in records:
        table.add_row(record["name"], record["date"])

    console.print(table)
