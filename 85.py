import json

f = open("students.json", "r")
students = json.load(f)
f.close()

students.pop(0)

f = open("students.json", "w")
json.dump(students, f, indent=4)
f.close()

print("Student deleted")