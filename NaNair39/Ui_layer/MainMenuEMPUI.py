from datetime import date
from Ui_layer.WorkReportMenu import WorkReportMenu
import Ui_layer.main_login
from Logic_layer.LLAPI import LLAPI
from Models.EmployeeModel import Employee
from Ui_layer.PropertyMenu import PropertyMenu
class EmployeeUI:
    def __init__(self, idnumber = "", name = "", email = "", location = "", title = "staff", logic_api:LLAPI = LLAPI()):
        self.idnumber = idnumber
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api
        
    def staff_menu(self):
        on = True
        while on:
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
                on = PropertyMenu(self.idnumber, self.name, self.email, self.location, self.title).location_options()
            elif selection == "2":
                on = WorkReportMenu(self.idnumber, self.name, self.email, self.location, self.title).work_report_staff_menu()
            elif selection == "3":
                contractorlist = self.llapi.list_all_contractors()
                self.llapi.list_printer(contractorlist)
                return self.staff_menu()
            elif selection.lower() == "q":
                on = False
            else:
                print("Invalid option put into selection field.")
                return self.staff_menu()

    