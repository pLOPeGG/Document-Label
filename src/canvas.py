import tkinter as tk 
import PIL.Image as pilimg
import PIL.ImageDraw as pildraw
import PIL.ImageTk as pilimgtk

from src.model import document

class DocumentCanvas(tk.Canvas):

    """Canvas displaying documents"""

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.config(bg='white')
        self.pack()
 
        self.base_image_pil = None  # Base image to draw upon #! Erase
        self.image_pil = None  # Current image without non validated selection #! Erase
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

        self.bind('s', self._validate_selection_f)

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

    def draw_rectangle(self, p1, p2):
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

        image = pilimg.alpha_composite(self.image_pil, overlay)
        image.convert('RGBA')
        
        self.draw_document(image)

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
                self.draw_rectangle(*self.position_buffer)
                self.selection_to_validate = (*self.position_buffer,)
        self.position_buffer = []  # reset

    def _motion_f(self, event):
        """Mouse motion event callback

        :event: TODO
        :returns: TODO

        """
        if len(self.position_buffer) > 0:
            self.draw_rectangle(self.position_buffer[0], (event.x, event.y))
    
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
        self.image_pil = self._image_pil

if __name__ == "__main__":
    root = tk.Tk()
    doc = DocumentCanvas(root, height=1200, width=900)

