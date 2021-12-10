from Models.EmployeeModel import Employee
from Models.LocationModel import Location
from Models.PropertyModel import Property
from Models.ContractorModel import Contractor
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest
from Data_layer.DLAPI import DLAPI

class RegistrationHandler():
    def __init__(self, dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api

    def get_employee_id_number(location):
        DLAPIinit = DLAPI()
        number = str(DLAPIinit.get_employee_id_number())
        if len(number) == 2:
            id_number = f"{location[0].upper()}{0}{number}"
        elif len(number) == 3:
            id_number = f"{location[0].upper()}{number}"
        else:
            return None
        return id_number 

    def get_work_report_id_number():
        DLAPIinit = DLAPI()
        number = str(DLAPIinit.get_work_report_id_number())
        id_number = f"VB0{number}"
        return id_number

    def get_work_request_id_number():
        DLAPIinit = DLAPI()
        number = str(DLAPIinit.get_work_request_id_number())
        id_number = f"VS0{number}"
        return id_number

    def register_employee(self, idnumber, name, email, location, address, phone, cellphone, title):
        """Registers a new employee and returns the employee."""
        new_employee = Employee(idnumber, name, email, location, address, phone, cellphone, title)
        self.dl_api.create_employee(new_employee) #register new data to database immediately!
        return new_employee

    def register_property(self, idnumber, name, location, address, size, rooms):
        """Registers a new property and returns the property."""
        new_property = Property(idnumber, name, location, address, size, rooms)
        self.dl_api.create_property(new_property)
        return new_property

    def register_contractor(self, name, phone, email, opening_hours, address):
        """Registers a new contractor and returns the contractor."""
        new_contractor = Contractor(name, phone, email, opening_hours, address)
        self.dl_api.create_contractor(new_contractor) #NOT IMPLEMENTED YET
        return new_contractor

    def register_work_report(self, id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done, approved):
        """Registers a new work report and returns the work report."""
        new_work_report = WorkReport(id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done, approved)
        self.dl_api.create_work_report(new_work_report)
        return new_work_report

    def register_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
        """Registers a new work request and returns the work request."""
        new_work_request = WorkRequest(id, work_request, location, properties, description, worker, priority, repeat, time, start, done)
        self.dl_api.create_work_request(new_work_request)
        return new_work_request
    
    def register_location(self, city, country, airport, phone, opening, manager):
        new_location = Location(city, country, airport, phone, opening, manager)
        print(new_location)
        self.dl_api.create_destination(new_location)
        return new_location

       