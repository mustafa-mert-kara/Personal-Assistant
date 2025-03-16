import tkinter as tk
from tkinter import ttk
from Calendar import CalendarFrame
from ListandMenu import Menu
from datetime import datetime


class Window(tk.Tk):
    def __init__(self,width,height,data_processor,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{width}x{height}")
        
        self.data_processor=data_processor
       

        self.Calendar=CalendarFrame(self,"CalendarFrame",datetime.today())
        # self.Calendar.pack(expand=True, fill='both')
        self.Calendar.grid(row=0,column=0)
        self.List=Menu(self,"listandmenu")
        # self.List.pack(expand=True, fill='both',side="right")
        self.List.grid(row=0,column=1)


        

    def redraw(self, delay=1000):
        
        self.after(delay, lambda: self.redraw(delay))

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    def close(self):
        self.is_running=False

    def change_mode(self,new_mode):
        pass