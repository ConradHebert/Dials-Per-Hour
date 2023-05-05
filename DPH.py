import tkinter as tk
from tkinter.font import Font
from datetime import datetime

class App:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        self.font = Font(size=20, weight='bold')

        self.label = tk.Label(master, text=str(self.counter), font=self.font, width=25, height=5)
        self.label.pack()

        self.master.bind("<Button-1>", self.increment_key)

        self.check_time()

        self.master.attributes("-topmost", True)

    def increment(self):
        self.counter += 1
        self.label.config(text=str(self.counter))

    def reset(self):
        self.counter = 0
        self.label.config(text=str(self.counter))

    def increment_key(self, event):
        self.increment()

    def check_time(self):
        now = datetime.now()
        if now.minute == 0 and now.second == 0:
            self.reset()
        self.master.after(1000, self.check_time)

root = tk.Tk()
app = App(root)
root.mainloop()