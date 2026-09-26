f = open("data.txt","r")
lines = f.readlines()
f.close()
f = open("reverse.txt","w")
for line in reversed(lines):
    f.write(line)
f.close()
print("File reversed")