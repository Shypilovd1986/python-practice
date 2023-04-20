""" module with function for saving dictionary and others in python """

import pickle


def save_dictionary(my_dictionary, path):
    """function for saving """
    with open(path, "wb") as file:
        pickle.dump(my_dictionary, file)


def load_dictionary(path):
    """function for loading """
    with open(path, "rb") as file:
        return pickle.load(file)


if __name__ == "__main__":
    a = {'one': 1, 'two': "two"}
    save_dictionary(a, "/Users/dmitriyshypilov/PycharmProjects/python-practice/level_up_python/test_file.txt")
    print(load_dictionary("/Users/dmitriyshypilov/PycharmProjects/python-practice/level_up_python/test_file.txt"))
