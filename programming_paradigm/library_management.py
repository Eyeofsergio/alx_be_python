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
    
    # Avaliablity

    def is_avaliable(self):
        return not self._is_checked_out
    
    #Library Class

class Library:
    def __init__(self):
        self._books =[]

    def add_book(self, Book):
        self._books.append(Book)

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

    def list_avaliable_books(self):
        avaliable_books = {book for book in self._books if book.is_avaliabe()}
        if avaliable_books:
            for book in avaliable_books:
                print(f"{book.title} by {book.author}")
            else:
                print("No avaliable books.")