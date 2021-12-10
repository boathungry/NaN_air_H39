import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI
from Logic_layer.LLAPI import LLAPI
from Models.WorkRequestModel import WorkRequest
import Data_layer.WorkRequestDL


class WorkReportMenu:
    def __init__(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done, logic_api:LLAPI = LLAPI()):
        self.id = id
        self.work_request = work_request
        self.location = location
        self.properties = properties
        self.description = description
        self.worker = worker
        self.priority = priority
        self.repeat = repeat
        self.time = time
        self.start = start
        self.done = done
        self.llapi = logic_api

    def Work_report_manager_menu(self):
        print("1. Create work request")
        print("2. Create work report")
        print("3. Change work request")
        print("4. Mark work request as done")
        print("5. Accept finished work reports")
        print("6. View work request")
        print("7. View work reports")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1":
            pass
        elif selection == "2":
            pass
        elif selection == "3":
            self.edit_work_request()
        elif selection == "4":
            pass
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "6":
            pass
        elif selection == "b":
            #current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.ID, self.name, self.email, self.location, self.title)
            #current_user.managers_menu()
            pass
        elif selection == "q":
            pass
        else:
            print("Wrong input!")
            self.Work_report_manager_menu()

 
#id,work_request,location,properties,description,worker,priority,repeat,time,start,done

    def edit_work_request(self):
        print("Change information about a work request")
        work_request_ID = input("What is the work request´s ID number?: ").capitalize()
        Work_requestinfo = self.llapi.dict_search(WorkRequest,  attribute="id", value = work_request_ID)
        results = Work_requestinfo
        print(results)

        id = results[0]["wreqid"]
        work_request = results[0]["wreqwork_request"]
        location = results[0]["wreqlocation"]
        properties = results[0]["wreqproperties"]
        description = results[0]["wreqdescription"]
        worker = results[0]["wreqworker"]
        priority = results[0]["wreqpriority"]
        repeat = results[0]["wreqrepeat"]
        time = results[0]["wreqtime"]
        start = results[0]["wreqstart"]
        done = results[0]["wreqdone"]

        staff_editor = True
        while staff_editor:
            print(f"ID number:      {id}")
            print(f"Work request:   {work_request}")
            print(f"Location:       {location}")
            print(f"Properties:     {properties}")
            print(f"Description:    {description}")
            print(f"Worker:         {worker}")
            print(f"Priority:       {priority}")
            print(f"Repeat:         {repeat}")
            print(f"Time:           {time}")
            print(f"Start:          {start}")
            print(f"Done:           {done}")

            print("Select a field to change: [w]ork request, [l]ocation, [p]roperties, [d]escription, [wo]rker, [pr]iority, [r]epeat, [t]ime, [s]tart, [d]one.")
            fieldchange = input("Input the letter of the field you wish to change: ")
            if fieldchange.lower() == "w":
                name = input("What is your new work request?: ")   
            elif fieldchange.lower() == "l":
                location_check_on = True
                while location_check_on:
                    available_locations = self.llapi.list_of_location_names()
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = input("What location is the new work request at?: ")
                    if location not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_check_on = False
            elif fieldchange.lower() == "p":    
                address = input("What is the new property?: ")
            elif fieldchange.lower() == "s":
                phone = input("What is the new size of the property?: ")
            elif fieldchange.lower() == "d":
                cellphone = input("What is the new description?: ")
            elif fieldchange.lower() == "wo":
                cellphone = input("Who is the new worker?: ")
            elif fieldchange.lower() == "pr":
                cellphone = input("What is the new priority?: ")
            elif fieldchange.lower() == "r":
                cellphone = input("Would you like to repeat (y/n)?: ")
            elif fieldchange.lower() == "t":
                cellphone = input("When would you like to repeat (none/daily/weekly/monthly/yearly)?: ")
            elif fieldchange.lower() == "s":
                cellphone = input("What is the new start date?: ")
            elif fieldchange.lower() == "d":
                cellphone = input("What is the new finished date?: ")
            else:
                print("Invalid option put into selection field.")
            editmore = input("Would you like to stop editing input [y] to commit changes and go back to the main menu, input [c] to cancel, input anything else to keep editing: ")
            if editmore == "y":
                staff_editor = False
                results_final = {}
                results_final["wreqid"] = id
                results_final["wreqwork_request"] = work_request
                results_final["wreqlocation"] = location
                results_final["wreqproperties"] = properties
                results_final["wreqdescription"] = description
                results_final["wreqworker"] = worker
                results_final["wreqpriority"] = priority
                results_final["wreqrepeat"] = repeat
                results_final["wreqtime"] = time
                results_final["wreqstart"] = start
                results_final["wreqdone"] = done
                #Skrifa í skrá
                init = Data_layer.WorkRequestDL.WorkRequestDL()
                init.change_information_work_request(results_final)
                #self.managers_menu()
            elif editmore == "c":
                staff_editor = False
            else:
                pass


    def create_work_request():
        pass

    def create_maintenance_report():
        pass

    def change_maintenance_report():
        pass

    def mark_meaitenance_or_work_report_as_ready_for_closing():
        pass

    def Accept_finished_maintenance_and_work_reports():
        pass
    
    def View_work_and_maintenance_reports():
        pass


    def work_report_staff_menu(self):
        print("1. Create work request")
        print("2. create maintenance request")
        print("3. Change maintenance report")
        print("4. Browse work and maintenance reports")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1":
            pass
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection.lower() == "b":
            current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.ID, self.name, self.email, self.location, self.title)
            current_user.staff_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.work_report_staff_menu()