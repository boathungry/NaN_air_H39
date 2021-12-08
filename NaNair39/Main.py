import Ui_layer.main_login
import Ui_layer.Login_menuUI
import Ui_layer.MainMenuEMPUI
import Ui_layer.MainMenuMANUI 
def main():
    user = Ui_layer.Login_menuUI.LogIn.innskra()
    
    print(user)
    Ui_layer.main_login.LogedIn.main_menu(user)
    """selection = Ui_layer.Login_menuUI.LogIn.temp_innskra()
    if selection == "1":
        user = ManagerUI("Manager")
        ManagerUI.managers_menu(user)
    elif selection == "2":
        Ui_layer.MainMenuEMPUI
    elif selection.lower == "q":
        Ui_layer.MainMenuMANUI.ManagerUI(title="manager").managers_menu()
        
    elif selection == "2":
        Ui_layer.MainMenuEMPUI.EmployeeUI(title="staff").staff_menu()
    elif selection.lower() == "q":
        pass
    else:
        print("Wrong input!")
        main()
main()
        main()"""
main()
