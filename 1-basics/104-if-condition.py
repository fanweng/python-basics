#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
104-if-condition.py
'''

################################### if... ######################################

birth_str = input("Your birthday: ")
birth_int = int(birth_str)
if birth_int <= 1990:
    print("old man :P")
elif birth_int <= 2000:
    print("mid age :)")
elif birth_int <= 2019:
    print("hey boy ;)")
else:
    print("go back to future please")