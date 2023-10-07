from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
  
        self.parent = parent
  
        self.initUI()
  
    def initUI(self):
        self.parent.title("Label")
  
        self.img = Image.open("Z:\\2115215\\image1\\pandora.png")
        rotunda = ImageTk.PhotoImage(self.img)
        label = Label(self, image=rotunda)
  
        label.image = rotunda
  
        label.pack()
        self.pack()
  
    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(f"{w}x{h}+300+300")


root = Tk()
ex = Example(root)
ex.setGeometry()
root.mainloop()