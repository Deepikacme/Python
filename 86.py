import json

employees = [
    {"name": "Ravi", "salary": 30000},
    {"name": "Priya", "salary": 40000},
    {"name": "Anjali", "salary": 35000}
]

f = open("employees.json", "w")
json.dump(employees, f, indent=4)
f.close()

print("Employee file created")