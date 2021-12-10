from Data_layer.EmployeeDL import EmployeeDL
from Data_layer.PropertiesDL import PropertyDL
from Data_layer.WorkReportDL import WorkReportDL
from Data_layer.WorkRequestDL import WorkRequestDL
from Data_layer.ContractorsDL import ContractorDL
from Data_layer.LocationsDL import locationDL
class DLAPI:
    
    def __init__(self):
        self.emplDL = EmployeeDL()
        self.propDL = PropertyDL()
        self.VB = WorkReportDL()
        self.reqDL = WorkRequestDL()
        self.contr = ContractorDL()
        self.locDL = locationDL()

    def get_all_employees(self):
        '''Lists all employees'''
        return self.emplDL.get_all_employees()
    
    def create_employee(self, empl):
        '''Creates a new employee'''
        return self.emplDL.create_employee(empl)

    def delete_employee(self,empl):
        '''Deletes an existing employee'''
        return self.emplDL.delete_employee(empl)

    def search_employee(self, attribute:str, value) -> list:
        """Searches for employees whose values in the given attribute matches the given value. Returns a list of employees."""
        return self.emplDL.search_for_employee(attribute, value)

    def dict_search_employee(self, attribute:str, value) -> dict:
        """Searches for employees whose values in the given attribute matches the given value. Returns a list of dictionaries for employees."""
        return self.emplDL.dict_search_for_employee(attribute, value)

    def change_information(self, empl):
        '''Changes information on given employee'''
        return self.emplDL.change_information_employee(empl)
    
    def get_employee_id_number(self):
        '''Gets employees ID number'''
        return self.emplDL.get_employee_id_number()
    
    def get_work_report_id_number(self):
        return self.VB.get_work_report_id_number()

    def get_work_request_id_number(self):
        return self.reqDL.get_work_request_id_number()

    def get_all_properties(self):
        '''Lists all properties'''
        return self.propDL.get_all_properties()
    
    def create_property(self,prop):
        '''Creates a new property'''
        return self.propDL.create_property(prop)

    def delete_property(self,prop):
        '''Deletes an existing property'''
        return self.propDL.delete_property(prop)

    def search_property(self, attribute:str, value) -> list:
        """Searches for properties whose values in the given attribute matches the given value. Returns a list of properties."""
        return self.propDL.search_for_property(attribute, value)

    def change_information_property(self,prop):
        '''Changes information on an existing property'''
        return self.propDL.change_information_property(prop)
    
    def get_all_work_reports(self):
        '''Lists all work reports'''
        return self.VB.get_all_work_reports()
    
    def create_work_report(self,VB):
        '''Creates a new work report'''
        return self.VB.create_work_report(VB)

    def delete_work_report(self,VB):
        '''Deletes an existing work report'''
        return self.VB.delete_work_report(VB)
    
    def search_work_report(self, attribute:str, value) -> list:
        """Searches for work reports whose values in the given attribute matches the given value. Returns a list of work reports."""
        return self.VB.search_for_work_report(attribute, value)

    def search_location(self, attribute:str, value) -> list:
        """searches for destinations"""
        return self.locDL.search_for_destination(attribute, value)
    
    def dict_search_location(self, attribute:str, value) -> dict:
        """searches for destinations"""
        return self.locDL.search_for_destination(attribute, value)
    
    def dict_search_property(self, attribute:str, value) -> dict:
        """searches for destinations"""
        return self.propDL.dict_search_for_property(attribute, value)

    def change_information_work_report(self,VB):
        '''Changes information on existing work report'''
        return self.VB.change_information_work_report(VB)

    def get_all_work_requests(self):
        '''Lists all work requests'''
        return self.reqDL.get_all_work_requests()
    
    def create_work_request(self,req):
        '''Creates a new work request'''
        return self.reqDL.create_work_request(req)

    def delete_work_request(self,req):
        '''Deletes an existing work request'''
        return self.reqDL.delete_work_request(req)

    def search_work_request(self, attribute:str, value) -> list:
        """Searches for work requests whose values in the given attribute matches the given value. Returns a list of work requests."""
        return self.reqDL.search_for_work_request(attribute, value)

    def dict_search_work_request(self, attribute:str, value) -> dict:
        """Searches for work requests whose values in the given attribute matches the given value. Returns a dict of work requests."""
        return self.reqDL.dict_search_for_work_request(attribute, value)

    def login_by_ID(self,email):    
        '''Logs employee in by ID'''
        return self.emplDL.login_by_ID(email)

    def list_all_contractors(self):
        '''List all contractors'''
        return self.contr.list_all_contractors()

    def create_contractor(self, contr):
        '''Creates a contractor'''
        return self.contr.create_contractor(contr)

    def create_destination(self, location):
        return self.locDL.create_new_destination(location)

    def get_all_destinations(self):
        """returns a list with info on all destinations available"""
        return self.locDL.get_all_locations()

    def search_destination(self, attribute:str, value) -> list:
        """Searches for properties whose values in the given attribute matches the given value. Returns a list of properties."""
        return self.locDL.search_for_destination(attribute, value)

    def get_all_location_names(self):
        '''Lists all work requests'''
        return self.locDL.get_all_location_names()
        
    def get_all_property_id(self):
        """returns a list of all used property id numbers"""
        return self.propDL.get_all_property_ID()

    def get_all_location_names_wr(self):
        '''Lists all work requests'''
        return self.reqDL.get_all_location_names_wr()