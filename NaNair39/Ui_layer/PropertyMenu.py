from Models.LocationModel import Location
from Models.PropertyModel import Property
import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI
from Logic_layer.LLAPI import LLAPI
import Data_layer.PropertiesDL
import string
#Mögulega að implementa baka um einn menu frekar en alltaf á main menu ef tími gefst

class PropertyMenu:
    def __init__(self, ID, name, email, location, title, logic_api:LLAPI = LLAPI()):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api

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
        print("2. Get list of existing destination.")
        print("3. Search for destination.")
        """print("4. Change existing destination.")"""
        print("b. Back to main menu.")
        print("q. Quit.")
        selection = input("Input selection: ")
        if selection == "1":
            self.create_destination()
        elif selection == "2":
            pass
        elif selection == "3":
            pass
            """elif selection == "4":
            self.edit_destination()"""
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.managers_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.destination_manager_menu()
    
    def property_manager_menu(self):
        current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
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
            self.edit_property()
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection.lower() == "b":
            
            current_user.managers_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input")
            self.property_manager_menu()
        
    def destination_staff_menu(self):
        current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
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
            
            current_user.staff_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.destination_staff_menu()

    def property_staff_menu(self):
        current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
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
            
            current_user.staff_menu()
    
    
    def create_destination(self):
        
        city_checker_on = True
        used_locations = self.llapi.list_of_location_names()
        while city_checker_on:
            city = string.capwords(input("In what city is the new destination: "))
            if city in used_locations:

                print("This location is already in use, please enter a different city.")
            else:
                city_checker_on = False            
        country = string.capwords(input(f"What country is {city} in: "))
        airport = string.capwords(input(f"What is the airport for {city}: "))
        phone = input(f"What is the phone number for your destination in {city}: ")
        open_hours = input("What are the opening hours for you new destination(input in format hh:mm - hh:mm): ")
        manager = string.capwords(input("What is the name of the manager of your new destination: "))
        createdestloop = True
        list_of_things = []
        list_of_things.append(city)
        list_of_things.append(country)
        list_of_things.append(airport)
        list_of_things.append(phone)
        list_of_things.append(open_hours)
        list_of_things.append(manager)
        current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
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
                self.llapi.create_destination(city, country, airport, phone, open_hours, manager)
                current_user.managers_menu()
            elif rightorwrong.lower() == "c":
                createdestloop = False
                current_user.ManagerUI.managers_menu()
            elif rightorwrong.lower() == "n":
                print("Select a field to change: [c]ity, countr[y}, [a]irport, [p]hone, [o]pening hours, [l]ocal manager.")
                fieldchange = input("Input the letter of the field you wish to change: ")
                if fieldchange.lower() == "c":
                    city = input("What is the name of the destination city?: ")
                    while city_checker_on:
                        if city in used_locations:
                            print("This location is already in use, please enter a different city.")
                        else:
                            city_checker_on = False 
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

    # C krafa
    """def edit_destination(self):
        print("Change information about a destination")
        cityname = string.capwords(input("What is the city name of the destination you wish to edit?: "))

        destinationinfo = self.llapi.dict_search(search_object=Location, attribute="city", value=cityname)
        results = destinationinfo
        print(destinationinfo)
        city = results[0]["city"]
        country = results[0]["country"]
        airport = results[0]["airport"]
        phone_number = results[0]["phone_number"]
        opening_hours = results[0]["opening_hours"]
        local_manager = results[0]["local_manager"]
        print(f"City:          {city}")
        print(f"Country:       {country}")
        print(f"Airport:       {airport}")
        print(f"Phone no:      {phone_number}")
        print(f"Opening hours: {opening_hours}")
        print(f"Local Manager: {local_manager}")
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
            print("Invalid option put into selection field.")"""

#idnumber,name,location,address,size,rooms

    def edit_property(self):
        print("Change information about a property")
        propertyID = input("What is the property´s ID number?: ").capitalize()
        Propertyinfo = self.llapi.dict_search(Property,  attribute="idnumber", value=propertyID.capitalize())
        results = Propertyinfo
        print(results)

        idnumber = results[0]["pridnumber"]
        name = results[0]["prname"]
        location = results[0]["prlocation"]
        address = results[0]["praddress"]
        size = results[0]["prsize"]
        rooms = results[0]["prrooms"]
        staff_editor = True
        while staff_editor:
            print(f"ID number:    {idnumber}")
            print(f"Name:         {name}")
            print(f"Location:     {location}")
            print(f"Address:      {address}")
            print(f"Size:         {size}")
            print(f"Rooms:        {rooms}")
            print("Select a field to change: [n]ame, [l]ocation, [a]ddress, [s]ize, [r]ooms.")
            fieldchange = input("Input the letter of the field you wish to change: ")
            if fieldchange.lower() == "n":
                name = input("What is the new name of the property?: ")   
            elif fieldchange.lower() == "l":
                location_check_on = True
                while location_check_on:
                    available_locations = self.llapi.list_of_location_names()
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = input("What location is the new property at?: ")
                    if location not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_check_on = False
            elif fieldchange.lower() == "a":    
                address = input("What is the address of the property?: ")
            elif fieldchange.lower() == "s":
                phone = input("What is the new size of the property?: ")
            elif fieldchange.lower() == "r":
                cellphone = input("What is the new number of rooms?: ")
            else:
                print("Invalid option put into selection field.")
            editmore = input("Would you like to stop editing input [y] to commit changes and go back to the main menu, input [c] to cancel, input anything else to keep editing: ")
            if editmore == "y":
                staff_editor = False
                results_final = {}
                results_final["pridnumber"] = idnumber
                results_final["prname"] = name
                results_final["prlocation"] = location
                results_final["praddress"] = address
                results_final["prsize"] = size
                results_final["prrooms"] = rooms
                #Skrifa í skrá
                init = Data_layer.PropertiesDL.PropertyDL(ID=results_final["pridnumber"], location=results_final["prlocation"])
                init.change_information_property(results_final)
                Ui_layer.MainMenuMANUI.ManagerUI.managers_menu()
            elif editmore == "c":
                staff_editor = False
            else:
                pass


            propertyID = input("What is the property´s ID number?: ").capitalize()
        Propertyinfo = self.llapi.dict_search(Property,  attribute="idnumber", value=propertyID.capitalize())
        results = Propertyinfo
        print(results)