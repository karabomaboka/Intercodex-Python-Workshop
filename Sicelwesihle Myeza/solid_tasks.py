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

member1 = Member("SihleMyeza", "sihlemyeza@gmail.com")
notification_system = Notification()

notification_system.send_notification(member1, "Your requested book is now available!")

inventory.update_book(book1, "New Title", "New Author")

inventory.remove_book(book2)

# Exercise 2: Open/Closed Principle (OCP)
# Scenario: Develop a graphics drawing application. The application should be able to draw different shapes, but it should also be easily extendable to include new shapes without modifying the existing code.
# Task: Implement the application's architecture, focusing on how you can add new shapes in the future without altering the existing ones.
# Your implementation here
###
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class DrawingApp:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_shapes(self):
        for shape in self.shapes:
            shape.draw()

# Example usage
circle = Circle()
rectangle = Rectangle()

app = DrawingApp()
app.add_shape(circle)
app.add_shape(rectangle)
app.draw_shapes()




# Exercise 3: Liskov Substitution Principle (LSP)
# Scenario: Create a system for a zoo that keeps track of different types of birds and their behaviors, such as flying and swimming.
# Task: Ensure that subclasses of the `Bird` class can be substituted without affecting the system's behavior. Consider how to handle birds that cannot fly.

# Your implementation here
class Bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the sound each bird makes

    def move(self):
        pass  # Placeholder for the movement behavior

class FlyingBird(Bird):
    def fly(self):
        print(f"{self.name} is flying")

class SwimmingBird(Bird):
    def swim(self):
        print(f"{self.name} is swimming")

class Sparrow(FlyingBird):
    def make_sound(self):
        print("Chirp chirp!")

class Penguin(SwimmingBird):
    def make_sound(self):
        print("Honk honk!")

# Zoo class to manage birds
class Zoo:
    def __init__(self):
        self.birds = []

    def add_bird(self, bird):
        self.birds.append(bird)

    def perform_activities(self):
        for bird in self.birds:
            bird.make_sound()
            bird.move()

# Example usage
sparrow = Sparrow("Sparrow1")
penguin = Penguin("Penguin1")

zoo = Zoo()
zoo.add_bird(sparrow)
zoo.add_bird(penguin)
zoo.perform_activities()


# Exercise 4: Interface Segregation Principle (ISP)
# Scenario: You are tasked with developing software for a multifunction printer. This printer can print, scan, fax, and photocopy.
# Task: Design the software components ensuring that clients (like a computer or a user) that use this software will not be forced to depend on interfaces they do not use.

# Your implementation here
# Interface for printing
class PrintFunctionality:
    def print_document(self):
        pass

# Interface for scanning
class ScanFunctionality:
    def scan_document(self):
        pass

# Interface for faxing
class FaxFunctionality:
    def send_fax(self):
        pass

# Interface for photocopying
class PhotocopyFunctionality:
    def photocopy_document(self):
        pass

# MultifunctionPrinter class implementing all interfaces
class MultifunctionPrinter(PrintFunctionality, ScanFunctionality, FaxFunctionality, PhotocopyFunctionality):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def send_fax(self):
        print("Sending fax")

    def photocopy_document(self):
        print("Photocopying document")

# Example usage
printer = MultifunctionPrinter()
printer.print_document()
printer.scan_document()
printer.send_fax()
printer.photocopy_document()


# Exercise 5: Dependency Inversion Principle (DIP)
# Scenario: Imagine creating an e-commerce application that processes orders and payments. The payment process can be done through various methods (e.g., credit card, PayPal, bank transfer).
# Task: Develop the system in a way that the high-level order processing module is not dependent on the low-level payment modules. Think about how you would design the system to easily accommodate new payment methods in the future.

# Your implementation here