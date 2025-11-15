from rich import print
from book.book import Book
from book.record import Record
from book.fields_type import Field, Name, Phone, Birthday, Email, Note
from handlers.autocomplete_handler import read_input
from handlers.process_command import process_command
from cache.book_repository import BookRepository


def main():
    book = BookRepository.load()
    print("[bold]\nWelcome to the assistant bot![/bold]\n")
    while True:
        try:
            command, args = read_input()
            result = process_command(command, args, book)
            if result is not None:
                print(result)
        except StopIteration:
            break
        finally:
            BookRepository.save(book)
    print(f"Goodbye!") 


if __name__ == "__main__":
    main()

