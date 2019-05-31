import tkinter as tk 
import PIL.Image as pilimg
import PIL.ImageTk as pilimgtk


class DocumentCanvas(tk.Canvas):

    """Canvas displaying documents"""

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.config(bg='white')
        self.pack()
        
        # Stores last positions clicked
        self.postion_buffer = []
        self.bind('<Button-1>', self._button_1_f)
        self.bind('<ButtonRelease-1>', self._button_1_release_f)
        self.bind('<Motion>', self._motion_f)

    def get_size(self):
        """Dynamic size of the widget

        :returns: update actual size of component

        """
        self.update()
        return self.winfo_width(), self.winfo_height()

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

        else:
            raise NotImplementedError
        
        size = self.get_size()
        image = image.resize(size=size,  
                resample=pilimg.BILINEAR,  # Adequate for text upsampling according to https://graphicdesign.stackexchange.com/questions/26385/difference-between-none-linear-cubic-and-sinclanczos3-interpolation-in-image
                )
        image_tk = pilimgtk.PhotoImage(image)
        self.ase_image_pil = image
        self._image_pil = image
        self._image_tk = image_tk
        self.create_image(0, 0,
                anchor=tk.NW,
                image=image_tk)

    def _button_1_f(self, event):
        """TODO: Docstring for _button_1_f.

        :event: TODO
        :returns: TODO

        """
        self.postion_buffer = [(event.x, event.y)]

    def _button_1_release_f(self, event):
        """TODO: Docstring for _button_1_release_f.

        :event: TODO
        :returns: TODO

        """
        if len(self.postion_buffer) > 0:
            self.postion_buffer.append((event.x, event.y))
            print(self.postion_buffer)
        self.postion_buffer = []  # reset

    def _motion_f(self, event):
        """Mouse motion event callback

        :event: TODO
        :returns: TODO

        """
        print(event.x, event.y)

if __name__ == "__main__":
    root = tk.Tk()
    doc = DocumentCanvas(root, height=1200, width=900)

