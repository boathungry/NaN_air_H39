from Login_menuUI import HomeMenu
from ForemanMenu import YfirmennUI
from EmployeeMenu import EmployeeUI
class LogIn:
    def __init__(self, email = "", name = "", staff_class = "", location = ""):
        self.name = name
        self.email = email
        self.staff_class = staff_class
        self.location = location

    def main_menu(self):
        HomeMenu.innskra()
        
        if self.staff_class == "y":
            YfirmennUI.valmynd_yfirmenn()
        elif self.staff_class == "s":
            EmployeeUI.valmynd_starfsfolk()
        else:
            print("Some information is wrong")
            HomeMenu.innskra()
    
    
            

            
