from tkinter import *
import parser
import math

root = Tk()
root.geometry("270x240")
root.title('Calculator')

# get the user input and place it in the textfield
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def calculate():
    entire_string = display.get()
    global i
    i = 0
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()

        display.insert(0, result)
        i+= len(str(result))
    except Exception:
        clear_all()
        display.insert(0, "Error")


def factor():
    entire_string = display.get()
    global i
    i = 0
    if len(entire_string) != 0:

        a = parser.expr(entire_string).compile()
        result = eval(a)
        result = math.factorial(result)
        clear_all()
        display.insert(0, result)
        i += len(str(result))
    else:
        clear_all()
        display.insert(0,"Error")


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def clear_all():
    display.delete(0, END)
    global i


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
# adding the input field
display = Entry(root, font = '44')
display.grid(row=1, columnspan=6, sticky=W + E,padx=5,pady=5)

# adding buttons to the calculator

Button(root, text="1", width=5, height=2, command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="2",  width=5, height=2, command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="3", width=5, height=2, command=lambda: get_variables(3)).grid(row=2, column=2)

Button(root, text="4", width=5, height=2, command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", width=5, height=2, command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", width=5, height=2, command=lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="7", width=5, height=2, command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", width=5, height=2, command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", width=5, height=2, command=lambda: get_variables(9)).grid(row=4, column=2)

# adding other buttons to the calculator
Button(root, text="AC", width=5, height=2, command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", width=5, height=2, command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", width=5, height=2, command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", width=5, height=2, command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", width=5, height=2, command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", width=5, height=2, command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", width=5, height=2, command=lambda: get_operation("/")).grid(row=5, column=3)

# adding new operations
Button(root, text="pi", width=5, height=2, command=lambda: get_operation("*3.15")).grid(row=2, column=4)
Button(root, text="%", width=5, height=2, command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(", width=5, height=2, command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", width=5, height=2, command=lambda: get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", width=5, height=2, command = lambda: undo()).grid(row=2, column=5)
Button(root, text="x!", width=5, height=2, command=lambda: factor()).grid(row=3, column=5)
Button(root, text=")", width=5, height=2, command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text="^", width=5, height=2, command=lambda: get_operation("**")).grid(row=5, column=5)

root.mainloop()
