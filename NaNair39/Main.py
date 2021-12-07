import Ui_layer.main_login
import Ui_layer.Login_menuUI
import Ui_layer.MainMenuEMPUI
from Ui_layer.MainMenuMANUI import ManagerUI
def main():
    """user = Ui_layer.Login_menuUI.LogIn.innskra()
    print(user)
    Ui_layer.main_login.LogedIn(user)"""
    selection = Ui_layer.Login_menuUI.LogIn.temp_innskra()
    if selection == "1":
        user = ManagerUI("manager")
        ManagerUI.managers_menu(user)
    elif selection == "2":
        Ui_layer.MainMenuEMPUI
    elif selection.lower == "q":
        pass
    else:
        print("Wrong input!")
        main()
main()
