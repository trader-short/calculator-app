#basic calculator app
from tkinter import *

#create a function to add input
def press(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#create a function to clear input
def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

#create a function to evaluate the results
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)

expression = ""

# create a GUI window
gui = Tk()
# set the title of GUI window
gui.title("Calculator")

#set the configuration of GUI window
gui.geometry("270x150")

# StringVar() is the variable class
# we create an instance of this class
input_text = StringVar()

# create the text entry box for
# showing the expression .
expression_field = Entry(gui, textvariable=input_text,font=('arial',10,'bold'))

# grid method is used for placing
# the widgets at respective positions
# in table like structure .
expression_field.grid(columnspan=4, ipadx=70)


button1 = Button(gui, text=' 1 ', bg="#eee",fg="black",command=lambda: press(1), height=1, width=7,cursor="hand2")
button1.grid(row=2, column=0)

button2 = Button(gui, text=' 2 ', bg="#eee",fg="black",command=lambda: press(2), height=1, width=7,cursor="hand2")
button2.grid(row=2, column=1)

button3 = Button(gui, text=' 3 ', bg="#eee",fg="black",command=lambda: press(3), height=1, width=7,cursor="hand2")
button3.grid(row=2, column=2)

button4 = Button(gui, text=' 4 ', bg="#eee",fg="black",command=lambda: press(4), height=1, width=7,cursor="hand2")
button4.grid(row=3, column=0)

button5 = Button(gui, text=' 5 ', bg="#eee",fg="black",command=lambda: press(5), height=1, width=7,cursor="hand2")
button5.grid(row=3, column=1)

button6 = Button(gui, text=' 6 ', bg="#eee",fg="black",command=lambda: press(6), height=1, width=7,cursor="hand2")
button6.grid(row=3, column=2)

button7 = Button(gui, text=' 7 ', bg="#eee",fg="black",command=lambda: press(7), height=1, width=7,cursor="hand2")
button7.grid(row=4, column=0)

button8 = Button(gui, text=' 8 ', bg="#eee",fg="black",command=lambda: press(8), height=1, width=7,cursor="hand2")
button8.grid(row=4, column=1)

button9 = Button(gui, text=' 9 ', bg="#eee",fg="black",command=lambda: press(9), height=1, width=7,cursor="hand2")
button9.grid(row=4, column=2)

button0 = Button(gui, text=' 0 ', bg="#eee",fg="black",command=lambda: press(0), height=1, width=7,cursor="hand2")
button0.grid(row=5, column=0)

plus = Button(gui, text=' + ', bg="#eee",fg="black",command=lambda: press("+"), height=1, width=7,cursor="hand2")
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', bg="#eee",fg="black",command=lambda: press("-"), height=1, width=7,cursor="hand2")
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', bg="#eee",fg="black",command=lambda: press("*"), height=1, width=7,cursor="hand2")
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', bg="#eee",fg="black",command=lambda: press("/"), height=1, width=7,cursor="hand2")
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', bg="#eee",fg="black",command=btn_equal, height=1, width=7,cursor="hand2")
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', bg="#eee",fg="black",command=btn_clear, height=1, width=7,cursor="hand2")
clear.grid(row=5, column='1')

Decimal= Button(gui, text='.', bg="#eee",fg="black",command=lambda: press('.'), height=1, width=7,cursor="hand2")
Decimal.grid(row=6, column=0)


gui.mainloop()
