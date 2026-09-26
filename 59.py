f = open("numbers.txt", "r")

numbers = [int(line) for line in f]
duplicates = []

for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print("Duplicate numbers:", duplicates)
f.close()