class Book: 
 def __init__ (self, title, author, year):
    self.title = title
    self.author = author 
    self.year = year
  
 def __del__(self):
  print()

 def __str__(self):
    return
  
 def __repr__(self):
    return
  
if __name__ == "__main__":
  book = Book
  print(book)
  print(repr(book))
  del book 
