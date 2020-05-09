#Generrate the GUI Tkinter window
from tkinter import*
import csv
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import font

window=Tk()
window.title("Welcome to CRISP")
window.geometry('500x400')

#create control label

lbl=Label(window,text='User_name')
lbl.grid(column=0,row=0)

lb2=Label(window,text='Password')
lb2.grid(column=0,row=1)

lb3=Label(window,text="")
lb3.grid(column=1,row=4)

txt=Entry(window,width=30)
txt.grid(column=1,row=0)

txt2=Entry(window,show="*",width=30)
txt2.grid(column=1,row=1)


btn1=Button(window,text="Click here to continue.....",bg="green",fg="black")
btn1.grid(column=1,row=20)

rad1=Radiobutton(window,text='Male',value=1)
rad1.grid(column=0,row=3)
rad2=Radiobutton(window,text='Female',value=2)
rad2.grid(column=2,row=3)

lb4=Label(window,text="Address")
lb4.grid(column=0,row=21)

#scrolledtext
txt3=scrolledtext.ScrolledText(window,width=25,height=3,bg="yellow")
txt3.grid(column=1,row=21)

btn3=Button(window,text="EXIT",bg="red",fg="white")
btn3.grid(column=7,row=25)

#from tkinter to importvvttk
coarse=["python","java","c++"]
cb=ttk.Combobox(window,values=coarse,width=23)
cb.grid(column=2,row=28)

#STYLE
style=ttk.Style()
style.configure("BW.TLabel",foreground="blue",background="pink")
myfont=font.Font(family="Helvetica",size=20,weight='bold')

lb5=ttk.Label(text="Heloooo....Bhayyu",style="BW.TLabel")
lb5.grid(column=2,row=30)
lb6=ttk.Label(window,text="This is style",style="BW.TLabel",font=myfont)
lb6.grid(column=2,row=32)


def csvbutton():
    with open("dataemail.csv",'r') as csvfile:
         reader=csv.reader(csvfile)
         for row in reader:
            print(row[3])
def clicked():
    lb3.configure(text="button was clicked..!!!!")
    window1=Tk()
    window1.title("Window2")
    window1.geometry('350x200')
    lbl1=Label(window1,text="Welcome to window2")
    lbl1.grid(column=2,row=3)
    lbl2=Label(window1,text='text2')
    lbl2.grid(column=0,row=5)
bttn1=Button(window,text="open_csv_file",command=csvbutton)
bttn1.grid(column=2,row=15)


    
btn=Button(window,text="Login..",bg="blue",command=clicked)
btn.grid(column=1,row=15)

    
window.mainloop()
