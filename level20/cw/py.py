# Get input from the user
age = int(input("Enter your age: "))

# Use if-elif-else statement to determine the age group
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")