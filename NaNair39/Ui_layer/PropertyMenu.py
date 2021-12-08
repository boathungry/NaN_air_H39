import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI
import Logic_layer.LLAPI
import Logic_layer.SearchHandler
#Mögulega að implementa baka um einn menu frekar en alltaf á main menu ef tími gefst

class PropertyMenu:
    def __init__(self, ID, name, email, location, title):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def location_options(self):
        location_options_on = True
        while location_options_on:
            print("1. Destinations")
            print("2. Properties")
            print("b. Back to main menu")
            print("q. Quit")
            selection = input("Input selection: ")
            if selection == "1" and self.title == "manager":
                location_options_on = False
                self.destination_manager_menu()
            elif selection == "1" and self.title == "employee":
                location_options_on = False
                self.destination_staff_menu()
            elif selection == "2" and self.title == "manager":
                location_options_on = False
                self.property_manager_menu()
            elif selection == "2" and self.title == "employee":
                location_options_on = False
                self.property_staff_menu()
            elif selection.lower() == "b" and self.title == "manager":
                location_options_on = False
                current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
                current_user.managers_menu()
            elif selection.lower() == "b" and self.title == "employee":
                location_options_on = False
                Ui_layer.MainMenuEMPUI.EmployeeUI(title="staff").staff_menu
            elif selection.lower() == "q":
                location_options_on = False
            else:
                print("Wrong input.")
                


    def destination_manager_menu(self):
        print("1. Register new destination.")
        print("2. Change existing destination.")
        print("3. Get list of existing destination.")
        print("4. Search for destination.")
        print("b. Back to main menu.")
        print("q. Quit.")
        selection = input("Input selection: ")
        if selection == "1":
            self.create_destination()
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.managers_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.destination_manager_menu()
    
    def property_manager_menu(self):
        
        print("1. Create new property")
        print("2. Edit existing property")
        print("3. Get list of properties")
        print("4. Look up property")
        print("b. back to main menu")
        print("q. quit")
        selection = input("Input selection: ")
        if selection == "1":
            pass
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.managers_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input")
            self.property_manager_menu()
        
    def destination_staff_menu(self):
        print("1. Get list of destinations")
        print("2. Search for destination")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1":
            #Implement list of destinations
            pass
        elif selection == "2":
            #Implement destination search class
            pass
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.staff_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.destination_staff_menu()

    def property_staff_menu(self):
        print("1. Get list of properties")
        print("2. Search for property")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection")
        if selection == "1":
            #implement list of properties class
            pass
        elif selection == "2":
            #implement search for properties class
            pass
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.staff_menu()
    
    
    def create_destination(self):
        city = input("In what city is the new destination: ")
        country = input(f"What country is {city} in: ")
        airport = input(f"What is the airport for {city}: ")
        phone = input(f"What is the phone number for your destination in {city}: ")
        open_hours = input("What are the opening hours for you new destination(input in format hh:mm - hh:mm): ")
        manager = input("What is the name of the manager of your new destination: ")
        createdestloop = True
        while createdestloop:
            print(f"City: {city}")
            print(f"Country: {country}")
            print(f"Local airport: {airport}")
            print(f"Phone: {phone}")
            print(f"Opening hours: {open_hours}")
            print(f"Local manager: {manager}")
            rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
            if rightorwrong.lower() == "y":
                createdestloop = False
                Logic_layer.LLAPI.LLAPI.create_destination(city, country, airport, phone, open_hours, manager)
            elif rightorwrong.lower() == "c":
                createdestloop = False
                Ui_layer.MainMenuMANUI.ManagerUI.managers_menu()
            elif rightorwrong.lower() == "n":
                print("Select a field to change: [c]ity, countr[y}, [a]irport, [p]hone, [o]pening hours, [l]ocal manager.")
                fieldchange = input("Input the letter of the field you wish to change: ")
                if fieldchange.lower() == "c":
                    city = input("What is the name of the destination city?: ")
                elif fieldchange.lower() == "y":
                    country = input(f"What country is {city} in?: ")
                elif fieldchange.lower() == "a":    
                    airport = input(f"What is the local airport for {city}?: ")
                elif fieldchange.lower() == "p":
                    phone = input("What is the phone number for the new destination?: ")
                elif fieldchange.lower() == "o":
                    open_hours = input("What are the opening hours(use format hh:mm - hh:mm)?: ")
                elif fieldchange.lower() == "l":
                    manager = input("What is the name of the local manager of the new destination?: ")
                else:
                    print("Invalid option put into selection field.")

    def edit_destination(self):
        print("Change information about a destination")
        cityname = input("What is the city name of the destination you wish to edit?: ")

        destinationinfo = Logic_layer.SearchHandler.SearchHandler.search(Des(), attribute="ID", value=employeeID)
        print(Employeeinfo)
        name = Employeeinfo.name
        email = Employeeinfo.email
        location = Employeeinfo.location
        address = Employeeinfo.address
        phone = Employeeinfo.phone
        cellphone = Employeeinfo.cellphone
        title = Employeeinfo.title
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Location: {location}")
        print(f"Address: {address}")
        print(f"Phone: {phone}")
        print(f"Cellphone: {cellphone}")
        print(f"Title: {title}")
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
            title = input('Is the employee a "manager" or a regular "employee"?: ')
        else:
            print("Invalid option put into selection field.")