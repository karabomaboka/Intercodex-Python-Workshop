# Exercise 2: Inheritance
# Objective: Understand and implement inheritance.
# Task: Create a 'Vehicle' class with attributes like 'make', 'model', 'year', 'engine_size' and whatever other attributes you see fit. 
# Also, create a few functions (like drive, etc.) that all vehicles share. Then, define two subclasses,
#       'Car' and 'Motorcycle', each with specific attributes.
# Expected Output: Demonstrate the use of inherited methods and attributes, as well as subclass-specific attributes.

class Vehicle:

    def __init__(self, make, model, year, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")


class Car(Vehicle):

    def __init__(self, make, model, year, engine_size, num_of_doors):
        super().__init__(make, model, year, engine_size)
        self.num_of_doors = num_of_doors

    def honk_horn(self):
        print("Beep! Beep!")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, engine_size, num_of_wheels):
        super().__init__(make, model, year, engine_size)
        self.num_of_wheels = num_of_wheels

    def rev_engine(self):
        print("Vroom!")


car = Car("Toyota", "Corolla", 2023, 2.0, 4)
car.drive()
car.honk_horn()

motorcycle = Motorcycle("Honda", "CBR1000RR", 2023, 1.0, 2)
motorcycle.drive()
motorcycle.rev_engine()