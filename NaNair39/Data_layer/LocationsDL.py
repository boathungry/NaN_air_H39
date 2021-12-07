import csv

from Models.LocationModel import Location

class locationDL:
    def __init__(self,city,country):
        self.city = city
        self.country = country
        self.filepath = "csv_files/Locations.csv"

    def get_all_locations(self):
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = Location(row["city"],row["country"])
                return_list.append(loct)
        return return_list

all_locations = locationDL.get_all_locations()
for i in all_locations:
    print(i)