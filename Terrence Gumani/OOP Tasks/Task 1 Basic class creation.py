class Book:
    def __init__(self, title:str, authour:str, publication_year:int):
        self._title = title
        self._authour = authour
        self._publication_year = publication_year
        
    def get_title(self) -> str:
        return self._title    
    def get_authour(self) -> str:
        return self._authour
    def get_publication_year(self) ->int:
        return self._publication_year
     
    def __str__(self) -> str:
        return f"Title: {self._title}, Author: {self._authour}, Publication Year: {self._publication_year}" 

book1 = Book('Harry Potter', 'JK rowling', 2003)
book2 = Book('Black Swan', 'Nassim Taleb', 2013)
book3 = Book('Grit', 'Angela Duckworth', 2018)

print(book1)
print(book2)
print(book3)
