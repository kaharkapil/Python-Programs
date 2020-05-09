from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import askopenfile

window=Tk()
window.geometry('350x200')

def Open_file():
     file=askopenfile(mode='r',filetype=[('Python Files','.py')])
     if file is not None:
           content=file.read()
           print(content)

btn=Button(window,text='Open',command=lambda:Open_file)
btn.pack(side=TOP,pady=10)
window.mainloop()
