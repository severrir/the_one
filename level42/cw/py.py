# Dictionary მონაცემებით
student_info = {
    "name": "საბა",
    "surname": "ვაშაძე",
    "academy": "პროგრამირების აკადემია",
    "fav-color": "ცისფერი",
    "city": "რუსთავი",
    "goa-student": True,  # იმ შემთხვევაში თუ სწავლობს, გამოსაყენებელია True/False
    "age": 13,
    "fav-programming-lang": "Python"
}

# თითოეული მნიშვნელობის დაბეჭდვა
print("სახელი:", student_info["name"])
print("გვარი:", student_info["surname"])
print("აკადემია:", student_info["academy"])
print("საყვარელი ფერი:", student_info["fav-color"])
print("ქალაქი:", student_info["city"])
print("GOA სტუდენტი:", student_info["goa-student"])
print("ასაკი:", student_info["age"])
print("საყვარელი პროგრამირების ენა:", student_info["fav-programming-lang"])
