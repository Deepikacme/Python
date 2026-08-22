text = input("Enter text: ") 
count = 0 
for character in text: 
    if character.isdigit(): 
      count+=1
print("digit count:",count)             