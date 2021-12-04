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

PROPERTIES = "properties"
DESCRIPTION = "description"

class ChangeHandler():
    def __init__(self, dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api

    def change_employee(self, employee:Employee, attribute:str, new_value):
        """Takes an employee, an attribute of that employee, and a new value for the attribute. Changes the attribute to the new value."""
        attribute = attribute.lower()
        if attribute == NAME:
            employee.name = new_value
        elif attribute == LOCATION:
            employee.location = new_value
        elif attribute == ADDRESS:
            employee.address = new_value
        elif attribute == PHONE:
            employee.phone = new_value
        elif attribute == CELLPHONE:
            employee.cellphone = new_value
        elif attribute == TITLE:
            employee.title = new_value
        else:
            return None
        
        self.dl_api.change_information(employee)
        return new_value

    def change_property(self, property:Property, attribute:str, new_value):
        """Takes a property, an attribute of that property, and a new value for the attribute. Changes the attribute to the new value."""
        attribute = attribute.lower()
        if attribute == NAME:
            property.name = new_value
        elif attribute == LOCATION:
            property.location = new_value
        elif attribute == SIZE:
            property.size = new_value
        elif attribute == ROOMS:
            property.rooms = new_value

    def change_contractor(self, contractor:Contractor, attribute:str, new_value):
        """Takes a contractor, an attribute of that employee, and a new value for the attribute. Changes the attribute to the new value."""
        attribute = attribute.lower()
        if attribute == NAME:
            contractor.name = new_value
        elif attribute == PHONE:
            contractor.phone = new_value
        elif attribute == EMAIL:
            contractor.email = new_value
        elif attribute == HOURS:
            contractor.opening_hours = new_value
        elif attribute == ADDRESS:
            contractor.address = new_value

    def change_work_report(self, work_report:WorkReport, attribute:str, new_value):
        """Takes a work report, an attribute of that work report, and a new value for the attribute. Changes the attribute to the new value."""
        attribute = attribute.lower()
        if attribute == LOCATION:
            work_report.location = new_value
        elif attribute == PROPERTIES:
            work_report.properties = new_value
        elif attribute == DESCRIPTION:
            work_report.description = new_value