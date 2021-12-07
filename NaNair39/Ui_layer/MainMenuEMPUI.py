from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
class EmployeeUI:
    def __init__(self, title = "staff"):
        self.title = title
        
        
    def staff_menu(self):
        
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        
        """print(f"Welcome {self.name}. Todays date is {today_string}")"""
        print("1. Locations and properties")
        print("2. Work requests/reports")
        """print("l. log out")"""
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            Ui_layer.PropertyMenu.PropertyMenu(title="staff").location_options()

        elif selection == "2":
            
            Ui_layer.WorkReportMenu.WorkReportMenu(title="staff").work_report_staff_menu()
            """elif selection.lower() == "l":
            on = False
            Main.main()"""
        elif selection.lower() == "q":
            pass
            
        else:
            print("Invalid option put into selection field.")
            self.staff_menu()

    