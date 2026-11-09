

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 5?",
        "options": ["A. 8", "B. 10", "C. 12", "D. 15"],
        "answer": "B"
    }
]

score = 0


def display_question(questions):
    global score
    
    for index , i in enumerate(questions, start=1):
        print("Question", index, "of" , len(questions))
        print(i["question"])

        for option in i["options"]:
            print(option)

        while True:
            user_answer = input("Enter your answer: ").strip().lower()
            if user_answer in ["a", "b", "c", "d"]:
                break
            else:
                print("Invalid answer. Try again")

        if user_answer == i["answer"].lower():
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")

        




display_question(questions)


total_questions = len(questions)
percentage = (score / total_questions) * 100

print("Final Score:" , score , "/", total_questions)
print("Percentage:", percentage , "%")



if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
