
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return 
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return 
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.file_size = PrintBook
    
    def __str__(self):
        return
    
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books = (book) 

    def list_books(self):

        for book in self.books:
            print(book)       



