#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:56:49 2020

@author: mohamad
"""

################################################
####################  10_1  ##################### 
################################################


# def nested_sum(t):
#     nsum = 0
#     for elem in t:
#         nsum = nsum + sum(elem)
#     return nsum

# t = [[1, 2], [3], [4, 5, 6]]
# print('10-1 : ', nested_sum(t))


################################################
####################  10_2  ##################### 
################################################

# def cumsum(t):
#     csum = []
#     for i in range(len(t)):
#         csum.append(sum(t[0:i+1]))
#     return csum

# t = [1, 2, 3]
# print('10-2 : ', cumsum(t))

################################################
####################  10_3  ##################### 
################################################

# def middle(t):
#     return t[1:-1]

# t = [1, 2 , 3, 4]
# print('10-3 : ' , middle(t))


################################################
####################  10_4  ##################### 
################################################

# def chop(t):
#     t.pop(0)
#     t.pop(-1)
    
# t = [1, 2 , 3, 4]
# #print(t)
# chop(t)
# print('10-40 : ', t)

################################################
####################  10_5  ##################### 
################################################


# def is_sorted(t):
#     return t == sorted(t)

# print(is_sorted([2, 3, 1]))
# print(is_sorted([1, 2, 3]))
# print(is_sorted(['a', 'b' , 'c']))
# print(is_sorted(['a', 'g' , 'c']))


################################################
####################  10_6  ##################### 
################################################

# def is_anagram(word1, word2):
#     return sorted(word1)==sorted(word2)

    
# print('10-6 : ', is_anagram('jello','ejllo'))


################################################
####################  10_7  ##################### 
################################################

# def has_duplicates(t):
#     ts = sorted(t)
#     for i in range(len(ts)-1):
#         if ts[i] == ts[i+1]:
#             return True
#     return False


# def count_duplicates(t):
#     ts = sorted(t)
#     count = 0
#     for i in range(len(ts)-1):
#         if ts[i] == ts[i+1]:
#             count = count + 1
#     return count

################################################
####################  10_8  ##################### 
################################################

# from random import randint


# def generate_sample():
#     sample = [randint(1, 365) for i in range(23)]
#     return sample


# count = 0    
# num_samples = 1000
# for i in range(num_samples):
#     sample = generate_sample()
#     if has_duplicates(sample):
#         count = count + 1
    
# print(count)


################################################
####################  10_9  #################### 
################################################

# import time



def read_word_list_append(filename='words.txt'):    
    fin = open(filename)
    word_list = []        
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


# def read_word_list_plus(filename='words.txt'):    
#     fin = open(filename)
#     word_list = []        
#     for line in fin:
#         word = line.strip()
#         word_list = word_list + [word]
#     return word_list



# t0 = time.time()
# word_list_append = read_word_list_append(filename='words.txt')
# t1 = time.time()

# total = t1-t0
# print("append time  = ", total)

# t0 = time.time()
# word_list_plus = read_word_list_plus(filename='words.txt')
# t1 = time.time()

# total = t1-t0
# print("plus time  = ", total)

################################################
###################  10_10  #################### 
################################################

def in_bisect(t, target):
    middle = int(len(t)/2)
    
    if middle==0:
        return False

    elif t[middle] == target:
        return True

    elif t[middle] > target:
        return in_bisect(t[0:middle], target)

    elif t[middle] < target:
        return in_bisect(t[middle:len(t)], target)

# l = [1, 2 , 3 , 5, 7, 10]
# print(in_bisect(l, 12))

################################################
###################  10_11  #################### 
################################################


# word_list = read_word_list_append(filename='words.txt')

# count = 0
# for word in word_list:
#     if in_bisect(word_list, word[::-1]):
#         print(word, ' , ' ,word[::-1])
        
        
################################################
###################  10_12  #################### 
################################################

from chp9 import uses_all, uses_only

word_list = read_word_list_append(filename='words.txt')

for word1 in word_list:
    for word2 in word_list:
        letters = word1 + word2
        for word in word_list:
            if uses_all(word, letters) and uses_only(word, letters):
                print(word1, ' , ', word2, ' , ', word)

