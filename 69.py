f = open("students.txt", "r")

total = 0
count = 0

for line in f:
    data = line.strip().split(",")
    total += int(data[3])
    count += 1

average = total / count

print("Average marks:", average)

f.close()