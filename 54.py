def topper(marks):
    return max(marks,key=marks.get)
students={
    "deepika":85,
    "manasa":92,
    "vijju":88
}
print(topper(students))
