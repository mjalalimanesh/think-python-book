import datetime


class Point:
    """ Represents a point in 2d space """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        """ add two point objects """
        s = Point(x=self.x + other.x, y=self.y + other.y)
        return s

    def add_tuple(self, other):
        """ add a point object and a tuple """
        s = Point(x=self.x + other[0], y=self.y + other[1])
        return s


class Time:
    """ Represents the time of the day 

    attrtibutes : hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        """ Print time in HH:MM:SS format """
        print(("{:02d}:{:02d}:{:02d}").format(self.hour, self.minute, self.second))

    def time_to_seconds(self):
        """ Convert hours, minutes and seconds to total seconds """
        return self.second + self.minute * 60 + self.hour * 3600


if __name__ == "__main__":
    time = Time()
    time.hour = 2
    time.minute = 3
    time.second = 22
    time.print_time()
    point = Point(1, 2)
    print(point)
    print(time)
    print(Point(1, 1) + point)
    print((1, 1) + point)

