def word_frequency(sentence):
    result={}
    words=sentence.split()
    for word in words:
        if word in result:
            result[word]+=1
        else:
            result[word]=1
    return result
sentence="python is easy python is useful"
print(word_frequency(sentence))