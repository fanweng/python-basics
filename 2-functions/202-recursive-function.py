#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
202-recursive-function.py
'''

################################ Function ######################################

def hanoi(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        hanoi(n-1, a, c, b)
        print(a, "-->", c)
        hanoi(n-1, b, a, c)

hanoi(4, 'A', 'B', 'C')
