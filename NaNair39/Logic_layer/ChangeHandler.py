from Models.EmployeeModel import Employee
from Logic_layer.LLAPI import LLAPI

NAME = "name"
LOCATION = "location"
ADDRESS = "address"
PHONE = "phone"
CELLPHONE = "cellphone"
TITLE = "title"

class ChangeHandler():
    def __init__(self) -> None:
        pass

    def change_employee(employee:Employee, attribute:str, new_value:str):
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

    def change_property(property:Property, attribute, new_value):
        pass

    def change_contractor(contractor:Contractor, attribute, new_value):
        pass

    def change_work_order(work_order:WorkOrder, attribute, new_value):
        pass