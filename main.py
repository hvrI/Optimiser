from optimise import *
from tkinter import *

class GUI(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        app.geometry("800x400")
        self.op = Optimiser()
        
        
        self.text = Text(self, state='disabled', height=6, width=40)
        self.text.pack(side="left", fill="both", expand=True)
        
    def powerOptimisation(self):
        return
    
    def memoryOptimisation(self):
        return


if __name__ == "__main__":
    app = Tk(className="Optimiser | By hurl")
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()