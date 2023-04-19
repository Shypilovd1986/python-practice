"""
 waiting game is a single function python module where after inputting, function choose random number and with delay \n
 offer user input again
  """

from random import randint
from time import sleep


def waiting_game():
    """ function with delay"""
    stop_word = input("Input word for stopping game  ")
    start = randint(2, 4)
    print(f"Your target time is {start} seconds")
    input("--Press Enter to Begin--  ")
    while start != stop_word:
        target_time = randint(2, 4)
        sleep(target_time)
        print(f"...Press enter again after {target_time} seconds... ")
        start = input()
    print("Game over. Good Luck")


if __name__ == "__main__":
    waiting_game()
