from models.library import Library
from models.book import Book
from models.user import User


class LibraryService:
    def __init__(self):
        self.library = Library("My Library")
        self.users = []

    def add_sample_data(self):
        b1 = Book("Python Basics", "John Doe", "111")
        b2 = Book("Advanced Python", "Jane Doe", "222")
        b3 = Book("OOP Design", "Mark Smith", "333")

        self.library.add_book(b1)
        self.library.add_book(b2)
        self.library.add_book(b3)

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def borrow_book(self, user, title):
        book = self.library.find_book(title)
        if book:
            user.borrow_book(book)
        else:
            print("Book not found")

    def return_book(self, user, title):
        book = self.library.find_book(title)
        if book:
            user.return_book(book)
        else:
            print("Book not found")

    def show_books(self):
        self.library.list_books()
