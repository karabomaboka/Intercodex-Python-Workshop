# Exercise 1: Single Responsibility Principle (SRP)
# Scenario: You are building a system for a library. The system needs to handle book inventory management and notify members about book availability. 
# Task: Design the system in such a way that each part of the system has a single responsibility. Think about how to separate concerns like managing the book inventory and notifying members.

# Your implementation here
# class Book:
#     def __init__(self, title, author, available=True):
#         self.title = title
#         self.author = author
#         self.available = available

# class InventoryManager:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def remove_book(self, book):
#         self.books.remove(book)

#     def check_availability(self, book_title):
#         for book in self.books:
#             if book.title == book_title:
#                 return book.available
#         return False

# class MemberNotification:
#     def notify_book_availability(self, member, book_title, is_available):
#         if is_available:
#             print(f"Dear {member}, the book '{book_title}' is available now!")
#         else:
#             print(f"Dear {member}, the book '{book_title}' is currently unavailable.")

class Book:
    def __init__(self, title: str, author: str, publication_year: int, available: bool = True):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__available = available

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_publication_year(self) -> int:
        return self.__publication_year

    def is_available(self) -> bool:
        return self.__available

    def set_availability(self, available: bool):
        self.__available = available


class InventoryManager:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, book: Book):
        self.__books.remove(book)

    def check_availability(self, book_title: str) -> bool:
        for book in self.__books:
            if book.get_title() == book_title:
                return book.is_available()
        return False


class NotificationService:
    def notify_member(self, member: str, message: str):
        print(f"Notifying {member}:\n{message}")


class LibrarySystem:
    def __init__(self):
        self.__inventory = InventoryManager()
        self.__notification_service = NotificationService()

    def add_book_to_inventory(self, book: Book):
        self.__inventory.add_book(book)

    def remove_book_from_inventory(self, book: Book):
        self.__inventory.remove_book(book)

    def check_book_availability(self, book_title: str) -> bool:
        return self.__inventory.check_availability(book_title)

    def notify_member_about_book(self, member: str, book_title: str, is_available: bool):
        message = f"The book '{book_title}' is now available." if is_available else f"The book '{book_title}' is currently unavailable."
        self.__notification_service.notify_member(member, message)

# Exercise 2: Open/Closed Principle (OCP)
# Scenario: Develop a graphics drawing application. The application should be able to draw different shapes, but it should also be easily extendable to include new shapes without modifying the existing code.
# Task: Implement the application's architecture, focusing on how you can add new shapes in the future without altering the existing ones.

# Your implementation here
from abc import ABC, abstractmethod

# Abstract Shape class (Closed for modification)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete shapes (Open for extension)
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

# New shapes (Can be added without modifying existing code)
class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

class Pentagon(Shape):
    def draw(self):
        print("Drawing Pentagon")

# Drawing application
class GraphicsDrawingApp:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            shape.draw()

# Usage
drawing_app = GraphicsDrawingApp()
drawing_app.add_shape(Circle())
drawing_app.add_shape(Square())
drawing_app.add_shape(Triangle())  # Adding a new shape without modifying existing code
drawing_app.add_shape(Pentagon())  # Another new shape

drawing_app.draw_all()  # Drawing all shapes


# Exercise 3: Liskov Substitution Principle (LSP)
# Scenario: Create a system for a zoo that keeps track of different types of birds and their behaviors, such as flying and swimming.
# Task: Ensure that subclasses of the `Bird` class can be substituted without affecting the system's behavior. Consider how to handle birds that cannot fly.

# Your implementation here

from abc import ABC, abstractmethod

# Abstract Bird class
class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# FlyingBird subclass
class FlyingBird(Bird):
    def fly(self):
        return f"{self.name} is flying"

# SwimmingBird subclass
class SwimmingBird(Bird):
    def swim(self):
        return f"{self.name} is swimming"

# Duck class (Can both fly and swim)
class Duck(FlyingBird, SwimmingBird):
    def make_sound(self):
        return "Quack!"

# Ostrich class (Cannot fly)
class Ostrich(SwimmingBird):
    def make_sound(self):
        return "Boom!"

