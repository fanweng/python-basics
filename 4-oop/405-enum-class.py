#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
405-enum-class.py
'''

############################## Enum Class ######################################

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class Weekday(Enum):    # use Enum parent class to define customized values
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Tue
day2 = Weekday['Sat']
print(day1)
print(day2)
print(day2.value)