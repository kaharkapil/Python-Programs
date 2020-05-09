from tkinter import*
from tkinter.ttk import*
from tkinter import ttk

tk=Tk()

style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='red')


progress=Progressbar(tk,orient=HORIZONTAL,length=100,mode='determinate',style='black.Horizontal.TProgressbar')

def bar():
     import time
     progress['value']=10
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=20
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=30
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=40
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=50
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=60
     tk.update_idletasks()
     time.sleep(1)
     
     progress['value']=70
     tk.update_idletasks()
     time.sleep(1)
     progress['value']=80
     tk.update_idletasks()
     time.sleep(1)
     progress['value']=90
     tk.update_idletasks()
     time.sleep(1)
     progress['value']=100
     tk.update_idletasks()
     time.sleep(1)
progress.pack()
Button(tk,text='Start',command=bar).pack()
tk.mainloop()
