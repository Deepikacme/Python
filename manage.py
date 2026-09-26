class Item:
    pass

class Book(Item):
    pass

class SearchService:
    def search(self):
        print("Book searched")

class Library:
    def __init__(self):
        self.books = [Book()]

    def search(self, service):
        service.search()

Library().search(SearchService())