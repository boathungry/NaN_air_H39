from Data_layer.DLAPI import DLAPI
from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest
from Models.ContractorModel import Contractor
from Models.LocationModel import Location

class SearchHandler:
    def __init__(self, search_results = "", dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api
        self.search_results = search_results

    def search(self, search_object, attribute:str, value) -> list:
        """Searches for objects of the given type whose values in the given attribute match the given value.
        Returns a list of the found objects."""

        if search_object == Employee:
            search_results = self.dl_api.search_employee(attribute, value)
        elif search_object == Property:
            search_results = self.dl_api.search_property(attribute, value)
        elif search_object == WorkReport:
            search_results = self.dl_api.search_work_report(attribute, value)
        elif search_object == WorkRequest:
            search_results = self.dl_api.search_work_request(attribute, value)
        elif search_object == Location:
            search_results = self.dl_api.search_location(attribute, value)
        self.search_results = search_results
        return self.search_results

    def dict_search(self, search_object, attribute:str, value) -> dict:
        """Searches for objects of the given type whose values in the given attribute match the given value.
        Returns a dictionary of the found objects."""

        if search_object == Employee:
            search_results = self.dl_api.dict_search_employee(attribute, value)
        elif search_object == Property:
            search_results = self.dl_api.dict_search_property(attribute, value)
        elif search_object == WorkReport:
            search_results = self.dl_api.dict_search_work_report(attribute, value)
        elif search_object == WorkRequest:
            search_results = self.dl_api.dict_search_work_request(attribute, value)
        elif search_object == Location:
            search_results = self.dl_api.dict_search_location(attribute, value)
        self.search_results = search_results
        return self.search_results
    
    def does_he_work_there(self, employee, location):
        """checks if a employee works at the selected location"""
        return self.dl_api.does_he_work_there(employee, location)

    def __str__(self):
        return self.search_results