# Usage
duck = Duck("Donald")
ostrich = Ostrich("Oscar")

print(duck.make_sound())  # Output: Quack!
print(duck.fly())        # Output: Donald is flying
print(duck.swim())       # Output: Donald is swimming

print(ostrich.make_sound())  # Output: Boom!
print(ostrich.swim())        # Output: Oscar is swimming

# Exercise 4: Interface Segregation Principle (ISP)
# Scenario: You are tasked with developing software for a multifunction printer. This printer can print, scan, fax, and photocopy.
# Task: Design the software components ensuring that clients (like a computer or a user) that use this software will not be forced to depend on interfaces they do not use.

# Your implementation here
from abc import ABC, abstractmethod

# Define separate interfaces for different functionalities

class PrintFunctionality(ABC):
    @abstractmethod
    def print_document(self):
        pass

class ScanFunctionality(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class FaxFunctionality(ABC):
    @abstractmethod
    def fax_document(self):
        pass

class PhotocopyFunctionality(ABC):
    @abstractmethod
    def photocopy_document(self):
        pass

# Implement the printer by combining specific functionalities

class MultifunctionPrinter(PrintFunctionality, ScanFunctionality, FaxFunctionality, PhotocopyFunctionality):
    def print_document(self):
        print("Printing document...")

    def scan_document(self):
        print("Scanning document...")

    def fax_document(self):
        print("Faxing document...")

    def photocopy_document(self):
        print("Photocopying document...")

# Example usage

printer = MultifunctionPrinter()

printer.print_document()
printer.scan_document()
printer.fax_document()
printer.photocopy_document()


# Exercise 5: Dependency Inversion Principle (DIP)
# Scenario: Imagine creating an e-commerce application that processes orders and payments. The payment process can be done through various methods (e.g., credit card, PayPal, bank transfer).
# Task: Develop the system in a way that the high-level order processing module is not dependent on the low-level payment modules. Think about how you would design the system to easily accommodate new payment methods in the future.

# Your implementation here
# from abc import ABC, abstractmethod

# # Define an interface for payment processing
# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass

# # Implement different payment methods as concrete classes
# class CreditCardPayment(PaymentProcessor):
#     def process_payment(self, amount):
#         print(f"Processing credit card payment of ${amount}")

# class PayPalPayment(PaymentProcessor):
#     def process_payment(self, amount):
#         print(f"Processing PayPal payment of ${amount}")

# # Order processing module that depends on PaymentProcessor interface
# class OrderProcessor:
#     def __init__(self, payment_processor: PaymentProcessor):
#         self.payment_processor = payment_processor

#     def process_order(self, total_amount):
#         # Business logic for processing an order
#         print(f"Processing order with total amount: ${total_amount}")
#         self.payment_processor.process_payment(total_amount)

# # Example usage
# credit_card_payment = CreditCardPayment()
# paypal_payment = PayPalPayment()

# order_processor_cc = OrderProcessor(credit_card_payment)
# order_processor_cc.process_order(100)

# order_processor_paypal = OrderProcessor(paypal_payment)
# order_processor_paypal.process_order(150)
############################################################################
from abc import ABC, abstractmethod

# Define abstract classes representing the high-level order processing module

class OrderProcessor(ABC):
    @abstractmethod
    def process_order(self):
        pass

# Define abstract classes representing payment methods

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

# Implement specific payment methods

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class BankTransferPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing bank transfer payment of {amount} in Rands")

# Implement the high-level order processing module

class OnlineOrder(OrderProcessor):
    def __init__(self, payment_method: PaymentMethod):
        self.__payment_method = payment_method

    def process_order(self, amount):
        self.__payment_method.make_payment(amount)

# Example usage

credit_card = CreditCardPayment()
paypal = PayPalPayment()
fnb_bank = BankTransferPayment()

online_order_cc = OnlineOrder(credit_card)
online_order_cc.process_order("$100")

online_order_paypal = OnlineOrder(paypal)
online_order_paypal.process_order("$150")

online_order_fnb = OnlineOrder(fnb_bank)
online_order_fnb.process_order("R200")
