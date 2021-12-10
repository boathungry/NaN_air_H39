import csv

from Models.WorkReportModel import WorkReport

class WorkReportDL:

    def __init__ (self):
        self.filepath = "csv_files/WorkReports.csv"

    #id,work_request_id,description,location,properties,worker,comment,regular_maintenance,expenses,start,done,approved
    def finalize_work_report(self,req):
        header = ["id", "work_request_id", "description", "location", "properties", "worker", "comment", "regular_maintenance", "expenses", "start", "done"]
        list_work_reports = []
        one_work_request = []
        with open("csv_files/WorkReports.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                print(row["work_request_id"])
                if (row["id"] == req["wropid"]):
                    with open("csv_files/ApprovedWorkReports.csv", 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = [row["id"], row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], req["wropdone"]]
                        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(fieldnames)
                else:
                    one_work_request = row["id"], row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"]
                    list_work_reports.append(one_work_request)
        #Write all file(all lines)
                    with open("csv_files/WorkReports.csv", mode="w", newline='', encoding='utf-8') as csvfile:
                        rep_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        rep_writer.writerow(header)
                        rep_writer.writerows(list_work_reports)

    def get_all_open_work_reports(self):
        '''Lists all work reports from the given filepath'''
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                VB = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"])
                return_list.append(VB)
        return return_list

    def get_all_closed_work_reports(self):
        '''Lists all work reports from the given filepath'''
        return_list = []
        with open("csv_files/ApprovedWorkReports.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                VB = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"])
                return_list.append(VB)
        return return_list

    def get_work_report_id_number(self):
        prev_temp = int(1)
        '''Checks the next avaliable id number and returns'''
        with open("csv_files/Employee.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                temp_number = row["id"]
                if int(temp_number[2:]) >= prev_temp:
                        prev_temp = (int(temp_number[1:])+1)
            return prev_temp  

    def create_work_report(self, VB):
        '''Appends a new work report to the given filepath'''
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "work_request_id", "description", "location", "properties", "worker", "comment", "regular_maintenance", "expenses", "start", "done"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': VB.id, 'work_request_id': VB.work_request_id, 'description': VB.description, 'location': VB.location, 'properties': VB.properties, 'worker': VB.worker, 'comment': VB.comment, 'regular_maintenance': VB.regular_maintenance, 'expenses': VB.expenses, 'start': VB.start, 'done': VB.done})

    def delete_work_report(self, VB):
        pass

    def search_for_open_work_report(self, attribute:str, value) -> list:
        '''Searches for work order within the given filepath, using the given attribute'''
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                report = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"])
                if row[attribute] == value:
                    results_list.append(report)
        return results_list

    def search_for_closed_work_report(self, attribute:str, value) -> list:
        '''Searches for work order within the given filepath, using the given attribute'''
        results_list = []
        attribute = attribute.lower()
        with open("csv_files/ApprovedWorkReports.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                report = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"])
                if row[attribute] == value:
                    results_list.append(report)
        return results_list

    def get_work_report_id_number(self):
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
                        return_id = "VS0"+str(prev_temp)
                    else: 
                        return_id = "VS"+str(prev_temp) 
            return return_id     

    def dict_search_for_work_report(self, attribute:str, value):
        '''Searches for a work request based on the given attribute'''
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[attribute] == value:
                    request = WorkReport(row["id"],row["work_request_id"],row["description"],row["location"],row["properties"],row["worker"],row["comment"],row["regular_maintenance"],row["expenses"],row["start"],row["done"]) #ROWS ADDED
                    Request_dict = {"wropid":request.id, "wropwork_request_id":request.work_request_id, "wropdescription":request.description, "wroplocation":request.location,"wropproperties":request.properties,"wropworker":request.worker, "wropcomment":request.comment, "wropregular_maintenance":request.regular_maintenance, "wropexpenses":request.expenses, "wropstart":request.start, "wropdone":request.done}
                    results_list.append(Request_dict)
            return results_list
