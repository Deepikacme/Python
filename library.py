class Book:
    def show(self):
        print("Book")
class Library:
    def __init__(self):
        self.books = [Book(), Book()]
l = Library()
for b in l.books:
    b.show()