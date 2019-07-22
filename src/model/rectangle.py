#!/usr/bin/env python3

"""
File:   rectangle.py
Author: Thibault Douzon
Date:   2019-07-08
        23:16:54
mail:   douzont@gmail.com
"""

from typing import Tuple

class Rectangle:
    def __init__(self, *boundaries):
        super().__init__()
        
        self._boundaries: Tuple[int] = boundaries
    
    @property
    def points(self) -> Tuple[Tuple[int, int], 
                                 Tuple[int, int]]:
        return ((self._boundaries[0], self._boundaries[1]),
                (self._boundaries[2], self._boundaries[3])) 