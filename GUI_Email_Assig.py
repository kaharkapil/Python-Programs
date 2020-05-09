from tkinter import *

root = Tk()

margin = 0.23
projectedSales = 100
profit = margin * int(projectedSales)

#My function that is linked to the event of my button
def profit_calculator(event):
    print(profit)


#the structure of the window
label_pan = Label(root, text="Projected annual sales:")
label_profit = Label(root, text="Projected profit")
label_result = Label(root, text=(profit), fg="red")

entry = Entry(root)

button_calc = Button(root, text= "Calculate", command=profit_calculator(1))
button_calc.bind("<Button-1>", profit_calculator(2))

#position of the elements on the window
label_pan.grid(row=0)
entry.grid(row=0, column=1)
button_calc.grid(row=1)              
label_profit.grid(row=2)
label_result.grid(row=2, column=1)

root.mainloop()
