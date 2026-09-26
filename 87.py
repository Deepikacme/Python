import json

f = open("employees.json", "r")
employees = json.load(f)
f.close()

highest = max(employees, key=lambda x: x["salary"])

print("Employee:", highest["name"])
print("Salary:", highest["salary"])