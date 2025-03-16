from abc import ABC,abstractmethod
from datetime import datetime

class Data(ABC):

    @abstractmethod
    def write_to_file(self,file):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __eq__(self, value):
        pass
    


class EventData(Data):
    def __init__(self,data_features):
        """
        Data Structure:
        Date
        Event Name
        Event_start?
        Event_end?
        Event_duration? Allday: True | some hours: False
        tags: **
        """

        if data_features is not None:
            self.date=datetime.strptime(data_features[0], '%Y-%m-%d').date()
            self.name=data_features[1]
            self.start=data_features[2]
            self.end=data_features[3]
            self.duration=data_features[4]
        self.tags=[]
        if len(data_features)>5:
            for val in data_features[5:]:
                self.tags.append(val)

    def write_to_file(self, file):
        write_str=f"{self.date},{self.name},{self.start},{self.end},{self.duration}"
        for tag in self.tags:
            write_str+=f",{tag}"
        write_str+="\n"
        file.write(write_str)
    def __str__(self):
        write_str=f"Date: {self.date}, Name: {self.name}, Event Start: {self.start}, End: {self.end}, isAllDay: {self.duration} Tags: "
        for tag in self.tags:
            write_str+=f",{tag}"
        return write_str
    def __eq__(self, value):
        if self.date==value.date and self.name==value.name and self.duration==value.duration and self.start==value.start and self.end == value.end:
            for val in self.tags:
                if val not in value.tags:
                    return False
            if len(self.tags)==len(value.tags):
                return True
        return False
    
    def str_to(self):
        return f"{self.date}::{self.name}::{self.duration}"
    

class ExpenseData(Data):
    def __init__(self,data_features=None):
        """
        Data Structure:
        Date
        Expense Type
        Expense Amount
        Expense Details
        Expense From?
        """
        if data_features is not None:
            self.date=datetime.strptime(data_features[0], '%Y-%m-%d').date()
            self.type=data_features[1]
            self.amount=int(data_features[2])
            self.source=data_features[3]
            self.details=data_features[4]

        super().__init__()

    def write_to_file(self, file):
        file.write(f"{self.date},{self.type},{self.amount},{self.source},{self.details}\n")

    def str_to(self):
        return f"{self.date}::{self.type}::{self.amount}"

    def __str__(self):
        return f"{self.date},{self.type},{self.amount},{self.source},{self.details}"
    def __eq__(self, value):
        if self.date==value.date and self.type == value.type and self.amount == value.amount and self.source==value.source and self.details==value.details:
            return True
        return False


def read_events(file):
    event_list=[]
    for line in file:
        new_event=EventData(line[:-1].split(","))
        event_list.append(new_event)
    return event_list

def read_expenses(file):
    expense_list=[]
    for line in file:
        new_expense=ExpenseData(line[:-1].split(","))
        expense_list.append(new_expense)
    return expense_list