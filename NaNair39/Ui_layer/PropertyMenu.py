import Ui_layer.MainMenuEMPUI
class PropertyMenu:
    def __init__(self):
        super().__init__()

    def location_options_mangers(self):
        location_deets = "get_location_details(self.location)"
        manpropon = True
        while manpropon:
            print("1. Destinations")
            print("2. Properties")
            print("b. Back")
            print("q. Quit")
            selection = input("Input selection")
            if selection == "1":
                self.destination_manager_menu()
            elif selection == "2":
                self.property_manager_menu()
            elif selection.lower() == "b":
                pass
            elif selection.lower() == "q":
                manpropon = False
            else:
                print("Wrong input.")

    def destination_manager_menu():
        manlocon = True
        while manlocon:
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
                Ui_layer.MainMenuEMPUI.ManagerUI.managers_menu()
            elif selection.lower() == "q":
                manlocon = False
    def property_manager_menu():
        propmanmenuon = True
        while propmanmenuon:
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
                Ui_layer.MainMenuEMPUI.ManagerUI.managers_menu()
            elif selection.lower() == "q":
                propmanmenuon = False
            else:
                print("Wrong input")