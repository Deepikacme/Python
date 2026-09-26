f = open("data.txt", "w")
lines = ["Apple\n", "Banana\n", "Mango\n"]
f.writelines(lines)
f.close()
print("Lines written")