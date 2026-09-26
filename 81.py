import json

student = {
    "name": "Deepika",
    "age": 20,
    "course": "CME",
    "marks": 85
}

f = open("student.json", "w")
json.dump(student, f)
f.close()

print("JSON file created")