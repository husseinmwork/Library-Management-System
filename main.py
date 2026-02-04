from services.library_service import LibraryService

service = LibraryService()

service.add_sample_data()

service.show_books()

user = service.register_user("Hussein")

service.borrow_book(user, "Python Basics")

service.show_books()

user.list_books()

service.return_book(user, "Python Basics")

service.show_books()
