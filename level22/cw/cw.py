items = ["ნული", "ერთი", "ორი", "სამი", "ოთხი", "ხუთი", "ექვსი", "შვიდი", "რვა", "ცხრა"]

try:
    index = int(input("შეიტანეთ რიცხვი: "))
    if 0 <= index < len(items):
        print(items[index])
    elif -len(items) <= index <= -1:
        print(items[index])
    else:
        print("არასწორი ინდექსი!")
except ValueError:
    print("გთხოვთ, შეიყვანოთ მხოლოდ მთელი რიცხვი!")
