f = open("data.txt", "r")
lines = f.readlines()
f.close()

unique = []

for line in lines:
    if line not in unique:
        unique.append(line)

f = open("newdata.txt", "w")
f.writelines(unique)
f.close()

print("Duplicate lines removed")