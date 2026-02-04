class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            status = "Available" if book.is_available() else "Borrowed"
            print(f"- {book.details()} [{status}]")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
