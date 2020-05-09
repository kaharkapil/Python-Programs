from tkinter import*
from tkinter import ttk

def msgbx():
     from tkinter import messagebox
     re=messagebox.askquestion('Welcome..','Congrats..Login successful,Do You Want To Continue')

def lgn():
    window01=Tk()
    window01.title("Login_Window")
    window01.geometry('200x200')

    lbl1=Label(window01,text="User_name:")
    lbl1.grid(column=3,row=0)
    lbl2=Label(window01,text="Password:")
    lbl2.grid(column=3,row=2)

    lb3=Entry(window01,width=20)
    lb3.grid(column=4,row=0)
    lb4=Entry(window01,width=20)
    lb4.grid(column=4,row=2)

    btn1=Button(window01,text="Continue......",command=msgbx)
    btn1.grid(column=4,row=3)
     

window=Tk()
window.title("Welcome.....")
window.geometry('350x200')

tab_control=ttk.Notebook(window)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)

tab_control.add(tab1,text='Student Details')
tab_control.add(tab2,text='Attendence')
tab_control.add(tab3,text='Results')

lbl1=Button(tab1,text='Login',command=lgn)
lbl1.grid(column=0,row=0)

tab_control.pack(expand=1,fill='both')

window.mainloop()
