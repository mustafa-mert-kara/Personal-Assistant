import tkinter as tk

from tkinter import ttk
from Calendar import CalendarFrame
from ListandMenu import Menu
from datetime import datetime
from DataProcessing import DataProcessor
from inputWin import ExpenseInput,EventInput
from detailsWin import DetailWindow


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

    def rebuild_calendar(self):
        self.Calendar.clean_calendar()
        self.Calendar.build_calendar()
        self.List.clean_list()

    def create_infos(self):
        if self.mode=="expense":
            data,daily_data=self.data_processor.prepare_expense_view()
            self.rebuild_calendar()
            self.Calendar.show_expenses(daily_data)            
            self.List.show_expenses(data,self.current_date)
        elif self.mode=="event":
            data,daily_data=self.data_processor.prepare_event_view()
            self.rebuild_calendar()
            self.Calendar.show_events(daily_data)
            self.List.show_events(data,self.current_date)

    def change_mode(self,new_mode):
        if new_mode=="expense" and self.mode!="expense":            
            self.mode="expense"
            self.create_infos()
        elif new_mode=="event" and self.mode!="event":           
            self.mode="event"
            self.create_infos()

    def add_expense(self):        
        ExpenseInput(self,title="Add Expense")
        

        
    def add_event(self):
        EventInput(self,title="Add Event")
        
    def new_input(self,input_dict):
        if "amount" in input_dict:
            new_data=self.data_processor.create_expense(input_dict)
        else:
            new_data=self.data_processor.create_event(input_dict)

        self.data_processor.write_to_file(new_data)
        self.create_infos()

    def detailed_daily(self,date):
        if self.mode=="expense":
            data,_=self.data_processor.prepare_expense_view()
            title="Expense Details For "+str(date)
            sort_logic=lambda x: x.amount
            reverse=True
        elif self.mode=="event":
            data,_=self.data_processor.prepare_event_view()
            title="Event Details For "+str(date)
            sort_logic=lambda x: abs((x.date-date).days)
            reverse=False


        current_data=list(filter(lambda x: x.date==date,data))
        print(current_data)
        current_data=sorted(current_data,key=sort_logic,reverse=reverse)
        DetailWindow(self,title,date,current_data)

        print(date)
        
        


