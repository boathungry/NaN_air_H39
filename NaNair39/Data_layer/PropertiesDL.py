import csv

from Models.PropertyModel import Property

class PropertyDL:

    def __init__(self, idnumber = ""):
        self.filepath = "csv_files/Properties.csv"
        self.idnumber = idnumber
    def __str__(self):
        return self.idnumber

    def get_all_properties(self):
        '''Lists all properties from the given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prop = Property(row["idnumber"],row["name"], row["location"], row["address"],row["size"],row["rooms"])
                return_list.append(prop)
        return return_list
    
    def create_property(self, prop):
        '''Appends a new property to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["idnumber","name","location","address","size","rooms"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'idnumber': prop.idnumber, 'name': prop.name, 'location': prop.location, 'address': prop.address, 'size': prop.size, 'rooms': prop.rooms})

    def delete_property(self, prop):
        pass

    def change_information_property(self, prop):
        header = ["idnumber", "name", "location", "address", "size", "rooms"]
        list_properties = []
        one_property = []

        #Get all file(all lines)
        with open("csv_files/Properties.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if (row["idnumber"] == prop["pridnumber"]):
                    one_property = (prop["pridnumber"], prop["prname"], prop["prlocation"], prop["praddress"], prop["prsize"], prop["prrooms"])
                else:
                    one_property = row["idnumber"],row["name"],row["location"], row["address"], row["size"], row["rooms"]
                list_properties.append(one_property)
        #Write all file(all lines)
        with open("csv_files/Properties.csv", mode="w", newline='', encoding='utf-8') as csvfile:
            prop_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            prop_writer.writerow(header)
            prop_writer.writerows(list_properties)

    """
    def search_property(self, idnumber):
        self.idnumber = idnumber
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader
            for row in reader:
                property = Property(row["idnumber"],row["name"], row["location"], row["address"],row["size"],row["cellphone"],row["rooms"])
                if row["idnumber"]==self.idnumber:
                    return property
                    
            return None
    """

    def search_for_property(self, attribute:str, value):
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prop = Property(row["idnumber"],row["name"], row["location"], row["address"], row["size"],row["rooms"])
                if row[attribute] == value:
                    results_list.append(prop)
            return results_list

    def dict_search_for_property(self, attribute:str, value):
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[attribute] == value:
                    prop = Property(row["idnumber"],row["name"], row["location"], row["address"],row["size"],row["rooms"])
                    Property_dict = {"pridnumber":prop.idnumber, "prname":prop.name, "prlocation":prop.location, "praddress":prop.address,"prsize":prop.size,"prrooms":prop.rooms }
                    results_list.append(Property_dict)
            return results_list

    def get_all_property_ID(self):
        '''Returns all location names in given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                idnumber = row["idnumber"].lower()
                return_list.append(idnumber)
        return return_list

    def is_it_there(self, id, location):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rowid = str(row["idnumber"]).lower()

                if rowid == id and row["location"] == location:
                    return True
            return False
                    