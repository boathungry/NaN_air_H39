from Data_layer.DLAPI import DLAPI
from Logic_layer.ChangeHandler import ChangeHandler
from Logic_layer.ListingHandler import ListingHandler
from Logic_layer.RegistrationHandler import RegistrationHandler
from Logic_layer.SearchHandler import SearchHandler
from Logic_layer.WorkReportLL import WorkReport
from Logic_layer.WorkRequestLL import WorkRequest
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest


class LLAPI():
    def __init__(self, data_API = DLAPI()) -> None:
        self.dl_API = data_API
        self.change_handler = ChangeHandler(data_API)
        self.registration_handler = RegistrationHandler(data_API)
        self.search_handler = SearchHandler(data_API)
        self.listing_handler = ListingHandler(data_API)

    def get_employee_id_number(self):
        return self.registration_handler.get_employee_id_number()

    def get_work_report_id_number(self):
        return self.registration_handler.get_work_report_id_number()
    
    def get_work_request_id_number(self):
        return self.registration_handler.get_work_request_id_number()

    def change_employee(self, employee, attribute, new_value):
        """Changes an attribute of an employee to a new value. Returns the given attribute if successful, otherwise returns None."""
        return self.change_handler.change_employee(employee, attribute, new_value)

    def change_property(self, property, attribute, new_value):
        """Changes an attribute of a property to a new value. Returns the given attribute if successful, otherwise returns None."""
        return self.change_handler.change_property(property, attribute, new_value)

    def change_contractor(self, contractor, attribute, new_value):
        """Changes an attribute of a contractor to a new value. Returns the given attribute if successful, otherwise returns None."""
        return self.change_handler.change_contractor(contractor, attribute, new_value)

    def change_work_report(self, work_report, attribute, new_value):
        """Changes an attribute of a work report to a new value. Returns the given attribute if successful, otherwise returns None."""
        return self.change_handler.change_work_report(work_report, attribute, new_value)

    def change_work_request(self, work_request, attribute, new_value):
        """Changes an attribute of a work request to a new value. Returns the given attribute if successful, otherwise returns None."""
        return self.change_handler.change_work_request(work_request, attribute, new_value)


    def create_employee(self, name, email, location, address, phone, cellphone, title):
        """Creates a new employee with the given attributes and returns the employee."""
        idnumber = RegistrationHandler.get_employee_id_number(location)
        return self.registration_handler.register_employee(idnumber, name, email, location, address, phone, cellphone, title)

    def create_property(self, name, location, size, rooms):
        """Creates a new property with the given attributes and returns the property."""
        return self.registration_handler.register_property(name, location, size, rooms)
    
    def create_contractor(self, name, phone, email, opening_hours, address):
        """Creates a new contractor with the given attributes and returns the contractor."""
        return self.registration_handler.register_contractor(name, phone, email, opening_hours, address)

    def create_work_report(self, id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done, approved):
        """Creates a new work report with the given attributes and returns the work report."""
        return self.registration_handler.register_work_report(id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done, approved)

    def create_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
        """Creates a new work request with the given attributes and returns the work request."""
        return self.registration_handler.register_work_request(id, work_request, location, properties, description, worker, priority, repeat, time, start, done)

    def create_destination(self, city, country, airport, phone, open_hours, manager):
        """Creates a new property with the given attributes and returns the property."""
        return self.registration_handler.register_property(city, country, airport, phone, open_hours, manager)


    def search(self, search_object, attribute:str, value) -> list:
        """Returns a list of objects whose value in the given attribute matches the given value."""
        return self.search_handler.search(search_object, attribute, value)
    
    def dict_search(self, search_object, attribute:str, value) -> dict:
        """Returns a dictionary of objects whose value in the given attribute matches the given value."""
        return self.search_handler.dict_search(search_object, attribute, value)

    def list_printer(self, input_list):
        """Prints a list one row at a time"""
        self.listing_handler.list_printer(input_list)

    def list_all_employees(self):
        "gives a list of all employees and information"
        return self.listing_handler.list_all_employees_unsorted()
    
    def list_of_location_names(self):
        """returns a list of all location names"""
        return self.listing_handler.list_all_location_names()
    
    #fæ ekki til að virka og koma login í gegnum apa frekar en beint í úr login í datalayer
    """def login_byID(self, idnumber):
        "logs user in with ID number"
        return DLAPI.login_by_ID(self, idnumber)"""