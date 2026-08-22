text = "Order123Amount5000" 
numbers = "" 
for character in text: 
    if character.isdigit(): numbers += character 
    print(numbers)