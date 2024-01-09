from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Concrete implementation of a shape - Square
class Square(Shape):
    def draw(self):
        print("Drawing a Square")

# A class that uses the shapes without modification
class GraphicsEditor:
    def draw_shape(self, shape):
        shape.draw()

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

if __name__ == "__main__":
    # Existing code using the graphics editor
    editor = GraphicsEditor()

    Rectangle = Rectangle()
    square = Square()

    editor.draw_shape(Rectangle)
    editor.draw_shape(square)

    triangle = Triangle()
    editor.draw_shape(triangle)
