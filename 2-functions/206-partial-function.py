#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
206-partial-function.py
'''

############################# Partial Function #################################
# "Freeze" some portion of a function's arguments/keywords for a simplified version

import functools

int2 = functools.partial(int, base=2)
print(int2("101010"))

max2 = functools.partial(max, 10)
print(max2(3, 5, 7))    # "10" is added to the left of *args, i.e. max(10, 3, 5, 7)