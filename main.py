"""Main entry point for the assistant bot application."""
from rich import print

from cache.book_repository import BookRepository
from handlers.autocomplete_handler import read_input
from handlers.process_command import process_command


def main():
    """Run the main bot loop."""
    repository = BookRepository()
    book = repository.load()
    print("[bold]\nWelcome to the assistant bot![/bold]\n")
    while True:
        try:
            command, args = read_input()
            result = process_command(command, args, book)
            if result is not None:
                print(result)
        except StopIteration:
            break
        except Exception as e:
            print(e)
        finally:
            repository.save(book)
    print("Goodbye!")


if __name__ == "__main__":
    main()
