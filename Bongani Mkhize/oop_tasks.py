# Exercise 1: Basic Class Creation
# Objective: Create a simple class with attributes and methods.
# Task: Define a 'Book' class with attributes 'title', 'author', and 'publication_year'. 
#       Include a method 'get_info()' that returns a string with all these details.
# Expected Output: Create instances of 'Book' and use 'get_info()' to display its attributes.

# class Book:
#     # Your implementation here
class Book:
    def __init__(self, title, author, publication_year):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year

    def get_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, Publication Year: {self.__publication_year}"

# Creating an instance of the Book class
book_instance = Book("o Kill a Mockingbird", "N.H. Salinger", 1960)

# Using the get_info() method to display its attributes
print(book_instance.get_info())


# Exercise 2: Inheritance
# Objective: Understand and implement inheritance.
# Task: Create a 'Vehicle' class with attributes like 'make', 'model', 'year', 'engine_size' and whatever other attributes you see fit. 
# Also, create a few functions (like drive, etc.) that all vehicles share. Then, define two subclasses,
#       'Car' and 'Motorcycle', each with specific attributes.
# Expected Output: Demonstrate the use of inherited methods and attributes, as well as subclass-specific attributes.

# class Vehicle:
#     # Your implementation hereclass Vehicle:
class Vehicle:
    def __init__(self, make, model, year, engine_size):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__engine_size = engine_size

    def drive(self):
        return f"The {self.__make} {self.__model} is now being driven."

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

# Subclass Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, engine_size, num_doors):
        super().__init__(make, model, year, engine_size)
        self.__num_doors = num_doors

    def display_info(self):
        return f"This car is a {self.get_year()} {self.get_make()} {self.get_model()} with {self.__num_doors} doors."

# Subclass Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size, bike_type):
        super().__init__(make, model, year, engine_size)
        self.__bike_type = bike_type

    def display_info(self):
        return f"This motorcycle is a {self.get_year()} {self.get_make()} {self.get_model()} ({self.__bike_type})."

# Creating instances of Car and Motorcycle
my_car = Car("Toyota", "Corolla", 2020, "2.0L", 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019, "1.2L", "Cruiser")

# Demonstrating inherited methods and subclass-specific methods
print(my_car.drive())  # Using inherited method
print(my_car.display_info())  # Using subclass-specific method
print(my_motorcycle.drive())  # Using inherited method
print(my_motorcycle.display_info())  # Using subclass-specific method

# Exercise 3: Composition
# Objective: Practice composition to combine classes.
# Task: Define a few classes, 'Engine', 'Wheels', 'Drivetrain' and others as you see fit. 
# Create attributes for these classes (e.g. for Engine, you can create attribute 'size', for Drivetrain you can create attribute 'number_of_gears etc.). Then create a class 'Car'. 
# The 'Car' class should use the created objects as its attributes.
#       Add methods in 'Car' to start and stop the 'Engine', to change 'Gears' etc.
# Expected Output: Show how a 'Car' object can use the functionalities of the 'Engine' through composition.

# class Engine:
#     # Your implementation here
# class Wheels:
#     # Your implementation here
# class Drivetrain:
#     # Your implementation here
# some more classes if you created them here...

# class Car:
#     # Your implementation here
class Engine:
    def __init__(self, size):
        self.size = size
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            return "Engine started."
        else:
            return "Engine is already running."

    def stop(self):
        if self.running:
            self.running = False
            return "Engine stopped."
        else:
            return "Engine is already stopped."

class Wheels:
    def __init__(self, size):
        self.size = size

class Drivetrain:
    def __init__(self, number_of_gears):
        self.number_of_gears = number_of_gears

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(2.0)  # Engine composition
        self.wheels = Wheels(18)  # Wheels composition
        self.drivetrain = Drivetrain(6)  # Drivetrain composition

    def start_engine(self):
        return self.engine.start()

    def stop_engine(self):
        return self.engine.stop()

    def change_gears(self, gears):
        self.drivetrain.number_of_gears = gears
        return f"Changed gears to {gears}."


# Exercise 4: Aggregation
# Objective: Understand and apply aggregation.
# Task: Create a 'Team' class and an 'Employee' class. Create an additional class that can also be aggregated by the Team class. 
# Then create one or more instances of the Team class, each with a list of the objects it aggregates (team of employees, team of students etc.)
#       Implement methods to add or remove an 'Employee' (or 'Student') from a 'Team'.
# Expected Output: Illustrate how 'Team' objects can manage aggregated objects without owning them.

# class Employee:
#     # Your implementation here

# your other class/es here...

# class Team:
#     # Your implementation here
class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Team:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print(f"{member.get_name()} is not in the team.")

# Creating instances of Employee and Student
employee1 = Employee("Anderson Moyo")
employee2 = Employee("Sicelwesihle Myeza")
student1 = Student("Sifiso Magwazi")
student2 = Student("Bongani Mkhize")

# Creating instances of Team and adding members
team1 = Team()
team1.add_member(employee1)
team1.add_member(student1)

# Removing a member from the team
team1.remove_member(employee2)  # This will print a message that employee2 is not in the team

# Adding another member
team1.add_member(student2)

# Displaying team members
for member in team1.members:
    print(member.get_name())


# Exercise 5: DRY Principle
# Objective: Reinforce the DRY principle in class methods.
# Context: You have a 'Calculator' class that has separate methods for adding two, three, and four numbers. 
#          This design repeats the addition logic, violating the DRY principle.
# Task: Refactor the 'Calculator' class to eliminate repetition. Implement a single method that can handle 
#       a variable number of arguments for addition.
# Example:
# class Calculator:
#     def add_two(self, a, b):
#         return a + b
#
#     def add_three(self, a, b, c):
#         return a + b + c
#
#     def add_four(self, a, b, c, d):
#         return a + b + c + d
#
#     # Refactor the above methods into a single method
#
#
    
#Hint: Consider using *args to allow the add method to accept a variable number of arguments.
class Calculator:
    def add(self, *args):
        return sum(args)

# Usage
calc = Calculator()

result_two = calc.add(2, 3)
result_three = calc.add(4, 5, 6)
result_four = calc.add(7, 8, 9, 10)

print(result_two)   
print(result_three) 
print(result_four)  

# ...
class Calculator:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, *args):
        # Define the subtract method implementation here
        pass
    
    def multiply(self, *args):
        # Define the multiply method implementation here
        pass

# Instantiate the Calculator class
calc = Calculator()

# Test the add method
print(calc.add(1, 2))
print(calc.add(1, 2, 3))
print(calc.add(1, 2, 3, 4))
