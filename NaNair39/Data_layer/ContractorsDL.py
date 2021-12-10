import csv
from Models.ContractorModel import Contractor

class ContractorDL:

    def __init__(self):

        self.filepath = "csv_files/Contractors.csv"

    def list_all_contractors(self):
        '''Lists all contractors in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cont = Contractor(row["name"],row["phone"], row["email"], row["opening_hours"],row["address"],row["location"])
                return_list.append(cont)
        return return_list

    def create_contractor(self,cont):
        '''Appends a contractor to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","phone","email","opening_hours","address","location",]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': cont.name, 'phone': cont.phone, 'email': cont.email, 'opening_hours': cont.opening_hours, 'address': cont.address, 'location': cont.location})
    

