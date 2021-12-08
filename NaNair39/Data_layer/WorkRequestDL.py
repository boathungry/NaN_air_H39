from Models.WorkRequestModel import WorkRequest
import csv

class WorkRequestDL():
    def __init__(self):
        pass

    def get_all_work_requests(self):
        '''Lists all work requests to the given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                req = WorkRequest(row["id"],row["work_request"], row["location"], row["properties"],row["description"],row["worker"],row["priority"],row["repeat"],row["time"],row["start"],row["done"])
                return_list.append(req)
        return return_list

    def create_work_request(self, req):
        '''appends a new work request to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","location","address","phone","cellphone","title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': req.id, 'location': req.location, 'properties': req.properties, 'description': req.description, 'worker': req.worker, 'priority': req.priority, 'repeat': req.repeat, 'time': req.time, 'start': req.start, 'done': req.done})
    


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
