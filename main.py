from rich import print
from book import book
from handlers.autocomplete_handler import read_input
from handlers.process_command import process_command


def main():
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
            pass
    print(f"Goodbye!")


if __name__ == "__main__":
    main()

