# Exercise 1: Single Responsibility Principle (SRP)
# Scenario: You are building a system for a library. The system needs to handle book inventory management and notify members about book availability. 
# Task: Design the system in such a way that each part of the system has a single responsibility. Think about how to separate concerns like managing the book inventory and notifying members.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

    def is_book_available(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False

class NotificationSystem:
    def send_notification(self, title):
        # Send notification to members that the book is available.
        pass

if __name__ == "__main__":
    book_inventory = BookInventory()
    book_inventory.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", 1954))
    book_inventory.add_book(Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997))

    notification_system = NotificationSystem()

    if book_inventory.is_book_available("The Lord of the Rings"):
        notification_system.send_notification("The Lord of the Rings")

        