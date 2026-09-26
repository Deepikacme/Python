import csv

f = open("students.csv", "r")

reader = csv.reader(f)
next(reader)

for row in reader:
    if int(row[3]) < 40:
        print(row)

f.close()