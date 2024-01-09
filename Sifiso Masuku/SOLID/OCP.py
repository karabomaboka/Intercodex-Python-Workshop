# Exercise 2: Open/Closed Principle (OCP)
# Scenario: Develop a graphics drawing application. The application should be able to draw different shapes, but it should also be easily extendable to include new shapes without modifying the existing code.
# Task: Implement the application's architecture, focusing on how you can add new shapes in the future without altering the existing ones.


class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

class DrawingApplication:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_all_shapes(self):
        for shape in self.shapes:
            shape.draw()

if __name__ == "__main__":
    app = DrawingApplication()
    app.add_shape(Rectangle())
    app.add_shape(Circle())
    app.add_shape(Triangle())

    app.draw_all_shapes()