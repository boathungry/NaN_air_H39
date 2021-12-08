from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
"""import Main"""
<<<<<<< HEAD
import Logic_layer.LLAPI
#import Main
=======
>>>>>>> b95217144dc85bd080b9d01a58e1213e02ba3606
class ManagerUI:
    def __init__(self, name, email, location, title = "manager"):
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        
        
    def managers_menu(self):
        
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        while on:
            """print(f"Welcome {self.name}. Todays date is {today_string}")"""
            print("1. Staff")
            print("2. Locations and properties")
            print("3. Work requests/reports")
            """print("l. log out")"""
            print("q. quit")
            selection = input("Input selection: ")
            if selection == "1":
                on = False
                self.staffing_options(self)
            elif selection == "2":
                on = False
                Ui_layer.PropertyMenu.PropertyMenu.location_options_mangers()
            elif selection == "3":
                on = False
                Ui_layer.WorkReportMenu.WorkReportMenu.WorkReportMenuMain()
                """elif selection.lower() == "l":
                on = False
                Main.main()"""
            elif selection.lower() == "q":
                on = False
                
            else:
                print("Invalid option put into selection field.")
<<<<<<< HEAD
=======

    def staffing_options(self):
>>>>>>> b95217144dc85bd080b9d01a58e1213e02ba3606
        
        print("1. Register a new staff member")
        print("2. Edit information about a staff member")
        print("3. Get staff list")
        print("4. Search for a staff member")
        print("b. back to main menu")
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            self.create_employee()
            
        elif selection == "2":
<<<<<<< HEAD
            Ui_layer.PropertyMenu.PropertyMenu(title= "manager").location_options()
        elif selection == "3":
            Ui_layer.WorkReportMenu.WorkReportMenu(title= "manager").Work_report_manager_menu()
            """elif selection.lower() == "l":
            on = False
            Main.main()"""
        elif selection.lower() == "q":
            pass 
        else:
            print("Invalid option put into selection field.")
            self.managers_menu()

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
=======
            staffmail = input("What is the email of the employee you wish to edit: ")
>>>>>>> b95217144dc85bd080b9d01a58e1213e02ba3606

                #vantar klasa til að breyta starfsfólki
        elif selection == "3":
            #vantar klasa til að fá lista yfir starfsfólk
            pass
        elif selection == "4":
            #vantar klasa til að leita í starfsfólki
            pass
        elif selection.lower() == "b":
            self.managers_menu()
        elif rightorwrong.lower() == "n":
            print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
            fieldchange = input("Input the letter of the field you wish to change")
            if fieldchange.lower() == "n":
                name = input("What is the name of the new employee?: ")
            elif fieldchange.lower() == "l":
                location = input("What location does the employee work at?: ")
            elif fieldchange.lower() == "a":    
                address = input("What is the address of the employee?: ")
            elif fieldchange.lower() == "p":
                phone = input("What is the employees phone number?: ")
            elif fieldchange.lower() == "c":
                cellphone = input("What is the employees cellphone number?: ")
            elif fieldchange.lower() == "t":
                title = input('Is the employee a "manager" or a regular "staff" member?: ')
            else:
                print("Wrong input!")

