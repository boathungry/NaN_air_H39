import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI 

class LogedIn:
    def __init__(self, name = "", email = "", location = "", title = ""):
        self.name = name
        self.email = email
        self.title = title
        self.location = location
        

    def main_menu(self):

        if self.title.lower() == "manager":
            Ui_layer.MainMenuMANUI.ManagerUI.managers_menu()
        elif self.title.lower() == "employee":
            "EmployeeUI.valmynd_starfsfolk()"
        else:
            print("Some information is wrong")
            self.main_menu()
    
    
            

            
