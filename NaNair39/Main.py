import Ui_layer.main_login
import Ui_layer.Login_menuUI
def main():
    user = Ui_layer.Login_menuUI.LogIn.innskra()
    print(user)
    Ui_layer.main_login.LogedIn(user)
    
main()