
import pickle
from pathlib import Path

FILE_PATH = Path("book_data.pkl")


class BookRepository:
    def __init__(self, file_path=FILE_PATH):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls):
        pass

    @classmethod
    def save(cls, book):
        pass
