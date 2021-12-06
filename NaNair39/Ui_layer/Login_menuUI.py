from Data_layer.EmployeeDL import EmployeeDL
class LogIn:
    def innskra():
        email = input("Please input your email: ")
        user = EmployeeDL.search_by_email(email)
        return user
        
        
        