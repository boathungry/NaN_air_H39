from Data_layer.DLAPI import DLAPI

NAME = "name"
LOCATION = "location"
TITLE = "title"
ADDRESS = "address"
SIZE = "size"
ROOMS = "rooms"
ID = "id"
WORKER = "worker"
PRIORITY = "priority"
START = "start"
TIME = "time"
DONE = "done"
REGULAR_MAINTENANCE = "regular maintenance"
PROPERTY = "property"
APPROVED = "approved"

class ListingHandler:
    def __init__(self, data_api:DLAPI = DLAPI()) -> None:
        self.dl_api = data_api
        self.filters = [NAME, LOCATION, TITLE, ADDRESS, SIZE, ROOMS, ID, WORKER, PRIORITY, START, TIME, DONE, REGULAR_MAINTENANCE, PROPERTY, APPROVED]



    def list_printer(self, list_to_print):
        for x in list_to_print:
            print(x)

    def location_existence_check(self, location):
        location = location


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



    def filter(self, attribute:str, unfiltered_list, filter, filter_max = 0):
        """Returns a list of items whose attributes match the given filter. Use filter_max if you'd like to get a list of items with values from {filter} to {filter_max}."""
        attribute = attribute.lower()
        if attribute in self.filters:
            if attribute == NAME:
                return self.filter_by_name(unfiltered_list, filter)
            elif attribute == LOCATION:
                return self.filter_by_location(unfiltered_list, filter)
            elif attribute == TITLE:
                return self.filter_by_title(unfiltered_list, filter)
            elif attribute == ADDRESS:
                return self.filter_by_address(unfiltered_list, filter)
            elif attribute == SIZE:
                return self.filter_by_size(unfiltered_list, filter, filter_max)
            elif attribute == ROOMS:
                return self.filter_by_rooms(unfiltered_list, filter, filter_max)
            elif attribute == ID:
                return self.filter_by_id(unfiltered_list, filter)
            elif attribute == WORKER:
                return self.filter_by_worker(unfiltered_list, filter)
            elif attribute == PRIORITY:
                return self.filter_by_priority(unfiltered_list, filter)
            elif attribute == START:
                return self.filter_by_start(unfiltered_list, filter)
            elif attribute == TIME:
                return self.filter_by_time(unfiltered_list, filter)
            elif attribute == DONE:
                return self.filter_by_done(unfiltered_list, filter)
            elif attribute == REGULAR_MAINTENANCE:
                return self.filter_by_regular_maintenance(unfiltered_list, filter)
            elif attribute == PROPERTY:
                return self.filter_by_property(unfiltered_list, filter)
            elif attribute == APPROVED:
                return self.filter_by_approved(unfiltered_list, filter)
        else:
            return None

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
    
    def filter_by_id(self, unfiltered_list, filter):
        """Returns a list of items whose IDs contain the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if filter in item.id or filter in item.idnumber:
                filtered_list.append(item)

        return filtered_list

    def filter_by_worker(self, unfiltered_list, filter):
        """Returns a list of items (most likely work reports/requests) whose workers match the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.worker == filter:
                filtered_list.append(item)

        return filtered_list

    def filter_by_priority(self, unfiltered_list, filter):
        """Returns a list of items whose priority matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.priority == filter:
                filtered_list.append(item)

        return filtered_list

    def filter_by_start(self, unfiltered_list, filter):
        """Returns a list of items whose start time matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.start == filter:
                filtered_list.append(item)

        return filtered_list

    def filter_by_time(self, unfiltered_list, filter):
        """Returns a list of items whose time value matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.time == filter:
                filtered_list.append(item)

        return filtered_list

    def filter_by_done(self, unfiltered_list, filter):
        """Returns a list of values whose 'done' variable matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.done == filter:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_regular_maintenance(self, unfiltered_list, filter):
        """Returns a list of values whose 'regular maintenance' variable matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.regular_maintenance == filter:
                filtered_list.append(item)
        
        return filtered_list

    def filter_by_property(self, unfiltered_list, filter):
        """Returns a list of items whose 'property' or 'properties' variables match or contain the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if filter in item.properties or item.property == filter:
                filtered_list.append(item)

        return filtered_list

    def filter_by_approved(self, unfiltered_list, filter):
        """Returns a list of items whose 'approved' variable matches the given filter."""
        filtered_list = []
        for item in unfiltered_list:
            if item.approved == filter:
                filtered_list.append(item)

        return filtered_list
