from NaNair39.Ui_layer.MainMenuMANUI import ManagerUI
from Ui_layer.main_login import LogIn


class PropertyMenu(LogIn):
    def __init__(self):
        super().__init__()
    def location_options(self):
        location_deets = get_location_details(self.location)
        on = True
        while on:
            if self.staff_class == "m":
                manpropon = True
                while manpropon:
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
                        ManagerUI.managers_menu()
            elif self.staff_class == "e":
                pass