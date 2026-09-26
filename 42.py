f=open("numbers.txt", "r")
o=open("odd.txt", "w")
for line in f:
    n = int(line)
    if n % 2 != 0:
        o.write(str(n) + "\n")
f.close()
o.close()
print("Odd numbers saved")