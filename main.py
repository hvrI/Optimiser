from optimise import *
from tkinter import *

class GUI(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        app.geometry("800x400")
        self.op = Optimiser()
        
        self.text = Text(self, state='disabled', height=2, width=30)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        
        self.button1 = Button(self, text="Powerplan", command=self.addPowerplan)
        self.button2 = Button(self, text="Power Optimisation", command=self.powerOptimisation)
        self.button3 = Button(self, text="Memory Optimisation", command=self.memoryOptimisation)
        self.button4 = Button(self, text="Clear Logs", command=self.clearText)
        
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        
    def deco(func):
        def inner(self):
            self.text.configure(state='normal')
            func(self)
            self.text.see("end")
            self.text.configure(state='disabled')
        return inner
    
    @deco
    def clearText(self):
        self.text.delete('1.0', END)
        
    @deco
    def addPowerplan(self):
        return self.text.insert("end", self.op.powerplan())
    
    @deco
    def powerOptimisation(self):
        results = self.op.power_optimisation()
        for path, valueName, value in results:
            text = f"{path}\nAdded {valueName} - {value}\n\n"
            self.text.insert("end", text)
        return
    
    @deco
    def memoryOptimisation(self):
        results = self.op.memory_optimisation()
        for path, valueName, value in results:
            text = f"{path}\nAdded {valueName} - {value}\n\n"

            self.text.insert("end", text)
        return


if __name__ == "__main__":
    app = Tk(className="Optimiser | By hurl")
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()