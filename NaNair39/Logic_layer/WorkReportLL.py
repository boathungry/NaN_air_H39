from Models.WorkReportModel import WorkReport
from Logic_layer.LLAPI import LLAPI
from ChangeHandler import ChangeHandler
from datetime import date

class WorkReport():

    def __init__(self) -> None:
        pass

    def approve_report(self, work_report:WorkReport):
        ChangeHandler.change_work_report(self, work_report, "approved", date.today())
