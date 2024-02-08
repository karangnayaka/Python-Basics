print("Welcome to Kaun Banega Crorepati")

questions = [
    ["Which language is used to create Facebook?", "Python", "JavaScript", "C++", "None", 4],
    ["Question 2?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 3?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 4?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 5?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 6?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 7?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 8?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 9?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 10?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 11?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 12?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 13?", "Option1", "Option2", "Option3", "Option4", 2],
    ["Question 14?", "Option1", "Option2", "Option3", "Option4", 3],
    ["Question 15?", "Option1", "Option2", "Option3", "Option4", 2]
    # Add more questions here if needed
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]  # Money levels for questions
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion: {question[0]}")
    print(f"Questions for Rs. {levels[i]}")
    print(f"a. {question[1]}  b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))

    if reply == question[5]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        money = levels[i]
        if(i >= 4 and i <9):
            print("you have won 10000")
        elif(i >= 9 and i<14):
            print("you have won 320000")
        elif(i == 14):
            print("you have won 10000000")
    else:
        print("Wrong answer!")
        if (i >= 4 and i < 9):
            print("you have won 10000 base set")
        elif (i >= 9 and i < 14):
            print("you have won 320000 base set")
        elif (i == 14):
            print("you have won 10000000")
        break

print(f"\nTotal money won: Rs. {money}")
