#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
101-data-types-and-var.py
'''

# Integer
a = 200
b = -120
c = 0xae86
print("a/b=", a/b)
print("a//b=", a//b)
print("a%b=", a%b)

# Float
d = 1.23
e = -3.9e-2

# Character
f = "abc"
g = "\\\t\\"
h = r'\\\t\\'
i = '''line1
   line2
   line3'''
print("g=", g, "\nh=", h, "\ni=", i)

# Bool
j = True
k = False
l = (j and k) or (not k)
print("l=", l)

# None
m = None

# Const
PI = 3.14159265359 # Use capital letters to distinguish, but still a variable