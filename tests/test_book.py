"""Import the requirements"""
from library.book import Book

def test_book_creation():
    """make a fucntion"""
    book = Book("Python Guide", "Guido", 2020)
    assert book.title == "Python Guide"
    assert book.is_available
