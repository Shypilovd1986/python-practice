""" module for sorting string , by alphabet """


def sort_string(some_string):
    """ function for sorting string , by alphabet , it doesn't depend on case"""
    return ' '.join(sorted(some_string.split(), key=str.casefold))


if __name__ == "__main__":
    print(sort_string('What a wonderful day today'))
