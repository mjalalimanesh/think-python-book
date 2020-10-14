"""
Created on Thu Feb 27 11:29:53 2020

@author: Mohamad Jalali Manesh
"""

import turtle

bob = turtle.Turtle()

#print(bob)

def polyline(t, n, length, angle):
    for i in range(round(n)):
        t.fd(length)
        t.lt(angle)


def polygen(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)
    
def circle(t, r):
    arc(t, r , 360)

    
def arc(t, r, angle):
    c = 2 * 3.1416 * r * (angle/360)
    n = (c / 3) + 1
    step_angle = angle/n
    step_length = c / n
    polyline(t, n, step_length, step_angle)

arc(bob, 50, 270)

#turtle.mainloop()

