from datetime import date
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
<<<<<<< HEAD
"""import Main"""
=======
import Logic_layer.LLAPI
#import Main
>>>>>>> af08d48a85a77809a569318da6dbcaa9d13547dc
class ManagerUI:
    def __init__(self):
        self.staff_class = "manager"
        
        
    def managers_menu(self):
        on = True
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
<<<<<<< HEAD
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
=======
        
        """print(f"Welcome {self.name}. Todays date is {today_string}")"""
        print("1. Staff")
        print("2. Locations and properties")
        print("3. Work requests/reports")
        print("l. log out")
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            self.staffing_options()
        elif selection == "2":
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
>>>>>>> af08d48a85a77809a569318da6dbcaa9d13547dc

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

<<<<<<< HEAD
                #vantar klasa til að breyta starfsfólki
            elif selection == "3":
                #vantar klasa til að fá lista yfir starfsfólk
                pass
            elif selection == "4":
                #vantar klasa til að leita í starfsfólki
                pass
            elif selection.lower() == "b":
=======
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
    def create_employee(self):
        name = input("What is the name of the new employee?: ")
        email = input("What is the employees email address?: ")
        location = input("What location does the employee work at?: ")
        address = input("What is the address of the employee?: ")
        phone = input("What is the employees phone number?: ")
        cellphone = input("What is the employees cellphone number?: ")
        title = input('Is the employee a "manager" or a regular "staff" member?: ')
        createemployeloop = True
        while createemployeloop:
            print("Is this the correct information?")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Location: {location}")
            print(f"Address: {address}")
            print(f"Phone: {phone}")
            print(f"Cellphone: {cellphone}")
            print(f"Title: {title}")
            rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
            if rightorwrong.lower() == "y":
                createemployeloop == False
                Logic_layer.LLAPI.LLAPI.create_employee(name, email, location, address, phone, cellphone, title)
            elif rightorwrong.lower() == "c":
                createemployeloop == False
>>>>>>> af08d48a85a77809a569318da6dbcaa9d13547dc
                self.managers_menu()
            elif selection.lower() == "q":
                on = False
            else:
                print("Invalid option put into selection field.")
        
    