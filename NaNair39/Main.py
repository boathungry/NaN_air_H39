from Ui_layer.main_login import LogedIn
from Ui_layer.Login_menuUI import LogIn
def main():
    user = LogIn.innskra()
    print(user)
    LogedIn(user)
    
main()