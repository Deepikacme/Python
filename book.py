class Book:
    pass

class SearchService:
    def search(self):
        print("Book searched")
class Library:
    def __init__(self):
        self.books = [Book(), Book()]
    def search_book(self, service):
        service.search()
l = Library()
l.search_book(SearchService())