f = open("numbers.txt", "r")

numbers = [int(line) for line in f]
f.close()

numbers.sort()

f = open("sorted.txt", "w")

for n in numbers:
    f.write(str(n) + "\n")
f.close()
print("Numbers sorted successfully")