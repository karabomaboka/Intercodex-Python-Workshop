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

    def start(self):
        print("The engine is starting.")

    def stop(self):
        print("The engine is stopping.")


class Wheels:

    def __init__(self, number):
        self.number = number

    def turn(self):
        print("The wheels are turning.")


class Drivetrain:

    def __init__(self, number_of_gears):
        self.number_of_gears = number_of_gears

    def change_gear(self, gear):
        print("The gear is changing to {}.".format(gear))


class Car:

    def __init__(self, engine, wheels, drivetrain):
        self.engine = engine
        self.wheels = wheels
        self.drivetrain = drivetrain

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def turn(self):
        self.wheels.turn()

    def change_gear(self, gear):
        self.drivetrain.change_gear(gear)


engine = Engine("V8")
wheels = Wheels(4)
drivetrain = Drivetrain(5)

car = Car(engine, wheels, drivetrain)

car.start()
car.turn()
car.change_gear(3)
car.stop()