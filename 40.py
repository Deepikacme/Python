f = open("data.txt", "r")

for line in f:
    if line.startswith("P"):
        print(line.strip())

f.close()