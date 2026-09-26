import json

questions = [
    {"question": "What is Python?", "answer": "Programming Language"},
    {"question": "What is HTML?", "answer": "Markup Language"}
]

f = open("quiz.json", "w")
json.dump(questions, f, indent=4)
f.close()

score = 0

for q in questions:
    print(q["question"])
    answer = input("Answer: ")

    if answer.lower() == q["answer"].lower():
        score += 1

print("Score:", score)