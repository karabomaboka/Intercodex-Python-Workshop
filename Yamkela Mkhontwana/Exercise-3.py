
# Exercise 3: Composition
# Objective: Practice composition to combine classes.
# Task: Define a few classes, 'Engine', 'Wheels', 'Drivetrain' and others as you see fit. 
# Create attributes for these classes (e.g. for Engine, you can create attribute 'size', for Drivetrain you can create attribute 'number_of_gears etc.). Then create a class 'Car'. 
# The 'Car' class should use the created objects as its attributes.
#       Add methods in 'Car' to start and stop the 'Engine', to change 'Gears' etc.
# Expected Output: Show how a 'Car' object can use the functionalities of the 'Engine' through composition.

class Engine:
    def __init__(self, size):
        self.size = size
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Engine started."

    def stop(self):
        self.is_running = False
        return "Engine stopped."

class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def rotate(self):
        return "Wheels are rotating."

class Drivetrain:
    def __init__(self, number_of_gears):
        self.number_of_gears = number_of_gears
        self.current_gear = 1

    def change_gear(self, new_gear):
        self.current_gear = new_gear
        return f"Changed to gear {new_gear}."

class Car:
    def __init__(self, make, model, year, engine_size, num_wheels, num_gears):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(engine_size)
        self.wheels = Wheels(num_wheels)
        self.drivetrain = Drivetrain(num_gears)

    def start(self):
        return f"The {self.make} {self.model}'s engine: {self.engine.start()}"

    def stop(self):
        return f"The {self.make} {self.model}'s engine: {self.engine.stop()}"

    def change_gear(self, new_gear):
        return f"The {self.make} {self.model}'s drivetrain: {self.drivetrain.change_gear(new_gear)}"

# Creating a Car instance
my_car = Car("Toyota", "Corolla", 2022, "1.8L", 4, 6)

# Using Car methods that utilize composition
print(my_car.start())
print(my_car.change_gear(3))
print(my_car.stop())