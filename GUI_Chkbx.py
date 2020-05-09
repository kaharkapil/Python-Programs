from tkinter.ttk import*
from tkinter import*

window=Tk()
window.title("Check-Box")
window.geometry('250x200')

chk_state=BooleanVar()
chk_state1=BooleanVar()
chk_state2=BooleanVar()

chk=Checkbutton(window,text='CPP',var=chk_state)
chk.grid(column=0,row=2)
#chk_state.set(True) #set check state

chk1=Checkbutton(window,text='PYTHON',var=chk_state1)
chk1.grid(column=0,row=3)

chk2=Checkbutton(window,text='JAVA',var=chk_state2)
chk2.grid(column=0,row=4)

window.mainloop()
