from Data_layer.EmployeeDL import EmployeeDL

class LogIn:


    def innskra():
        print("---------- NAN Air ----------")
        print("1. Login")
        print("q. Quit")
        answer = input("\nAðgerð: ")
    
        if answer == "1": 
            print("\n--------- LOGIN ----------")
            useremail = input("Enter email: ")

            if len(useremail) > 0:
                print("fékk email: " + useremail)
                #employeeDL = EmployeeDL
                #print(employeeDL)
                all_employees = EmployeeDL.get_all_employees()
                print("\n------------------------------------\n")
                print(all_employees)
                #usermail = EmployeeDL(email)
                    #print(usermail)
                    #user = EmployeeDL.login_by_email(usermail)
                    #print(user)
                    #return user
            else:
                print("Ekki gild email-addressa")
        elif answer == "q":
            print("----------- END --------------\n")

        
    def temp_innskra():
        print("1. Managers")
        print("2. Staff")
        print("q. Quit")
        selection = input("Input selection: ")
        return selection
