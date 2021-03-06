from Models.LocationModel import Location
from Models.WorkRequestModel import WorkRequest
import csv

class WorkRequestDL:
    
    def __init__(self, id = "", location = ""):
        self.filepath = "csv_files/WorkRequests.csv"
        self.filepath_finished = "csv_files/FinishedWorkRequests.csv"
        self.id = id
        self.location = location

    def finalize_work_request(self,req):
        header = ["id", "work_request", "location", "properties", "description", "worker", "priority", "repeat", "time", "start", "done"]
        list_work_requests = []
        one_work_request = []
        with open("csv_files/WorkRequests.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if (row["id"] == req["wreqid"]):
                    with open(self.filepath_finished, 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = [row["id"], row["work_request"], row["location"], row["properties"], row["description"], row["worker"], row["priority"], row["repeat"], row["time"], row["start"], row["done"]]
                        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(fieldnames)
                else:
                    one_work_request = row["id"], row["work_request"], row["location"], row["properties"], row["description"], row["worker"], row["priority"], row["repeat"], row["time"], row["start"], row["done"]
                    list_work_requests.append(one_work_request)
        #Write all file(all lines)
                    with open("csv_files/WorkRequests.csv", mode="w", newline='', encoding='utf-8') as csvfile:
                        req_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        req_writer.writerow(header)
                        req_writer.writerows(list_work_requests)



    def get_all_open_work_requests(self):
        '''Lists all work requests to the given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                req = WorkRequest(row["id"],row["work_request"], row["location"], row["properties"],row["description"],row["worker"],row["priority"],row["repeat"],row["time"],row["start"],row["done"])
                return_list.append(req)
        return return_list

    def get_all_closed_work_requests(self):
        '''Lists all work requests to the given filepath'''
        return_list = []
        with open(self.filepath_finished, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                req = WorkRequest(row["id"],row["work_request"], row["location"], row["properties"],row["description"],row["worker"],row["priority"],row["repeat"],row["time"],row["start"],row["done"])
                return_list.append(req)
        return return_list

    def get_work_request_id_number(self):
        prev_temp = int(1)
        '''Checks the next avaliable id number and returns'''
        with open("csv_files/WorkRequests.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                temp_number = row["id"]
                if int(temp_number[2:]) >= prev_temp:
                    prev_temp = (int(temp_number[2:])+1)
                    prev_temp_string = str(prev_temp)
                    if len(prev_temp_string) == 1:
                        return_id = "VB0"+str(prev_temp)
                    else: 
                        return_id = "VB"+str(prev_temp) 
            return return_id     

    def create_work_request(self, req):
        '''appends a new work request to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id","work_request","location","properties","description","worker","priority","repeat","time","start","done"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': req.id, 'work_request': req.work_request, 'location': req.location, 'properties': req.properties, 'description': req.description, 'worker': req.worker, 'priority': req.priority, 'repeat': req.repeat, 'time': req.time, 'start': req.start, 'done': req.done})

    def change_information_work_request(self, req):
        header = ["id", "work_request", "location", "properties", "description", "worker", "priority", "repeat", "time", "start", "done"]
        list_work_requests = []
        one_work_request = []

        #Get all file(all lines)
        with open("csv_files/WorkRequests.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if (row["id"] == req["wreqid"]):
                    one_work_request = (req["wreqid"], req["wreqwork_request"], req["wreqlocation"], req["wreqproperties"], req["wreqdescription"], req["wreqworker"], req["wreqpriority"], req["wreqrepeat"], req["wreqtime"], req["wreqstart"], req["wreqdone"])
                else:
                    one_work_request = row["id"], row["work_request"], row["location"], row["properties"], row["description"], row["worker"], row["priority"], row["repeat"], row["time"], row["start"], row["done"]
                list_work_requests.append(one_work_request)
        #Write all file(all lines)
        with open("csv_files/WorkRequests.csv", mode="w", newline='', encoding='utf-8') as csvfile:
            req_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            req_writer.writerow(header)
            req_writer.writerows(list_work_requests)

    def delete_work_request(self, req):
        pass

    def search_for_work_request(self, attribute:str, value):
        '''Searches for a work request based on the given attribute'''
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                request = WorkRequest(row["id"],row["work_request"],row["location"],row["properties"],row["description"],row["worker"],row["priority"],row["repeat"],row["time"],row["start"],row["done"]) #ROWS ADDED
                if row[attribute] == value:
                    results_list.append(request)
            return results_list


    def dict_search_for_work_request(self, attribute:str, value):
        '''Searches for a work request based on the given attribute'''
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[attribute] == value:
                    request = WorkRequest(row["id"],row["work_request"],row["location"],row["properties"],row["description"],row["worker"],row["priority"],row["repeat"],row["time"],row["start"],row["done"]) #ROWS ADDED
                    Request_dict = {"wreqid":request.id, "wreqwork_request":request.work_request, "wreqlocation":request.location, "wreqproperties":request.properties,"wreqdescription":request.description,"wreqworker":request.worker, "wreqpriority":request.priority, "wreqrepeat":request.repeat, "wreqtime":request.time, "wreqstart":request.start, "wreqdone":request.done}
                    results_list.append(Request_dict)
            return results_list

    def get_all_location_names_wr(self):
        '''Returns all location names in given filepath'''
        return_list = ["All locations"]
        with open('csv_files/Locations.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loct = str(row["city"]+" - "+row["country"])
                if loct in return_list:
                    pass
                else:
                    return_list.append(loct)
            
        return return_list
    
    def get_your_location_name_wr(self, location):
        '''Returns all location names in given filepath'''
        return_list = []
        with open('csv_files/Locations.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["city"] == location:
                    loct = str(row["city"]+" - "+row["country"])
                    if loct in return_list:
                        pass
                    else:
                        return_list.append(loct)
            
        return return_list
    