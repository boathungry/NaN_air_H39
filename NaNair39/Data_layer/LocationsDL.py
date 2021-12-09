import csv

from Models.LocationModel import Location

class locationDL:
    def __init__(self,city = "",country = ""):
        self.city = city
        self.country = country
        self.filepath = "csv_files/Locations.csv"

    def get_all_locations(self):
        '''Returns all locations in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = Location(row["city"],row["country"],row["airport"],row["phone number"],row["opening hours"],row["local manager"])
                return_list.append(loct)
        return return_list

    def search_for_destination(self, attribute:str, value):
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prop = Location(row["city"],row["country"], row["airport"], row["phone number"],row["opening hours"],row["local manager"])
                if row[attribute] == value:
                    results_list.append(prop)
            return results_list

    def get_all_location_names(self):
        '''Returns all location names in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = Location(row["city"])
                return_list.append(loct)
        return return_list