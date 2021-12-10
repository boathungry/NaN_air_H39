from datetime import date
from Models.EmployeeModel import Employee
from Logic_layer.LLAPI import LLAPI
from Models.LocationModel import Location
import Ui_layer.PropertyMenu
import Ui_layer.WorkReportMenu 
import Ui_layer.main_login
import string
import Data_layer.EmployeeDL

class ManagerUI:
    def __init__(self, idnumber = "", name = "", email = "", location = "", title = "manager", logic_api:LLAPI = LLAPI()):
        self.idnumber = idnumber
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
            print("")
            print(f"Welcome {self.title} {self.name}. Todays date is {today_string}")
            print("")
            print("1. Staff")
            print("2. Locations and properties")
            print("3. Work requests/reports")
            print("4. Contractors")
            print("q. quit")
            print("")
            selection = input("Input selection: ")
            if selection == "1":
                on = self.staffing_options()
            elif selection == "2":
                current_user = Ui_layer.PropertyMenu.PropertyMenu(self.idnumber, self.name, self.email, self.location, self.title)
                on = current_user.location_options()
            elif selection == "3":
                #current_user = Ui_layer.WorkReportMenu.WorkReportMenu(self.idnumber, self.name, self.email, self.location, self.title)
                current_user = Ui_layer.WorkReportMenu.WorkReportMenu("", "", "", "", "", "", "", "", "", "", "")
                on = current_user.Work_report_manager_menu()
            elif selection == "4":
                on = self.contractors_menu_man()
            elif selection.lower() == "q":
                on = False
                print("")
                print("Thank you and have a nice day.")
                
            else:
                print("Invalid option put into selection field.")

    def staffing_options(self):
        print("")
        print("1. Register a new staff member")
        print("2. Edit information about a staff member")
        print("3. Get staff list")
        print("4. Search for a staff member")
        print("b. back to main menu")
        print("q. quit")
        print("")
        selection = input("Input selection: ")
        print("")
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
        elif selection.lower() == "b":
            return True
        elif selection.lower() == "q":
            print("Thank you and have a nice day.")
            return False
        else:
            print("Invalid option put into selection field.")
            self.managers_menu()

    

    def create_employee(self):
        counter = 0
        print("")
        create_employee_loop = True
        fieldchange = ""
        while create_employee_loop:
            print(counter)
            if counter != 0:
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
                    create_employee_loop = False
                    self.llapi.create_employee(name, email, location, address, phone, cellphone, title)
                    self.managers_menu()
                elif rightorwrong.lower() == "c":
                    create_employee_loop = False
                    fieldchange = ""
                    return True
                elif rightorwrong.lower() == "n":
                    print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
                    fieldchange = input("Input the letter of the field you wish to change: ")
            if counter == 0 or counter !=0 and fieldchange.lower() == "n":
                name_comma_check_on = True
                while name_comma_check_on:
                    name = string.capwords(input("What is the name of the new employee?: "))
                    comma_check = self.llapi.comma_checker(name)
                    if comma_check:
                        print("Please don't have commas in the name, it messes with our database.")
                    else:
                        name_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "e":
                email_comma_checkon = True
                while email_comma_checkon:
                    email = input("What is the employees email address?: ")
                    comma_check = self.llapi.comma_checker(email)
                    if comma_check:
                        print("Plese don't use commas in the email, only use periods. Commas mess with our database.")
                    else:
                        email_comma_checkon = False
            if counter == 0 or counter !=0 and fieldchange == "l":
                print("")
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
            if counter == 0 or counter !=0 and fieldchange == "a":            
                address_comma_check_on = True
                while address_comma_check_on:                  
                    address = string.capwords(input("What is the address of the employee?: "))
                    comma_check = self.llapi.comma_checker(address)
                    if comma_check:
                        print("Please don't have a comma in the address. It messes with our database")
                    else:
                        address_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "p":
                phone_comma_check_on = True
                while phone_comma_check_on: 
                    phone = input("What is the employees phone number?: ")
                    comma_check = self.llapi.comma_checker(phone)
                    if comma_check:
                        print("Please don't have a comma in the phone number. It messes with our database")
                    else:
                        phone_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "c":
                gsm_comma_check_on = True
                while gsm_comma_check_on:
                    cellphone = input("What is the employees cellphone number?: ")
                    comma_check = self.llapi.comma_checker(cellphone)
                    if comma_check:
                        print("Please don't have a comma in the cell phone number. It messes with our database")
                    else:
                        gsm_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "t":
                titlechecker_on = True
                while titlechecker_on:
                    title = input('Is the employee a "manager" or a regular "staff" member?: ').lower()
                    if title.lower() not in ["manager", "staff"]:
                        print('Not a valid title, please input either the word "manager" or the word "staff"')
                    else:
                        titlechecker_on = False
            counter +=1


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
            print("Select a field to change: [n]ame, [e]mail, [l]ocation, [a]ddress, [p]hone, [c]ellphone, [t]itle.")
            fieldchange = input("Input the letter of the field you wish to change: ")
            if fieldchange.lower() == "l":
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
            elif fieldchange.lower() == "t":
                    titlechecker_on = True
                    while titlechecker_on:
                        title = input('Is the employee a "manager" or a regular "staff" member?: ').lower()
                        if title.lower() not in ["manager", "staff"]:
                            print('Not a valid title, please input either the word "manager" or the word "staff"')
                        else:
                            titlechecker_on = False   
            elif fieldchange.lower() in ["n", "e", "a", "p", "c"]:
                comma_check_on = True
                while comma_check_on:
                    fieldinput = input(f"What would you like it changed to?: ")
                    comma_check = self.llapi.comma_checker(fieldinput)
                    if comma_check:
                        print("Please don't have a comma in the input. It messes with the database")
                    else:
                        comma_check_on = False
                if fieldchange.lower() == "n":
                    name = string.capwords(fieldinput)
                elif fieldchange.lower() == "e":    
                    email = string.capwords(fieldinput)  
                elif fieldchange.lower() == "a":    
                    address = string.capwords(fieldinput)
                elif fieldchange.lower() == "p":
                    phone = string.capwords(fieldinput)
                elif fieldchange.lower() == "c":
                    cellphone = string.capwords(fieldinput)
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
                return True
            elif editmore == "c":
                staff_editor = False
                return True
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

    def contractors_menu_man(self):
        on = True
        while on:
            print("")
            print("1. Get a list of contractors")
            print("2. Register a new contractor")
            print("b. Go back")
            print("q. quit")
            print("")
            selection = input("Input selection: ")
            if selection == "1":
                contractorlist = self.llapi.list_all_contractors()
                self.llapi.list_printer(contractorlist)
                self.contractors_menu_man()
            elif selection == "2":
                on = self.create_contractor()
            elif selection == "b":
                self.create_contractor()
            elif selection == "q":
                print("Thank you and have a nice day.")
                return False
            else:
                print("Invalid option put into selection field.")
                pass
        
    def create_contractor(self):
        name = string.capwords(input("What is the name of the contractor/company?: "))
        phone = input("What is the contractors phone number?: ")
        email = input("What is the contractors email address?: ")
        opening_hours = input("What are the contractors opening hours?: ")
        address = input("What is the contractors address?: ")
        avaliable_locations = self.llapi.list_of_location_names()
        location_checker_on = True
        while location_checker_on:
            print("Avaliable locations are a follows: ")
            self.llapi.list_printer(avaliable_locations)
            location = string.capwords(input("At what location is the contractor?: "))
            if string.capwords(location) not in avaliable_locations:
                print("Not a valid location, please either create a new location or select an avaliable one")
            else:
                location_checker_on = False
                createcontractorloop = True
                while createcontractorloop:
                    print("")
                    print("Is this the correct information?")
                    print(f"Name:          {name}")
                    print(f"phone:         {phone}")
                    print(f"Email:         {email}")
                    print(f"Opening hours: {opening_hours}")
                    print(f"Address:       {address}")
                    print(f"Location:      {location}")
                    print("")
                    rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
                    if rightorwrong.lower() == "y":
                        createcontractorloop = False
                        self.llapi.create_contractor(name,phone,email,opening_hours,address,location)
                        self.contractors_menu_man()
                    elif rightorwrong.lower() == "c":
                        createcontractorloop = False
                        self.contractors_menu_man
                    elif rightorwrong.lower() == "n":
                        print("Select a field to change: [n]ame, [p]hone, [e]mail, [o]pening hours, [a]ddress, [l]ocation.")
                        fieldchange = input("Input the letter of the field you wish to change: ")
                        if fieldchange.lower() == "n":
                            name = input("What is the revised name of the contractor?: ")
                        elif fieldchange.lower() == "p":
                            phone = input("What is the revised phone number of the contractor?: ")
                        elif fieldchange.lower() == "e":
                            email = input("What is the revised phone number of the contractor?: ")
                        elif fieldchange.lower() == "o":
                            opening_hours = input("What are the revised opening hours?: ")
                        elif fieldchange.lower() == "a":
                            address = input("What is the revised address?: ")
                        elif fieldchange.lower() == "l":
                            location_checker_on = True
                            while location_checker_on:
                                avaliable_locations = self.llapi.list_of_location_names()
                                print("Avaliable locations are as follows:")
                                location = input("What is the revised location?: ")
                                if location not in avaliable_locations:
                                    print("Not a valid location, please either create a new location or select an avaliable one")
                                else:
                                    location_checker_on = False
                        else:
                            print("Invalid option put into selection field.")

#            employeelist = self.llapi.list_all_employees()
#            self.llapi.list_printer(employeelist)
#            self.staffing_options()
#name,phone,email,opening hours,address,location