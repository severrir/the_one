def generate_big_sentence(name, surname, age):
    print(f"სახელი: {name}, გვარი: {surname}, ასაკი: {age}")

name = input("შეიყვანეთ სახელი: ")
surname = input("შეიყვანეთ გვარი: ")
age = input("შეიყვანეთ ასაკი: ")

generate_big_sentence(name, surname, age)


def my_split(main_string, string_to_split):
    print(main_string.split(string_to_split))

main_string = input("შეიყვანეთ მთავარი სტრინგი: ")
string_to_split = input("შეიყვანეთ დასაყოფი სტრინგი: ")

my_split(main_string, string_to_split)


def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

my_list = [1, 2, 3, 4]
manual_append(my_list, 5)
print(my_list)
