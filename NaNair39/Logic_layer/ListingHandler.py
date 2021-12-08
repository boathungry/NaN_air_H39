from Data_layer.DLAPI import DLAPI
from Logic_layer.LLAPI import LLAPI
from Models.EmployeeModel import Employee
from Models.PropertyModel import Property
from Models.WorkRequestModel import WorkRequest
from Models.WorkReportModel import WorkReport
from Models.ContractorModel import Contractor

class ListingHandler():
    def __init__(self, data_api:DLAPI = DLAPI, logic_api:LLAPI = LLAPI) -> None:
        self.dl_api = data_api
        self.ll_api = logic_api

    def list_all_employees(self, sort_by:str = "name", ascending_descending:str = "ascending"):
        employees_list = self.dl_api.get_all_employees()
        if sort_by == "name" and ascending_descending == "ascending":
            sorted_list = sorted(employees_list, key=lambda employee: employee.name)
        return sorted_list

handler = ListingHandler()
sort_list = handler.list_all_employees()
print(sort_list)