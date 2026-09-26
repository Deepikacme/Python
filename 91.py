import json

student = {
    "name": "Deepika",
    "course": "CME",
    "marks": 85
}

f = open("student.json", "w")

json.dump(student, f, indent=4)

f.close()

print("Dictionary converted to JSON")
