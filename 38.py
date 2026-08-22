employees = [
    ("Ravi", "Manager", 50000),
    ("Priya", "Developer", 60000),
    ("Rahul", "Tester", 40000)
]
highest = employees[0]
for employee in employees:
    if employee[2] > highest[2]:
        highest = employee
print(highest)