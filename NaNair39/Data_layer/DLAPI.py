from EmployeeDL import EmployeeDL

class DLAPI:
    
    def __init__(self):
        self.emplDL = EmployeeDL()

    def get_all_employees(self):
        return self.emplDL.get_all_employees()

    def create_employee(self, empl):
        return self.emplDL.create_employee(empl)

    def delete_employe(self,empl):
        return self.emplDL.delete_employee(empl)

    def change_information(self, empl):
        return self.emplDL.change_information
