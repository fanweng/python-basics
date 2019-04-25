#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
dunder.py
'''

# "Dunder" is double underscore in the Python community

### Get path to the current module
print(__file__)

### Get module name
# Running this module as a script will return "__main__"
# If this module is imported as "$ python3 -c "import dunder.py"", it will return "dunder"
print(__name__)