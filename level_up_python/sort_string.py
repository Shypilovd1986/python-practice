""" module for sorting string , by alphabet """


def sort_string(some_string):
    """ function for sorting string , by alphabet , it doesn't depend on case"""
    return ' '.join(sorted(some_string.split(), key=str.casefold))
