from window import Window
from DataProcessing import DataProcessor
import datetime
import random
import os

def main():
    
    data_processor=DataProcessor("Data","expenses.csv","events.csv")

    # for _ in range(100):
    #     delta=random.randint(-30,30)
    #     expense_data=data_processor.create_data_object([(datetime.datetime.today()+datetime.timedelta(days=delta)).date(),"Food",random.randint(150,500),"YemekSepeti Lahmacun","CreditCard",0])

    #     # event_data=data_processor.create_data_object([datetime.datetime.today().date(),"Deneme Toplantısı","","",True,"tmp","Deneme","willdelete",1])        
    #     data_processor.write_to_file(expense_data)

    for _ in range(100):
        delta=random.randint(-30,30)
        # expense_data=data_processor.create_data_object([(datetime.datetime.today()+datetime.timedelta(days=delta)).date(),"Food",random.randint(150,500),"YemekSepeti Lahmacun","CreditCard",0])

        event_data=data_processor.create_data_object([(datetime.datetime.today()+datetime.timedelta(days=delta)).date(),"Toplanti","","",True,"tmp","Deneme","willdelete",1])        
        data_processor.write_to_file(event_data)
    
    # expenses=data_processor.read_all_file("events")
    # for val in expenses:
    #     print(val)

    program_window=Window(1200,800,data_processor)


    program_window.mainloop()




if __name__=="__main__":
    main()