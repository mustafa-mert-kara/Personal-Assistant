import tkinter as tk
from tkinter import ttk
import datetime
from callendarRect import CalendarSquare

class CalendarFrame(ttk.Frame):
    def __init__(self, parent, tag, date):
        tk.Frame.__init__(self, parent,width=500, height=500,background="white")
        self.curr_date=date
        
        self.tag=tag
        self.date_list=self.create_date_list(self.curr_date)
        print(self.date_list[0],self.date_list[-1],len(self.date_list))
        # self.__menu=ttk.Frame(self)
        # self.__menu.pack(expand=True, fill='both')
        
        
        self.CalendarFrame=ttk.Frame(self)
        self.CalendarFrame.pack(expand=True, fill='both',padx=10,pady=10)
        self.rect = {} 
        self.create_body(self.date_list)

        

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
        row_count=len(date_list)//7
        for column in range(7):
            for row in range(row_count):
                date=date_list[row*7+column]
                if date.month!=self.curr_date.month:
                    incurrent=False
                else:
                    incurrent=True
                self.rect[row,column] = CalendarSquare(self.CalendarFrame,f"{row}+{column}",str(date.day),incurrent)
                self.rect[row,column].grid(row=row,column=column,sticky='nswe',padx=(0,0),pady=(0,0))
                