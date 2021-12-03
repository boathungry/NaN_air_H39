from EmployeeDL import EmployeeDL
from NaNair39.Data_layer.PropertiesDL import PropertyDL
from PropertiesDL import PropertyDL
from WordordersDL import WorkorderDL

class DLAPI:
    
    def __init__(self):
        self.emplDL = EmployeeDL()
        self.propDL = PropertyDL()
        self.VB = WorkorderDL()

    def get_all_employees(self):
        return self.emplDL.get_all_employees()

    def create_employee(self, empl):
        return self.emplDL.create_employee(empl)

    def delete_employe(self,empl):
        return self.emplDL.delete_employee(empl)

    def change_information(self, empl):
        return self.emplDL.change_information_employee(empl)
    
    def get_all_properties(self):
        return self.propDL.get_all_properties()
    
    def create_property(self,prop):
        return self.propDL.create_property(prop)

    def delete_property(self,prop):
        return self.propDL.delete_property(prop)

    def change_information_property(self,prop):
        return self.propDL.change_information_property(prop)
    
    def get_all_workorders(self):
        return self.VB.get_all_Workorders()
    
    def create_workorder(self,VB):
        return self.VB.create_workorder(VB)

    def delete_workorder(self,VB):
        return self.VB.delete_workorder(VB)

    def change_information_workorder(self,VB):
        return self.VB.change_information_workorder(VB)
