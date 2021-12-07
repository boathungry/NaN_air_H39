from Models.WorkReportModel import WorkReport
from Data_layer.DLAPI import DLAPI
from Logic_layer.ChangeHandler import ChangeHandler
from datetime import date

class WorkReport():

    def __init__(self, dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api

    def approve_report(self, work_report:WorkReport):
        ChangeHandler.change_work_report(self, work_report, "approved", date.today())
