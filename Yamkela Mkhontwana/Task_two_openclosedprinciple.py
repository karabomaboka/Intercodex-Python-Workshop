from abc import ABC, abstractmethod

# Part 1: Shape Management (SRP)

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_all_shapes(self):
        for shape in self.shapes:
            shape.draw()

# Part 2: Notification System (SRP)

class NotificationService:
    def notify_user(self, user, message):
        # Implement the notification mechanism (e.g., email, SMS, push notification)
        print(f"Notifying {user}: {message}")

# Example Usage:

# Initialize components
shape_manager = ShapeManager()
notification_service = NotificationService()

# Create shapes
circle = Circle()
square = Square()
triangle = Triangle()

# Add shapes to the manager
shape_manager.add_shape(circle)
shape_manager.add_shape(square)
shape_manager.add_shape(triangle)

# Draw all shapes
shape_manager.draw_all_shapes()

# Notify a user
notification_service.notify_user("Alice", "Your shapes have been drawn.")
