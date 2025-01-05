def greet_user():
    print("Hello! Welcome to this Python program.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    print("Here's a quick math question for you.")

def math_question():
    answer = int(input("What is 5 + 3? "))
    if answer == 8:
        print("Correct! You're good at math!")
    else:
        print("Oops! The correct answer is 8.")

# Run the program
greet_user()
math_question()

print("Thanks for trying this program. Goodbye!")
