
import pickle
from pathlib import Path
from book import Book

FILE_PATH = Path("book_data.pkl")


class BookRepository:
    """A repository for saving and loading Book objects to/from a file using pickle."""
    def __init__(self, file_path=FILE_PATH):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls, file_path=FILE_PATH) -> Book:
        """Load a Book object from the file.
        If the file does not exist, return a new Book instance."""
        path = Path(file_path)

        if not path.exists():
            print("WARNING: Data file not found. A brand new address book will be created.\n")
            print("-"*100 + "\n")
            return Book()
        
        try:
            with open(path, "rb") as file:
                book = pickle.load(file)
                return book
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError) as e:
            print("WARNING: Data load failed (Empty/Corrupted file). A brand new address book will be created.\n")
            print("-"*100 + "\n")
            return Book()

    @classmethod
    def save(cls, book: Book, file_path=FILE_PATH):
        """Save the Book object to the file."""
        path = Path(file_path)

        try:
            with open(path, "wb") as file:
                pickle.dump(book, file)
                print(f"File '{path}' saved successfully.")
        except Exception as e:
            print(f"ERROR: Failed to save data to file '{path}': {e}")
