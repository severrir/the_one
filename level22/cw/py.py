my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = int(input("Enter an index: "))

if 0 <= index < len(my_list):
    print(my_list[index])
elif -len(my_list) <= index <= -1:
    print(my_list[index])
else:
    print("Index is out of range.")

