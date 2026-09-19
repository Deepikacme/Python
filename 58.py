def character_frequency(text):
    result={}
    for ch in text:
        if ch in result:
          result[ch]=1
        else:
           result[ch]=1
    return result     
text="hello"
print(character_frequency(text)) 