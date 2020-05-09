from tkinter import*
from tkinter import Menu
from tkinter import ttk
import os
import tkinter.filedialog

def save_file():
     f=tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".txt")
     if f is None:
         return
     txt2sve=str(btns1.get(1.0,END))
     f.write(txt2sve)
     f.close()

#def sve():
#    print("Thank you...!!! Your Details are saved successfully!")

def studentwindow():
    window1=Tk()
    window1.title("Student")
    window1.geometry('650x500')
    lb1=Label(window1,text="Wel-Come ....Students......!!!!!!!")
    lb1.grid(column=4,row=0)
    
    lbls1=Label(window1,text="Name:")
    lbls1.grid(column=3,row=6)
    
    lbls2=Label(window1,text="Address")
    lbls2.grid(column=3,row=8)
    
    lbs3=Entry(window1,width=20)
    lbs3.grid(column=4,row=6)
    
    lbs4=Entry(window1,width=20)
    lbs4.grid(column=4,row=8)
    
    lbls5=Label(window1,text="Phone_No.")
    lbls5.grid(column=3,row=10)
    
    lbls6=Label(window1,text="Email")
    lbls6.grid(column=3,row=12)
    
    lbs7=Entry(window1,width=20)
    lbs7.grid(column=4,row=10)
    
    lbs8=Entry(window1,width=20)
    lbs8.grid(column=4,row=12)
    
    btns1=Button(window1,text="Save",bg="yellow",fg="blue",command=save_file)
    btns1.grid(column=4,row=14)
    window1.mainloop()

def facultywindow():
    window02=Tk()
    window02.title("Student")
    window02.geometry('650x500')
    lb1=Label(window02,text="Wel-Come........Sir/Mam ..........!!!!!!!")
    lb1.grid(column=4,row=0)
    
    lbls1=Label(window02,text="Name")
    lbls1.grid(column=3,row=6)
    
    lbls2=Label(window02,text="Address")
    lbls2.grid(column=3,row=8)
    
    lbs3=Entry(window02,width=20)
    lbs3.grid(column=4,row=6)
    
    lbs4=Entry(window02,width=20)
    lbs4.grid(column=4,row=8)
    
    lbls5=Label(window02,text="Phone_No.")
    lbls5.grid(column=3,row=10)
    
    lbls6=Label(window02,text="Email")
    lbls6.grid(column=3,row=12)
    
    lbs7=Entry(window02,width=20)
    lbs7.grid(column=4,row=10)
    
    lbs8=Entry(window02,width=20)
    lbs8.grid(column=4,row=12)

    lbls9=Label(window02,text="Subject")
    lbls9.grid(column=3,row=14)
   
    lbs10=Entry(window02,width=20)
    lbs10.grid(column=4,row=14)

    lbls9=Label(window02,text="Department:")
    lbls9.grid(column=3,row=16)
    coarse=["IT","EC","ME","CE","EE"]
    cb=ttk.Combobox(window02,values=coarse,width=18)
    cb.grid(column=4,row=16)

    rad1=Radiobutton(window02,text='Male',value=1)
    rad1.grid(column=4,row=18)
    rad2=Radiobutton(window02,text='Female',value=2)
    rad2.grid(column=5,row=18)
        
    btns1=Button(window02,text="Save",bg="yellow",fg="blue",command=sve)
    btns1.grid(column=4,row=20)
    window02.mainloop()

def notepad1():
     os.system("notepad.exe")

def MsPaint(): 
     os.system("mspaint.exe")

def cmra():
    os.startfile('C:\Program Files (x86)\ArcSoft\WebCam Companion 3\\uWebCam.exe')
     
def clc():
     os.system("calc.exe")
     
def mainwindow():
       window=Tk()
       window.title("Welcome.............!!!!!!!!")
       window.geometry('650x500')
       menu =Menu(window)
       #tearoff is used foe floating members in menu
                    #NEW
       filemenu=Menu(menu,tearoff=0)
       menu.add_cascade(label='New',menu=filemenu)
       filemenu.add_command(label='Student',command=studentwindow)
       filemenu.add_separator()
       filemenu.add_command(label='Faculty',command=facultywindow)
       filemenu.add_separator()
       filemenu.add_command(label='Exit',command=quit)
       window.config(menu=menu)
                    #EDIT
       editmenu=Menu(menu,tearoff=0)
       menu.add_cascade(label='Edit',menu=editmenu)
       editmenu.add_command(label='Marks',)
       editmenu.add_separator()
       editmenu.add_command(label='Attendence')
       editmenu.add_command(label='Profile')
       window.config(menu=menu)
      
                  #OPEN
       opnmenu=Menu(menu,tearoff=0)
       menu.add_cascade(label='Open',menu=opnmenu)
       opnmenu.add_command(label='Notepad',command=notepad1)
       opnmenu.add_separator()
       opnmenu.add_command(label='Paint',command=MsPaint)
       opnmenu.add_separator()
       opnmenu.add_command(label='Calculator',command=clc)
       opnmenu.add_separator()
       opnmenu.add_command(label='Camera',command=cmra)
       window.config(menu=menu)
       window.mainloop()
       
#Login Window.............                   
window01=Tk()
window01.title("Login_Window")
window01.geometry('650x500')

lbl1=Label(window01,text="User_name:")
lbl1.grid(column=3,row=4)
lbl2=Label(window01,text="Password:")
lbl2.grid(column=3,row=6)

lb3=Entry(window01,width=20)
lb3.grid(column=4,row=4)
lb4=Entry(window01,width=20)
lb4.grid(column=4,row=6)

btn1=Button(window01,text="Login...",command=mainwindow,)
btn1.grid(column=5,row=7)

window01.mainloop()







