import tkinter as tk
from tkinter import ttk


class CalendarSquare(ttk.Frame):
    def __init__(self, parent, tag, date,curr,width,height,fulldate):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        self.__width=width
        self.__height=height
        self.tag=tag
        self.date=date
        self.__curr=curr
        self.__canvas = tk.Canvas(self,height=self.__height,width=self.__width,bg = '#afeeee')
        self.__canvas.pack(fill="both", expand=True)
        self.__canvas.bind("<Button-1>",lambda x: parent.master.parent.detailed_daily(fulldate))
        self.create_dateText()
        

    def mark_current_day(self):
        coords=list(self.__canvas.bbox("date_number"))
        coords[0]-=3
        coords[2]+=1

        self.__canvas.create_oval(coords)
        

    def create_dateText(self):
        if self.__curr:
            self.__canvas.create_text(self.__width-10,10,text=self.date,fill="black",font=('Helvetica 15'),tags="date_number")
        else:
            self.__canvas.create_text(self.__width-10,10,text=self.date,fill="grey",font=('Helvetica 15'),tags="date_number")

    def delete_rect(self):
        self.__canvas.delete("all")
        self.__canvas.configure(bg = 'white')

    def show_expense(self,amount):
        self.__canvas.create_text(45,self.__height//2,text=f"Amount: {amount}",fill="black")
    def show_monthly_expense(self,amount):
        self.__canvas.create_text(50,self.__height//2+20,text=f"Monthly: {amount}",fill="black")
    
    def find_max_length(self,events):
        max_length=-1
        for val in events:
            string=str(val.name)
            if len(string)>max_length:
                max_length=len(string)
        if max_length>18:
            max_length=14
        return max_length
    
    def show_event(self,events):
        bias=20
        vertical=self.__height//2-bias
        max_length=self.find_max_length(events)
        if len(events)>2:
            events=events[:2]  

        for event in events:
                string=event.name
                string_len=len(string)
                if string_len>max_length:
                    string=string[:max_length-3]+"..."
                    string_len=max_length
                self.__canvas.create_text(max_length*3+3-(max_length-string_len)*3,vertical,text=f"{string}",fill="black")
                vertical+=bias
        
        if len(events)>2:      
            self.__canvas.create_text(40,vertical,text="...",fill="black")

        