# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:30:15 2020

@author: Mohamad Jalali Manesh
"""

def print_spam(value):
    print(value)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_twice(print_spam, value):
    print_spam(value)
    print_spam(value)

def do_four(func, value):
    do_twice(func,value)
    do_twice(func, value)


do_four(print_twice, 2)

print('+', '-') 
print('+', end=' ')
print('-')

print('+', '- '*4+ '+', '- '*4+ '+' )
do_twice(print_twice, '|         '*2+ '|')
print('+', '- '*4+ '+', '- '*4+ '+' )
do_twice(print_twice, '|         '*2+ '|')
print('+', '- '*4+ '+', '- '*4+ '+' )

