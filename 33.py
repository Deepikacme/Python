f = open("data.txt", "r")
data = f.read()
print("Total characters:", len(data))
f.close()