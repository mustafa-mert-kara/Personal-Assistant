import tkinter as tk
from tkinter import ttk
from Calendar import CalendarFrame
from callendarRect import CalendarSquare
from datetime import datetime

class Window(tk.Tk):
    def __init__(self,width,height,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{width}x{height}")
        
       
        self.rows = 100
        self.columns = 100
        self.cellwidth = 100
        self.cellheight = 100

        self.Calendar=CalendarFrame(self,"CalendarFrame",datetime.today())
        self.Calendar.pack(expand=True, fill='both')
        # self.CalendarFrame=ttk.Frame(self)
        # self.CalendarFrame.pack(expand=True, fill='both',padx=10,pady=10)
        # tmp=CalendarSquare(self.CalendarFrame,"asd","15",True)
        # tmp.pack()    
        

    def redraw(self, delay=1000):
        
        self.after(delay, lambda: self.redraw(delay))

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    def close(self):
        self.is_running=False