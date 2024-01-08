# Exercise 4: Aggregation
# Objective: Understand and apply aggregation.
# Task: Create a 'Team' class and an 'Employee' class. Create an additional class that can also be aggregated by the Team class. 
# Then create one or more instances of the Team class, each with a list of the objects it aggregates (team of employees, team of students etc.)
#       Implement methods to add or remove an 'Employee' (or 'Student') from a 'Team'.
# Expected Output: Illustrate how 'Team' objects can manage aggregated objects without owning them.

class Team:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def __str__(self):
        return f"Employee: {self.__name}, Age: {self.__age}, Salary: {self.__salary}"

class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def __str__(self):
        return f"Student: {self.__name}, Age: {self.__age}, Grade: {self.__grade}"

team = Team()
team.add_member(Employee("Thenjiwe", 30, 100000))
team.add_member(Employee("Gontse", 25, 50000))
team.add_member(Student("Kgothatso", 18, 10))

for member in team.members:
    print(member)

team.remove_member(team.members[0])

for member in team.members:
    print(member)