"""Repository for persisting and loading address book data."""
import pickle
from pathlib import Path

from book.book import Book


class BookRepository:
    """Repository for saving and loading Book data to/from disk."""

    def __init__(self, file_path="book_data.pkl"):
        """Initialize repository with file path."""
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> Book:
        """Load Book from file, return empty Book if file not found."""
        try:
            with open(self.file_path, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Book()
        except Exception as e:
            print("WARNING: Data load failed (Empty/Corrupted file). A brand new address book will be created.\n")
            return Book()

    def save(self, book: Book):
        """Save Book to file."""
        try:
            with open(self.file_path, "wb") as file:
                pickle.dump(book, file)
        except Exception as e:
            print(f"ERROR: Failed to save data to file '{self.file_path}': {e}")
