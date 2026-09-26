f = open("data.txt", "r")

data = f.read()
count = 0

for ch in data:
    if ch.isdigit():
        count += 1

print("Digits:", count)

f.close()