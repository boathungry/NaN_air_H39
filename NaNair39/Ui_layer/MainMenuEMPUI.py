from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
class EmployeeUI:
    def __init__(self, title = "staff"):
        self.title = title
        
        
    def managers_menu(self):
        
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        
        """print(f"Welcome {self.name}. Todays date is {today_string}")"""
        print("1. Locations and properties")
        print("2. Work requests/reports")
        """print("l. log out")"""
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            Ui_layer.PropertyMenu.PropertyMenu(EmployeeUI).location_options()

        elif selection == "3":
            
            Ui_layer.WorkReportMenu.WorkReportMenu.WorkReportMenuMain()
            """elif selection.lower() == "l":
            on = False
            Main.main()"""
        elif selection.lower() == "q":
            pass
            
        else:
            print("Invalid option put into selection field.")
            self.managers_menu()

    def staffing_options(self):
        
        print("1. Register a new staff member")
        print("2. Edit information about a staff member")
        print("3. Get staff list")
        print("4. Search for a staff member")
        print("b. back to main menu")
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            pass
            #vantar klasa til að búa til starfsfólk
        elif selection == "2":
            staffmail = input("What is the email of the employee you wish to edit: ")

            #vantar klasa til að breyta starfsfólki
        elif selection == "3":
            #vantar klasa til að fá lista yfir starfsfólk
            pass
        elif selection == "4":
            #vantar klasa til að leita í starfsfólki
            pass
        elif selection.lower() == "b":
            self.managers_menu()
        elif selection.lower() == "q":
            on = False
        else:
            print("Invalid option put into selection field.")
            self.staffing_options()