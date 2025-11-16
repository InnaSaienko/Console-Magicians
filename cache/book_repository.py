"""Repository for persisting and loading address book data."""
import pickle
from pathlib import Path

from book.book import Book

FILE_PATH = Path("book_data.pkl")


class BookRepository:
    """Repository for saving and loading Book data to/from disk."""

    def __init__(self, file_path=FILE_PATH):
        """Initialize repository with file path."""
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls, file_path=FILE_PATH) -> Book:
        """Load Book from file, return empty Book if file not found."""
        path = Path(file_path)
        try:
            with open(path, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Book()
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError):
            raise

    @classmethod
    def save(cls, book: Book, file_path=FILE_PATH):
        """Save Book to file."""
        path = Path(file_path)
        try:
            with open(path, "wb") as file:
                pickle.dump(book, file)
        except Exception:
            raise
