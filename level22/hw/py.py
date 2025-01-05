my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(my_list[num2:num1])
elif num2 > num1:
    print(my_list[num1:num2])
else:
    print([])

