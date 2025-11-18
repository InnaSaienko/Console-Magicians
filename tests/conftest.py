import pytest
from book.book import Book

@pytest.fixture
def book():
    """Фікстура для створення нової адресної книги для кожного тесту."""
    return Book()