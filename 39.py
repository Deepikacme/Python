<<<<<<< HEAD
def profile(**person):
    for key, value in person.items():
        print(key, ":", value)
profile(name="Deepika", age=20, city="Rajahmundry")
=======
students = [
    ["Deepika", 80, 70, 90],
    ["Priya", 70, 60, 80]
]
for student in students:
    total = student[1] + student[2] + student[3]
    average = total / 3
print(student[0], total, average)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
