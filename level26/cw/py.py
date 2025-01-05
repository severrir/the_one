def manual_range(start, end, step):
    for num in range(start, end, step):
        if num % 2 == 0:
            print(num)

# Function calls with different arguments
manual_range(0, 10, 1)
manual_range(5, 20, 3)
manual_range(10, 30, 5)
manual_range(1, 15, 2)
manual_range(0, 50, 7)

