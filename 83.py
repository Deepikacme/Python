import json

f = open("students.json", "r")
students = json.load(f)
f.close()

new_student = {
    "name": "Priya",
    "age": 21,
    "course": "CSE",
    "marks": 80
}

students.append(new_student)

f = open("students.json", "w")
json.dump(students, f, indent=4)
f.close()

print("Student added")