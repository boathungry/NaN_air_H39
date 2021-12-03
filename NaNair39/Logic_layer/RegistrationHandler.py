from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.ContractorModel import Contractor
from Models.WorkorderModel import Workorder
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
        new_employee = Employee(name, location, address, phone, cellphone, title)
        DLAPI.create_employee(new_employee)
        return new_employee

    def register_property(self, name, location, size, rooms):
        new_property = Property(name, location, size, rooms)
        DLAPI.create_property(new_property)
        return new_property

    def register_contractor(self, name, phone, email, opening_hours, address):
        new_contractor = Contractor(name, phone, email, opening_hours, address)
        DLAPI.create_contractor(new_contractor)
        return new_contractor

    def register_workorder(self, work_request, location, properties, description):
        new_workorder = Workorder(work_request, location, properties, description)
        DLAPI.create_workorder(new_workorder)
        return new_workorder

    def register_work_request(self, id, open_date, due_date, repeat:bool, repeat_interval_days:int = 0, priority:str, property:Property):
        pass