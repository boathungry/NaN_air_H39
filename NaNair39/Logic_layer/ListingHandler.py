from Data_layer.DLAPI import DLAPI
from Models.EmployeeModel import Employee



class ListingHandler:
    def __init__(self, data_api:DLAPI = DLAPI()) -> None:
        self.dl_api = data_api

    def list_all_employees_unsorted(self) -> list:
        """Returns a list of all employees."""
        return self.dl_api.get_all_employees()
        
    def list_all_location_names(self) -> list:
        """Returns a list of all location names."""
        return self.dl_api.get_all_location_names()

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
        """Returns a list of items whose name contains the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if filter in item.name:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_location(self, unfiltered_list, filter) -> list:
        """Returns a list of items whose location matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.location == filter:
                filtered_list.append(item)
        
        return filtered_list

    def list_printer(self, list_to_print):
        for x in list_to_print:
            print(x)

    def filter_by_title(self, unfiltered_list, filter) -> list:
        """Returns a list of items whose title matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.title == filter:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_address(self, unfiltered_list, filter) -> list:
        """Returns a list of items whose address contains the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if filter in item.address:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_size(self, unfiltered_list, min_size:int, max_size:int = 0):
        """If both min_size and max_size are specified, returns a list of items of size min_size to max_size.
        If only min_size is specified, returns a list of items of size min_size."""
        filtered_list = []
        if max_size == 0:
            for item in unfiltered_list:
                if int(item.size) == min_size:
                    filtered_list.append(item)
        else:
            for item in unfiltered_list:
                if int(item.size) >= min_size and int(item.size) <= max_size:
                    filtered_list.append(item)

        return filtered_list

    def filter_by_rooms(self, unfiltered_list, min_rooms:int, max_rooms:int = 0):
        """If both min_rooms and max_rooms are specified, returns a list of items with room count min_rooms to max_rooms.
        If only min_rooms is specified, returns a list of items with room count min_rooms."""
        filtered_list = []
        if max_rooms == 0:
            for item in unfiltered_list:
                if int(item.rooms) == min_rooms:
                    filtered_list.append(item)
        else:
            for item in unfiltered_list:
                if int(item.rooms) >= min_rooms and int(item.rooms) <= max_rooms:
                    filtered_list.append(item)

        return filtered_list
    
    def location_existence_check(self, location):
        location = location



    #Filters still missing:
    #ID
    #work request
    #worker
    #priority
    #repeat
    #time
    #start
    #done
    #work request id
    #properties
    #regular maintenance
    #approved