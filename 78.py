import csv

f = open("students.csv", "r")

reader = csv.reader(f)
next(reader)

total = 0
count = 0

for row in reader:
    total += int(row[3])
    count += 1

print("Average:", total / count)

f.close()