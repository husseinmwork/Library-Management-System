class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Book '{book.title}' is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print("You did not borrow this book")

    def list_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        for book in self.borrowed_books:
            print("- " + book.details())
