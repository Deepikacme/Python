f = open("data.txt", "r")

data = f.read()
count = 0

for ch in data:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants:", count)

f.close()