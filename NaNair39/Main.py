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
<<<<<<< HEAD
        user = ManagerUI("Manager")
        ManagerUI.managers_menu(user)
    elif selection == "2":
        Ui_layer.MainMenuEMPUI
    elif selection.lower == "q":
=======
        Ui_layer.MainMenuMANUI.ManagerUI(title="manager").managers_menu()
        
    elif selection == "2":
        Ui_layer.MainMenuEMPUI.EmployeeUI(title="staff").staff_menu()
    elif selection.lower() == "q":
>>>>>>> af08d48a85a77809a569318da6dbcaa9d13547dc
        pass
    else:
        print("Wrong input!")
<<<<<<< HEAD
        main()
main()
=======
        main()"""
main()
>>>>>>> 2d07f59c42ece422c8a32fd932f0f4ff11c0d2fa
