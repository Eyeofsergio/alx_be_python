class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False 

    # Check Out
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    # Return Book
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    # Availablity

    def is_available(self):
        return not self._is_checked_out
    
    #Library Class

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books = ()

    #check out book
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"check out; {title}")
                else:
                    print(f"The book '{title}' is already out.")
                return
            print(f"the book '{title}' is already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Retured: {title}")
                else:
                    print(f"The book '{title}' was not checked out")

    def list_available_books(self):
        available_books = {book for book in self._books if book.is_availabe()}
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
            else:
                print("No available books.")