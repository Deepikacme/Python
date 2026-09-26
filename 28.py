f = open("data.txt", "r")
f.seek(5)
print(f.read())
f.close()