import tkinter as tk
import tkinter.messagebox
from datetime import datetime
from tkinter import ttk
from abc import ABC, abstractmethod

class InputWindow(ttk.Frame,ABC):
    def __init__(self, master,title,width=300,height=400):
        super().__init__(master,width=width,height=height)
        self.parent=master

        self.top=tk.Toplevel(master)
        self.top.geometry("300x400")
        self.top.title(title)
        self.center()

        self.curr_date=datetime.today().date()
        self.width=width
        self.height=height
        self.input_frame=ttk.Frame(self.top,width=self.width,height=self.height)
        
        # self.__menu.pack(expand=True, fill='both')
        self.input_frame.grid(row=0,column=0)
        self.send_button=ttk.Button(self.top,text="Add",command=lambda: self.send_input())
        self.send_button.grid(row=1,column=0)
        self.create_components()

    @abstractmethod
    def create_components(self):
        pass
    @abstractmethod
    def create_input(self):
        pass
    @abstractmethod
    def send_input(self):
        pass
    
    def center(self):
        self.top.update_idletasks()

        # Tkinter way to find the screen resolution
        # screen_width = self.toplevel.winfo_screenwidth()
        # screen_height = self.toplevel.winfo_screenheight()

        # PyQt way to find the screen resolution
        
        screen_width = 1920
        screen_height = 1200

        size = tuple(int(_) for _ in self.top.geometry().split('+')[0].split('x'))
        x = screen_width/2 - size[0]/2
        y = screen_height/2 - size[1]/2

        self.top.geometry("+%d+%d" % (x, y))

class ExpenseInput(InputWindow):
    def __init__(self, master,title):
        super().__init__(master,title)
        
    def create_components(self):
        
        date_label = tk.Label(self.input_frame, text="Date")
        date_label.pack()
        self.date_entry = tk.Entry(self.input_frame)
        self.date_entry.insert(0,datetime.today().date())
        self.date_entry.pack()

        type_label = tk.Label(self.input_frame, text="Expense Type")
        type_label.pack()
        self.type_entry = tk.Entry(self.input_frame)
        self.type_entry.pack()

        amount_label = tk.Label(self.input_frame, text="Expense Amount")
        amount_label.pack()
        self.amount_entry = tk.Entry(self.input_frame)
        self.amount_entry.pack()

        detail_label = tk.Label(self.input_frame, text="Details")
        detail_label.pack()
        self.detail_entry = tk.Entry(self.input_frame)
        self.detail_entry.pack()
        
        from_label = tk.Label(self.input_frame, text="From")
        from_label.pack()
        self.from_entry = tk.Entry(self.input_frame)
        self.from_entry.insert(0,"Credit Card")
        self.from_entry.pack()

    def create_input(self):
        input_dict={}
        input_dict["date"]=self.date_entry.get()
        input_dict["type"]=self.type_entry.get()
        input_dict["amount"]=self.amount_entry.get()
        input_dict["detail"]=self.detail_entry.get()
        input_dict["from"]=self.from_entry.get()
        if input_dict["date"]=="" or not is_it_date(input_dict["date"]):
            tkinter.messagebox.showinfo(self.top,"Date is Wrong or Missing")
            raise ValueError()

        if input_dict["amount"]=="" or not str.isdigit(input_dict["amount"]):
            tkinter.messagebox.showinfo(self.top,"Amount is Wrong or Missing")
            raise ValueError()



        return input_dict

    def send_input(self):
        try:
            input_dict=self.create_input()
            self.parent.new_input(input_dict)
        except:
            return
        
class EventInput(InputWindow):
    def __init__(self, master,title):
        super().__init__(master,title)
        
    def create_components(self):
        
        date_label = tk.Label(self.input_frame, text="Date")
        date_label.pack()
        self.date_entry = tk.Entry(self.input_frame)
        self.date_entry.insert(0,datetime.today().date())
        self.date_entry.pack()

        name_label = tk.Label(self.input_frame, text="Event Name")
        name_label.pack()
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.pack()

        start = tk.Label(self.input_frame, text="Event Start")
        start.pack()
        self.start_entry = tk.Entry(self.input_frame)
        self.start_entry.pack()

        end = tk.Label(self.input_frame, text="Event End")
        end.pack()
        self.end_entry = tk.Entry(self.input_frame)
        self.end_entry.pack()
        
        all_day = tk.Label(self.input_frame, text="All Day")
        all_day.pack()
        self.all_day_entry = tk.IntVar()
        tk.Checkbutton(self.input_frame,variable=self.all_day_entry).pack()
        

        tags_label = tk.Label(self.input_frame, text="Tags")
        tags_label.pack()
        self.tags_entry = tk.Entry(self.input_frame)
        self.tags_entry.pack()

    def create_input(self):
        input_dict={}
        input_dict["date"]=self.date_entry.get()
        input_dict["name"]=self.name_entry.get()
        input_dict["start"]=self.start_entry.get()
        input_dict["end"]=self.end_entry.get()

        input_dict["allday"]=self.all_day_entry.get()==1
        input_dict["tags"]=self.tags_entry.get()
        print(self.all_day_entry.get()==1)
        if input_dict["date"]=="" or not is_it_date(input_dict["date"]):
            tkinter.messagebox.showinfo(self.top,"Date is Wrong or Missing")
            raise ValueError()

        if input_dict["name"]=="":
            tkinter.messagebox.showinfo(self.top,"Name is Missing")
            raise ValueError()



        return input_dict

    def send_input(self):
        try:
            input_dict=self.create_input()
            self.parent.new_input(input_dict)
        except:
            return


def is_it_date(string):
    try:
        tmp=len(string.split("-"))
        print(tmp)
        if tmp==3:
            return True
        tmp=len(string.split("/"))
        print(tmp)
        if tmp==3:
            return True
        tmp=len(string.split("."))
        print(tmp)
        if tmp==3:
            return True
        

        return False
    except:
        return False