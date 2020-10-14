
####################  7_1  ####################

import math


def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root():
    print('a' + ' '*8 + 'mysqrt(a)' + ' '*16 +
          'math.sqrt(a)' + ' '*16 + 'diff/n')
    print('-' + ' '*8 + '---------' + ' '*16 +
          '------------' + ' '*16 + '-------')
    for i in range(9):
        num = float(i+1)
        print(num, ' '*5, mysqrt(num), ' '*8, math.sqrt(num),
              ' '*8, abs(math.sqrt(num)-mysqrt(num)), '\n')


#a = mysqrt(36)
# test_square_root()

####################  7_2  ####################

def eval_loop():
    while True:
        inp = input('Type to Evaluate \n')
        if inp == 'done':
            return 'Done!'
        print(eval(inp))

# eval_loop()

####################  7_3  ####################


def estimate_pi():
    my_pi = 0
    while True:
        term = 1  # need edit
        if term < 1e-15:
            return my_pi
        my_pi = my_pi + term
