
import pickle
from pathlib import Path

from book.book import Book

FILE_PATH = Path("book_data.pkl")


class BookRepository:

    def __init__(self, file_path=FILE_PATH):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls, file_path=FILE_PATH) -> Book:
        path = Path(file_path)
        
        try:
            with open(path, "rb") as file:
                book = pickle.load(file)
                return cls()
        except FileNotFoundError:
            return cls()
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError) as e:
            raise

    @classmethod
    def save(cls, book: Book, file_path=FILE_PATH):
        path = Path(file_path)

        try:
            with open(path, "wb") as file:
                pickle.dump(book, file)
        except Exception as e:
            raise
