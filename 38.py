<<<<<<< HEAD
def average(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
print(average(10, 20, 30, 40))
=======
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
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
