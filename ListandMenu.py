import tkinter as tk
from tkinter import ttk
import datetime
import tkinter.font as TkFont

class Menu(ttk.Frame):
    def __init__(self, parent, tag):
        tk.Frame.__init__(self, parent,width=100, height=100,background="white")
        self.tag=tag
        self.parent_window=parent

        self.__menu=ttk.Frame(self)
        
        self.__menu.pack(expand=True, fill='both')


        self.__List=ttk.Frame(self)
        self.__List.pack(expand=True, fill='both')
        
        self.create_menu()

    def create_menu(self):
        expense_tracking=ttk.Button(self.__menu,text="Expense Tracking",command=lambda: self.parent_window.change_mode("expense"))
        expense_tracking.grid(row=0,column=0)        
        event_tracking=ttk.Button(self.__menu,text="Planned Events",command=lambda: self.parent_window.change_mode("event"))
        event_tracking.grid(row=0,column=1)
