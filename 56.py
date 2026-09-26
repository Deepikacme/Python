f = open("numbers.txt", "r")
sq = open("squares.txt", "w")

for line in f:
    n = int(line)
    sq.write(str(n * n) + "\n")
f.close()
sq.close()
print("Squares saved")