from Data_layer.EmployeeDL import EmployeeDL
class LogIn:
    def innskra():
        print("To quit put q in email field")
        email = input("Please input your email: ")
        if email.lower() == "q":
            pass
        else:
            user = EmployeeDL.login_by_email(email)
            return user

        
        