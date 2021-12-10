from Data_layer.EmployeeDL import EmployeeDL
import Logic_layer.LLAPI
class LogIn:
    def __init__(self, user= ""):
        self.user = user
    
    def innskra():
        loginon = True
        while loginon:
            print("To quit put q in the ID field")
            loginID = input("Please input your employee ID: ").capitalize()
            if loginID.lower() == "q":
                loginon = False
                return "q"
            else:
                userID = EmployeeDL(loginID)
                user = EmployeeDL.login_by_ID(userID)
                if user == None:
                    print("ID number not found")
                else:
                    return user

    def __str__(self):
        return self.user 
        