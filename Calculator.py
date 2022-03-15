# Thomas Simpson
# Calculator Program
# 05/07/21



# Importing Modules
import tkinter as tk
from tkinter.font import Font



# Defining methods
def build_window():

    # Button Size
    button_height = 10
    button_width = 10


    # Building window
    root = tk.Tk()
    root.geometry("500x800+300+300")
    root.config(background="white")

    # Current equation display
    global display_text
    display_text = tk.StringVar()
    display = tk.Label(root, textvariable=display_text, width=40, height=3, font=("Courier", 15))
    display.grid(row = 1, column = 1, columnspan = 4)

    # Button functions
    functions = []


    # Function Factory
    def make_f(z):
        def f():
            global display_text
            display_text.set(display_text.get() + str(z))
        return f



    # Making buttons
    # Numbers
    counter1 = 1
    counter2 = 2
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:

        num_button = tk.Button(root, text=x, command=make_f(x), height=button_height, width=button_width)
        num_button.grid(row= counter2, column = counter1)

        counter1 += 1
        if counter1 == 4:
            counter1 = 1
            counter2 += 1



    # Operators
    operators = ["+", "-", "*", "/"]
    counter = 2

    for x in operators:

        operator_button = tk.Button(root, text=x, command= make_f(x), height=button_height, width=button_width)
        operator_button.grid(row = counter, column = 4)
        counter += 1



    # Brackets
    brackets = ["(", ")"]
    counter = 2

    for x in brackets:

        brackets_button = tk.Button(root, text=x, command=make_f(x), height=button_height, width=button_width)
        brackets_button.grid(row=5, column=counter)
        counter +=1



    # Equals button
    def run_input():

        global display_text
        display_text.set((eval(display_text.get())))

    equals_button = tk.Button(root, text="=", command= run_input, height=button_height, width=button_width)
    equals_button.grid(row = 6, column = 1)



    # Delete Button
    def backspace():

        global display_text
        string = display_text.get()
        display_text.set(string[:len(string)-1])

    delete_button = tk.Button(root, text="del", command=backspace, height=button_height, width=button_width)
    delete_button.grid(row=6, column=2)


    root.mainloop()
    return root



# --- Main program --- #
def main_program():

    root = build_window()

    while True:
        root.update_idletasks()
        root.mainloop()



# Running program
main_program()