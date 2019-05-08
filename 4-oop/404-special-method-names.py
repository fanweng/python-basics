#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
404-special-method-names.py
'''

######################### Special Method Names #################################

class Student(object):
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name: %s)" % self.name

    __repr__ = __str__

    # if user calls some attributes that are undefined, Python will try call __getattr__()
    def __getattr__(self, attr):
        if attr == 'score':
            return 99   # return object can be data or function

    # direct instance call will use __call__() method
    def __call__(self):
        print("My name is %s" % self.name)

s1 = Student('Mike')

print(s1)
print(s1.score) # 'score' attribute is not defined

print(callable(s1)) # check if instance s1 is callable
s1()    # call the instance directly

class Fib1(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

for n in Fib1():
    print(n)

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n is an index
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f2 = Fib2()
print(f2[7])
print(f2[5:20])