from tkinter import*
from tkinter.font import Font
from tkinter import ttk

window03=Tk()
window03.title("Spin Bar...")
window03.geometry('300x200')


spin=Spinbox(window03,from_=0,to=100,width=5,font=Font(family='Helvetica',size=36,weight='bold'))
spin.pack()

window03.mainloop()
