weight = float(input("გთხოვთ, ჩაწერეთ თქვენი წონა (კილოგრამებში): "))
height = float(input("გთხოვთ, ჩაწერეთ თქვენი სიმაღლე (მეტრებში): "))

bmi = weight / height ** 2

print("თქვენი BMI არის:", round(bmi, 2))
