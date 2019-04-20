#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
103-list-tuple.py
'''

#################################### List ######################################
# List elements can be modified

classmates_list = ["Alice", "Bob", "Charlie"]
print(classmates_list)
print("len(classmates_list)=", len(classmates_list))
print("classmates_list[-1]=", classmates_list[-1])

classmates_list.append("Dan")
print(classmates_list)
classmates_list.insert(4, "Ella")
print(classmates_list)
classmates_list.pop()
print(classmates_list)
classmates_list.pop(3)
print(classmates_list)

list = [123, "ABC", True, [1, 2]]   # list elements can be different types
print(list)

#################################### Tuple #####################################
# Tuple elements cannot be modified after initialization.
tuple1 = (1, 2)
print(tuple1)
tuple2 = (1)    # this is not a tuple actually
print(tuple2)
tuple3 = (1,)   # this is a tuple
print(tuple3)
