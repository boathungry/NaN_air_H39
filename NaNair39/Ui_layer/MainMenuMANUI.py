from datetime import date
from Models.EmployeeModel import Employee
from Logic_layer.LLAPI import LLAPI
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
import Logic_layer.LLAPI
import Logic_layer.ListingHandler
import Logic_layer.SearchHandler
import string
import Data_layer.EmployeeDL
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
            employeelist = self.llapi.list_all_employees()
            self.llapi.list_printer(employeelist)
            self.staffing_options()
        elif selection == "4":
            self.staff_search()
        elif selection.lower() == "q":
            pass 
        else:
            print("Invalid option put into selection field.")
            self.managers_menu()

    

    def create_employee(self):
        name = string.capwords(input("What is the name of the new employee?: "))
        email = input("What is the employees email address?: ")
        available_locations = self.llapi.list_of_location_names()
        location_checker_on = True
        while location_checker_on:
            print("Available locations are as follows:")
            self.llapi.list_printer(available_locations)
            location = string.capwords(input("What location does the employee work at?: "))
            if string.capwords(location) not in available_locations:
                print("Not a valid location, please either create a new location or select an available one")
            else:
                location_checker_on = False
                address = string.capwords(input("What is the address of the employee?: "))
                phone = input("What is the employees phone number?: ")
                cellphone = input("What is the employees cellphone number?: ")
                titlechecker_on = True
                while titlechecker_on:
                    title = input('Is the employee a "manager" or a regular "staff" member?: ').lower()
                    if title.lower() not in ["manager", "staff"]:
                        print('Not a valid title, please input either the word "manager" or the word "staff"')
                    else:
                        titlechecker_on = False
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
                                self.llapi.create_employee(name, email, location, address, phone, cellphone, title)
                                self.managers_menu()
                            elif rightorwrong.lower() == "c":
                                createemployeloop = False
                                self.managers_menu()
                            elif rightorwrong.lower() == "n":
                                print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
                                fieldchange = input("Input the letter of the field you wish to change: ")
                                if fieldchange.lower() == "n":
                                    name = input("What is the name of the new employee?: ")
                                elif fieldchange.lower() == "l":
                                    location_check_on = True
                                    while location_check_on:
                                        available_locations = self.llapi.list_of_location_names()
                                        print("Available locations are as follows:")
                                        self.llapi.list_printer(available_locations)
                                        location = input("What location does the employee work at?: ")
                                        if location not in available_locations:
                                            print("Not a valid location, please either create a new location or select an available one")
                                        else:
                                            location_check_on = False
                                elif fieldchange.lower() == "a":    
                                    address = input("What is the address of the employee?: ")
                                elif fieldchange.lower() == "p":
                                    phone = input("What is the employees phone number?: ")
                                elif fieldchange.lower() == "c":
                                    cellphone = input("What is the employees cellphone number?: ")
                                elif fieldchange.lower() == "t":
                                    titlechecker_on = True
                                    while titlechecker_on:
                                        title = input('Is the employee a "manager" or a regular "staff" member?: ').lower()
                                        if title.lower() not in ["manager", "staff"]:
                                            print('Not a valid title, please input either the word "manager" or the word "staff"')
                                        else:
                                            titlechecker_on = False
                                else:
                                    print("Invalid option put into selection field.")

    def edit_staff(self):
        print("Change information about employee")
        employeeID = input("What is the employees ID number?: ").capitalize()
        Employeeinfo = self.llapi.dict_search(Employee,  attribute="id", value=employeeID)
        results = Employeeinfo
        print(results)
        id = results[0]["emid"]
        name = results[0]["emname"]
        email = results[0]["ememail"]
        location = results[0]["emlocation"]
        address = results[0]["emaddress"]
        phone = results[0]["emphone"]
        cellphone = results[0]["emcellphone"]
        title = results[0]["emtitle"]
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
                location_check_on = True
                while location_check_on:
                    available_locations = self.llapi.list_of_location_names()
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = input("What location does the employee work at?: ")
                    if location not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_check_on = False

            elif fieldchange.lower() == "a":    
                address = input("What is the address of the employee?: ")
            elif fieldchange.lower() == "p":
                phone = input("What is the employees phone number?: ")
            elif fieldchange.lower() == "c":
                cellphone = input("What is the employees cellphone number?: ")
            elif fieldchange.lower() == "t":
                titlechecker_on = True
                while titlechecker_on:
                    title = input('Is the employee a "manager" or a regular "staff" member?: ').lower()
                    if title.lower() not in ["manager", "staff"]:
                        print('Not a valid title, please input either the word "manager" or the word "staff"')
                    else:
                        titlechecker_on = False
            else:
                print("Invalid option put into selection field.")
            editmore = input("Would you like to stop editing input [y] to commit changes and go back to the main menu, input [c] to cancel, input anything else to keep editing: ")
            if editmore == "y":
                staff_editor = False
                results_final = {}
                results_final["emid"] = id
                results_final["emname"] = name
                results_final["ememail"] = email
                results_final["emlocation"] = location
                results_final["emaddress"] = address
                results_final["emphone"] = phone
                results_final["emcellphone"] = cellphone
                results_final["emtitle"] = title
                #Skrifa í skrá
                init = Data_layer.EmployeeDL.EmployeeDL(ID=results_final["emid"], location=results_final["emlocation"])
                init.change_information_employee(results_final)
                self.managers_menu()
            elif editmore == "c":
                staff_editor = False
            else:
                pass


    def staff_search(self):
        print("What paremeter would you like to search by?")
        print("[I]D number, [n]ame, [e]mail, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle")
        print("Use [b] to go back to main menu and [q] to quit")
        search_attribute = input("Input search attribute: ")
        if search_attribute.lower() == "i":
            employeeID = input("What is the ID number you wish to search for?: ")
            Employeeinfo = self.llapi.search(Employee,  attribute="id", value=employeeID.capitalize())
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "n":
            employeename = input("What is name you wish to search for?: ")
            namestring = string.capwords(employeename)
            Employeeinfo = self.llapi.search(Employee,  attribute="name", value=namestring)
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "e":
            employeeemail = input("What is the email you wish to search for?: ")
            Employeeinfo = self.llapi.search(Employee,  attribute="email", value=employeeemail.lower())
            print(len(Employeeinfo))
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "l":
            employeelocation = input("What is the location you wish to search for?: ")
            locationstring = string.capwords(employeelocation)
            Employeeinfo = self.llapi.search(Employee,  attribute="location", value=locationstring)
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
            
        elif search_attribute.lower() == "a":
            employeeaddress = input("What is the address you wish to search for?: ")
            addressstring = string.capwords(employeeaddress)
            Employeeinfo = self.llapi.search(Employee,  attribute="address", value=addressstring)
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "p":
            employeephone = input("What is the phone number you wish to search for? (use the format +00 00 00 00 00): ")
            Employeeinfo = self.llapi.search(Employee,  attribute="phone", value=employeephone)
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "c":
            employeegsm = input("What is the cellphone number you wish to search for(use the format +000 000 0000)?: ")
            Employeeinfo = self.llapi.search(Employee,  attribute="cellphone", value=employeegsm)
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "t":
            employeetitle = input("Do you want to list all staff or managers?: ")
            Employeeinfo = self.llapi.search(Employee,  attribute="title", value=employeetitle.lower())
            if len(Employeeinfo) < 1:
                print("No results were found")
                self.staff_search()
            else:
                self.llapi.list_printer(Employeeinfo)
                self.managers_menu()
        elif search_attribute.lower() == "b":
            self.managers_menu()
        elif search_attribute.lower() == "q":
            pass
        else:
            print("Not a valid attribute")
            self.staff_search()