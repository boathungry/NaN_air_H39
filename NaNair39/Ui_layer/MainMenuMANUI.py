from NaNair39.Ui_layer.main_login import LogIn
class ManagerUI(LogIn):
    def __init__(self, name):
        super().__init__(name, staff_class="y")
        
    def valmynd_yfirmenn(self):
        on = True
        while on:
            print(f"Welcome {self.name}")
            print("1. Staff")
            print("2. Locations")
            print("3. Work order")
            print("q. quit")
            selection = input("Input selection: ")
            if selection == "1":
                self.staffing_options()
            elif selection == "2":
                self.location_options()
            elif selection == "3":
                pass
            elif selection == "q":
                on = False
            else:
                print("Invalid option put into selection field.")

    def staffing_options(self):
        on = True
        while on:
            print("1. Register a new staff member")
            print("2. Edit information about a staff member")
            print("3. Get staff list")
            print("4. Search for a staff member")
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
                self.valmynd_yfirmenn()
            elif selection.lower() == "q":
                on = False
    