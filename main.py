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
        self.button4 = Button(self, text="Debloat", command=self.fullDebloating)
        self.button5 = Button(self, text="Cleaner", command=self.fullCleaner)
        self.button6 = Button(self, text="Clear Logs", command=self.clearText)
        
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        
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
        return self.text.insert("end", self.op.powerplan() + '\n\n')
    
    @deco
    def powerOptimisation(self):
        results = self.op.power_optimisation()
        for path, valueName, value, rcode in results:
            text = "Something went wrong.\n\n" if rcode else f"{path}\nAdded \"{valueName}\" - \"{value}\"\n\n"
            self.text.insert("end", text)
        return
    
    @deco
    def memoryOptimisation(self):
        results = self.op.memory_optimisation()
        for result in results:
            if len(result) == 4:
                text = "Something went wrong.\n\n" if result[3] else f"{result[0]}\nAdded \"{result[1]}\" - \"{result[2]}\"\n\n"
                self.text.insert("end", text)
            else:
                text = "Something went wrong.\n\n" if result[1] else f"{result[0]}\n\n"
                self.text.insert("end", text)
        return
    
    @deco
    def fullDebloating(self):
        results = self.op.debloat()
        for result in results:
            if len(result) == 4:
                text = "Something went wrong.\n\n" if result[3] else f"{result[0]}\nAdded \"{result[1]}\" - \"{result[2]}\"\n\n"
                self.text.insert("end", text)
            else:
                text = "Unable to find the specified registry key or value.\n\n" if result[1] else f"Deleted \"{result[0]}\"\n\n"
                self.text.insert("end", text)

    @deco
    def fullCleaner(self):
        for result in self.op.cleaner():
            text = f"Unable to delete {result[0]}\n\n" if result[1] else f"Deleted {result[0]}\n\n"
            self.text.insert("end", text)


if __name__ == "__main__":
    app = Tk(className="Optimiser | By hurl")
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()