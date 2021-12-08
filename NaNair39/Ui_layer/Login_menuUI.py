from Data_layer.EmployeeDL import EmployeeDL
class LogIn:
    def innskra():
        print("To quit put q in email field")
        email = input("Please input your email: ")
        if email.lower() == "q":
            pass
        else:
            usermail = EmployeeDL(email)
            print(usermail)
            user = EmployeeDL.login_by_email(usermail)
            return user
    def temp_innskra():
        print("1. Managers")
        print("2. Staff")
        print("q. Quit")
        selection = input("Input selection: ")
        return selection

        
        