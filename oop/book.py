class book: 
 def __init__ (self, title, author, year):
    self.title = title
    self.author = author 
    self.year = year

def __del__(self):
  print(f"Deleting '{self.title}'")

  def __Str__(self):
    return(f"{self.title} by {self.author} in {self.year}")
  
  def __repr__(self):
    return f"Book('{self.title}', '{self.author}', '{self.year}')"
  