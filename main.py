import time
from optimise import *
from tkinter import *



class GUI(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        file_path = os.path.realpath(__file__)
        modificationTime = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(os.path.getatime(file_path)))

        self.app = app
        self.app.title("Optimiser 0.0.1")
        self.app.geometry("800x405")
        self.op = Optimiser()

        self.menu = Menu(self.app)
        self.systemMenu(self.menu)
        self.app.config(menu=self.menu)
        
        self.text = Text(self, state='disabled', height=23, width=77)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.place(x=150, y=10)
        self.vsb.pack(side="right", fill="y")
        
        self.lastUsedLabel = Label(self, text=f"Last used at: {modificationTime}", font=("Arial", 8)).pack(anchor="w", side="bottom")
        
        self.button1 = Button(self, text="Powerplan", height=1, width=17, command=self.addPowerplan)
        self.button2 = Button(self, text="Power Optimisation", height=1, width=17, command=self.powerOptimisation)
        self.button3 = Button(self, text="Memory Optimisation", height=1, width=17, command=self.memoryOptimisation)
        self.button4 = Button(self, text="Debloat", height=1, width=17, command=self.fullDebloating)
        self.button5 = Button(self, text="Cleaner", height=1, width=17, command=self.fullCleaner)
        self.button6 = Button(self, text="Game Booster", height=1, width=17, command=self.gameOptimisation)
        self.button7 = Button(self, text="Clear Logs", height=1, width=17, command=self.clearText)

        self.button1.place(x=10, y=10)
        self.button2.place(x=10, y=50)
        self.button3.place(x=10, y=90)
        self.button4.place(x=10, y=130)
        self.button5.place(x=10, y=170)
        self.button6.place(x=10, y=210)
        self.button7.place(x=10, y=250)

    def deco(func):
        def inner(self):
            self.text.configure(state='normal')
            func(self)
            self.text.see("end")
            self.text.configure(state='disabled')
        return inner

    @deco
    def about(self):
        top = Toplevel(self.app)
        top.geometry("300x150")
        top.title("About Optimiser")
        Label(top, text = "Optimiser 0.0.1\n\nCopyright (C) 2022-2022\n\nOptimiser is a free program that optimise\npc for a better performance.\n\nOwned by hurl").pack(side=TOP)

    @deco
    def exit(self):
        self.app.quit()

    def systemMenu(self, menu):
        submenu = Menu(menu, tearoff=0)
        submenu.add_command(label="About", command=self.about)
        submenu.add_separator()
        submenu.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="System", menu=submenu)
    
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

    @deco
    def gameOptimisation(self):
        results = self.op.gameBooster()
        for path, valueName, value, rcode in results:
            text = "Something went wrong.\n\n" if rcode else f"{path}\nAdded \"{valueName}\" - \"{value}\"\n\n"
            self.text.insert("end", text)
        return


if __name__ == "__main__":
    app = Tk()
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()