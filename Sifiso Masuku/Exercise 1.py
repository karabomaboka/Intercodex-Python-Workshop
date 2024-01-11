# Exercise 1: Basic Class Creation
# Objective: Create a simple class with attributes and methods.
# Task: Define a 'Book' class with attributes 'title', 'author', and 'publication_year'. 
#       Include a method 'get_info()' that returns a string with all these details.
# Expected Output: Create instances of 'Book' and use 'get_info()' to display its attributes.

class Book:

    def __init__(self, title, author, publication_year):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year

    def get_info(self):
        return f"{self.__title} by {self.__author} was published in {self.__publication_year}."


book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)


print(book.get_info())


