#!/usr/bin/env python3

"""
File:   label.py
Author: Thibault Douzon
Date:   2019-07-08
        23:21:42
mail:   douzont@gmail.com
"""
from typing import Tuple

class Label:
    def __init__(self, name, color):
        super().__init__()
        self._name: str = name
        self._color: Tuple[int] = color