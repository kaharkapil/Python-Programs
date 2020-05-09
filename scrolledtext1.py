from tkinter import *
from tkinter import font

#def ct(self):
#    self.Text.delete("1.0","end")

window=Tk()
menu = Menu(window)
# tearoff is use for floating members in menu
FileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=FileMenu)
FileMenu.add_command(label='New') #, command = ct
FileMenu.add_separator()
FileMenu.add_command(label='Open')
FileMenu.add_command(label='Exit', command=quit)

dFont=font.Font(family = "Helvetica",size = 36,weight = "bold")
lb=Text(window, width=5, height=2, font=dFont)
lb.pack(side=LEFT, fill=BOTH, expand = YES)

yscrollbar=Scrollbar(window, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"]=yscrollbar.set
window.config(menu=menu)
window.mainloop()


