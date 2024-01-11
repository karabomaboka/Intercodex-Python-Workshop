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
# Hint: Consider using *args to allow the add method to accept a variable number of arguments.

class Calculator:

    def add(self, *args):
        return sum(args)


calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.add(1, 2, 3))
print(calculator.add(1, 2, 3, 4))