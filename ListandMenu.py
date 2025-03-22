import tkinter as tk
from tkinter import ttk
import datetime
import tkinter.font as TkFont

class Menu(ttk.Frame):
    def __init__(self, parent, tag,width,height):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        self.tag=tag
        self.parent_window=parent

        self.__height=height
        self.__width=width

        self.__menu=ttk.Frame(self)
        
        self.__menu.pack(expand=True, fill='both')


        self.__List=ttk.Frame(self)
        self.__List.pack(expand=True, fill='both')

        self.__add_buttons=ttk.Frame(self)
        self.__add_buttons.pack(expand=True, fill='both')
        
        self.create_menu()
        self.create_list()
        self.create_footer()

    def clean_list(self):
        self.__canvas.delete("all")
        
        

    def create_menu(self):
        expense_tracking=ttk.Button(self.__menu,text="Expense Tracking",command=lambda: self.parent_window.change_mode("expense"))
        expense_tracking.grid(row=0,column=0)        
        event_tracking=ttk.Button(self.__menu,text="Planned Events",command=lambda: self.parent_window.change_mode("event"))
        event_tracking.grid(row=0,column=1)
    
    def create_list(self):
        self.__canvas=tk.Canvas(self.__List,height=self.__height,width=self.__width,bg="white")
        self.__canvas.grid(row=1,column=0)
    
    def show_expenses(self,data,date):
        self.clean_list()
        current_data=list(filter(lambda x: x.date.month==date.month,data))
        current_data=sorted(current_data,key=lambda x: x.amount,reverse=True)
        max_length=-1
        for val in current_data:
            string=val.str_to()
            if len(string)>max_length:
                max_length=len(string)
        position=10
        bias=20
        for val in current_data:
            string=val.str_to()
            string_len=len(string)
            self.__canvas.create_text(max_length*3+3-(max_length-string_len)*3,position,text=string,fill="black")
            position+=bias
            if position>self.__height-20:
                return
        
    def show_events(self,data,date):
        self.clean_list()
        current_data=list(filter(lambda x: x.date.month==date.month,data))
        current_date=datetime.datetime.today().date()

        current_data=sorted(current_data,key=lambda x: abs((x.date-current_date).days))
        
        position=10
        bias=20
        max_length=-1
        for val in current_data:
            string=val.str_to()
            if len(string)>max_length:
                max_length=len(string)
        for val in current_data:
            string=val.str_to()
            string_len=len(string)
            self.__canvas.create_text(max_length*3+3-(max_length-string_len)*3,position,text=string,fill="black")
            position+=bias
            if position>self.__height-20:
                return
            
    def create_footer(self):
        add_expense=ttk.Button(self.__add_buttons,text="+Add Expense",command=lambda: self.parent_window.add_expense())
        add_expense.grid(row=0,column=0)        
        add_event=ttk.Button(self.__add_buttons,text="+Add Event",command=lambda: self.parent_window.add_event())
        add_event.grid(row=0,column=1)
        