from Logic_layer.LLAPI import LLAPI
from Data_layer.DLAPI import DLAPI
from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest

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

WORK_REQUEST_ID = "work_request_id"
COMMENT = "comment"
REGULAR_MAINTENANCE = "regular_maintenance"
EXPENSES = "expenses"
APPROVED = "approved"

class SearchHandler():
    def __init__(self, dl_api:DLAPI = DLAPI(), ll_api:LLAPI = LLAPI()) -> None:
        self.data_api = dl_api
        self.logic_api = ll_api

    def search(self, search_object, attribute:str, value):

        if search_object == Employee:
            search_results = self.search_for_empl(search_object, attribute, value)
        elif search_object == Property:
            search_results = self.search_for_prop(search_object, attribute, value)
        elif search_object == WorkReport:
            search_results = self.search_for_report(search_object, attribute, value)
        elif search_object == WorkRequest:
            search_results = self.search_for_request(search_object, attribute, value)

        return search_results

    def search_for_empl(self, employee:Employee, attribute:str, value):
        """Searches for employees whose given attribute (name, email, ID, etc.) matches the given value."""
        if attribute.lower() == NAME:
            result = self.data_api.search_by_name(employee) #NOT IMPLEMENTED YET
        elif attribute.lower() == EMAIL:
            result = self.data_api.search_by_email(employee)
        elif attribute.lower() == LOCATION:
            result = self.data_api.search_by_location(employee) #NOT IMPLEMENTED YET
        elif attribute.lower() == ADDRESS:
            result = self.data_api.search_by_address(employee) #NOT IMPLEMENTED YET
        elif attribute.lower() == PHONE:
            result = self.data_api.search_by_phone(employee) #NOT IMPLEMENTED YET
        elif attribute.lower() == CELLPHONE:
            result = self.data_api.search_by_cellphone(employee) #NOT IMPLEMENTED YET

    def search_for_prop(self, property:Property, attribute:str, value):
        pass

    def search_for_report(self, work_report:WorkReport, attribute:str, value):
        pass

    def search_for_request(self, work_request:WorkRequest, attribute:str, value):
        pass