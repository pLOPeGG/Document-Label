import PIL.Image as pilimg
import PIL.ImageTk as pilimgtk
import tkinter as tk
import numpy as np

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
        
        self.doc_canvas = tk.Canvas(self.middle_frame,
            height=1200,
            width=900,
            )
        self.doc_canvas.config(bg='black')
        self.doc_canvas.grid()

    def load_image(self, image):
        """Load an image and diplay it in the Canvas

        :image: Either PIL Image or path to image
        :returns: TODO

        """
        if isinstance(image, str):
            print(image)
            image = pilimg.open(image, 'r')
        
        elif isinstance(image, pilimg.Image):
            pass
        image = image.resize(size=(900, 1200), 
                resample=pilimg.BILINEAR,  # Adequate for text upsampling according to https://graphicdesign.stackexchange.com/questions/26385/difference-between-none-linear-cubic-and-sinclanczos3-interpolation-in-image
                )
        image_tk = pilimgtk.PhotoImage(image)
        self._image_tk = image_tk
        self._image = image
        self.doc_canvas.create_image(0, 0,
                anchor=tk.NW,
                image=image_tk)

def main():
    app = Window("")
    app.load_image("img/sample_0.png")
    tk.mainloop()


if __name__ == "__main__":
    main()

