#!/usr/bin/env python3

"""
File:   main.py
Author: Thibault Douzon
Date:   2019-07-09
        20:29:55
mail:   douzont@gmail.com
"""

from pathlib import Path

import PIL.Image as pilimg
import PIL.ImageTk as pilimgtk
import tkinter as tk
import numpy as np

from src.my_util import Singleton
from src.view import canvas, menu
from src.model import document
from src.controller import control


class Window(tk.Tk, metaclass=Singleton):

    """Main window starting application"""

    def __init__(self):
        """

        :doc_pa: TODO

        """
        super().__init__()
        
        self._controller: control.Controller = control.Controller(self)
        self._build()

    def _build(self):
        """Build all components in the window

        """
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=tk.TOP)
        
        self.menu = menu.Menu(self)
       
        # TOP Frame for navigation / buttons
        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(side=tk.TOP)

        self.next_button = tk.Button(self.top_frame,
                                     text="Next",
                                     )
        self.next_button.pack(side=tk.RIGHT)

        # Middle frame for canvas
        self.middle_frame = tk.Frame(self.main_frame)
        self.middle_frame.pack(side=tk.BOTTOM)
        
        self.doc_canvas = canvas.DocumentCanvas(self.middle_frame,
                                                height=1200,
                                                width=900,
                                                )
        self.doc_canvas.pack()


def main():
    app = Window()
    doc = document.Document(Path("img/sample_0.png"))
    app.doc_canvas.load_document(doc)
    tk.mainloop()


if __name__ == "__main__":
    main()

