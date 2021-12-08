from Data_layer.EmployeeDL import EmployeeDL
class LogIn:
    def __init__(self, user= ""):
        self.user = user
    
    def innskra():
        loginon = True
        while loginon:
            print("To quit put q in email field")
            email = input("Please input your email: ")
            if email.lower() == "q":
                loginon = False
                return "q"
            else:
                usermail = EmployeeDL(email)
                print(usermail)
                user = EmployeeDL.login_by_email(usermail)
                if user == None:
                    print("Email adress not found")
                else:
                    return user
                
                    
                
    
    def temp_innskra():
        print("1. Managers")
        print("2. Staff")
        print("q. Quit")
        selection = input("Input selection: ")
        return selection

    def __str__(self):
        return self.user 
        