from Data_layer.DLAPI import DLAPI
from Logic_layer.LLAPI import LLAPI
from Models.EmployeeModel import Employee



class ListingHandler:
    def __init__(self, data_api:DLAPI = DLAPI, logic_api:LLAPI = LLAPI) -> None:
        self.dl_api = data_api
        self.ll_api = logic_api

    def list_all_employees_unsorted(self) -> list:
        """Returns a list of all employees."""
        return self.dl_api.get_all_employees()

    def list_all_properties_unsorted(self) -> list:
        """Returns a list of all properties."""
        return self.dl_api.get_all_properties()

    def list_all_work_reports_unsorted(self) -> list:
        """Returns a list of all work reports."""
        return self.dl_api.get_all_work_reports()

    def list_all_work_requests_unsorted(self) -> list:
        """Returns a list of all work requests."""
        return self.dl_api.get_all_work_requests()


    def sort_by_name(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.name, reverse=descending)

    def sort_by_location(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.location, reverse=descending)

    def sort_by_address(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.address, reverse=descending)

    def sort_by_size(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.size, reverse=descending)

    def sort_by_rooms(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.rooms, reverse=descending)

    def sort_by_priority(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.priority, reverse=descending)

    def sort_by_start(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.start, reverse=descending)
    
    def sort_by_expenses(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.expenses, reverse=descending)

    def sort_by_worker(self, unsorted_list, descending:bool = False) -> list:
        return sorted(unsorted_list, key=lambda item: item.worker, reverse=descending)


    def filter_by_name(self, unfiltered_list, filter) -> list:
        """Returns a list of items whose name matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.name == filter:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_location(self, unfiltered_list, filter) -> list:
        """Returns a list of items whose location matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.location == filter:
                filtered_list.append(item)
        
        return filtered_list