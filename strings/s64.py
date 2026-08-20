text = input("Enter sentence: ") 
count = 0
for character in text: 
    if character == " ": count += 1 
    print("Space Count:", count)