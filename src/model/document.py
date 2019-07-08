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
import PIL.ImageTk as piltk

from src.model import label, picture, rectangle


class Document:
    def __init__(self, image_path: Path):
        super().__init__()
        self._image_path = image_path
        self._current_image: pilimg.Image = None
        self._tk_image: piltk.PhotoImage = None

        self._base_image = picture.Picture(image_path)
        self._update(self._base_image._array)
        
    def _update(self, new_image: pilimg.Image):
        self._current_image = new_image
        self._tk_image = piltk.PhotoImage(image=self._current_image)
        
    def resize(self, 
               size: Tuple[int, int],
               *args,
               **kwargs):
        self._current_image = self._current_image.resize(size, *args, **kwargs)
        self._update(self._current_image)


def main():
    doc = Document(Path("img/sample_0.png"))


if __name__ == '__main__':
    main()
