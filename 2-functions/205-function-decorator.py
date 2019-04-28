#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
205-function-decorator.py
'''

############################ Function Decorator ################################
# Decorator adds features to a function and doesn't need to modify the original
# function definition.

import functools
import datetime
now = datetime.datetime.now()

# Decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)  # copy attributes of "func" to "wrapper", e.g. wrapper.__name__=func.__name__
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute") # Attach the "log" decorator using "@" right before the function def
def today_date():
    print("%d-%d-%d" % (now.year, now.month, now.day))

today_date()    # today_date = log("execute")(today_date)
print(today_date.__name__)