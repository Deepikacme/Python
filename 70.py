f = open("students.txt", "r")

for line in f:
    data = line.strip().split(",")

    if int(data[3]) > 75:
        print(data[1], data[3])

f.close()