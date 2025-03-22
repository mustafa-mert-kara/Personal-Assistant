import tkinter as tk
import tkinter.messagebox
from datetime import datetime
from tkinter import ttk


class DetailWindow(ttk.Frame):
    def __init__(self, master,title,date,data,width=800,height=800):
        super().__init__(master,width=width,height=height)
        self.parent=master

        self.top=tk.Toplevel(master)
        self.top.geometry(f"{width}x{height}")
        self.top.title(title)
        self.center()

        self.curr_date=date
        self.data=data
        self.width=width
        self.height=height

        self.__canvas=tk.Canvas(self.top,height=self.height,width=self.width,bg="white")
        self.__canvas.grid(row=0,column=0)
        self.show_data()

    def show_data(self):
        position=10
        bias=20
        max_length=-1
        for val in self.data:
            string=str(val)
            if len(string)>max_length:
                max_length=len(string)
        print(max_length)
        for val in self.data:
            string=str(val)
            string_len=len(string)
            print(-max_length-(max_length-string_len))
            self.__canvas.create_text(max_length*3+3-(max_length-string_len)*3,position,text=string,fill="black")
            position+=bias
            if position>self.height-20:
                return
            

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