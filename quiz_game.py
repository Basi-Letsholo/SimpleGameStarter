#!/usr/bin/python3

questions = ("What is the name of the train that takes students to Hogwarts?",
             "What is the name of Harry Potter's pet owl?",
             "Which house at Hogwarts does Harry Potter belong to?",
             "What is the name of the potion that grants good luck to the drinker?",
             "Which magical object allows its user to turn back time?")

options = (("A. Hogwarts Train", "B. Hogwarts Express", "C. Gravy Train", "D. The Magic School Train"), 
           ("A. Buckbeak", "B. Scabbers", "C. Padfoot", "D. Hedwig"), 
           ("A. Gryffindor", "B. Slytherin", "C. Hufflepuff", "D. Ravenclaw"), 
           ("A. Fortuna Liquida", "B. Felix Potio", "C. Felix Felicis", "D. Buona Fortuna"),
           ("A. Time Machine", "B. Time Cloak", "C. Time Turner", "D. Hands of Time")
           )

answers = ("B", "D", "A", "C", "C")
guesses = []
score = 0
q_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[q_num]:
        print(option)

    guess = str(input("Enter: (A, B, C, D): ")).upper()
    guesses.append(guess)
    if guess == answers[q_num]:
        score += 1
        print("CORRECT")
    else:
        print("Incorrect")
        print(f"{answers[q_num]} is the correct answer")

    q_num += 1

print(f"Score: {score}/{len(questions)}")

if (score / len(questions) * 100) < 40:
    print("Good Try!")
elif (score / len(questions) * 100) > 90:
    print("Amazing! You must be Hermione.")
else:
    print("Well Done!")
