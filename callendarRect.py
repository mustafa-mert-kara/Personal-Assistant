import tkinter as tk
from tkinter import ttk


class CalendarSquare(ttk.Frame):
    def __init__(self, parent, tag, date,curr):
        tk.Frame.__init__(self, parent,width=500, height=500,background="white")
        self.__width=120
        self.__height=110
        self.tag=tag
        self.date=date
        self.__curr=curr
        self.__canvas = tk.Canvas(self,height=self.__height,width=self.__width,bg = '#afeeee')
        self.__canvas.pack(fill="both", expand=True)
        self.create_dateText()

    def create_dateText(self):
        if self.__curr:
            self.__canvas.create_text(self.__width-10,10,text=self.date,fill="black",font=('Helvetica 15'))
        else:
            self.__canvas.create_text(self.__width-10,10,text=self.date,fill="grey",font=('Helvetica 15'))

    def delete_rect(self):
        self.__canvas.delete("all")
        self.__canvas.configure(bg = 'white')