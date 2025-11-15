from book.book import Book
from utils.command_to_handler import COMMAND_TO_HANDLER


def process_command(command, args, book: Book):
    try:
        handler = COMMAND_TO_HANDLER[command]
        return handler(args, book)
    except KeyError:
        print("[red]Invalid command.[/red]")
