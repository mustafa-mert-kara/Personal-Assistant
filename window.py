import tkinter as tk
from tkinter import ttk
from Calendar import CalendarFrame
from ListandMenu import Menu
from datetime import datetime
from DataProcessing import DataProcessor


class Window(tk.Tk):
    def __init__(self,width,height,data_processor,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{width}x{height}")
        
        self.data_processor=data_processor
       
        self.mode=""

        self.Calendar=CalendarFrame(self,"CalendarFrame",datetime.today())
        # self.Calendar.pack(expand=True, fill='both')
        self.Calendar.grid(row=0,column=0)
        self.List=Menu(self,"listandmenu")
        # self.List.pack(expand=True, fill='both',side="right")
        self.List.grid(row=0,column=1)
        self.change_mode("expense")


        

    def redraw(self, delay=1000):
        
        self.after(delay, lambda: self.redraw(delay))

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    def close(self):
        self.is_running=False

    def month_change(self):
        tmp=self.mode
        self.mode=""
        self.change_mode(tmp)

    def change_mode(self,new_mode):
        if new_mode=="expense" and self.mode!="expense":
            data,daily_data=self.data_processor.prepare_expense_view()
            self.Calendar.show_expenses(daily_data)
            self.List.show_expenses(data)
            self.mode="expense"
        elif new_mode=="event" and self.mode!="event":
            data,daily_data=self.data_processor.prepare_event_view()
            self.Calendar.show_events(daily_data)
            self.List.show_events(data)
            self.mode="event"