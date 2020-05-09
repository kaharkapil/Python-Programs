from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.filedialog

def file_save():
     f=tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".txt")
     if f is None:
         return
     text2save=str(text.get(1.0,END))
     f.write(text2save)
     f.close()
    

window=Tk()
window.title("Scrollbar")
window.geometry('350x200')

menu=Menu(window)
editmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=editmenu)
editmenu.add_command(label='Save',command=file_save)
editmenu.add_separator()
editmenu.add_command(label='Attendence')
editmenu.add_command(label='Profile')

dFont=font.Font(family = "Helvetica",size = 36,weight = "bold")
text=Text(window, width=5, height=2, font=dFont)
text.pack(side=LEFT, fill=BOTH, expand = YES)

yscrollbar=Scrollbar(window, orient=VERTICAL, command=text.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
text["yscrollcommand"]=yscrollbar.set

window.config(menu=menu)

window.mainloop()

