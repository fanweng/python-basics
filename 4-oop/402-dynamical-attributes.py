#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
402-dynamical-attributes.py
'''

##################### Dynamically Adding Attributes ############################

class Student(object):
    __slots__ = ('name', 'age', 'set_age')  # define attribute names allowed to be added

s1 = Student()
s1.name = 'Bruce'   # attribute is added dynamically at runtime to an instance, and for this instance ONLY
s1.age = 0

from types import MethodType
def set_age(self, age):
    self.age = age

s1.set_age = MethodType(set_age, s1)
s1.set_age(29)
print(s1.age)

try:
    s1.gender = 'male'
except AttributeError as e:
    print('AttributeError:', e)

class GraduateStudent(Student): # child class won't inherit parent's slots unless it defines slots, too
    __slots__ = ('score')       # this will has "name", "age" and "score" slots

s2 = GraduateStudent()
try:
    s2.gender = 'male'
except AttributeError as e:
    print('AttributeError:', e)
