#!/usr/bin/env python3

"""
File:   control.py
Author: Thibault Douzon
Date:   2019-07-09
        20:31:35
mail:   douzont@gmail.com
"""
import tkinter as tk
from tkinter import colorchooser

from src.my_util import Singleton
from src.model import label
from src import main

class Controller(metaclass=Singleton):
    def __init__(self, window=None):
        super().__init__()
        
        self._window: main.Window = window
        
        self._label_d = {}
    
    def show_label(self):
        for n, l in self._label_d.items():
            print(f"{n} : {l}")
    
    def add_label(self):
        label_info = {}
        
        window_popup = tk.Toplevel()
        window_popup.wm_title('Create a new label')
        
        name_frame = tk.Frame(window_popup)
        name_frame.pack(side=tk.TOP)
        
        name_label = tk.Label(name_frame, text='Label name : ')
        name_label.pack(side=tk.LEFT)
        
        name_entry = tk.Entry(name_frame)
        name_entry.pack(side=tk.LEFT)
        
        name_entry.focus()
        
        shortcut_frame = tk.Frame(window_popup)
        shortcut_frame.pack(side=tk.TOP)
        
        shortcut_label = tk.Label(shortcut_frame, text='Label shortcut : ')
        shortcut_label.pack(side=tk.LEFT)
        
        
        
        # TODO: validate input so new label isn't one of the previous
        def get_key():
            window_key = tk.Toplevel()
            window_key.wm_title('Select key')
            
            window_key.focus()
            window_key.grab_set()
            key_text_var = tk.StringVar(value='No key pressed')
            key_label = tk.Label(window_key, textvariable=key_text_var)
            key_label.pack()
            
            def key_helper(e: tk.Event):
                key_text_var.set(e.keysym)
                shortcut_button.config(text=e.keysym)
                label_info['key'] = (e.keysym, e.keycode)
                
                window_key.destroy()
                window_popup.grab_set()
                
            window_key.bind('<Key>', func=key_helper)
        
        shortcut_button = tk.Button(shortcut_frame, text='Select key', command=get_key)
        shortcut_button.pack(side=tk.LEFT)
        
        def get_color():
            color = colorchooser.askcolor()[1]
            window_popup.config(bg=color)
            
            name_frame.config(bg=color)
            shortcut_frame.config(bg=color)
            
            name_label.config(bg=color)
            shortcut_label.config(bg=color)
            
            label_info['color'] = color
            
        tk.Button(window_popup, text='Select Color', command=get_color).pack()

        def create_label():
            label_name = name_entry.get()
            label_key = label_info['key']
            label_color = label_info['color']
            
            label_ = label.Label(label_name, label_key, label_color)
            
            if not label_name in self._label_d:
                self._label_d[label_name] = label_
            window_popup.destroy()
            
        tk.Button(window_popup, text='Done', command=create_label).pack()
        
        window_popup.grab_set()