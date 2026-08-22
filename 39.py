students = [
    ["Deepika", 80, 70, 90],
    ["Priya", 70, 60, 80]
]
for student in students:
    total = student[1] + student[2] + student[3]
    average = total / 3
print(student[0], total, average)