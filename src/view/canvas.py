#!/usr/bin/env python3

"""
File:   canvas.py
Author: Thibault Douzon
Date:   2019-07-09
        20:30:05
mail:   douzont@gmail.com
"""

import tkinter as tk 
import PIL.Image as pilimg
import PIL.ImageDraw as pildraw
import PIL.ImageTk as piltk

from src.model import document, rectangle

class DocumentCanvas(tk.Canvas):

    """Canvas displaying documents"""

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.config(bg='white')
        self.pack()
 
        self._document: document.Document = None  # Current working document
       
        # Stores last positions clicked
        self.position_buffer = []
        # Stores all selections validated
        self.selection_l = []
        # Stores last selection that pends validation
        self.selection_to_validate = None

        self.bind('<Enter>', lambda e: self.focus_set())
        self.bind('<Button-1>', self._button_1_f)
        self.bind('<ButtonRelease-1>', self._button_1_release_f)
        self.bind('<Motion>', self._motion_f)

        self.bind('<space>', self._validate_selection_f)
    
    def get_size(self):
        """Dynamic size of the widget

        :returns: update actual size of component

        """
        self.update()
        return self.winfo_width(), self.winfo_height()

    def draw_document(self):
        """TODO: Docstring for draw_document.

        :returns: TODO

        """
        self.create_image(0, 0,
                          anchor=tk.NW,
                          image=self._document._tk_image)

    def load_document(self, doc: document.Document):
        """Load an image and diplay it in the Canvas

        :image: Either PIL Image or path to image
        :returns: TODO

        """       
        if not isinstance(doc, document.Document):
            raise TypeError
         
        size = self.get_size()
        doc.resize(size=size,  
                   resample=pilimg.BILINEAR,  # Adequate for text upsampling according to https://graphicdesign.stackexchange.com/questions/26385/difference-between-none-linear-cubic-and-sinclanczos3-interpolation-in-image
                  )
        self._document = doc
        self.draw_document()

    def draw_rectangle(self, rect: rectangle.Rectangle):
        """Draws a rectangle

        :rect: 
        :returns: TODO

        """
        if self._document is None:
            return
        self._document.draw_rectangle(rect)
        self.draw_document()

        pass

    def _button_1_f(self, event):
        """TODO: Docstring for _button_1_f.

        :event: TODO
        :returns: TODO

        """
        self.position_buffer = [(event.x, event.y)]

    def _button_1_release_f(self, event):
        """TODO: Docstring for _button_1_release_f.

        :event: TODO
        :returns: TODO

        """
        if len(self.position_buffer) > 0:
            self.position_buffer.append((event.x, event.y))
            print(self.position_buffer)
            if self.position_buffer[0][0] != self.position_buffer[1][0] \
                    and self.position_buffer[0][1] != self.position_buffer[1][1]:
                self._document.draw_rectangle(rectangle.Rectangle(*self.position_buffer[0], 
                                                                  *self.position_buffer[1]))
                self.selection_to_validate = (*self.position_buffer,)
                self.draw_document()
        self.position_buffer = []  # reset

    def _motion_f(self, event):
        """Mouse motion event callback

        :event: TODO
        :returns: TODO

        """
        if len(self.position_buffer) > 0:
            self._document.draw_rectangle(rectangle.Rectangle(*self.position_buffer[0], 
                                                              *(event.x, event.y)))
            self.draw_document()
    
    def _validate_selection_f(self, event):
        """Validate last selection

        :event: TODO
        :returns: TODO

        """
        if self.selection_to_validate is None:
            return
        self.selection_l.append(self.selection_to_validate)
        self.selection_to_validate = None
        
        # Modify stored image
        self._document.save_modifications()

if __name__ == "__main__":
    root = tk.Tk()
    doc = DocumentCanvas(root, height=1200, width=900)

