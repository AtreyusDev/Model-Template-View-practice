from model import Calculator
from tkinter import messagebox
from tkinter import *

class Controller():
    def __init__(self):
        pass

    def get_data(self, entry1, entry2, operation, entry_total):
        value1 = entry1.get()
        value2 = entry2.get()
        if len(value1) == 0 or len(value2) == 0:
            return messagebox.showerror('Empty Fields', 'The field´s values must be grater than 0.')
        else:
            if value1.isdigit() and value2.isdigit():
                total = Calculator.Calculate(self, int(value1), int(value2), operation)
                entry_total.delete(0, END)
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry_total.insert(0, total)
            else:
                messagebox.showerror('Invalid Fields', 'The fields just allow numbers.')
                