import csv

try:
    f = open("students.csv", "r")
    reader = csv.reader(f)

    for row in reader:
        print(row)

    f.close()

except FileNotFoundError:
    print("CSV file not found")
except Exception:
    print("Error while reading CSV file")