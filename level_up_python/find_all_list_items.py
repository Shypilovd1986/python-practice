""" module for finding indexes of items in lists """


def find_index(search_list, item):
    """ function for finding indexes of items"""
    list_of_indexes = []
    for index, value in enumerate(search_list):
        if value == item:
            list_of_indexes.append([index])
        elif isinstance(search_list[index], list):
            for i in find_index(search_list[index], item):
                list_of_indexes.append([index]+i)
    return list_of_indexes


if __name__ == "__main__":
    print(find_index([2, 3, 65, [2, 1, 4, [3, 2, 1]], 3, [22, 3, 1]], 3))
