import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI 

class LogedIn:
    def __init__(self, ID, name, email, location, title):
        self.ID = ID
        self.name = name
        self.email = email
        self.title = title
        self.location = location

    def __str__(self):
        return f"ID: {self.ID} name: {self.name}, email: {self.email}, title: {self.title}, location: {self.location}"

    def main_menu(self):

        if self.title.lower() == "manager":
            manager_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
            manager_user.managers_menu()
        elif self.title.lower() == "employee":
            staff_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
            staff_user.staff_menu()
        else:
            print("Some information is wrong")
            
    
    
        