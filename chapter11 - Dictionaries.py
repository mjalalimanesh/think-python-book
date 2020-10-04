#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:12:19 2020

@author: mohamad
"""


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

hist = histogram('bronteoust')


################################################
###################  11_1  ##################### 
################################################


def read_words_to_dic(path='words.txt'):
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d        

#d = read_words_to_dic(path='words.txt')


################################################
###################  11_2  ##################### 
################################################

def invert_dict_2(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse

#inv = invert_dict_2(hist)


################################################
###################  11_3  ##################### 
################################################
known = {}
def ackermann_memoizd(m, n):
    if (m, n) in known:
        return known[(m, n)]
    if m==0 :
        res = n + 1
        known[(m, n)] = res
        return res
    elif n==0:
        res = ackermann_memoizd(m-1, 1)
        known[(m, n)] = res
        return res
    res = ackermann_memoizd(m-1, ackermann_memoizd(m, n-1))
    known[(m, n)] = res
    return res
#print(ackermann_memoizd(3, 4))
################################################
###################  11_4  ##################### 
################################################
def has_duplicates(t):
    ts = sorted(t)
    for i in range(len(ts)-1):
        if ts[i] == ts[i+1]:
            return True
    return False

def has_duplicates_dict(t):
    d = {}
    for elem in t:
        if elem in d:
            return True
        d[elem] = True
    return False
#print(has_duplicates_dict(['h', 2, 'h', 3]))
################################################
###################  11_5  ##################### 
################################################

def rotate_words(path='words.txt'):
    d = read_words_to_dic(path)
    for key in d:
        if key[::-1] in d:
            print(key, " , " ,key[::-1])

#rotate_words()
################################################
###################  11_6  ##################### 
################################################







