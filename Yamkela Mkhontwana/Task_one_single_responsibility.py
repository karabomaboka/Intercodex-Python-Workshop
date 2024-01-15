# Part 1: Book Management

class Book:
    def __init__(self, title, author, status="available"):
        self.title = title
        self.author = author
        self.status = status  # status can be "available" or "checked out"

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

# Part 2: Notification System

class MemberNotification:
    def send_notification(self, member, message):
        # Implement the notification mechanism (e.g., email, SMS, push notification)
        print(f"Notification sent to {member}: {message}")

# Part 3: Library System

class LibrarySystem:
    def __init__(self, book_catalog, notification_system):
        self.book_catalog = book_catalog
        self.notification_system = notification_system

    def borrow_book(self, member, book):
        if book.status == "available":
            book.status = "checked out"
            message = f"The book '{book.title}' by {book.author} is now checked out."
            self.notification_system.send_notification(member, message)
        else:
            message = f"Sorry, the book '{book.title}' by {book.author} is currently checked out."
            self.notification_system.send_notification(member, message)

    def return_book(self, member, book):
        if book.status == "checked out":
            book.status = "available"
            message = f"Thank you, {member}! The book '{book.title}' by {book.author} has been returned."
            self.notification_system.send_notification(member, message)
        else:
            message = f"Error: The book '{book.title}' by {book.author} was not checked out to {member}."
            self.notification_system.send_notification(member, message)

# Example Usage

# Initialize components
book_catalog = BookCatalog()
notification_system = MemberNotification()
library_system = LibrarySystem(book_catalog, notification_system)

# Add books to the catalog
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("1984", "George Orwell")
book_catalog.add_book(book1)
book_catalog.add_book(book2)

# Borrow a book
library_system.borrow_book("Alice", book1)

# Return a book
library_system.return_book("Alice", book1)
