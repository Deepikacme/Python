def student_info(*marks, **details):
    print("Student Details:")
    for key, value in details.items():
        print(key, ":", value)
    print("Marks:", marks)
student_info(80, 90, 85, name="Deepika", course="Python")