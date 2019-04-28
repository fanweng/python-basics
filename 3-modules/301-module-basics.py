#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
301-module-basics.py
'''

########################### Packages & Modules #################################

# NOTE: Try to use different module name, function name and variable name from Python built-in ones
# e.g. Python has a "sys" module, do not write a sys.py yourself. Use "import your_mod" to check if "your_mod" violates any module name installed.

# NOTE: Every package directory must have a "__init__.py"
# "__init__.py" itself is a module as well. It can be empty or has some Python code

r'''
my_package
|- sub_package
|  |- __init__.py
|  |- mod_1.py
|  |- mod_2.py
|- __init__.py
|- mod_3.py
|- mod_4.py
'''
# Module name of "mod_1.py" is "my_package.sub_package.mod_1"
# "my_package" is a module as well, its code is in the "__init__.py"

################################# Scope ########################################

# NOTE: Normal variables and functions are public, e.g. abc, PI...
# NOTE: Private var/func are named as "_xxx", "__yyy". It can be but shouldn't be referenced outside the module
# NOTE: Special variables as "__zzz__" can be referenced, e.g. __author__, __name__

################################# Path #########################################
# Add the path to a module so that Python can find it when importing

# NOTE: 1. Set the environment variable PYTHONPATH.
# e.g. PYTHONPATH=/path/to/my/module.
# This works for every program started in that environemnt.

# NOTE: 2. Append to sys.path.
# e.g. sys.path.append("/path/to/my/module") after "import sys".
# This temporarily adds the path during the runtime and we'll lose it after program exits.
