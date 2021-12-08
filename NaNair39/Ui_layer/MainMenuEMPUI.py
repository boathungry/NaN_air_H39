from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login

class EmployeeUI:
    def __init__(self, ID, name, email, location, title):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        
    def staff_menu(self):
        
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        
        print(f"Welcome {self.title} member {self.name}. Todays date is {today_string}")
        print("1. Locations and properties")
        print("2. Work requests/reports")
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            current_user = Ui_layer.PropertyMenu.PropertyMenu(self.ID, self.name, self.email, self.location, self.title)
            current_user.location_options()

        elif selection == "2":
            
            current_user = Ui_layer.WorkReportMenu.WorkReportMenu(self.ID, self.name, self.email, self.location, self.title)
            current_user.work_report_staff_menu()
        elif selection.lower() == "q":
            pass
            
        else:
            print("Invalid option put into selection field.")
            self.staff_menu()

    