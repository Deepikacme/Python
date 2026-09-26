f = open("data.txt", "r")
lines = f.readlines()
f.close()
f = open("reverse.txt", "w")
for line in lines:
    f.write(line.strip()[::-1] + "\n")
f.close()
print("Lines reversed")