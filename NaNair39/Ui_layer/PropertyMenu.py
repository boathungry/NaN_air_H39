import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI

#Mögulega að implementa baka um einn menu frekar en alltaf á main menu ef tími gefst

class PropertyMenu:
    def __init__(self, name, email, location, title):
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def location_options(self):
        """location_deets = "get_location_details(self.location)"""
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
            elif selection == "1" and self.title == "staff":
                location_options_on = False
                self.destination_staff_menu()
            elif selection == "2" and self.title == "manager":
                location_options_on = False
                self.property_manager_menu()
            elif selection == "2" and self.title == "staff":
                location_options_on = False
                self.property_staff_menu()
            elif selection.lower() == "b" and self.title == "manager":
                location_options_on = False
                current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.name, self.email, self.location, self.title)
                current_user.managers_menu()
            elif selection.lower() == "b" and self.title == "staff":
                location_options_on = False
                Ui_layer.MainMenuEMPUI.EmployeeUI(title="staff").staff_menu
            elif selection.lower() == "q":
                location_options_on = False
            else:
                print("Wrong input.")
                


    def destination_manager_menu(self):
        print("1. Register new destination")
        print("2. Change existin destination")
        print("3. Get list of existing destination")
        print("4. Search for destination")
        print("b. Back to main menu")
        print("q. Quit")
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
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.name, self.email, self.location, self.title)
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
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.name, self.email, self.location, self.title)
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
            Ui_layer.MainMenuEMPUI.EmployeeUI(title="staff").staff_menu()
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
            Ui_layer.MainMenuEMPUI.EmployeeUI(title= "staff").staff_menu()
