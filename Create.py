from tkinter import *
from tkinter import messagebox

def create():
    name = "Name " + e1.get() + " " + e2.get() + " Added Successfully!"
    messagebox.showinfo("Dialog Box", name)
def read():
    my_list.append(name)
    messagebox.showinfo("Data", My_list)


def read():
    my_list.append(name)
    messagebocx.info("Data", my_list)
    
master = Tk()
Label(master, text='Employee Number').grid(row=0, padx=20, pady=10)
Label(master, text='Employee Name').grid(row=1, padx=20, pady=10)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1, padx=20, pady=10)
e2.grid(row=1, column=1, padx=20, pady=10)

b1 = Button(master, text="Add Employee", command=create)
b1.grid(row=2, column=1, padx=20, pady=10)
b2 = Button(master, text="Show List", command=create)
b2.grid(row=3, column=1, padx=20, pady=10)

mainloop()
