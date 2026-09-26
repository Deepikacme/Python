import csv

f = open("contacts.csv", "w", newline="")

writer = csv.writer(f)

writer.writerow(["Name", "Phone"])
writer.writerow(["Deepika", "9876543210"])
writer.writerow(["Priya", "9876501234"])

f.close()

print("Contacts saved")