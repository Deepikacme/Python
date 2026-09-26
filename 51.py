f = open("numbers.txt", "w")

for i in range(1, 21):
    f.write(str(i) + "\n")

f.close()
f = open("numbers.txt", "r")
total = 0
for line in f:
    total += int(line)
print("Total:", total)
f.close()