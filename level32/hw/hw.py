def format_vs_fstring():
    return ("format() ფუნქცია იყენებს .format() მეთოდს სტრინგში ცვლადების ჩასასმელად, "
            "მაგალითად: 'Hello, {}'.format(name). "
            "f-string იყენებს f-პრეფიქსს და ცვლადებს პირდაპირ სტრინგში, მაგალითად: f'Hello, {name}'. "
            "f-string უფრო სწრაფი და კითხვისთვის მარტივია.")

def append_vs_insert():
    return ("append() ამატებს ელემენტს სიაში ბოლოში. "
            "insert() საშუალებას გვაძლევს ელემენტი ჩავამატოთ კონკრეტულ ინდექსზე.")

def welcome_message(name, age):
    return f"Welcome, {name}! You are {age} years old."

def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

def reverse_string(sentence):
    return f"The reversed string is: {sentence[::-1]}"

def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return " ".join(words)

def sentence_to_words(sentence):
    return sentence.split()

def csv_to_list(csv_string):
    return csv_string.split(",")

def paragraph_to_sentences(paragraph):
    return paragraph.split(".")

def append_to_list(lst, item):
    lst.append(item)

def append_items_to_list(lst, items):
    for item in items:
        lst.append(item)

def merge_lists(list1, list2):
    list1.extend(list2)

def insert_into_list(lst, index, item):
    lst.insert(index, item)

def insert_at_beginning(lst, item):
    lst.insert(0, item)

def insert_at_end(lst, item):
    lst.insert(len(lst), item)
