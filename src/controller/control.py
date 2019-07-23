#!/usr/bin/env python3

"""
File:   control.py
Author: Thibault Douzon
Date:   2019-07-09
        20:31:35
mail:   douzont@gmail.com
"""
from collections import deque
from typing import Tuple, Deque
import tkinter as tk
from tkinter import colorchooser

from src.my_util import Singleton
from src.model import label, rectangle, document
from src import main


class Controller(metaclass=Singleton):
    def __init__(self, window=None):
        super().__init__()

        self._window: main.Window = window

        self._box_q: Deque[Tuple[rectangle.Rectangle, label.Label]] = deque()

        self._label_d = {
            label.default_label_none._key: label.default_label_none}
        self._selected_label: label.Label = label.default_label_none

        self._shortcut_d = {
            ('BackSpace', 8): self._undo,
            ('Tab', 9): None,
            ('Return', 13): None,
            ('Escape', 27): self._clear_volatile_box,
            ('Left', 37): None,
            ('Up', 38): None,
            ('Right', 39): None,
            ('Down', 40): None
        }

    def apply_shortcut(self, key: Tuple[str, int], doc: document.Document):
        if key in self._shortcut_d:
            if self._shortcut_d[key] is not None:
                self._shortcut_d[key](doc)
        else:
            pass

    def push_box(self, new_box: Tuple[rectangle.Rectangle, label.Label]):
        self._box_q.append(new_box)

    def show_label(self):
        for n, l in self._label_d.items():
            print(f"{n} : {l}")

    def add_label(self):
        """
        :returns: 
        """
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

        def get_key():
            window_key = tk.Toplevel()
            window_key.wm_title('Select key')

            window_key.focus()
            window_key.grab_set()
            key_text_var = tk.StringVar(value='No key pressed')
            key_label = tk.Label(window_key, textvariable=key_text_var)
            key_label.pack()

            def key_helper(e: tk.Event):
                if (e.keysym, e.keycode) not in self._label_d \
                   and (e.keysym, e.keycode) not in self.shortcut_d:
                    key_text_var.set(e.keysym)
                    shortcut_button.config(text=e.keysym)
                    label_info['key'] = (e.keysym, e.keycode)

                    window_key.destroy()
                    window_popup.grab_set()
                else:
                    key_text_var.set(f"Key «{e.keysym}» is not available")

            window_key.bind('<Key>', func=key_helper)

        shortcut_button = tk.Button(shortcut_frame,
                                    text='Select key',
                                    command=get_key)
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

            if label_name not in self._label_d:
                self._label_d[label_key] = label_
            window_popup.destroy()

        tk.Button(window_popup, text='Done', command=create_label).pack()

        window_popup.grab_set()

    def select_label(self, label_key: Tuple[str, int]):
        """Change current selected label to another
        :param label_key: tuple keysym and keycode of a label
        """
        if label_key in self._label_d:
            self._selected_label = self._label_d[label_key]
        else:
            pass

    def _undo(self, doc: document.Document):
        if len(self._box_q) > 0:
            deleted_box = self._box_q.pop()
            doc.draw_from_start(self._box_q)
            print(f"Removed {deleted_box}, remains {self._box_q}")
        else:
            pass

    def _clear_volatile_box(self, doc: document.Document):
        doc.clear_volatile_box()
