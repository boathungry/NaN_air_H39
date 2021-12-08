from NaNair39.Logic_layer.LLAPI import LLAPI
from NaNair39.Data_layer.DLAPI import DLAPI
from NaNair39.Models.EmployeeModel import Employee
from NaNair39.Models.PropertyModel import Property
from NaNair39.Models.WorkReportModel import WorkReport
from NaNair39.Models.WorkRequestModel import WorkRequest
from NaNair39.Models.ContractorModel import Contractor


class SearchHandler():
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
        #elif search_object == Contractor:
        #    search_results = self.data_api.search_contractor(attribute, value)
        #NOT IMPLEMENTED YET

        return search_results