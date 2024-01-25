import tkinter
ready_to_clear = False
main_window = tkinter.Tk()

eq_label = tkinter.StringVar()

main_window.title("Python Calculator")
main_window.geometry("500x500")

label = tkinter.Label(main_window, textvariable=eq_label, font=("consolas", 24), fg="black",
                      bg="white", height=2, width=24)
label.pack()

def button_press(num):
    global ready_to_clear
    if ready_to_clear:
        eq_label.set("")
        ready_to_clear = False
    eq_text = eq_label.get() + str(num)
    eq_label.set(eq_text)


def equals():
    global ready_to_clear
    total = str(eval(eq_label.get()))
    eq_label.set(total)
    ready_to_clear = True


frame = tkinter.Frame(main_window)
frame.pack()


class NumButton:
    def __init__(self, num, row, column, width):
        button = tkinter.Button(frame, text=str(num), height=2, width=width, font=("consolas", 35),
                                command=lambda: button_press(num))
        button.grid(row=row, column=column)


button1 = NumButton(1, 0, 0, 4)
button2 = NumButton(2, 0, 1, 4)
button3 = NumButton(3, 0, 2, 4)

button4 = NumButton(4, 1, 0, 4)
button5 = NumButton(5, 1, 1, 4)
button6 = NumButton(6, 1, 2, 4)

button7 = NumButton(7, 2, 0, 4)
button8 = NumButton(8, 2, 1, 4)
button9 = NumButton(9, 2, 2, 4)

button0 = NumButton(0, 3, 0, 4)


class OpButton:
    def __init__(self, operator, row, column):
        button = tkinter.Button(frame, text=operator, height=2, width=4, font=("consolas", 35),
                                command=lambda: button_press(operator))
        button.grid(row=row, column=column)


plus = OpButton("+", 0, 3)
minus = OpButton("-", 1, 3)
multiply = OpButton("*", 2, 3)
divide = OpButton("/", 3, 3)

decimal = OpButton(".", 3, 1)

equalsbutton = tkinter.Button(frame, text="=", height=2, width=4, font=("consolas", 35), command=lambda: equals())
equalsbutton.grid(row=3, column=2)

main_window.mainloop()  # Main loop for the program
