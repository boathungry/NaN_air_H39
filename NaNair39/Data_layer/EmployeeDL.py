import csv
from Models.LoginModel import LoginAccount
from Models.EmployeeModel import Employee

class EmployeeDL:

    def __init__ (self, email= "", location= ""):
        self.location = location
        self.email = email
        self.filepath = "csv_files/Employee.csv"


    def __str__(self):
        '''Returns the necessary string'''
        return self.email


    def get_all_employees(self):
        '''Returns a list of employees in the given filepath'''
        return_list = []
        with open("/Users/valdisosk/Desktop/csvtest/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                print(row["name"], "-", row["email"], "-", row["location"], "-", row["address"], "-", row["phone"], "-", row["cellphone"], "-", row["title"])
                empl = Employee(row["name"], row["email"], row["location"], row["address"], row["phone"], row["cellphone"], row["title"])
                print("-----", empl)
                return_list.append(empl)
                print("_?_?_?_?_?_?_?_", return_list)
        return return_list
    

    def create_employee(self, empl):
        '''Appends a new employee to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","location","address","phone","cellphone","title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': empl.name, 'email': empl.email, 'location': empl.location, 'address': empl.address, 'phone': empl.phone, 'cellphone': empl.cellphone, 'title': empl.title})

    
    def get_employee_id_number(self,empl):
        '''Checks the next avaliable id number and returns'''
    

    def change_information_employee(self, attribute, new_value, employee):
        self.attribute = attribute
        self.employee = employee
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
        


    def search_for_employee(self, attribute:str, value):
        """Searches for employees whose values in the given attribute matches the given value. Returns a list of employees."""
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[attribute]==value:
                    empl = Employee(row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
                    results_list.append(empl)
            return results_list
            
            
    def login_by_email(self):
        '''Given the users email checks if user is a registered employee or a manager'''
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    user = LoginAccount(row["name"],row["email"], row["location"],row["title"])
                    
                    return user

    