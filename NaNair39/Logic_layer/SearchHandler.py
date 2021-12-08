from Logic_layer.LLAPI import LLAPI
from Data_layer.DLAPI import DLAPI
from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest
from Models.ContractorModel import Contractor
from Models.LocationModel import Location

class SearchHandler:
    def __init__(self, dl_api:DLAPI = DLAPI(), ll_api:LLAPI = LLAPI()) -> None:
        self.data_api = dl_api
        self.logic_api = ll_api

    def search(self, search_object, attribute:str, value) -> list:
        """Searches for objects of the given type whose values in the given attribute match the given value.
        Returns a list of the found objects."""

        if search_object == Employee:
            search_results = self.data_api.search_employee(attribute, value)
        elif search_object == Property:
            search_results = self.data_api.search_property(attribute, value)
        elif search_object == WorkReport:
            search_results = self.data_api.search_work_report(attribute, value)
        elif search_object == WorkRequest:
            search_results = self.data_api.search_work_request(attribute, value)
        elif search_object == Location:
            search_results = self.data_api.search_work_request(attribute, value)

        return search_results