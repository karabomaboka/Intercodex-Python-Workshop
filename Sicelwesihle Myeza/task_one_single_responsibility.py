# Exercise 1: Single Responsibility Principle (SRP)
# Scenario: You are building a system for a library. The system needs to handle book inventory management and notify members about book availability. 
# Task: Design the system in such a way that each part of the system has a single responsibility. Think about how to separate concerns like managing the book inventory and notifying members.

# Your implementation here
class Book :
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        
class BookInventory :
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def update_book(self, book, new_title, new_author):
        book.title = new_title
        book.author = new_author

    def check_available(self,book):
        return book in self.books

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Notification:
    def send_notification(self, member, message):
        print(f"Notification sent to {member.name} ({member.email}): {message}")

book1 = Book(" Alice in Wonderland", "Lewis Carrol")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The great gatsby", "Scott Fitgerald")

inventory = BookInventory()

inventory.add_book(book1)
inventory.add_book(book2)

print( inventory.check_available(book1))
print( inventory.check_available(Book("1984", "George Orwell")))

member1 = Member("Sihle Myeza", "sihlemyeza@gmail.com")
#notification_system = Notification()

#notification_system.send_notification(member1, "Your requested book is now available!")

#inventory.update_book(book1, "New Title", "New Author")

#inventory.remove_book(book2)