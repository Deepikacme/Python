f = open("data.txt", "r")

data = f.read()
count = data.count(" ")

print("Spaces:", count)

f.close()