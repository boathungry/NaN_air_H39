import Ui_layer.MainMenuMANUI
class PropertyMenu:
    def __init__(self, title):
        super().__init__()

    def location_options(self):
        """location_deets = "get_location_details(self.location)"""
        
        print("1. Destinations")
        print("2. Properties")
        print("b. Back")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1" and self.title == "manager":
            self.destination_manager_menu()
        elif selection == "1" and self.title == "staff":
            self.destination_staff_menu()
        elif selection == "2" and self.title == "manager":
            self.property_manager_menu()
        elif selection == "2" and self.title == "staff":
            self.property_staff_menu()
        elif selection.lower() == "b" and self.title == "manager":
            user = Ui_layer.MainMenuMANUI.ManagerUI("manager")
            Ui_layer.MainMenuMANUI.ManagerUI.managers_menu(user)
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input.")
            self.location_options()


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
            user = Ui_layer.MainMenuMANUI.ManagerUI("manager")
            Ui_layer.MainMenuMANUI.ManagerUI.managers_menu(user)
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
            user = Ui_layer.MainMenuMANUI.ManagerUI("manager")
            Ui_layer.MainMenuMANUI.ManagerUI.managers_menu(user)
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input")
            self.property_manager_menu()