#!/usr/bin/env python3

"""
File:   my_util.py
Author: Thibault Douzon
Date:   2019-07-09
        20:39:42
mail:   douzont@gmail.com
"""

class Singleton(type):
    __instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            print('in')
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
