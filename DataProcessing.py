import os
from Data import Data,ExpenseData,EventData,read_events,read_expenses

from datetime import datetime
class DataProcessor():
    def __init__(self,folder_path,expense_file,event_file):


        self.check_or_create_path("",folder_path)
        self.files={}
        self.file_paths={}
        self.file_paths["expenses"]=os.path.join(folder_path,expense_file)

        self.file_paths["events"]=os.path.join(folder_path,event_file)

        self.files["expenses"]=self.return_or_create_file(os.path.join(folder_path,expense_file))

        self.files["events"]=self.return_or_create_file(os.path.join(folder_path,event_file))
        


    def check_or_create_path(self,current_path,folder_path):
        if folder_path=="":
            return
        folders=os.path.normpath(folder_path).split(os.path.sep)
        if not os.path.exists(os.path.join(current_path,folders[0])):
           os.mkdir(os.path.join(current_path,folders[0]))
            

        self.check_or_create_path(os.path.join(current_path,folders[0]),"/".join(folders[1:]))

    def return_or_create_file(self,file_path):
        if not os.path.exists(file_path):
            f=open(file_path, "w+")
            f.flush()
        else:
            f=open(file_path, "a+")
        
        return f
    
    def write_to_file(self,data:Data):
        if type(data) is ExpenseData:
            mode="expenses"
        elif type(data) is EventData:
            mode="events"
        else:
            raise Exception("Wrong data type")
    
        data.write_to_file(self.files[mode])
        self.files[mode].flush()


    def create_data_object(self,data_features):
        if data_features[-1]==0:
            return ExpenseData(data_features[:-1])
        else:
            return EventData(data_features[:-1])
    
    def read_all_file(self,mode):
        fp=open(self.file_paths[mode])
        if mode=="expenses":            
            res= read_expenses(fp)
        else:            
            res= read_events(fp)
        fp.close()
        return res
    def prepare_expense_view(self):
        data=self.read_all_file("expenses")
        daily_total={}
        for val in data:
            if val.date not in daily_total:
                daily_total[val.date]=0
            daily_total[val.date]+=val.amount
        return data,daily_total
    def prepare_event_view(self):
        data=self.read_all_file("events")
        daily_events={}
        for val in data:
            if val.date not in daily_events:
                daily_events[val.date]=[]
            daily_events[val.date].append(val)
        return data,daily_events