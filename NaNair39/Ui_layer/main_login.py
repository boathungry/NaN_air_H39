from Ui_layer.MainMenuMANUI import ManagerUI
from Ui_layer.MainMenuEMPUI import EmployeeUI

class LogIn:
    def __init__(self, email = "", name = "", staff_class = "", location = ""):
        self.name = name
        self.email = email
        self.staff_class = staff_class
        self.location = location
        

    def main_menu(self):
        
        if self.staff_class == "m":
            ManagerUI.managers_menu()
        elif self.staff_class == "e":
            EmployeeUI.valmynd_starfsfolk()
        else:
            print("Some information is wrong")
            self.main_menu()
    
    
            

            
