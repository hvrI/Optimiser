import time
import tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.text = tk.Text(self, height=6, width=40)
        #self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        #self.text.configure(yscrollcommand=self.vsb.set)
        #self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        

        self.add_timestamp()
        
    def deco(func):
        def inner(self):
            self.text.configure(state='normal')
            func(self)
            self.text.see("end")
            self.text.configure(state='disabled')
        return inner

    @deco
    def add_timestamp(self):
        self.text.insert("end", time.ctime() + "\n")
        #self.text.see("end")
        self.after(1000, self.add_timestamp)

if __name__ == "__main__":
    root =tk.Tk()
    frame = Example(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()