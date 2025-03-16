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

        self.__calendar_width=840
        self.__calendar_height=760

        self.current_date=datetime.today().date()
       
        self.mode=""

        self.Calendar=CalendarFrame(self,"CalendarFrame",datetime.today(),height=self.__calendar_height,width=self.__calendar_width)
        # self.Calendar.pack(expand=True, fill='both')
        self.Calendar.grid(row=0,column=0)
        self.List=Menu(self,"listandmenu",height=self.__calendar_height-170,width=width-self.__calendar_width-50)
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

    def month_change(self,next_date):
        tmp=self.mode
        self.mode=""
        self.current_date=next_date
        self.change_mode(tmp)
        

    def change_mode(self,new_mode):
        if new_mode=="expense" and self.mode!="expense":
            data,daily_data=self.data_processor.prepare_expense_view()
            self.Calendar.clean_calendar()
            self.Calendar.build_calendar()
            self.Calendar.show_expenses(daily_data)
            self.List.clean_list()
            self.List.show_expenses(data,self.current_date)
            self.mode="expense"
        elif new_mode=="event" and self.mode!="event":
            data,daily_data=self.data_processor.prepare_event_view()
            self.Calendar.clean_calendar()
            self.Calendar.build_calendar()
            self.Calendar.show_events(daily_data)
            self.List.clean_list()
            self.List.show_events(data,self.current_date)
            self.mode="event"