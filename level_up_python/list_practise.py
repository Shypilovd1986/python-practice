""" making some list """
__version__ = '0.1'

def make_list(*args):
    """ like 'list' function """
    empty_list = []
    for i in args:
        empty_list.append(i)
    return empty_list


test_list = ['one', 'two', 'tree', 4, 5, 6, 7, 'eight']


def pop_elements(our_list: list, quantity_pop_elements: int):
    """pop last element n times"""
    for i in range(quantity_pop_elements):
        our_list.pop()
    return our_list


if __name__ == "__main__":
    print(make_list('one', 2, [1, 2, 3]))
    print(pop_elements(test_list, 3))
