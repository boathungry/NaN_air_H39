from Ui_layer.main_login import LogIn
from datetime import date
from Ui_layer.PropertyMenu import PropertyMenu
from Ui_layer.WorkReportMenu import WorkReportMenu

class ManagerUI(LogIn):
    def __init__(self, name):
        super().__init__(name, staff_class="m")
        
    def managers_menu(self):
        on = True
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        while on:
            print(f"Welcome {self.name}. Todays date is {today_string}")
            print("1. Staff")
            print("2. Locations and properties")
            print("3. Work requests/reports")
            print("l. log out")
            print("q. quit")
            selection = input("Input selection: ")
            if selection == "1":
                self.staffing_options()
            elif selection == "2":
                PropertyMenu.location_options(self.staff_class)
            elif selection == "3":
                WorkReportMenu.WorkReportMenuMain()
            elif selection.lower() == "l":
                LogIn.main_menu
            elif selection.lower() == "q":
                on = False
            else:
                print("Invalid option put into selection field.")

    def staffing_options(self):
        on = True
        while on:
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
        
    