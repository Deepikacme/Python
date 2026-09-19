class SearchService:
    def search(self):
        print("Book found")
class Library:
    def find_book(self, service):
        service.search()
Library().find_book(SearchService())