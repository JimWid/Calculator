from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('My Calculator :D')
root.geometry('300x220')
MyFrame = Frame(root)
MyFrame.pack()
Result = 0

#----------------Putting the Entries--------------
e1= Entry(MyFrame) #Number 1
e2 = Entry(MyFrame) #Number 2
e3 = Entry(MyFrame) #Result
e1.grid(row = 1, column = 2, columnspan = 5)
e2.grid(row = 3, column = 2, columnspan = 5)
e3.grid(row = 8, column = 2, columnspan = 5)
 
#----------------Putting the labels--------------
Label_1 = Label(MyFrame, text = 'Number 1')
Label_2 = Label(MyFrame, text = 'Number 2')
Label_3 = Label(MyFrame, text = 'The Result')
Label_1.grid(row = 0, column = 2, columnspan = 5)
Label_2.grid(row = 2, column = 2, columnspan = 5)
Label_3.grid(row = 7, column = 2, columnspan = 5)

#-------------Putting the results functions-------------
def result_A():
    N1 = e1.get()
    global f_num
    global math
    math = 'Addition'
    f_num = int(N1)

def result_S():
    N1 = e1.get()
    global f_num
    global math
    math = 'Subtraction'
    f_num = int(N1)

def result_M():
    N1 = e1.get()
    global f_num
    global math
    math = 'Multiplication'
    f_num = int(N1)

def result_D():
    N1 = e1.get()
    global f_num
    global math
    math = 'Division'
    f_num = int(N1)

#-------------Putting the equal buttom conditions------------
def equal_Button():
    N2 = e2.get()

    if math == 'Addition':
        e3.insert(0, f_num + int(N2))
    if math == 'Subtraction':
        e3.insert(0, f_num - int(N2))
    if math == 'Multiplication':
        e3.insert(0, f_num * int(N2))
    if math == 'Division':
        e3.insert(0, f_num / int(N2))

#--------------Clear Button functions------------------
def Clear_Button1():
    e1.delete(0, END)

def Clear_Button2():
    e2.delete(0, END)

def Clear_Button3():
    e3.delete(0, END)
    
#-------------Buttons----------------width = 9, height = 4
addition = Button(MyFrame, text = '+', command = result_A) 

substraction = Button(MyFrame, text = '-', command = result_S) 

multiplication = Button(MyFrame, text = '×', command = result_M)

division = Button(MyFrame, text = '÷', command = result_D) 

equal = Button(MyFrame, text = 'ENTER', command = equal_Button) 

clear1 = Button(MyFrame, text = 'Clear', command = Clear_Button1)

clear2 = Button(MyFrame, text = 'Clear', command = Clear_Button2)

clear3 = Button(MyFrame, text = 'Clear', command = Clear_Button3)

#------------------Positions-------------
addition.grid(row = 4, column = 2)

substraction.grid(row = 4, column = 3)

multiplication.grid(row = 5, column = 2)

division.grid(row = 5, column = 3)

equal.grid(row = 6, column = 2, columnspan = 2)

clear1.grid(row = 1, column = 1)

clear2.grid(row = 3, column = 1)

clear3.grid(row = 8, column = 1)

root.mainloop()