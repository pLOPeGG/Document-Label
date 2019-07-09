#!/usr/bin/env python3

"""
File:   control.py
Author: Thibault Douzon
Date:   2019-07-09
        20:31:35
mail:   douzont@gmail.com
"""
import tkinter as tk

from src.my_util import Singleton

class Controller(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        
    def add_label(self):
        window_popup = tk.Toplevel()
        window_popup.wm_title('Create a new label')
        
        name_frame = tk.Frame(window_popup)
        name_frame.pack(side=tk.TOP)
        
        name_label = tk.Label(name_frame, text='Label name : ')
        name_label.pack(side=tk.LEFT)
        
        # TODO: validate input so new label isn't one of the previous
        name_entry = tk.Entry(name_frame)
        name_entry.pack(side=tk.LEFT)
