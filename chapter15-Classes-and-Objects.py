"""
Created on Sun Oct 25 17:38:52 2020
@author: mohamad jalalimanesh
"""
import numpy as np
import copy


class Point:
    """ Represents a point in 2d space """


class Rectangle:
    """
    Represents a rectangle
    
    attributes: width, height, corner
    """


class Circle:
    """
    Represents a circle
    
    attributes: center, radius
    """


def distance_between_pints(p1, p2):
    """ Find Distance between two Point Object """
    dist = np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    return dist


def move_rectangle(rect, dx, dy):
    """ move rect object corner by dx, dy """
    rect_copy = copy.deepcopy(rect)
    rect_copy.corner.x = rect.corner.x + dx
    rect_copy.corner.y = rect.corner.y + dy
    return rect_copy


def print_point(p):
    print("({}, {})".format(p.x, p.y))


def point_in_circle(circle_obj, point_obj):
    dist = distance_between_pints(circle_obj.center, point_obj)
    return dist < circle_obj.radius


def rect_in_circle(circle_obj, rect_obj):
    # Find 4 corners and check them
    return


if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    p1.x = 0
    p2.x = 1
    p1.y = 0
    p2.y = 1
    print("dist between points : {:0.3}".format(distance_between_pints(p1, p2)))
    box = Rectangle()
    box.width = 2.0
    box.height = 3.0
    box.corner = Point()
    box.corner.x = 1.0
    box.corner.y = 1.0
    new_box = move_rectangle(box, dx=1.0, dy=1.0)
    print("new box corner point : ", end="")
    print_point(new_box.corner)
    circle = Circle()
    circle.radius = 75.0
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    print("Exercise 15-1 :")
    print("point_in_circle : ", point_in_circle(circle, p1))
