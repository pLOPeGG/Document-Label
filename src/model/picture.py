#!/usr/bin/env python3

"""
File:   picture.py
Author: Thibault Douzon
Date:   2019-07-08
        22:42:16
mail:   douzont@gmail.com
"""
from pathlib import Path
from typing import Tuple
from copy import deepcopy

import numpy as np
import PIL.Image as pilimg


class Picture:
    def __init__(self, image_path: Path):
        super().__init__()
        
        self._image_path: Path = image_path
        self._array: pilimg.Image = self._open()
        self._base_array = deepcopy(self._array)
        
    def _open(self):
        return pilimg.open(str(self._image_path), 'r').convert("RGBA")
    
    def resize(self, 
               size: Tuple[int, int],
               *args,
               **kwargs) -> pilimg.Image:
        """ Resize and return new image
        """
        self._array = self._array.resize(size=size,
                                         *args,
                                         **kwargs)
        
        self._base_array = self._base_array.resize(size=size,
                                                   *args,
                                                   **kwargs)
        return self._array
