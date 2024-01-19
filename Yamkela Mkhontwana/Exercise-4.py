# Exercise 4: Aggregation
# Objective: Understand and apply aggregation.
# Task: Create a 'Team' class and an 'Employee' class. Create an additional class that can also be aggregated by the Team class. 
# Then create one or more instances of the Team class, each with a list of the objects it aggregates (team of employees, team of students etc.)
#       Implement methods to add or remove an 'Employee' (or 'Student') from a 'Team'.
# Expected Output: Illustrate how 'Team' objects can manage aggregated objects without owning them.

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