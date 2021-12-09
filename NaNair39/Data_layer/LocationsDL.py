import csv

from Models.LocationModel import Location

class locationDL:
    def __init__(self,city = "",country = "", location= ""):
        self.city = city
        self.country = country
        self.location = location
        self.filepath = "csv_files/Locations.csv"

        def __str__(self):
            return self.city

    def get_all_locations(self):
        '''Returns all locations in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = Location(row["city"],row["country"],row["airport"],row["phone_number"],row["opening_hours"],row["local_manager"])
                return_list.append(loct)
        return return_list

    def create_new_destination(self, location):
        '''Appends a new destination to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["city","country","airport","phone_number","opneing_hours","local_manager"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'city': location.city,'country': location.country, 'airport': location.airport, 'phone_number': location.phone_number, 'opening_hours': location.opening_hours, 'local_manager': location.local_manager})
    
    def search_for_destination(self, attribute:str, value):
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prop = Location(row["city"],row["country"], row["airport"], row["phone_number"],row["opening_hours"],row["local_manager"])
                if row[attribute] == value:
                    results_list.append(prop)
            return results_list

    def get_all_location_names(self):
        '''Returns all location names in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = row["city"]
                return_list.append(loct)
        return return_list