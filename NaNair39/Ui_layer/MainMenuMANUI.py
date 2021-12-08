from datetime import date
from Models.EmployeeModel import Employee
from Logic_layer.LLAPI import LLAPI
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
import Logic_layer.LLAPI
import Data_layer.EmployeeDL
import Logic_layer.ListingHandler
import Logic_layer.SearchHandler
class ManagerUI:
    def __init__(self, ID = "", name = "", email = "", location = "", title = "manager", logic_api:LLAPI = LLAPI()):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api
        
        
    def managers_menu(self):
        on = True
        today = date.today()
        today_string = today.strftime("%d/%m/%Y")
        while on:
            print(f"Welcome {self.title} {self.name}. Todays date is {today_string}")
            print("1. Staff")
            print("2. Locations and properties")
            print("3. Work requests/reports")
            print("q. quit")
            selection = input("Input selection: ")
            if selection == "1":
                on = False
                self.staffing_options()
            elif selection == "2":
                on = False
                current_user = Ui_layer.PropertyMenu.PropertyMenu(self.ID, self.name, self.email, self.location, self.title)
                current_user.location_options()
            elif selection == "3":
                on = False
                current_user = Ui_layer.WorkReportMenu.WorkReportMenu(self.ID, self.name, self.email, self.location, self.title)
                current_user.Work_report_manager_menu()
            elif selection.lower() == "q":
                on = False
                
            else:
                print("Invalid option put into selection field.")

    def staffing_options(self):
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
            self.edit_staff()
        elif selection == "3":
            emplyeelist_init = Logic_layer.ListingHandler.ListingHandler()
            emplyeelist = emplyeelist_init.list_all_employees_unsorted()
            Logic_layer.ListingHandler.ListingHandler.list_printer(emplyeelist)
            self.staffing_options()
        elif selection == "4":
            self.staff_search()
        elif selection.lower() == "q":
            pass 
        else:
            print("Invalid option put into selection field.")
            self.managers_menu()

    

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
            print(f"Name:      {name}")
            print(f"Email:     {email}")
            print(f"Location:  {location}")
            print(f"Address:   {address}")
            print(f"Phone:     {phone}")
            print(f"Cellphone: {cellphone}")
            print(f"Title:     {title}")
            rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
            if rightorwrong.lower() == "y":
                createemployeloop = False
                Logic_layer.LLAPI.LLAPI.create_employee(name, email, location, address, phone, cellphone, title)
            elif rightorwrong.lower() == "c":
                createemployeloop = False
                self.managers_menu()
            elif rightorwrong.lower() == "n":
                print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
                fieldchange = input("Input the letter of the field you wish to change: ")
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
                    print("Invalid option put into selection field.")

    def edit_staff(self):
        print("Change information about employee")
        employeeID = input("What is the employees ID number?: ")
        Employeeinfo = Data_layer.EmployeeDL.EmployeeDL(ID=employeeID)
        results = Employeeinfo.search_by_ID()
        name = results["emname"]
        email = results["ememail"]
        location = results["emlocation"]
        address = results["emaddress"]
        phone = results["emphone"]
        cellphone = results["emcellphone"]
        title = results["emtitle"]
        staff_editor = True
        while staff_editor:
            print(f"Name:      {name}")
            print(f"Email:     {email}")
            print(f"Location:  {location}")
            print(f"Address:   {address}")
            print(f"Phone:     {phone}")
            print(f"Cellphone: {cellphone}")
            print(f"Title:     {title}")
            print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
            fieldchange = input("Input the letter of the field you wish to change: ")
            if fieldchange.lower() == "n":
                name = input("What is the new name of the employee?: ")   
            elif fieldchange.lower() == "l":
                location = input("What location does the employee work at?: ")
            elif fieldchange.lower() == "a":    
                address = input("What is the address of the employee?: ")
            elif fieldchange.lower() == "p":
                phone = input("What is the employees phone number?: ")
            elif fieldchange.lower() == "c":
                cellphone = input("What is the employees cellphone number?: ")
            elif fieldchange.lower() == "t":
                title = input('Is the employee a "manager" or a regular "employee"?: ')
            else:
                print("Invalid option put into selection field.")

    def staff_search(self):
        print("What paremeter would you like to search by?")
        print("[I]D number, [n]ame, [e]mail, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle")
        print("Use [b] to go back to main menu and [q] to quit")
        search_attribute = input("Input search attribute: ")
        if search_attribute.lower() == "i":
            pass
        elif search_attribute.lower() == "n":
            pass
        elif search_attribute.lower() == "e":
            pass
        elif search_attribute.lower() == "l":
            pass
        elif search_attribute.lower() == "a":
            pass
        elif search_attribute.lower() == "p":
            pass
        elif search_attribute.lower() == "c":
            pass
        elif search_attribute.lower() == "t":
            pass
        elif search_attribute.lower() == "b":
            self.managers_menu()
        elif search_attribute.lower() == "q":
            pass
        else:
            print("Not a valid attribute")
            self.staff_search