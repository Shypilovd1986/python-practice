"""Module allow to input text and output it in terminal with chosen color"""
# we must install module termcolor first
from termcolor import colored


def choose_color():
    """main function of module"""
    possible_color = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    our_text = input('Input your text \n')
    chosen_color = input('Which color do you want?\n')
    while chosen_color not in possible_color:
        print('You choose wrong color, pick another one! \
        Possible colors are red, yellow, green, cyan, blue, magenta')
        chosen_color = input('Which color do you want?\n')
    print(colored(our_text, chosen_color))


if __name__ == '__main__':
    choose_color()
