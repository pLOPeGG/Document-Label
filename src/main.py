from pathlib import Path

import PIL.Image as pilimg
import PIL.ImageTk as pilimgtk
import tkinter as tk
import numpy as np

from src import canvas
from src.model import document

class Window(tk.Tk):

    """Main window starting application"""

    def __init__(self, doc_pa):
        """

        :doc_pa: TODO

        """
        super().__init__()

        self._doc_pa = doc_pa
        
        self._build()

    def _build(self):
        """Build all components in the window

        """
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=tk.TOP)
       
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
    app = Window("")
    doc = document.Document(Path("img/sample_0.png"))
    app.doc_canvas.load_document(doc)
    tk.mainloop()


if __name__ == "__main__":
    main()

