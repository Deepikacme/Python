f = open("numbers.txt", "r")
cube = open("cubes.txt", "w")

for line in f:
    n = int(line)
    cube.write(str(n * n * n) + "\n")
f.close()
cube.close()
print("Cubes saved")