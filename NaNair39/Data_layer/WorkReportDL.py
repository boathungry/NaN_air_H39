import csv

from Models.WorkReportModel import WorkReport

class WorkReportDL:

    def __init__ (self):
        self.filepath = "csv_files/Workorders.csv"

    def get_all_work_reports(self):
        return_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                VB = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"], row["approved"])
                return_list.append(VB)
        return return_list
    
    def create_work_report(self, VB):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "work_request_id", "description", "location", "properties", "worker", "comment", "regular_maintenance", "expenses", "start", "done", "approved"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': VB.id, 'work_request_id': VB.work_request_id, 'description': VB.description, 'location': VB.location, 'properties': VB.properties, 'worker': VB.worker, 'comment': VB.comment, 'regular_maintenance': VB.regular_maintenance, 'expenses': VB.expenses, 'start': VB.start, 'done': VB.done, 'approved': VB.approved})

    def delete_work_report(self, VB):
        pass

    def change_information_work_report(self, VB):
        pass

    def search_for_work_report(self, attribute:str, value) -> list:
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                report = WorkReport(row["id"],row["work_request_id"], row["description"], row["location"], row["properties"], row["worker"], row["comment"], row["regular_maintenance"], row["expenses"], row["start"], row["done"], row["approved"])
                if row[attribute] == value:
                    results_list.append(report)
        return results_list
