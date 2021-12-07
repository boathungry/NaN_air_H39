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
        self.empl_attributes = [NAME, LOCATION, ADDRESS, PHONE, CELLPHONE, TITLE]
        self.prop_attributes = [NAME, LOCATION, SIZE, ROOMS]

    def search(self, search_object, attribute:str, value) -> list:
        """Searches for objects of the given type whose values in the given attribute match the given value.
        Returns a list of the found objects."""

        if search_object == Employee:
            if attribute in self.empl_attributes:
                search_results = self.data_api.search_employee(attribute, value)
            else:
                search_results = []
        elif search_object == Property:
            if attribute in self.prop_attributes:
                search_results = self.data_api.search_property(attribute, value)
            else:
                search_results = []
        elif search_object == WorkReport:
            search_results = self.data_api.search_workreport(attribute, value)
        elif search_object == WorkRequest:
            search_results = self.data_api.search_workrequest(attribute, value)

        return search_results