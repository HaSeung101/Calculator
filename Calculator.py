from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clearpress():
    global expression
    expression = ""
    equation.set("")

root = Tk()
root.title("Calculator")
root.geometry("260x160")
root.configure(bg="#1f1f1f")
#root.iconbitmap("calc_icon.ico")
root.resizable(False, False)

equation = StringVar()

expressionField = Entry(root, textvariable=equation)
expressionField.grid(row=0, column=0, columnspan=4, ipadx=65, pady=5)
expressionField.configure(fg='white', bg='#171717', borderwidth=2, highlightthickness=1,
                          highlightbackground='white')
equation.set("")

button1 = Button(root, text='9', fg='white', bg='#070707',
                 command=lambda: press(9), height=1, width=7, borderwidth=0) 
button1.grid(row=2, column=0, padx=5, pady=5) 
  
button2 = Button(root, text='8', fg='white', bg='#070707',
                 command=lambda: press(8), height=1, width=7, borderwidth=0) 
button2.grid(row=2, column=1, padx=5, pady=5)
  
button3 = Button(root, text='7', fg='white', bg='#070707',
                 command=lambda: press(7), height=1, width=7, borderwidth=0) 
button3.grid(row=2, column=2, padx=5, pady=5) 
  
button4 = Button(root, text='6', fg='white', bg='#070707',
                 command=lambda: press(6), height=1, width=7, borderwidth=0) 
button4.grid(row=3, column=0, padx=5, pady=5) 
  
button5 = Button(root, text='5', fg='white', bg='#070707',
                 command=lambda: press(5), height=1, width=7, borderwidth=0) 
button5.grid(row=3, column=1, padx=5, pady=5) 
  
button6 = Button(root, text='4', fg='white', bg='#070707',
                 command=lambda: press(4), height=1, width=7, borderwidth=0) 
button6.grid(row=3, column=2, padx=5, pady=5) 
  
button7 = Button(root, text='3', fg='white', bg='#070707',
                 command=lambda: press(3), height=1, width=7, borderwidth=0) 
button7.grid(row=4, column=0, padx=5, pady=5) 
  
button8 = Button(root, text='2', fg='white', bg='#070707',
                 command=lambda: press(2), height=1, width=7, borderwidth=0) 
button8.grid(row=4, column=1, padx=5, pady=5) 
  
button9 = Button(root, text='1', fg='white', bg='#070707',
                 command=lambda: press(1), height=1, width=7, borderwidth=0) 
button9.grid(row=4, column=2, padx=5, pady=5) 
  
button0 = Button(root, text='0', fg='white', bg='#070707',
                 command=lambda: press(0), height=1, width=7, borderwidth=0) 
button0.grid(row=5, column=0, padx=5, pady=5) 
  
plusButton = Button(root, text='+', fg='white', bg='#070707',
              command=lambda: press("+"), height=1, width=7, borderwidth=0) 
plusButton.grid(row=2, column=3, padx=5, pady=5) 
  
minusButton = Button(root, text='-', fg='white', bg='#070707',
               command=lambda: press("-"), height=1, width=7, borderwidth=0) 
minusButton.grid(row=3, column=3, padx=5, pady=5) 
  
multiplyButton = Button(root, text='*', fg='white', bg='#070707',
                  command=lambda: press("*"), height=1, width=7, borderwidth=0) 
multiplyButton.grid(row=4, column=3, padx=5, pady=5) 
  
divideButton = Button(root, text='/', fg='white', bg='#070707',
                command=lambda: press("/"), height=1, width=7, borderwidth=0) 
divideButton.grid(row=5, column=3, padx=5, pady=5) 
  
equalButton = Button(root, text='=', fg='white', bg='#070707',
               command=equalpress, height=1, width=7, borderwidth=0) 
equalButton.grid(row=5, column=2, padx=5, pady=5) 
  
clearButton = Button(root, text='C', fg='white', bg='#070707',
               command=clearpress, height=1, width=7, borderwidth=0) 
clearButton.grid(row=5, column=1, padx=5, pady=5) 
  
decimalButton = Button(root, text='.', fg='white', bg='#070707',
                command=lambda: press('.'), height=1, width=7, borderwidth=0) 
decimalButton.grid(row=6, column=0, padx=5, pady=5)

root.mainloop()
