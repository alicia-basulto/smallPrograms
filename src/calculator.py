import tkinter as tk
import math
from tkinter import ttk
BUTTON_LIST = [
        ['7', '8', '9', '÷', 'log(x)'],
        ['4', '5', '6', 'x', '1/x'],
        ['1', '2', '3', '-', 'x!'],
        ['0', 'C', '=', '+', 'sqrt']
    ]
OPERATORS = ['x', '-', '+', '÷', '=']
FONT = ("Courier New", 20)

class Calculator:
    """The Calculator class is a GUI calculator implemented using the tkinter library in Python.
     It provides a graphical interface for performing
     basic arithmetic operations and other mathematical functions."""


    def __init__(self, master):
        """The __init__ method of the Calculator class initializes
        the calculator GUI and sets up the necessary components and layout."""
        self.master = master
        master.title("Calculator")
        master.geometry("1012x1024")
        self.total = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.total, font=("Courier New", 40), justify= "right", bg="black", fg="white")
        self.entry.grid(row=0, column=0, columnspan=105, pady=5)
        self.create_buttons()

        # Change the theme
        style = ttk.Style()
        style.theme_use("clam")
    def create_buttons(self):
        """The buttons are created and displayed on the calculator interface."""

        operators = ['x','-','+','÷','=']

        for i, row in enumerate(BUTTON_LIST):
            for j, button_text in enumerate(row):
                bg_color = "orange" if button_text in OPERATORS else "black"
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=FONT,
                    command=lambda text=button_text: self.click(text), bg=bg_color, fg="white",
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)

        for i in range(5):
            self.master.columnconfigure(i, weight=2)

    def click(self, button_text):
        """The click method is a part of the Calculator class
        and is responsible for handling button clicks in the calculator GUI.
         It performs different operations based on the button text
         and updates the display accordingly."""

        try:
            if button_text == '=':
                result = eval(self.entry.get())
                self.total.set(result)
            elif button_text == 'C':
                self.total.set("")
            elif button_text == 'log(x)':
                result = math.log(float(self.entry.get()))
                self.total.set(result)
            elif button_text == '1/x':
                result = 1 / float(self.entry.get())
                self.total.set(result)
            elif button_text == 'x!':
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            elif button_text == '10^x':
                result = 10 ** float(self.entry.get())
                self.total.set(result)
            elif button_text == 'sqrt':
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
            elif button_text == 'x':
                self.total.set(self.entry.get() + '*')
            elif button_text == '÷':
                self.total.set(self.entry.get() + '/')
            else:
                self.total.set(self.entry.get() + button_text)
        except:
            self.total.set("Error")




