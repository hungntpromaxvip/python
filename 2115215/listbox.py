from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Gun")
        self.pack(fill=BOTH, expand=1)

        Gun = ["AK Asimov", "AWM Dragon Lore", "Desert Eagle Printstream", "M4A1 Wibu", "M4A1-S (M4A1 Silent)", "Galil AR (IDF Sentinel 22)", "FAMAS (Clarion 5.56)"]

        lb = Listbox(self)

        for i in Gun:
            lb.insert(END, i)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, textvariable=self.var)
        self.label.pack()

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        if idx:
            value = sender.get(idx[0])
            self.var.set(value)


root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()