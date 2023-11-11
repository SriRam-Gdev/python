score = 0 
total_questions = 3 


print("Welcome to the quiz game!")
answer = input("Question 1: What is the capital of India? ")


if answer.lower() == "new delhi":
    score += 1
    print("Correct!")
else:
    print("Wrong answer :(")


answer = input("Question 2: What is the largest animal in the world? ")


if answer.lower() == "blue whale":
    score += 1
    print("Correct!")
else:
    print("Wrong answer :(")


answer = input("Question 3: Who is the author of Harry Potter? ")


if answer.lower() == "j.k. rowling":
    score += 1
    print("Correct!")
else:
    print("Wrong answer :(")


print(f"Thank you for playing the quiz game, you answered {score} questions correctly!")
mark = (score / total_questions) * 100
print(f"Marks obtained: {mark}")
print("Bye!")
