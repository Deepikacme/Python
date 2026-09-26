class Book:
    pass
class Library:
    def __init__(self):
        self.books=[Book(),Book()]
print("Library HAS-A Books")