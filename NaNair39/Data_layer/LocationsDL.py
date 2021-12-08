import csv

from Models.LocationModel import Location

class locationDL:
    def __init__(self,city,country):
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

