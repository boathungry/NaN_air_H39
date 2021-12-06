import csv

from Models.EmployeeModel import Employee

class EmployeeDL:

    def __init__ (self):
        self.filepath = "csv_files/Employee.csv"

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
    
    def delete_employee(self, empl):
        pass

    def change_information_employee(self, empl):
        pass

    def search_by_email(self, email):
        self.email = email
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    empl = Employee(row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
            return empl

    def login_by_email(self, email):
        self.email = email
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    user = Employee(row["name"],row["email"], row["location"],row["title"])
            return user
