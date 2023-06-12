import os


def show_list_of_directory(name_directory):
    return os.walk(name_directory)


if __name__ == '__main__':
    g = show_list_of_directory('/Users/dmitriyshypilov/PycharmProjects/python-practice/level_up_python')
    print(g)
    print(type(g))
    for x, y, z in g:
        print(x, y, z)
        print()
