import json

books = [
    {"id": 1, "name": "Python", "author": "John"},
    {"id": 2, "name": "Java", "author": "James"}
]

f = open("books.json", "w")
json.dump(books, f, indent=4)
f.close()

print("Books saved successfully")