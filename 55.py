f = open("numbers.txt","r")
even = open("even.txt","w")
odd = open("odd.txt","w")
for line in f:
    n = int(line)
    if n % 2 == 0:
        even.write(str(n) + "\n")
    else:
        odd.write(str(n) + "\n")
f.close()
even.close()
odd.close()
print("Numbers separated")