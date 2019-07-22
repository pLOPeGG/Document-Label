#!/usr/bin/env python3

"""
File:   document.py
Author: Thibault Douzon
Date:   2019-07-08
        23:26:14
mail:   douzont@gmail.com
"""
from pathlib import Path
from typing import Tuple

import numpy as np
import PIL.Image as pilimg
import PIL.ImageDraw as pildraw
import PIL.ImageTk as piltk

from src.model import label, picture, rectangle
from src.controller import control


class Document:
    def __init__(self, image_path: Path):
        super().__init__()
        self._image_path = image_path
        self._base_image: picture.Picture = picture.Picture(image_path)
        self._working_image: pilimg.Image = self._base_image._array
        self._current_image: pilimg.Image = None
        self._tk_image: piltk.PhotoImage = None

        self._update(self._working_image)
        
        self._last_box: Tuple[rectangle.Rectangle, label.Label] = None
        
    def _update(self, new_image: pilimg.Image):
        self._current_image = new_image
        self._tk_image = piltk.PhotoImage(image=self._current_image)
    
    @property
    def size(self):
        return self._working_image.size
    
    def resize(self, 
               size: Tuple[int, int],
               *args,
               **kwargs):
        self._working_image = self._working_image.resize(size, *args, **kwargs)
        self._update(self._working_image)
    
    def draw_rectangle(self, rect: rectangle.Rectangle):
        """Draws a rectangle

        :rect: 
        :returns: TODO

        """
        selected_label = control.Controller()._selected_label
        
        self._last_box = (rect, selected_label)
        
        overlay =  pilimg.new('RGBA', 
                              self.size,
                              (0, 0, 0, 0),
                              )
        draw_overlay = pildraw.Draw(overlay)
        draw_overlay.rectangle(rect.points, 
                               fill=(*selected_label.color, 127),
                               outline=(*selected_label.color, 255),
                               )
        image = pilimg.alpha_composite(self._working_image, overlay)
        self._update(image)
        
    def save_modifications(self):
        self._working_image = self._current_image
        
        control.Controller().push_box(self._last_box)


def main():
    doc = Document(Path("img/sample_0.png"))


if __name__ == '__main__':
    main()
