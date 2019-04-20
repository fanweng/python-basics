#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
106-dict-set.py
'''

############################### Dictionary #####################################
# dict is similar to map in other programming language
# key-value mapping mechanism makes value retrieving very fast
# dict is faster on searching/insertion, but requires more memory than list data

dict = {"Alice": 95, "Bob": 93, "Charlie": 99}
print(dict)
print("Bob's score is", dict["Bob"])
print("Dan" in dict)
print(dict.get("Dan"))
print(dict.get("Dan", -1))  # return a specified vaule if key isn't found

dict["Dan"] = 88
dict.update({"Ella": 94})
print(dict)
dict.pop("Dan")
print(dict)

################################## Set #########################################
# Set is similar to dict, but only has keys. Each key must be identical.

a_set = {1, 3, 2}
print(a_set)
a_set.add(13)
print(a_set)
a_set.remove(2)
print(a_set)

b_set = set([2, 6, 4, 9, 4])    # set is orderless, has no duplicate elements
print(b_set)
b_set.add(9)
print(b_set)

set1 = set([1, 2, 4]) 
set2 = set([2, 5])
print(set1 & set2)  # intersection of sets
print(set1 | set2)  # union of sets