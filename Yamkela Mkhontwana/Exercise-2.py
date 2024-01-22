
# Exercise 2: Inheritance
# Objective: Understand and implement inheritance.
# Task: Create a 'Vehicle' class with attributes like 'make', 'model', 'year', 'engine_size' and whatever other attributes you see fit. 
# Also, create a few functions (like drive, etc.) that all vehicles share. Then, define two subclasses,
#       'Car' and 'Motorcycle', each with specific attributes.
# Expected Output: Demonstrate the use of inherited methods and attributes, as well as subclass-specific attributes.

class Vehicle:
    def __init__ (self, make, model, year, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size
        
    def drive(self):
        return f"The {self.make}  {self.model} is now driving"
    def stop(self):
        return f" The {self.make}  {self.model} is stopping"

class Car(Vehicle):
    def __init__(self, make, model, year, engine_size, number_of_gears):
        super(). __init__ (make, model, year, engine_size)
        self.number_of_gears = number_of_gears

    def honk(self):
        return f"The {self.make} {self.model} is honking its horn"
    



class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size, number_of_wheels):
        super(). __init__(make, model, year, engine_size)
        self.number_of_wheels = number_of_wheels
    
    def wheelie(self):
        return f"The {self.make}  {self.model} is wheeling"
    
car1 = Car("BMW" , "X4 M40i", 2023, "3.0L" , 4)
motorcycle = Motorcycle("Harley-Devision" , "Sporter", 2022, "1200cc", 2)
    
print(car1.drive)
print(motorcycle.drive)


print(car1.honk())
print(motorcycle.wheelie())