#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
203-higher-order-function.py
'''

########################### Function as Argument ###############################

def my_add_1(x, y, f):
    return f(x) + f(y)

print(my_add_1(-2, 5, abs))

################################### Map ########################################

def f(x):
    return x * x

# map() applies function "f" to every element in the Iterable object individually
# map(f, [x1, x2, x3]) = [f(x1), f(x2), f(x3)]
m = map(f, [1, 2, 3, 4, 5, 6])
# r is a iterable map object, list() makes it as a list
print(list(m))

################################# Reduce #######################################

from functools import reduce
def my_add_2(x, y):
    return x + y

# reduce() applies function "f" to first two elements in the sequence, and applies "f" to the returned value and next element in the sequence...
# reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)
r = reduce(my_add_2, [1, 2, 3, 4, 5, 6])
print(r)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

rm = reduce(lambda x, y : x * 10 + y, map(char2num, '84751785'))
print(type(rm), rm)