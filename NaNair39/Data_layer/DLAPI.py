from Data_layer.EmployeeDL import EmployeeDL
from Data_layer.PropertiesDL import PropertyDL
from Data_layer.WorkReportDL import WorkReportDL
from Data_layer.WorkRequestDL import WorkRequestDL

class DLAPI:
    
    def __init__(self):
        self.emplDL = EmployeeDL()
        self.propDL = PropertyDL()
        self.VB = WorkReportDL()
        self.reqDL = WorkRequestDL()

    def get_all_employees(self):
        return self.emplDL.get_all_employees()

    def create_employee(self, empl):
        return self.emplDL.create_employee(empl)

    def delete_employe(self,empl):
        return self.emplDL.delete_employee(empl)

    def change_information(self, empl):
        return self.emplDL.change_information_employee(empl)

    def search_by_email(self, empl):
        return self.emplDL.search_by_email(empl)
    
    def get_all_properties(self):
        return self.propDL.get_all_properties()
    
    def create_property(self,prop):
        return self.propDL.create_property(prop)

    def delete_property(self,prop):
        return self.propDL.delete_property(prop)

    def change_information_property(self,prop):
        return self.propDL.change_information_property(prop)
    
    def get_all_work_reports(self):
        return self.VB.get_all_work_reports()
    
    def create_work_report(self,VB):
        return self.VB.create_work_report(VB)

    def delete_work_report(self,VB):
        return self.VB.delete_work_report(VB)

    def change_information_work_report(self,VB):
        return self.VB.change_information_work_report(VB)

    def get_all_work_requests(self):
        return self.reqDL.get_all_work_requests()
    
    def create_work_request(self,req):
        return self.reqDL.create_work_request(req)

    def delete_work_request(self,req):
        return self.reqDL.delete_work_request(req)

    
