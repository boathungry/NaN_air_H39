import csv

from Models.WorkorderModel import Workorder

class Workorder:

    def __init__ (self):
        self.filepath = "csv_files/Workorders.csv"

    def get_all_Workorders(self):
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                VB = Workorder(row["work request"],row["location"], row["properties"], row["description"])
                return_list.append(VB)
        return return_list
    
    def create_employee(self, VB):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["work request","location","properties","description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'': VB.workorder, 'location': VB.location, 'property': VB.properties, 'description': VB.description})
    
    def delete_employee(self, VB):
        pass

    def change_information(self, VB):
        pass

"work request,location,properties,description"
