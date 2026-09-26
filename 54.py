f = open("numbers.txt", "r")
numbers = []
for line in f:
    numbers.append(int(line))
print("Smallest:", min(numbers))
f.close()