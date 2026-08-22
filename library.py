from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def item_type(self):
        pass

    def display(self):
        print("Title:", self.title)


class Book(LibraryItem):
    def item_type(self):
        print("Item Type: Book")


class Magazine(LibraryItem):
    def item_type(self):
        print("Item Type: Magazine")


class DVD(LibraryItem):
    def item_type(self):
        print("Item Type: DVD")


items = [
    Book("Python Programming"),
    Magazine("Technology Today"),
    DVD("Python Tutorial")
]

for item in items:
    item.item_type()
    item.display()
    print()