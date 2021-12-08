import csv
from os import name
from Models.LoginModel import LoginAccount
from Models.EmployeeModel import Employee

class EmployeeDL:

    def __init__ (self, name, email, location, address, phone, cellphone, title):
        self.name = name
        self.email = email
        self.location = location
        self.address = address
        self.phone = phone
        self.cellphone = cellphone
        self.title = title

        #filepath = "csv_files/Employee.csv"
        #correct_filepath = Users/valdisosk/Desktop/3\ vikna/NaN_air_H39/NaNair39/csv_files
    def __str__(self):
        return self.email

    def get_all_employees():
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
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","location","address","phone","cellphone","title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': empl.name, 'email': empl.email, 'location': empl.location, 'address': empl.address, 'phone': empl.phone, 'cellphone': empl.cellphone, 'title': empl.title})


    def change_information_employee(self, attribute, new_value,employee):
        self.attribute = attribute
        self.employee = employee
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            pass


    def search_by_email(self):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    empl = Employee(row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
            return empl

    def search_by_location(self):
        empl_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader = csv.DictReader
            for row in reader:
                if row["location"]==self.location:
                    empl = Employee(row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
                    empl_list.append(empl)
            return empl_list
            
    def login_by_email(self):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == self.email:
                    user = LoginAccount(row["name"],row["email"], row["location"],row["title"])
                    return user

    