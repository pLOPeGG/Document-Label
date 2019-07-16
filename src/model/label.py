#!/usr/bin/env python3

"""
File:   label.py
Author: Thibault Douzon
Date:   2019-07-08
        23:21:42
mail:   douzont@gmail.com
"""
from typing import Tuple

import tkinter as tk
class Label:
    def __init__(self, name: str, key, color):
        super().__init__()
        self._name: str = name
        self._key: Tuple[str, int] = key
        self._color: str = color  # «#ffffff»
        
    def __repr__(self):
        return f"Label(name={self._name.__repr__()}, key={self._key}, color={self._color.__repr__()})"    
        
    def __str__(self):
        return self.__repr__()