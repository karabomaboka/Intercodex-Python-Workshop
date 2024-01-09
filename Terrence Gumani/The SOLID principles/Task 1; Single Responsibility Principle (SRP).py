class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        
class BookInventoryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_availability(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_borrowed:
                return True
        return False        
class MemberNotifier:
    def notify_member(self, member_name, book_title):
        print(f"Dear {member_name}, the book '{book_title}',is now available for borrowing.")

if __name__ == "__main__":
    # Initialize instances
    inventory_manager = BookInventoryManager()
    notifier = MemberNotifier()

    # Initialize objects
    book1 = Book("Bible", "God", "978-3-16-148410-0")
    book2 = Book("Extreme Ownership", "H. Lee", "978-0-06-112008-4")
    
    inventory_manager.add_book(book1)
    inventory_manager.add_book(book2)

    # Check book availability and notify members
    member_name = "Themba"
    book_title = "Bible"

    if inventory_manager.check_availability(book_title):
        notifier.notify_member(member_name, book_title)
    else:
        print(f"Sorry, '{book_title}' is not available at the moment.")
