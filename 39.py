f = open("data.txt", "r")

for line in f:
    if "Python" in line:
        print(line.strip())

f.close()