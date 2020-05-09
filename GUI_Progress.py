from tkinter import*
from tkinter.ttk import Progressbar
from tkinter import ttk

window03=Tk()
window03.title("Progress..")
window03.geometry('300x200')

style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='black')
bar=Progressbar(window03,length=150,style='black.Horizontal.TProgressbar')

bar['value']=15   
bar.grid(column=3,row=3)
