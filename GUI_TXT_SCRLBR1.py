from tkinter import*
from tkinter import font

window04=Tk()
dFont=font.Font(family="Helvetica",size=23,weight="bold")
lb=Text(window04,width=5,height=2,font=dFont)
lb.pack(side=LEFT,fill=BOTH,expand=YES)

yscrollbar=Scrollbar(window04,orient=VERTICAL,command=lb.yview)
yscrollbar.pack(side=RIGHT,fill=Y)
lb["yscrollcommand"]=yscrollbar.set

winow04.mainloop()
