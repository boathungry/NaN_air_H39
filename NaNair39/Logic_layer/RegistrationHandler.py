from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.ContractorModel import Contractor
from Models.WorkReportModel import WorkReport
from Data_layer.DLAPI import DLAPI

NAME = "name"
LOCATION = "location"
ADDRESS = "address"
PHONE = "phone"
CELLPHONE = "cellphone"
TITLE = "title"

SIZE = "size"
ROOMS = "rooms"

EMAIL = "email"
HOURS = "opening hours"

REQUEST = "work request"
PROPERTIES = "properties"
DESCRIPTION = "description"

class RegistrationHandler():
    def __init__(self) -> None:
        pass

    def register_employee(self, name, location, address, phone, cellphone, title):
        """Registers a new employee and returns the employee."""
        new_employee = Employee(name, location, address, phone, cellphone, title)
        DLAPI.create_employee(new_employee)
        return new_employee

    def register_property(self, name, location, size, rooms):
        """Registers a new property and returns the property."""
        new_property = Property(name, location, size, rooms)
        DLAPI.create_property(new_property)
        return new_property

    def register_contractor(self, name, phone, email, opening_hours, address):
        """Registers a new contractor and returns the contractor."""
        new_contractor = Contractor(name, phone, email, opening_hours, address)
        DLAPI.create_contractor(new_contractor)
        return new_contractor

    def register_work_report(self, work_request, location, properties, description):
        """Registers a new work report and returns the work report."""
        new_work_report = WorkReport(work_request, location, properties, description)
        DLAPI.create_work_report(new_work_report)
        return new_work_report

    def register_work_request(self, request_id, open_date, due_date, priority:str, property:Property, repeat:bool = False, repeat_interval_days:int = 0):
        pass