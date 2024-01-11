# Exercise 2: Open/Closed Principle (OCP)
# Scenario: Develop a graphics drawing application. The application should be able to draw different shapes, but it should also be easily extendable to include new shapes without modifying the existing code.
# Task: Implement the application's architecture, focusing on how you can add new shapes in the future without altering the existing ones.
# Your implementation here

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


