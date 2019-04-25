#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
204-function-as-return.py
'''

########################### Function as Return ###############################

def lazy_sum(*args):    # "*args" passes a variable-length argument list to function
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4, 5)
print(f)        # function object is returned
print(f())      # function returns value once it is actually called

# Function returns a new function object every time even though they may have the same argument list
f1 = lazy_sum(2, 3, 4)
f2 = lazy_sum(2, 3, 4)
print("f1 == f2?", f1 == f2)

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# f() doesn't execute here
f3, f4, f5 = count()
# f() executes here and "i" has become 3 after three functions return above
# NOTE for returning a closure: Don't use any loop variable or any variable will change
print(f3(), f4(), f5())


