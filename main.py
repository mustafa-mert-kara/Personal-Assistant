from window import Window
from DataProcessing import DataProcessor
import datetime

import os

def main():
    
    data_processor=DataProcessor("Data","expenses.csv","events.csv")

    # expense_data=data_processor.create_data_object([datetime.datetime.today().date(),"Food",300,"YemekSepeti Lahmacun","CreditCard",0])

    event_data=data_processor.create_data_object([datetime.datetime.today().date(),"Deneme Toplantısı","","",True,"tmp","Deneme","willdelete",1])
    data_processor.write_to_file(event_data)
    data_processor.write_to_file(event_data)

    expenses=data_processor.read_all_file("events")
    for val in expenses:
        print(val)

    program_window=Window(1200,800,data_processor)


    program_window.mainloop()




if __name__=="__main__":
    main()