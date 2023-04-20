""" module runs function with some delay"""

import time


def schedule_function(delay, function, *args):
    """ function work like module sched """
    time.sleep(delay)
    function(args)
    print(f"function {function.__name__} was executed with {delay} seconds delay")
    current_time = time.asctime(time.localtime())
    print(f"current time {current_time}")


if __name__ == "__main__":
    schedule_function(5, print, "some text")
