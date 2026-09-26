import csv

f = open("employees.csv", "w", newline="")

writer = csv.writer(f)

writer.writerow(["ID", "Name", "Salary"])
writer.writerow([1, "Ravi", 30000])
writer.writerow([2, "Priya", 40000])

f.close()

print("Employee records saved")