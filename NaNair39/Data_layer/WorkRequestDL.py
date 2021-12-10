from Models.WorkRequestModel import WorkRequest
import csv

class WorkRequestDL:
    
    def __init__(self):
        self.filepath = "csv_files/WorkRequests.csv"

    def get_all_work_requests(self):
        '''Lists all work requests to the given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
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
                        prev_temp = (int(temp_number[1:])+1)
            return prev_temp      

    def create_work_request(self, req):
        '''appends a new work request to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id","location","properties","description","worker","priority","repeat","time","start","done"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': req.id, 'location': req.location, 'properties': req.properties, 'description': req.description, 'worker': req.worker, 'priority': req.priority, 'repeat': req.repeat, 'time': req.time, 'start': req.start, 'done': req.done})

    def change_information_work_request(self, req):
        header = ["id", "work_request", "location", "properties", "description", "worker", "priority", "repeat", "time", "start", "done"]
        list_work_requests = []
        one_work_request = []

        #Get all file(all lines)
        with open("csv_files/WorkRequests.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if (row["id"] == ["wreqid"]):
                    one_work_request = (req["wreqid"], req["wreqwork_request"], req["wreqlocation"], req["wreqproperties"], req["wreqdescription"], req["wreqworker"], req["wreqpriority"], req["wreqrepeat"], req["wreqtime"], req["wreqstart"], req["wreqdone"])
                else:
                    one_work_request = row["wreqid"], row["wreqwork_request"], row["wreqlocation"], row["wreqproperties"], row["wreqdescription"], row["wreqworker"], row["wreqpriority"], row["wreqrepeat"], row["wreqtime"], row["wreqstart"], row["wreqdone"]
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
