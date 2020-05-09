from tkinter import *
import pyodbc

window=Tk()
window.title("Registration Form")
window.geometry('500x400')

Name=StringVar()
Address=StringVar()

def datastore():
     name=Name.get()
     address=Address.get()

     conn=pyodbc.connect("Driver={SQL Server Native Client 11.0}; Server=202.66.174.144,1533; Database=igecsagar; Uid=igecsagar; Pwd=bhopal*123;")
     with conn:
         cursor=conn.cursor()
     #cursor.execute("CREATE TABLE Students1(Name TEXT,Address TEXT)")
     cursor.execute("INSERT INTO Students1(Name,Address) VALUES(?,?)",(name,address,))
     conn.commit()
     print("Successfull.......::::")

 

label0=Label(window,text="Registration form")
label0.place(x=90,y=53)

label1=Label(window,text="Name:")
label1.place(x=80,y=130)

label2=Label(window,text="Address:")
label2.place(x=68,y=180)

entry1=Entry(window)
entry1.place(x=240,y=130)

entry2=Entry(window)
entry2.place(x=240,y=180)

btn=Button(window,text="Submit",command=datastore)
btn.place(x=180,y=380)

window.mainloop()

