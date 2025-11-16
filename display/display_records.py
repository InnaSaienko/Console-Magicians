from rich.console import Console
from rich.table import Table

console = Console(record=True)

def show_records(records, title="Contacts"):
    if not records:
        console.print("[yellow]No records found[/yellow]")
        return

    table = Table(title=title)
    table.add_column("Contact name", style="cyan", no_wrap=True)
    table.add_column("Birthday", style="magenta")
    table.add_column("Phones", style="green")
    table.add_column("Emails", style="blue")
    table.add_column("Address", style="light_slate_grey")
    table.add_column("Notes", style="yellow")
    table.add_column("Tags", style="cyan")

    for record in records:
        phones = "; ".join(p.value for p in record.phones)
        birthday = str(record.birthday) if record.birthday else "-"
        emails = "; ".join(e.value for e in record.emails)
        address = "+" if record.address else "-"
        notes = "+" if record.notes else "-"
        tags = "+" if any(n.tags for n in record.notes) else "-"
        table.add_row(record.name.value, birthday, phones, emails, address, notes, tags)

    console.print(table)