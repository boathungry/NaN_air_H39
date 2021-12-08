import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI 
import Models.LoginModel
class LogedIn(Models.LoginModel.LoginAccount):
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return f"name: {self.name}, emai: {self.email}, title: {self.title}, location: {self.location}"

    def main_menu(self):

        if self.title.lower() == "manager":
            Ui_layer.MainMenuMANUI.ManagerUI.managers_menu()
        elif self.title.lower() == "employee":
            Ui_layer.MainMenuEMPUI.EmployeeUI.staff_menu()
        else:
            print("Some information is wrong")
            self.main_menu()
    
    
        