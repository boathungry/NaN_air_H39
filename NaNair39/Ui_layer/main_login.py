from Ui_layer.MainMenuMANUI import ManagerUI
from Ui_layer.MainMenuEMPUI import EmployeeUI

class LogedIn:
    def __init__(self, email = "", name = "", title = "", location = ""):
        self.name = name
        self.email = email
        self.title = title
        self.location = location
        

    def main_menu(self):

        if self.title.lower() == "manager":
            ManagerUI.managers_menu()
        elif self.title.lower() == "employee":
            "EmployeeUI.valmynd_starfsfolk()"
        else:
            print("Some information is wrong")
            self.main_menu()
    
    
            

            
