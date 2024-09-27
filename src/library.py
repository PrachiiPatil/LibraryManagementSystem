class Library:
    """
    Library class to manage books and their availability.
    """
    def __init__(self):
        self.books = {}  # Dictionary to store books with ISBN as keys
        self.borrowed_books = set()  # Set to track borrowed books' ISBNs

    def add_book(self, book):
        """
        Adds a new book to the library.
        """
        if book.isbn not in self.books:
            self.books[book.isbn] = book

    def borrow_book(self, isbn):
        """
        Allows a user to borrow a book if it's available.
        Raises an exception if the book is not available.
        """
        if isbn in self.books and isbn not in self.borrowed_books:
            self.borrowed_books.add(isbn)
        else:
            raise Exception(f"Book with ISBN {isbn} is not available for borrowing.")

    def return_book(self, isbn):
        """
        Allows a user to return a borrowed book.
        """
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def get_available_books(self):
        """
        Returns a list of all books that are available to be borrowed.
        """
        return [book for isbn, book in self.books.items() if isbn not in self.borrowed_books]
