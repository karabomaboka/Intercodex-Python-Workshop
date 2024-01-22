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

#     def add_three(self, a, b, c):
#         return a + b + c

#     def add_four(self, a, b, c, d):
#         return a + b + c + d

#     # Refactor the above methods into a single method

# Hint: Consider using *args to allow the add method to accept a variable number of arguments.

class Calculator:
    def add(self, *args):
        return sum(args)

# Creating an instance of the Calculator class
my_calculator = Calculator()

# Testing the add method with different numbers of arguments
result_two_numbers = my_calculator.add(5, 10)
result_three_numbers = my_calculator.add(3, 7, 11)
result_four_numbers = my_calculator.add(2, 4, 6, 8)

# Displaying the results
print(f"Result for two numbers: {result_two_numbers}")
print(f"Result for three numbers: {result_three_numbers}")
print(f"Result for four numbers: {result_four_numbers}")


