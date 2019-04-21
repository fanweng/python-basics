#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
201-function-basics.py
'''

################################ Function ######################################

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Wrong argument type!")
    if x >= 0:
        return x
    else:
        return -x

#print(my_abs('A'))
print(my_abs(-3))

def nop():
    pass    # do nothing, like a placeholder

######################### Return Multiple Values ###############################

import math
def cal_sin_cos(angle):
    sin_x = math.sin(angle)
    cos_x = math.cos(angle)
    return sin_x, cos_x # return a tuple, and "()" can be ignored

a = cal_sin_cos( math.pi/6 )
x, y = cal_sin_cos( math.pi/3 ) # multiple variables can accept a tuple
print(a)
print(x, y)

############################### Parameters #####################################

def power(x, n=2):  # default n=2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(2, 4))

def add_end_bad(L=[]):  # default L points to a list and its update is remembered after each call
    L.append("END")
    return L

print(add_end_bad())
print(add_end_bad())

def add_end_good(L=None):   # default parameter must be a const to avoid defect above
    if L == None:
        L = []
    L.append("END")
    return L

print(add_end_good())
print(add_end_good())

# '*numbers' accepts an arbitrary number of parameters, making them a tuple
def sum_a_to_z(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

nums = [1, 2, 3, 4, 5]
print(sum_a_to_z(1, 2, 3))
print(sum_a_to_z(*nums))    # '*' pass all elements as a single parameter

# '**keyword’ accepts a parameter with name, making them a dictionary
def person(name, age, **keyword):
    if "city" in keyword:
        pass    # do something
    if "job" in keyword:
        pass    # do something
    print("name:", name, "age:", age, "other:", keyword)

person("Ada", 24)
person("Bill", 26, city="Ottawa")
opt_info = {"city": "Toronto", "job": "Engineer"}
person("Chris", 26, **opt_info)

# Only accepts keyword parameters after '*'
def person_2(name, age, *, city="Ottawa", job):
    print(name, age, city, job)

person_2("Dick", 22, job="Doctor")
#person_2("Dick", 22, city="Montreal", height="173")   # height won't be accepted
