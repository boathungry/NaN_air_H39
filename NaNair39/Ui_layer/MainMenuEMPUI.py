from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
from Logic_layer.LLAPI import LLAPI

class EmployeeUI:
    def __init__(self, ID, name, email, location, title,logic_api:LLAPI = LLAPI()):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api
        
    def staff_menu(self):
        
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        print("")
        print(f"Welcome {self.name}. Todays date is {today_string}")
        print("")
        print("1. Locations and properties")
        print("2. Work requests/reports")
        print("3. Get a list of contractors")
        print("q. quit")
        print("")
        selection = input("Input selection: ")
        if selection == "1":
            current_user = Ui_layer.PropertyMenu.PropertyMenu(self.ID, self.name, self.email, self.location, self.title)
            current_user.location_options()

        elif selection == "2":
    
            current_user = Ui_layer.WorkReportMenu.WorkReportMenu(self.ID, self.name, self.email, self.location, self.title)
            current_user.work_report_staff_menu()
        
        elif selection == "3":
            contractorlist = self.llapi.list_all_contractors()
            self.llapi.list_printer(contractorlist)
            self.staff_menu()

        elif selection.lower() == "q":
            pass
            
        else:
            print("Invalid option put into selection field.")
            self.staff_menu()

    