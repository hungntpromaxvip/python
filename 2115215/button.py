from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Button")
        self.style = Style()
        self.style.theme_use("default")
  
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(frame, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(frame, text="OK")
        okButton.pack(side=RIGHT)


root = Tk()
root.geometry("300x200+300+300")
app = Example(root)
root.mainloop()