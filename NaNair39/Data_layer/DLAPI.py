from Data_layer.EmployeeDL import EmployeeDL
from Data_layer.PropertiesDL import PropertyDL
from Data_layer.WorkReportDL import WorkReportDL
from Data_layer.WorkRequestDL import WorkRequestDL
from Data_layer.ContractorsDL import ContractorDL

class DLAPI:
    
    def __init__(self):
        self.emplDL = EmployeeDL()
        self.propDL = PropertyDL()
        self.VB = WorkReportDL()
        self.reqDL = WorkRequestDL()
        self.contr = ContractorDL()

    def get_all_employees(self):
        return self.emplDL.get_all_employees()

    def create_employee(self, empl):
        return self.emplDL.create_employee(empl)

    def delete_employee(self,empl):
        return self.emplDL.delete_employee(empl)

    def search_employee(self, attribute:str, value) -> list:
        """Searches for employees whose values in the given attribute matches the given value. Returns a list of employees."""
        return self.emplDL.search_for_employee(attribute, value)

    def change_information(self, empl):
        return self.emplDL.change_information_employee(empl)
    
    def get_employee_id_number(self):
        return self.emplDL.get_employee_id_number()

    def get_all_properties(self):
        return self.propDL.get_all_properties()
    
    def create_property(self,prop):
        return self.propDL.create_property(prop)

    def delete_property(self,prop):
        return self.propDL.delete_property(prop)

    def search_property(self, attribute:str, value) -> list:
        """Searches for properties whose values in the given attribute matches the given value. Returns a list of properties."""
        return self.propDL.search_for_property(attribute, value)

    def change_information_property(self,prop):
        return self.propDL.change_information_property(prop)
    
    def get_all_work_reports(self):
        return self.VB.get_all_work_reports()
    
    def create_work_report(self,VB):
        return self.VB.create_work_report(VB)

    def delete_work_report(self,VB):
        return self.VB.delete_work_report(VB)
    
    def search_work_report(self, attribute:str, value) -> list:
        """Searches for work reports whose values in the given attribute matches the given value. Returns a list of work reports."""
        return self.VB.search_for_work_report(attribute, value)

    def change_information_work_report(self,VB):
        return self.VB.change_information_work_report(VB)

    def get_all_work_requests(self):
        return self.reqDL.get_all_work_requests()
    
    def create_work_request(self,req):
        return self.reqDL.create_work_request(req)

    def delete_work_request(self,req):
        return self.reqDL.delete_work_request(req)

    def search_work_request(self, attribute:str, value) -> list:
        """Searches for work requests whose values in the given attribute matches the given value. Returns a list of work requests."""
        return self.reqDL.search_for_work_request(attribute, value)

    def login_by_email(self,email):    
        return self.emplDL.login_by_email(email)

    def list_all_contractors(self, contr):
        return self.contr.list_all_contractors(contr)

    def create_contractor(self, contr):
        return self.contr.create_contractor(contr)
