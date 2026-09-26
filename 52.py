f = open("numbers.txt", "r")
numbers = []
for line in f:
    numbers.append(int(line))
average = sum(numbers) / len(numbers)
print("Average:", average)
f.close()