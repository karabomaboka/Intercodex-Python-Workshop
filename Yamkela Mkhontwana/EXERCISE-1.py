# Exercise 1: Basic Class Creation
# Objective: Create a simple class with attributes and methods.
#  Task: Define a 'Book' class with attributes 'title', 'author', and 'publication_year'. 
#       Include a method 'get_info()' that returns a string with all these details.
# Expected Output: Create instances of 'Book' and use 'get_info()' to display its attributes.

# class Book:
#     # Your implementation here
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_info(self):
        return f'Title: {self.title}, Author: {self.author}, Publication year {self.publication_year}'
    
book1 = Book("SOAR", "T.D. JAKES" , 2009)
book2 = Book("A REVELATION OF THE DIVINE LIFE", "JOSHUA SELMAN" , 2018)

print(book1.get_info())
print(book2.get_info())