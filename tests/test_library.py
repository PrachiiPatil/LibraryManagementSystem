import pytest
from src.book import Book
from src.library import Library


def test_add_books():
    library = Library()
    book1 = Book('1234567890', 'Book Title 1', 'Author 1', 2022)
    book2 = Book('0987654321', 'Book Title 2', 'Author 2', 2021)

    library.add_book(book1)
    library.add_book(book2)

    available_books = library.get_available_books()
    assert len(available_books) == 2
    assert book1 in available_books
    assert book2 in available_books


def test_borrow_books():
    library = Library()
    book = Book('1234567890', 'Book Title', 'Author', 2022)
    library.add_book(book)

    library.borrow_book('1234567890')

    available_books = library.get_available_books()
    assert len(available_books) == 0


def test_borrow_unavailable_book():
    library = Library()
    book = Book('1234567890', 'Book Title', 'Author', 2022)
    library.add_book(book)
    library.borrow_book('1234567890')

    with pytest.raises(Exception):
        library.borrow_book('1234567890')


def test_return_books():
    library = Library()
    book = Book('1234567890', 'Book Title', 'Author', 2022)
    library.add_book(book)
    library.borrow_book('1234567890')

    library.return_book('1234567890')

    available_books = library.get_available_books()
    assert len(available_books) == 1
    assert book in available_books


def test_view_available_books():
    library = Library()
    book1 = Book('1234567890', 'Book Title 1', 'Author 1', 2022)
    book2 = Book('0987654321', 'Book Title 2', 'Author 2', 2021)

    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book('1234567890')

    available_books = library.get_available_books()
    assert len(available_books) == 1
    assert book2 in available_books
