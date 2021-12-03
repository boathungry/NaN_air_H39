import csv

from Models.PropertyModel import Property

class PropertyDL:

    def __init__(self):
        self.filepath = "csv_files/Properties.csv"

    def get_all_properties(self):
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prop = Property(row["idnumber"],row["name"], row["location"], row["address"],row["size"],row["rooms"])
                return_list.append(prop)
        return return_list
    
    def create_property(self, prop):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["idnumber","name","location","address","size","rooms"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Property': prop.idnumber, 'name': prop.name, 'location': prop.location, 'address': prop.address, 'size': prop.size, 'no of rooms': prop.rooms})
    
    def delete_property(self, prop):
        pass

    def change_information_property(self, prop):
        pass
