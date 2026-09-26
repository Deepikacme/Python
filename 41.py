f = open("numbers.txt", "r")
e = open("even.txt", "w")

for line in f:
    n=int(line)
    if n%2==0:
        e.write(str(n)+"\n")
f.close()
e.close()
print("Even numbers saved")