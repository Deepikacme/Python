<<<<<<< HEAD
def student_info(*marks, **details):
    print("Student Details:")
    for key, value in details.items():
        print(key, ":", value)
    print("Marks:", marks)
student_info(80, 90, 85, name="Deepika", course="Python")
=======
products = [
    ("Pen", 10, 5),
    ("Book", 50, 2)
]
for product in products:
    total=product[1] * product[2]
    print(product[0], total)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
