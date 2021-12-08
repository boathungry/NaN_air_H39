from Data_layer.DLAPI import DLAPI
from Logic_layer.ChangeHandler import ChangeHandler
from Logic_layer.RegistrationHandler import RegistrationHandler
from Logic_layer.WorkReportLL import WorkReport
from Logic_layer.WorkRequestLL import WorkRequest
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest


class LLAPI():
    def __init__(self, data_API = DLAPI()) -> None:
        self.dl_API = data_API
        self.change_handler = ChangeHandler(data_API)
        self.registration_handler = RegistrationHandler(data_API)
        self.work_report = WorkReport(data_API)
        self.work_request = WorkRequest(data_API)

    def get_employee_id_number(self):
        return self.registration_handler.get_employee_id_number()

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

    def create_employee(self, name, location, address, phone, cellphone, title):
        """Creates a new employee with the given attributes and returns the employee."""
        return self.registration_handler.register_employee(name, location, address, phone, cellphone, title)

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
