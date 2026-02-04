class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available

    def details(self):
        return f"{self.title} - {self.author} (ISBN: {self.isbn})"
