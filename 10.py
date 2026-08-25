def is_positive(number):
    if number>0:
        return"Positive"
    elif number <0:
        return"Negative"
    else:
        return "Zero"
result=is_positive(-5)
print(result)