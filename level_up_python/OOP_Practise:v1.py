""" module which works with geometric figures """


class Point:
    """ class of points , which consists of x, y cord"""
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y

    def __repr__(self):
        return '<Cords object at 0x105231790>'

    def __str__(self):
        return f'<Current point has cords x: {self.cord_x}, y: {self.cord_y} >'


if __name__ == '__main__':
    point = Point(3, 8)
    print(point)
    print(point.cord_x)
    print(point.cord_y)
    print(type(point))
