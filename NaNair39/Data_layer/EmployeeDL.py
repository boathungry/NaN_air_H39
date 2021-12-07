import csv
from Models.LoginModel import LoginAccount
from Models.EmployeeModel import Employee

class EmployeeDL:

    def __init__ (self, email= "", location= ""):
        self.location = location
        self.email = email
        self.filepath = "csv_files/Employee.csv"
    def __str__(self):
        return self.email
    def get_all_employees(self):
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                empl = Employee(row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
                return_list.append(empl)
        return return_list
    
    def create_employee(self, empl):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","location","address","phone","cellphone","title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': empl.name, 'email': empl.email, 'location': empl.location, 'address': empl.address, 'phone': empl.phone, 'cellphone': empl.cellphone, 'title': empl.title})
    


    def change_information_employee(self, attribute, new_value,employee):
        self.attribute = attribute
        self.employee = employee
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            pass


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
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    user = LoginAccount(row["name"],row["email"], row["location"],row["title"])
                    return user
