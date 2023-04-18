""" module for checking , if word is palindrome """
from string import ascii_letters


def check_palindrome(word):
    """ function for checking word for palindrome """
    sample = []
    lower_word = word.lower()
    for i in lower_word:
        if i in ascii_letters:
            sample.append(i)
    return bool(sample[:] == sample[::-1])
