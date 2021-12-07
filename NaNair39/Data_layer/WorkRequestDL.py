from NaNair39.Models.WorkRequestModel import WorkRequest


class WorkRequestDL():
    def __init__(self) -> None:
        pass

    def get_all_work_requests(self):
        pass

    def create_work_request(self, req):
        pass

    def delete_work_request(self, req):
        pass

    def search_for_work_request(self, attribute:str, value):
        results_list = []
        attribute = attribute.lower()
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                request = WorkRequest(row["?????"]) #ROWS NOT ADDED YET
                if row[attribute] == value:
                    results_list.append(request)
        return results_list
