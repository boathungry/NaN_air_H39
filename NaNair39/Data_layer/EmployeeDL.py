import csv
from Models.LoginModel import LoginAccount
from Models.EmployeeModel import Employee


class EmployeeDL:

    def __init__ (self, ID= "", location= ""):
        self.location = location
        self.ID = ID
        self.filepath = "csv_files/Employee.csv"


    def __str__(self):
        '''Returns the necessary string'''
        return self.ID


    def get_all_employees(self):
        '''Returns a list of employees in the given filepath'''
        return_list = []
        with open("csv_files/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                empl = Employee(row["id"],row["name"], row["email"], row["location"], row["address"], row["phone"], row["cellphone"], row["title"])
                return_list.append(empl)
        return return_list
    

    def create_employee(self, empl):
        '''Appends a new employee to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id","name","email","location","address","phone","cellphone","title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': empl.idnumber,'name': empl.name, 'email': empl.email, 'location': empl.location, 'address': empl.address, 'phone': empl.phone, 'cellphone': empl.cellphone, 'title': empl.title})

    
    def get_employee_id_number(self):
        prev_temp = int(1)
        '''Checks the next avaliable id number and returns'''
        with open("csv_files/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                temp_number = row["id"]
                if int(temp_number[1:]) >= prev_temp:
                        prev_temp = (int(temp_number[1:])+1)
            return prev_temp  


    def change_information_employee(self, employee):
        pass
    """
        self.employee = employee
        header = ["id", "name", "email", "location", "address", "phone", "cellphone", "title"]
        new_list = []
        
        #Get all file(all lines)
        with open("csv_files/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if (row["id"] == self.employee.id):
                    empl = Employee(self.employee.id, self.employee.name, self.employee.email, self.employee.location, self.employee.address, self.employee.phone, self.employee.cellphone, self.employee.title)
                else:
                    empl = Employee(row["id"],row["name"], row["email"], row["location"], row["address"], row["phone"], row["cellphone"], row["title"])
            new_list.append(empl)
        #Write all file(all lines)
        with open("csv_files/Employee.csv", mode="w", newline='', encoding='utf-8') as csvfile:
            employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(header)
            employee_writer.writerow(new_list)
    """
    def search_for_employee(self, attribute:str, value):
        """Searches for employees whose values in the given attribute matches the given value. Returns a list of employees."""
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[attribute]==value:
                    empl = Employee(row["id"],row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
                    
                    results_list.append(empl)
            return results_list
            
            
    def login_by_ID(self):
        '''Given the users ID checks if user is a registered employee or a manager'''
        with open("csv_files/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["id"] == self.ID:
                    user = LoginAccount(row["id"],row["name"],row["email"], row["location"],row["title"])
                    
                    return user
    def search_by_ID(self):
        '''Given the users ID checks if user is a registered employee or a manager'''
        with open('csv_files/Employee.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["id"] == self.ID:
                    empl = Employee(row["id"],row["name"],row["email"], row["location"], row["address"],row["phone"],row["cellphone"],row["title"])
                    Employeedict = {"emid":empl.idnumber, "emname":empl.name, "ememail":empl.email, "emlocation":empl.location,"emaddress":empl.address,"emphone":empl.phone,"emcellphone":empl.cellphone,"emtitle":empl.title }
                    return Employeedict