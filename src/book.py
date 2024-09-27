class Book:
    """
    Represents a book in the library with unique ISBN, title, author, and publication year.
    """
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"<Book {self.title} by {self.author}, {self.year}>"
