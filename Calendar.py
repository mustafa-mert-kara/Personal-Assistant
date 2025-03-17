import tkinter as tk
from tkinter import ttk
import datetime
from callendarRect import CalendarSquare
import tkinter.font as TkFont

class CalendarFrame(ttk.Frame):
    def __init__(self, parent, tag, date,width=840,height=760):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        self.curr_date=date
        self.width=width
        self.height=height
        self.header_height=100
        self.parent=parent

        self.rect_width,self.rect_height=self.calculate_rect_size()
        self.date_list=self.create_date_list(self.curr_date)
        self.tag=tag
        
        self.__menu=ttk.Frame(self,width=self.width,height=self.header_height)
        
        # self.__menu.pack(expand=True, fill='both')
        self.__menu.grid(row=0,column=0)
        self.create_header()
        
        self.CalendarFrame=ttk.Frame(self,width=self.width,height=self.height)
        # self.CalendarFrame.pack(expand=True, fill='both',padx=10,pady=10)
        self.CalendarFrame.grid(row=1,column=0)
        self.rect = {} 
        # self.create_body(self.date_list)
        self.build_calendar()

    def build_calendar(self,next_date=None):
        if len(self.rect)!=0:
            self.clean_calendar()
        if next_date is not None:
            self.date_list=self.create_date_list(next_date)
        self.clean_calendar()
        self.create_body(self.date_list)
        self.create_header()
        

    def create_date_list(self,today_date):
        date_list=[]
        date_list.append(today_date)
        curr_date=today_date-datetime.timedelta(days=1)
        while curr_date.month==today_date.month:
            date_list.append(curr_date)
            curr_date-=datetime.timedelta(days=1)
            
        curr_date=today_date+datetime.timedelta(days=1)
        while curr_date.month==today_date.month:
            date_list.append(curr_date)
            curr_date+=datetime.timedelta(days=1)
            
        date_list=sorted(date_list)
        month_begining=date_list[0]
        counter=month_begining.weekday()
        month_begining-=datetime.timedelta(days=1)
        
        while counter!=0:            
            date_list.insert(0,month_begining)
            month_begining-=datetime.timedelta(days=1)
            counter-=1
        month_ending=date_list[-1]
        counter=month_ending.weekday()
        month_ending+=datetime.timedelta(days=1)        
        while counter!=6:
            date_list.append(month_ending)
            month_ending+=datetime.timedelta(days=1)
            counter+=1
        
        return date_list

    def create_body(self,date_list):   
        current_date=datetime.datetime.today().date()
        row_count=len(date_list)//7
        active_month=self.date_list[15].month
        for column in range(7):
            for row in range(row_count):
                date=date_list[row*7+column]
                if date.month!=active_month:
                    incurrent=False
                else:
                    incurrent=True
                self.rect[date.date()] = CalendarSquare(self.CalendarFrame,f"{row}+{column}",str(date.day),incurrent,self.rect_width,self.rect_height)
                self.rect[date.date()].grid(row=row,column=column,sticky='nswe',padx=(0,0),pady=(0,0))
                if date.date()==current_date:
                    self.rect[date.date()].mark_current_day()
    def create_header(self):
        previous=ttk.Button(self.__menu,text="<",command=lambda: self.change_month("prev"))
        previous.grid(row=0,column=0)
        self.header_canvas=tk.Canvas(self.__menu,height=self.header_height,width=self.width-115)
        self.header_canvas.grid(row=0,column=1)
        self.header_canvas.create_text(365,50,text=self.date_list[15].strftime("%B"),font=TkFont.Font(family='fixed',size=20))
        next_month=ttk.Button(self.__menu,text=">",command=lambda: self.change_month("next"))
        next_month.grid(row=0,column=2)

        
        
    def clean_calendar(self):
        for val in self.rect:
            self.rect[val].delete_rect()
        self.header_canvas.delete("all")

    def change_month(self,mode):
        if mode=="next":
            next_date=self.date_list[15]+datetime.timedelta(days=30)            
        else:
            next_date=self.date_list[15]-datetime.timedelta(days=30)
        self.build_calendar(next_date=next_date)        
        self.header_canvas.create_text(365,50,text=self.date_list[15].strftime("%B"),font=TkFont.Font(family='fixed',size=20))
        self.parent.month_change(next_date)



    def calculate_rect_size(self):
        return self.width//7,(self.height-self.header_height)//6
    
    def show_expenses(self,dail_expenses):
        for date in self.date_list:
            date=date.date()
            if date in dail_expenses.keys():
                self.rect[date].show_expense(dail_expenses[date])

        curr_date=datetime.datetime.today().date()
        monthly_sum=0
        for _ in range(31):
            if curr_date in dail_expenses.keys():
                monthly_sum+=dail_expenses[curr_date]
            curr_date-=datetime.timedelta(days=1)
        self.rect[datetime.datetime.today().date()].show_monthly_expense(monthly_sum)
        

        
    def show_events(self,daily_events):
        for date in self.date_list:
            date=date.date()
            if date in daily_events.keys():
                self.rect[date].show_event(daily_events[date])
        