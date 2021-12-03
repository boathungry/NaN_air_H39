from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.ContractorModel import Contractor
from Models.WorkorderModel import Workorder

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

class ChangeHandler():
    def __init__(self) -> None:
        pass

    def change_employee(employee:Employee, attribute:str, new_value):
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

    def change_property(property:Property, attribute:str, new_value):
        attribute = attribute.lower()
        if attribute == NAME:
            property.name = new_value
        elif attribute == LOCATION:
            property.location = new_value
        elif attribute == SIZE:
            property.size = new_value
        elif attribute == ROOMS:
            property.rooms = new_value

    def change_contractor(contractor:Contractor, attribute:str, new_value):
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

    def change_work_order(work_order:Workorder, attribute:str, new_value):
        attribute = attribute.lower()
        if attribute == REQUEST:
            work_order.work_request = new_value
        elif attribute == LOCATION:
            work_order.location = new_value
        elif attribute == PROPERTIES:
            work_order.properties = new_value
        elif attribute == DESCRIPTION:
            work_order.description = new_value