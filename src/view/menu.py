#!/usr/bin/env python3

"""
File:   menu.py
Author: Thibault Douzon
Date:   2019-07-09
        22:48:11
mail:   douzont@gmail.com
"""

import tkinter as tk

from src.controller import control

class Menu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        super().__init__(bd=10, tearoff=0)
        self.root = root
        
        self.root['menu'] = self
        
        controller = control.Controller()
        
        self.sub_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label='label', menu=self.sub_menu)
        self.sub_menu.add_command(label='add label', command=controller.add_label)
        self.sub_menu.add_command(label='remove label', command=lambda: print('coucou2'))
        