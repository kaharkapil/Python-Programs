from tkinter import*
from tkinter import Menu
window=Tk()
window.title("welcome")
def newwindow():
    window1=Tk()
    window1.title("New Registration")
    window1.geometry('400x200')
    lb1=Label(window1,text="W_E_L_C_O_M_E ..........!!!!!!!")
    lb1.grid(column=0,row=2)


menu =Menu(window)
#tearoff is used foe floating members in menu

filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New registration',command=newwindow)
filemenu.add_separator()
filemenu.add_command(label='Add Marks')
filemenu.add_command(label='Exit',command=quit)
window.config(menu=menu)

editmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_separator()
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
window.config(menu=menu)


window.mainloop()
