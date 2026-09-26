f = open("students.txt", "r")

highest = 0
student = ""

for line in f:
    data = line.strip().split(",")
    marks = int(data[3])

    if marks > highest:
        highest = marks
        student = data[1]

print("Topper:", student)
print("Marks:", highest)

f.close()
