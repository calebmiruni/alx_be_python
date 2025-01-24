class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is not checked out.

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store books.

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.check_out():
                print(f"'{title}' has been checked out.")
                return True
        print(f"'{title}' is not available for checkout.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.return_book():
                print(f"'{title}' has been returned.")
                return True
        print(f"'{title}' was not checked out or is not in the library.")
        return False

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")
