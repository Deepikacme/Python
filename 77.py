import csv

f = open("students.csv", "r")

reader = csv.reader(f)
next(reader)

topper = ""
highest = 0

for row in reader:
    marks = int(row[3])

    if marks > highest:
        highest = marks
        topper = row[1]

print("Topper:", topper)
print("Marks:", highest)

f.close()