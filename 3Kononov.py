from tkinter import *
root = Tk()

t1 = Text(width=50, height=10)
t2 = Text(width=50, height=10)
b1 = Button(text="Save", font=("Arial", 24))
b2 = Button(text="Open", font=("Arial", 24))

t1.pack()
t2.pack()
b1.pack()

root.mainloop()