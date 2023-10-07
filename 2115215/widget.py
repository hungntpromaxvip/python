from tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
  
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
    
        cb = Checkbutton(self, text="Show Title", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)
        
        self.updateTitle()
  
    def onClick(self):
        self.updateTitle()
  
    def updateTitle(self):
        if self.var.get() == True:
            self.parent.title("Checked")
        else:
            self.parent.title("Unchecked")


root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()