from tkinter import messagebox
re=messagebox.askquestion('Thanks','Message content')
print(re)
re=messagebox.askyesno('Thanks','Message content')
print(re)
re=messagebox.askyesnocancel('Data Save..','Do you want to save the data')
print(re)
if re==True:
    print("You choosed to save the file")
elif re==false:
    print("You choosed NO")
else:
    print("None")
re=messagebox.askokcancel('Message title','Message Content')
print(re)
re=messagebox.askretrycancel('Welcome','last Dialog,Thanks')
print(re)



