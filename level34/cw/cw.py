def remove_elements(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            del main_list[index]
    print(main_list)


def remove_one_element(main_list, index):
    if 0 <= index < len(main_list):
        del main_list[index]
    print(main_list)
