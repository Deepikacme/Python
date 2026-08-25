def greater_than_50(data):
    result = []

    for key, value in data.items():
        if value > 50:
            result.append(key)

    return result


marks = {
    "Maths": 75,
    "English": 45,
    "Python": 80,
    "Science": 40
}

print(greater_than_50(marks))