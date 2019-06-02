import tkinter as tk 
import PIL.Image as pilimg
import PIL.ImageDraw as pildraw
import PIL.ImageTk as pilimgtk


class DocumentCanvas(tk.Canvas):

    """Canvas displaying documents"""

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        
        self.base_image_pil = None  # Base image to draw upon 

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

    def draw_image(self, image):
        """TODO: Docstring for draw_image.

        :image: TODO
        :returns: TODO

        """
        if not isinstance(image, pilimg.Image):
            raise TypeError
        image_tk = pilimgtk.PhotoImage(image)
        self._image_pil = image
        self._image_tk = image_tk
        self.create_image(0, 0,
                anchor=tk.NW,
                image=image_tk)



    def load_image(self, image):
        """Load an image and diplay it in the Canvas

        :image: Either PIL Image or path to image
        :returns: TODO

        """
        if isinstance(image, str):
            print(image)
            image = pilimg.open(image, 'r')
            image = image.convert('RGBA')
        elif isinstance(image, pilimg.Image):
            pass

        else:
            raise NotImplementedError
        
        size = self.get_size()
        image = image.resize(size=size,  
                resample=pilimg.BILINEAR,  # Adequate for text upsampling according to https://graphicdesign.stackexchange.com/questions/26385/difference-between-none-linear-cubic-and-sinclanczos3-interpolation-in-image
                )
        self.base_image_pil = image
        self.draw_image(image)

    def draw_rect(self, p1, p2):
        """Draws a rectangle at p1, p2

        :p1: TODO
        :p2: TODO
        :returns: TODO

        """
        if self.base_image_pil is None:
            return
        overlay =  pilimg.new('RGBA', 
                self.base_image_pil.size,
                (0, 0, 0, 0),
                )
        draw_overlay = pildraw.Draw(overlay)
        draw_overlay.rectangle((p1, p2), 
                fill=(125, 0, 0, 127),
                outline=(125, 0, 0, 255),
                )

        image = pilimg.alpha_composite(self.base_image_pil, overlay)
        image.convert('RGBA')
        
        self.draw_image(image)

        pass

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
            self.draw_rect(*self.postion_buffer)
        self.postion_buffer = []  # reset

    def _motion_f(self, event):
        """Mouse motion event callback

        :event: TODO
        :returns: TODO

        """
        if len(self.postion_buffer) > 0:
            self.draw_rect(self.postion_buffer[0], (event.x, event.y))

if __name__ == "__main__":
    root = tk.Tk()
    doc = DocumentCanvas(root, height=1200, width=900)

