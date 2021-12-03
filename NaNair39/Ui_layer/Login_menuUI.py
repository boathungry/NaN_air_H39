
class HomeMenu:
    def __init__(self, email = ""):
        self.email = email

    def innskra(self):
        self.email = input("Please input your email: ")
        #input file opener and use dictionary to input all the things
        self.main_menu(self.staff_class)