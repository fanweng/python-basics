#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
105-loop.py
'''

################################ for-loop ######################################

classmates = ["Alice", "Bob", "Charlie"]
for name in classmates:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

############################## while-loop ######################################

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

p = 5
while p > 0:
    if p < 3:   # "break" ends the entire while-loop
        break
    print(p)
    p = p - 1

q = 6
while q > 0:
    q = q - 1
    if ((q % 2) == 0):  # "continue" ends the current iteration and skips the following statements
        continue
    print(q)

