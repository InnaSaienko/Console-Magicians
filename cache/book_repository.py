
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
                return pickle.load(file)
        except FileNotFoundError:
            return cls()
        except Exception as e:
            print("WARNING: Data load failed (Empty/Corrupted file). A brand new address book will be created.\n")
            return cls()

    @classmethod
    def save(cls, book: Book, file_path=FILE_PATH):
        path = Path(file_path)

        try:
            with open(path, "wb") as file:
                pickle.dump(book, file)
        except Exception as e:
            print(f"ERROR: Failed to save data to file '{path}': {e}")
