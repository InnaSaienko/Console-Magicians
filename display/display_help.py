from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console(markup=False)

HELP_SECTIONS = [
    ("👥 Contact Management", "blue", [
        ("add-contact", "add-contact [name] [phone] [email (optional)]", "Adds a new contact or updates existing one"),
        ("add-birthday", "add-birthday [name] [birthday date]", "Adds a birthday date to a contact. Format: `DD.MM.YYYY`."),
        ("update-birthday", "update-birthday [name] [birthday date]", "Update the date of birth for the specified contact."),
        ("show-birthday", "show-birthday [name]", "Displays the birthday date of the contact."),
        ("find-birthday", "find-birthday [birthday date]", "Show contact with specified date of birth."),
        ("add-email", "add-email [name] [email]", "Adds an email for the contact"),
        ("update-email", "update-email [name] [old email] [new email]", "Updates contact's email"),
        ("show-email", "show-email [name]", "Displays contact's email"),
        ("find-email", "find-email [email]", "Shows contact who has this email"),
        ("update-phone", "update-phone [name] [old phone] [new phone]", "Updates contact's phone number"),
        ("show-phone", "show-phone [name]", "Shows all stored phone numbers for the contact."),
        ("add-address", "add-address [name] [\"user address\"]", "Adds or updates a contact's address."),
        ("show-address", "show-address [name]", "Shows contact's address"),
        ("upcoming-birthdays", "upcoming-birthdays", "Shows birthdays in next 7 days"),
        ("find-contact", "find-contact [name]", "Displays full contact information"),
        ("delete-contact", "delete-contact [name]", "Removes the contact from the address book."),
        ("all-contact", "all-contact", "Shows a full list of all contacts."),
    ]),
    ("📝 Notes Management", "yellow", [
        ("add-note", "add-note [name] [\"note\"] [\"tags...\"]", "Adds a note with one or more tags to a contact."),
        ("show-contact-notes", "show-contact-notes [name]", "Displays all notes of the specified contact. "),
        ("delete-note", "delete-note [name] [keyword]", "Removes notes containing the specified keyword."),
        ("update-note", "update-note [name] [keyword] [\"new note\"]", "Updates note text found by keyword."),
        ("find-notes-by-tag", "find-notes-by-tag [name] [tag]", "Shows notes filtered by tag."),
    ]),
    ("🏷️  Tags Management", "green", [
        ("add-tag", "add-tag [name] [\"keywords\"] [tag]", "Adds a tag to a specific note"),
        ("change-tag", "change-tag [name] [kw] [old] [new]", "Replaces an existing tag"),
        ("delete-contact-tag", "delete-contact-tag [name] [kw] [tag]", "Removes a tag from a note"),
    ]),
    ("🤖 Other Commands", "red", [
        ("hello", "hello", "Displays a welcome message"),
        ("close / exit", "close / exit", "Ends the program"),
        ("help", "help", "Shows this help menu"),
    ]),
]


def show_help():
    title = Text("📒 Bot Commands Guide", style="bold cyan", justify="left")
    console.print()
    console.print(Panel(title, border_style="cyan"))
    console.print()
    
    for section_title, border_color, commands in HELP_SECTIONS:
        table = Table(
            show_header=True, 
            header_style="bold magenta", 
            border_style=border_color,
            box=None
        )
        table.add_column("Command", style="cyan", no_wrap=True, width=20)
        table.add_column("Usage", style="green", no_wrap=False)
        table.add_column("Description", style="white", no_wrap=False)
        
        for cmd, usage, desc in commands:
            table.add_row(cmd, usage, desc)
        
        console.print(Panel(table, title=section_title, border_style=border_color, title_align="left"))
        console.print()

