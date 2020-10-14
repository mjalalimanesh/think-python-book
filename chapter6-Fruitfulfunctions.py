
####################  6_2  #####################
def ack(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    return ack(m-1, ack(m, n-1))

#print(ack(3, 4))

####################  6_2  #####################


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    mid = middle(word)
    f = first(word)
    l = last(word)
    if f == l:
        if len(mid) == 0:
            return True
        return is_palindrome(mid)
    else:
        return False

#print( is_palindrome('aa') )

####################  6_4  #####################


def is_power(a, b):
    """
    Function takes a, b and returns if a = b^n
    for some n
    a : float
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.
    Returns
    -------
    True or False.
    """
    if a == b:
        return True
    if a % b != 0:
        return False
    return is_power(a/b, b)


#print(is_power(4096, 2))

####################  6_5  #####################
def gcd(a, b):
    """

    """
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

#print(gcd(40, 24))
