import Ui_layer.main_login
import Ui_layer.Login_menuUI
import Ui_layer.MainMenuEMPUI
import Ui_layer.MainMenuMANUI 
def main():
    user = Ui_layer.Login_menuUI.LogIn.innskra()

    if user == "q":
        print("Thank you and have a nice day.")
    else:
        userstring = str(user)
        splituser = userstring.split(", ")
        loggedin = Ui_layer.main_login.LogedIn(splituser[0], splituser[1], splituser[2], splituser[3])
        loggedin.main_menu()
    
    """selection = Ui_layer.Login_menuUI.LogIn.temp_innskra()
    if selection == "1":
        user = ManagerUI("Manager")
        ManagerUI.managers_menu(user)
    elif selection == "2":
        Ui_layer.MainMenuEMPUI
    elif selection.lower == "q":
<<<<<<< HEAD
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
=======
        pass
    else:
        print("Wrong input!")"""

main()

        
>>>>>>> b95217144dc85bd080b9d01a58e1213e02ba3606
