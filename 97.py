import json

try:
    f = open("student.json", "r")
    data = json.load(f)
    print(data)
    f.close()

except json.JSONDecodeError:
    print("Invalid JSON data")