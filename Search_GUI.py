import os,fnmatch
from tkinter import*

window=Tk()
window.title('Search')
window.geometry('500x500')

Pattern=StringVar()
Path=StringVar()


def filesrch(pattern,path):
    result=[]
    for root,dirs,files in os.walk(path):
         for name in files:
              if fnmatch.fnmatch(name,pattern):
                  result.append(os.path.join(root,name))
    
    print('\n',result)
def find_file():
     pattern1=Pattern.get()
     path1=Path.get()
     filesrch(pattern1,path1)




label_1 = Label(window, text="Type_of_FILES",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(window,textvar=Pattern)
entry_1.place(x=240,y=130)

label_2 = Label(window, text="Path:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(window,textvar=Path)
entry_2.place(x=240,y=180)

Button(window, text='Search',width=20,bg='brown',fg='white',command=find_file).place(x=180,y=380)
window.mainloop()




      
     
     
