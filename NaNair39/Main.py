import Ui_layer.main_login
import Ui_layer.Login_menuUI
import Ui_layer.MainMenuEMPUI
import Ui_layer.MainMenuMANUI 
def main():
    user = Ui_layer.Login_menuUI.LogIn.innskra()

    if user == "q":
        print("")
        print("Thank you and have a nice day.")
    else:
        userstring = str(user)
        print(userstring)
        splituser = userstring.split(", ")
        loggedin = Ui_layer.main_login.LogedIn(splituser[0], splituser[1], splituser[2], splituser[3], splituser[4])
        loggedin.main_menu()
    
main()