from controller import Controller
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Window():

    # Root
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('300x300')
        self.win.title('Calculator')
        self.win.config(bg='#e66312')
        self.widgets()
        self.win.mainloop()

    # Widgets
    
    def widgets(self):

        # Title
        self.title = Label(self.win, text='Sum two numbers', bg='#e66312')
        self.title.place(x= 100, y= 20)

        # Entry
        self.label1 = Label(self.win, text='First number:', bg='#e66312')
        self.label1.place(x=20, y= 70)

        self.label2 = Label(self.win, text='Second number:', bg='#e66312')
        self.label2.place(x=20, y= 100)

        self.label3 = Label(self.win, text='Result:', bg='#e66312')
        self.label3.place(x=20, y= 140)

        self.entry1 = Entry(self.win)
        self.entry1.place(x=120, y= 70)
        self.entry1.focus()
        self.entry1.delete(0, END)

        self.entry2 = Entry(self.win)
        self.entry2.place(x= 120, y= 100)
        self.entry2.delete(0, END)

        self.entry3 = Entry(self.win, width=15)
        self.entry3.place(x=120, y= 140)
        self.entry3.delete(0, END)

        # Button

        self.button_sum = Button(self.win, text='Sum', width=20, command= self.call_controller_sum)
        self.button_sum.place(x=80, y= 200)

        self.button_rest = Button(self.win, text='Rest', width=20, command= self.call_controller_rest)
        self.button_rest.place(x=80, y= 220)

        self.button_mult = Button(self.win, text='Multiply', width=20, command= self.call_controller_mult)
        self.button_mult.place(x=80, y= 240)

        self.button_div = Button(self.win, text='Divide', width=20, command= self.call_controller_div)
        self.button_div.place(x=80, y= 260)

    # Functions

    def call_controller_sum(self):
        Controller.get_data(self, self.entry1, self.entry2, '+', self.entry3)

    def call_controller_rest(self):
        Controller.get_data(self, self.entry1, self.entry2, '-', self.entry3)

    def call_controller_mult(self):
        Controller.get_data(self, self.entry1, self.entry2, '*', self.entry3)

    def call_controller_div(self):
        Controller.get_data(self, self.entry1, self.entry2, '/', self.entry3)