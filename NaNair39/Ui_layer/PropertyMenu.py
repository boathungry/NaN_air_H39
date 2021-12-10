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
                return self.destination_manager_menu()
            elif selection == "1" and self.title == "employee":
                location_options_on = False
                return self.destination_staff_menu()
            elif selection == "2" and self.title == "manager":
                location_options_on = False
                return self.property_manager_menu()
            elif selection == "2" and self.title == "employee":
                location_options_on = False
                return self.property_staff_menu()
            elif selection.lower() == "b" and self.title == "manager":
                location_options_on = False
                return True
            elif selection.lower() == "b" and self.title == "employee":
                location_options_on = False
                return True
            elif selection.lower() == "q":
                location_options_on = False
                return False
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
            return self.create_destination()
        elif selection == "2":
            all_destinations = self.llapi.list_all_destinations()
            self.llapi.list_printer(all_destinations)
            return True
        elif selection == "3":
            return self.destination_search()
            """elif selection == "4":
            self.edit_destination()"""
        elif selection.lower() == "b":
            return True
        elif selection.lower() == "q":
            return False
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
            return self.create_property()
        elif selection == "2":
            return self.edit_property()
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection.lower() == "b":
            return True
        elif selection.lower() == "q":
            return False
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
            all_destinations = self.llapi.list_all_destinations()
            self.llapi.list_printer(all_destinations)
            return True
        elif selection == "2":
            #Implement destination search class
            pass
        elif selection.lower() == "b":
            
            return True
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
            return True
        elif selection.lower() == "q":
            return False
    
    
    def create_destination(self):
        city_checker_on = True
        used_locations = self.llapi.list_of_location_names()
        while city_checker_on:
            city = string.capwords(input("In what city is the new destination: "))
            comma_check = self.llapi.comma_checker(city)
            if city in used_locations:
                print("This location is already in use, please enter a different city.")
            elif comma_check:
                print("Please don't have a comma in the city name it messes with our database.")
            else:
                city_checker_on = False            
        countrycommaon = True
        while countrycommaon:
            country = string.capwords(input(f"What country is {city} in: "))
            comma_check = self.llapi.comma_checker(input=country)
            if comma_check:
                print("Please don't have a comma in the country name, it messes with our database")
            else:
                countrycommaon = False
        airpcommaon = True
        while airpcommaon:
            airport = string.capwords(input(f"What is the airport for {city}: "))
            comma_check = self.llapi.comma_checker(input=airport)
            if comma_check:
                print("Please don't have a comma in the airport name, it messes with our database")
            else:
                airpcommaon = False
        phonecommaon = True
        while phonecommaon:
            phone = input(f"What is the phone number for your destination in {city}: ")
            comma_check = self.llapi.comma_checker(input=phone)
            if comma_check:
                print("Please don't have a comma in the phone number, it messes with our database")
            else:
                phonecommaon = False
        timecommaon = True
        while timecommaon:
            open_hours = input("What are the opening hours for you new destination(input in format hh:mm - hh:mm): ")
            comma_check = self.llapi.comma_checker(input=open_hours)
            if comma_check:
                print("Please don't have a comma in the opening hours, it messes with our database")
            else:
                timecommaon = False
        mancommaon = True
        while mancommaon:
            manager = string.capwords(input("What is the name of the manager of your new destination: "))
            comma_check = self.llapi.comma_checker(input=manager)
            if comma_check:
                print("Please don't have a comma in the managers name, it messes with our database")
            else:
                airpcommaon = False
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
                self.llapi.create_destination(city, country, airport, phone, open_hours, manager)
                return True
            elif rightorwrong.lower() == "c":
                createdestloop = False
                return True
            elif rightorwrong.lower() == "n":
                print("Select a field to change: [c]ity, countr[y}, [a]irport, [p]hone number, [o]pening hours, [l]ocal manager.")
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
        propertyID = input("What is the propertys ID number?: ")
        print("input fyrir prop_id: ", propertyID)
        Propertyinfo = self.llapi.dict_search(Property,  attribute="idnumber", value=propertyID)
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
                commaon = True
                while commaon:
                    name = input("What is the new name of the property?: ")
                    comma_check = self.llapi.comma_checker(input=name)
                    if comma_check:
                        print("Please don't have a comma in the name, it messes with our database")
                    else:
                        commaon = False
            elif fieldchange.lower() == "l":
                location_check_on = True
                while location_check_on:
                    available_locations = self.llapi.list_of_location_names()
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = string.capwords(input("What location is the new property at?: "))
                    if location not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_check_on = False
            elif fieldchange.lower() == "a":    
                commaon = True
                while commaon:
                    address = string.capwords(input("What is the address of the property?: "))
                    comma_check = self.llapi.comma_checker(input=address)
                    if comma_check:
                        print("Please don't have a comma in the address, it messes with our database")
                    else:
                        commaon = False
            elif fieldchange.lower() == "s":
                commaon = True
                while commaon:
                    size = input("What is the new size of the property? use the format [xx.xm2]: ")
                    comma_check = self.llapi.comma_checker(input=size)
                    if comma_check:
                        print("Please don't have a comma in the size, it messes with our database use a period instead of the comma.")
                    else:
                        commaon = False
            elif fieldchange.lower() == "r":
                roomnrson = True
                while roomnrson:
                    rooms = input("What is the new number of rooms?: ")
                    try:
                        int(rooms)
                        roomnrson = False
                    except:
                        print("Please only use whole numebers for number of rooms")
                
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
                init = Data_layer.PropertiesDL.PropertyDL()
                init.change_information_property(results_final)
                return True
            elif editmore == "c":
                staff_editor = False
                return True
            else:
                pass


    def destination_search(self):
        print("")
        print("What paremeter would you like to search by?")
        print("[c]ity, countr[y], [a]irport, [p]hone number, [l]ocal manager")
        print("Use [b] to go back to main menu and [q] to quit")
        search_attribute = input("Input search attribute: ")
        if search_attribute.lower() == "c":
            print("")
            cityname = string.capwords(input("What city would you like to look for?: "))
            Locationinfo = self.llapi.search(Location,  attribute="city", value=cityname)
            if len(Locationinfo) < 1:
                print("No results were found")
                return self.destination_search()
            else:
                print("")
                print("results: ")
                self.llapi.list_printer(Locationinfo)
                return True
        elif search_attribute.lower() == "y":
            print("")
            countryname = string.capwords(input("What is country name you wish to search for?: "))
            Locationinfo = self.llapi.search(Location,  attribute="country", value=countryname)
            if len(Locationinfo) < 1:
                print("No results were found")
                return self.destination_search()
            else:
                print("")
                print("results: ")
                self.llapi.list_printer(Locationinfo)
                return True
        elif search_attribute.lower() == "a":
            print("")
            airportname = string.capwords(input("What is the airport name you wish to search for?: "))
            Locationinfo = self.llapi.search(Location,  attribute="airport", value=airportname)
            if len(Locationinfo) < 1:
                print("No results were found")
                return self.destination_search()
            else:
                print("")
                print("results: ")
                self.llapi.list_printer(Locationinfo)
                return True
        elif search_attribute.lower() == "p":
            print("")
            phone = input("What is the phone number you wish to search for?: ")
            Locationinfo = self.llapi.search(Location,  attribute="phone_number", value=phone)
            if len(Locationinfo) < 1:
                print("No results were found")
                return self.destination_search()
            else:
                print("")
                print("results: ")
                self.llapi.list_printer(Locationinfo)
                return True   
        elif search_attribute.lower() == "l":
            print("")
            local_manager = string.capwords(input("Who is the local manager you wish to search for?: "))
            Locationinfo = self.llapi.search(Location,  attribute="local_manager", value=local_manager)
            if len(Locationinfo) < 1:
                print("No results were found")
                return self.destination_search()
            else:
                print("")
                print("results: ")
                self.llapi.list_printer(Locationinfo)
                return True
        
        elif search_attribute.lower() == "b":
            return True
        elif search_attribute.lower() == "q":
            return False
        else:
            print("Not a valid attribute")
            return self.destination_search()

    def create_property(self):
        counter = 0
        print("")
        create_property_loop = True
        fieldchange = ""
        while create_property_loop:
            print(counter)
            if counter != 0:
                print("Is this the correct information?")
                print(f"IDnumber:  {idnumber}")
                print(f"Name:      {name}")
                print(f"Location:  {location}")
                print(f"Address:   {address}")
                print(f"Size:      {size}")
                print(f"Rooms:     {rooms}")
                rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
                if rightorwrong.lower() == "y":
                    create_property_loop = False
                    self.llapi.create_property(idnumber, name, location, address, size, rooms)
                    return True
                elif rightorwrong.lower() == "c":
                    create_property_loop = False
                    fieldchange = ""
                    return True
                elif rightorwrong.lower() == "n":
                    print("Select a field to change: [i]dnumber [n]ame, [l]ocation, [a]ddress, [s]ize, number of [r]ooms.")
                    fieldchange = input("Input the letter of the field you wish to change: ")
            if counter == 0 or counter !=0 and fieldchange.lower() == "i":
                id_comma_check_on = True
                while id_comma_check_on:
                    idlist = self.llapi.get_all_property_ID()
                    idnumber = input("What is the idnumber of the new property?: ").lower()
                    comma_check = self.llapi.comma_checker(idnumber)
                    number_of_ids = len(idlist)
                    if idnumber in idlist:
                        in_list_loop = True
                        while in_list_loop:
                            print("Id number is already taken, please use a different one.")
                            list_ids = input(f"There are currently {number_of_ids} number of ids in use, would you like a list of them all? y/n?: ").lower()
                            if list_ids == "y":
                                whatkind = input("What format would you like: python [l]ist or [o]ne per line?: ").lower()
                                if whatkind =="l":
                                    print(idlist)
                                    in_list_loop = False
                                elif whatkind == "o":
                                    self.llapi.list_printer(idlist)
                                    in_list_loop = False
                                else:
                                    print("Invalid input!")
                            elif list_ids == "n":
                                in_list_loop = False
                            else:
                                print("invalid input")
                        else:
                            in_list_loop = False                   
                    elif comma_check:
                        print("Please don't have commas in the name, it messes with our database.")
                    else:
                            id_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "n":
                name_comma_check_on = True
                while name_comma_check_on:
                    name = string.capwords(input("What is the name of the new property?: "))
                    comma_check = self.llapi.comma_checker(name)
                    if comma_check:
                        print("Please don't have commas in the name, it messes with our database.")
                    else:
                        name_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "l":
                print("")
                available_locations = self.llapi.list_of_location_names()
                location_checker_on = True
                while location_checker_on:
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = string.capwords(input("What location is the property in?: "))
                    if string.capwords(location) not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                        quit = input("would you like to go [b]ack to the main menu to create a new destination. Any other input will go back to selecting destination: ")
                        if quit.lower() == "b":
                            return True
                        else:
                            pass  
                    else:
                        location_checker_on = False
            if counter == 0 or counter !=0 and fieldchange == "a":            
                address_comma_check_on = True
                while address_comma_check_on:                  
                    address = string.capwords(input("What is the address of the new property?: "))
                    comma_check = self.llapi.comma_checker(address)
                    if comma_check:
                        print("Please don't have a comma in the address. It messes with our database")
                    else:
                        address_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "s":
                size_check_on = True
                while size_check_on: 
                    size = input("What is the size of the new property (use format xx.xm2)?: ")
                    comma_check = self.llapi.comma_checker(size)
                    if comma_check:
                        print("Please don't have a comma in the phone number. It messes with our database")
                    else:
                        size_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "r":
                rooms_int_check_on = True
                while rooms_int_check_on:
                    rooms = input("What is the number of rooms in the new property?: ")
                    try:
                        int(rooms)
                        rooms_int_check_on = False
                    except:
                        print("Please only use whole numbers for the rooms")
            counter +=1
