from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.ContractorModel import Contractor
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest
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

ID = "id"
REQUEST = "work_request"
LOCATION = "location"
PROPERTIES = "properties"
DESCRIPTION = "description"
WORKER = "worker"
PRIORITY = "priority"
REPEAT = "repeat"
TIME = "time"
START = "start"
DONE = "done"

OPEN = "open date"
DUE = "due date"
PRIORITY = "priority"
REPEAT = "repeat"
INTERVAL = "repeat interval"

class ChangeHandler():
    def __init__(self, dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api

    def change_employee(self, employee:Employee, attribute:str, new_value):
        """Takes an employee, an attribute of that employee, and a new value for the attribute. Changes the attribute to the new value.
        Returns the given attribute if the function found an attribute by that name and managed to change it, otherwise returns None."""
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
        
        self.dl_api.change_information(employee) #Make sure to change the employee data immediately
        return attribute

    def change_property(self, property:Property, attribute:str, new_value):
        """Takes a property, an attribute of that property, and a new value for the attribute. Changes the attribute to the new value.
        Returns the given attribute if the function found an attribute by that name and managed to change it, otherwise returns None."""
        attribute = attribute.lower()
        if attribute == NAME:
            property.name = new_value
        elif attribute == LOCATION:
            property.location = new_value
        elif attribute == SIZE:
            property.size = new_value
        elif attribute == ROOMS:
            property.rooms = new_value
        else:
            return None

        self.dl_api.change_information_property(property)
        return attribute

    def change_contractor(self, contractor:Contractor, attribute:str, new_value):
        """Takes a contractor, an attribute of that employee, and a new value for the attribute. Changes the attribute to the new value.
        Returns the given attribute if the function found an attribute by that name and managed to change it, otherwise returns None."""
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
        else:
            return None

        self.dl_api.change_information_contractor(contractor) #NOT IMPLEMENTED YET
        return attribute

    def change_work_report(self, work_report:WorkReport, attribute:str, new_value):
        """Takes a work report, an attribute of that work report, and a new value for the attribute. Changes the attribute to the new value.
        Returns the given attribute if the function found an attribute by that name and managed to change it, otherwise returns None."""
        attribute = attribute.lower()
        if attribute == LOCATION:
            work_report.location = new_value
        elif attribute == PROPERTIES:
            work_report.properties = new_value
        elif attribute == DESCRIPTION:
            work_report.description = new_value
        elif attribute == DONE:
            work_report.done == new_value
        else:
            return None
        
        self.dl_api.change_information_work_report(work_report)
        return attribute

    def change_work_request(self, work_request:WorkRequest, attribute:str, new_value):
        attribute = attribute.lower()
        if attribute == REQUEST:
            work_request.work_request = new_value
        elif attribute == LOCATION:
            work_request.location = new_value
        elif attribute == PROPERTIES:
            work_request.properties = new_value
        elif attribute == DESCRIPTION:
            work_request.description = new_value
        elif attribute == WORKER:
            work_request.worker= new_value
        elif attribute == PRIORITY:
            work_request.priority= new_value
        elif attribute == REPEAT:
            work_request.repeat= new_value
        elif attribute == TIME:
            work_request.time= new_value
        elif attribute == START:
            work_request.start= new_value
        elif attribute == DONE:
            work_request.done= new_value
        else: return None

        self.dl_api.change_information_work_request(work_request) #NOT IMPLEMENTED YET
        return attribute
