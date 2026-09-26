import json

f = open("students.json", "r")
students = json.load(f)
f.close()

students[0]["marks"] = 90

f = open("students.json", "w")
json.dump(students, f, indent=4)
f.close()

print("Student information updated")