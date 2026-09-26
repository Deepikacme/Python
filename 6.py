f = open("sample.txt", "r")

data = f.read()
for ch in data:
    print(ch)
f.close()