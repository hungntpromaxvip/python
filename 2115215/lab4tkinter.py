import tkinter as tk
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
  
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("hung nt")
        self.style = Style()
        self.style.theme_use("default")
  
        self.pack(fill=tk.BOTH, expand=True)
  
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)
  
root = tk.Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()