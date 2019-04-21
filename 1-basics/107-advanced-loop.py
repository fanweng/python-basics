#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
107-advanced-loop.py
'''

################################# Slice ########################################
# list, tuple and string are available for slicing

numbers = list(range(100))
print(numbers[1:3])
print(numbers[:2])
print(numbers[-4:-1])
print(numbers[-2:])
print(numbers[:10:2])
print(numbers[::10])

############################### Iteration ######################################

dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict.items():
    print(key, value)

# 'enumberate' changes a list to index-value pairs
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

########################## List Comprehensions #################################

list1 = list(range(1, 11))
print(list1)

list2 = [x * x for x in range(0,10)]
print(list2)

import os
list3 = [d.upper() for d in os.listdir('.') ]
print(list3)

################################ Generator #####################################

# list is created once and takes a lots of memory space
list4 = [x * x for x in range(10)]
# generator calculates the next element at one iteration, less memory consumed
generator1 = (x * x for x in range(10))
for n in generator1:
    print(n)

# if a function has 'yield', this function becomes a generator
# calling next(gen_func) will return at 'yield', calling next(gen_func) again will resume at the previous 'yield'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "Done!"

for n in fib(6):
    print(n)

# get the return value of generator function
g = fib(6)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator returns:", e.value)
        break

# Exercise of Yanghui Triangle using generator
def yanghui_triangle(max):
    n = 0
    L = [1,]
    #buf_L = []
    while n < max:
        yield L
        L = [1] + [ L[i]+L[i+1] for i in range(len(L)-1) ] + [1]
        #L.insert(0, 0)
        #L.append(0)
        #for i in range(len(L)-1):
        #    buf_L.append(L[i] + L[i+1])
        #L = buf_L
        #buf_L = []
        n = n + 1
    return "Done!"

for l in yanghui_triangle(6):
    print(l)

############################### Iterator #######################################
# Objects in for-loop are Iterable type, e.g. list, tuple, dict, set, str, etc.
# Objects in next() are Iterator type, e.g. generator.

from collections.abc import Iterable, Iterator
print("Iterable:")
print("abc:", isinstance('abc', Iterable))
print("123:", isinstance(123, Iterable))
print("[1,2,3]:", isinstance([1,2,3], Iterable))

print("Iterator:")
print("(x for x in range(10)):", isinstance((x for x in range(10)), Iterator))
print("[]:", isinstance([], Iterator))
print("{}:", isinstance({}, Iterator))
