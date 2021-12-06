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
                VB = WorkReport(row["work request"],row["location"], row["properties"], row["description"])
                return_list.append(VB)
        return return_list
    
    def create_work_report(self, VB):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["work request","location","properties","description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'': VB.workreport, 'location': VB.location, 'property': VB.properties, 'description': VB.description})
    
    def delete_work_report(self, VB):
        pass

    def change_information_work_report(self, VB):
        pass
