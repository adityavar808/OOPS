class Book():
    def __init__(self, title , author, pyear):
        self.title = title
        self.author = author
        self.year = pyear
    
    def __str__(self):
        return f" The Book {self.title} is published in {self.year} and written by {self.author}."

class Ebook(Book):
    def __init__(self, size, name , author, year):
        self.size = size
        super().__init__(name, author, year)

    def __str__(self):
        return f" The Book {self.title} is published in {self.year} and written by {self.author}."

b1 = Book("100 dreams", "ALOK SHARMA", 2009)
b1.__str__()
print(b1)

eb1 = Ebook("1000000 jhoot", "ALOK SHARMA", 2005, "500 MB")
print(eb1)