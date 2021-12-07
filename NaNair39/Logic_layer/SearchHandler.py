from Logic_layer.LLAPI import LLAPI
from Data_layer.DLAPI import DLAPI
from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.WorkReportModel import WorkReport


class SearchHandler():
    def __init__(self) -> None:
        pass

    def search(self, object, attribute, value):
        pass

    def search_for(self, object):
        """Determines whether the object being searched for is an employee, property, etc. and returns the object type."""
        pass

    def search_for_empl_by(self, attribute, value):
        """Searches for employees whose given attribute (name, email, ID, etc.) matches the given value."""
        pass