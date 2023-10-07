from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
  
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("MY PROFILE")
        self.pack(fill=tk.BOTH, expand=True)
  
        Style().configure("TFrame", background="#333")
  
        bard = Image.open("C:\Users\CICT\Downloads\2115215\image1.jpg.png")
        bard = bard.resize((100, 100), Image.LANCZOS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = tk.Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
    
        rot = Image.open("C:\Users\CICT\Downloads\2115215\image1.jpg.png")
        rot = rot.resize((100, 100), Image.LANCZOS)
        rotunda = ImageTk.PhotoImage(rot)
        label2 = tk.Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)
  
        minc = Image.open("C:\Users\CICT\Downloads\2115215\image1.jpg.png")
        minc = minc.resize((100, 100), Image.LANCZOS)
        mincol = ImageTk.PhotoImage(minc)
        label3 = tk.Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)


root = tk.Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()