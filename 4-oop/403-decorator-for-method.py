#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
403-decorator-for-method.py
'''

######################### Decorator - @roperty #################################
# @property decorator makes a method as a class attribute

class Student(object):

    @property
    def birthday(self):     # getter() function
        return self._birthday
    
    @birthday.setter
    def birthday(self, year):
        self._birthday = year

    @property
    def age(self):          # if no setter() for "age", it is a read-only attribute
        return (2019 - self._birthday)

s1 = Student()
s1.birthday = 1990  # actually call getter() although it looks like assigning a value to the attribute
print(s1.birthday)  # actually call setter()
try:
    s1.age = 21
except AttributeError as e:
    print('AttributeError:', e)
print(s1.age)