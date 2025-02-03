# 1) Function Basics
def hello_world():
    print("Hello, World!")

# 2) Arguments and Parameters
def sum_two_numbers(a, b):
    print(a + b)

# 3) Return Statement
def multiply_by_10(number):
    return number * 10

# 4) Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

# 5) Boss level: Nested Functions
def outer_function():
    def inner_function():
        print("This is the inner function.")
    inner_function()

# 6) Check Even or Odd
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

# 7) Find the Maximum
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 8) Positive Numbers
def get_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

# 9) Sum of Numbers Divisible by 3
def sum_divisible_by_3():
    total = 0
    for num in range(1, 101):
        if num % 3 == 0:
            total += num
    return total

# Testing all functions
hello_world()  # Hello, World!
sum_two_numbers(5, 10)  # 15
print(multiply_by_10(5))  # 50
greet("John")  # Hello, John!
outer_function()  # This is the inner function.
check_even_odd([1, 2, 3, 4, 5])  # Odd, Even, Odd, Even, Odd
print(find_max([1, 5, 3, 9, 2]))  # 9
print(get_positive_numbers([-1, 2, 3, -4, 5]))  # [2, 3, 5]
print(sum_divisible_by_3())  # Sum of numbers divisible by 3 from 1 to 100
