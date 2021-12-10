import string
from Logic_layer.LLAPI import LLAPI
from Models.WorkRequestModel import WorkRequest
import Data_layer.WorkRequestDL


class WorkReportMenu:
    def __init__(self, idnumber = "", name = "", email = "", location = "", title = "", logic_api:LLAPI = LLAPI()):
        self.idnumber = idnumber
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api
        self.llapi = logic_api

    def Work_report_manager_menu(self):
        print("1. Create work request")
        print("2. Create work report")
        print("3. Change work request")
        print("4. Mark work request as done")
        print("5. Accept finished work reports")
        print("6. View work requests")
        print("7. View work reports")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1":
            return self.create_work_request()
        elif selection == "2":
            return self.create_work_report()
        elif selection == "3":
            return self.edit_work_request()
        elif selection == "4":
            return self.finalize_work_request()
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            pass
        elif selection == "b":
            return True
        elif selection == "q":
            return False
        else:
            print("Wrong input!")
            return self.Work_report_manager_menu()

 
#id,work_request,location,properties,description,worker,priority,repeat,time,start,done
    def finalize_work_request(self):
        print("What work request would you like to approve/close")
        work_request_id = (input("Enter work request ID number: "))
        work_request_info = self.llapi.dict_search(WorkRequest, attribute="id", value=work_request_id)
        results = work_request_info
        if len(results)<1:
            print("No requests found with that ID")
            return self.finalize_work_request()
        else:
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
            editor = True
            while editor:
                print("")
                print("Please confirm the following details.")
                print("")
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
                print("")
                approve = string.capwords(input("Do you confirm the details above and wish to approve this work request?(y/n): "))
                if approve == "Y":
                    editor = False
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
                    init = Data_layer.WorkRequestDL.WorkRequestDL(id=results_final["wreqid"], location=results_final["wreqlocation"])
                    init.finalize_work_request(results_final)
                    return True
                elif approve == "N":
                    editor = False
                    return True
                else:
                    print("Wrong input")
                    editor = True



    def edit_work_request(self):
        print("Change information about a work request")
        work_request_ID = input("What is the work requests ID number?: ")
        Work_requestinfo = self.llapi.dict_search(WorkRequest,  attribute="id", value=work_request_ID)
        results = Work_requestinfo
        if len(results) < 1:
            print("No requests found with that ID")
            return self.edit_work_request() 
        else:
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
            

            request_editor = True
            while request_editor:
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

                print("Select a field to change: [w]ork request, [l]ocation, [p]roperties, [d]escription, [wo]rker, [pr]iority, [r]epeat, [t]ime, [s]tart, [do]ne.")
                fieldchange = input("Input the letter of the field you wish to change: ")
                if fieldchange.lower() == "w":
                    work_request = input("What is your new work request?: ")   
                elif fieldchange.lower() == "l":
                    location_check_on = True
                    while location_check_on:
                        available_locations = self.llapi.list_of_location_names_wr()
                        print("Available locations are as follows:")
                        self.llapi.list_printer(available_locations)
                        location = input("What location is the new work request at?: ")
                        if location not in available_locations:
                            print("Not a valid location, please either create a new location or select an available one")
                        else:
                            location_check_on = False
                elif fieldchange.lower() == "p":    
                    properties = input("What is the new property?: ")
                elif fieldchange.lower() == "d":
                    description = input("What is the new description?: ")
                elif fieldchange.lower() == "wo":
                    worker = input("Who is the new worker?: ")
                elif fieldchange.lower() == "pr":
                    priority = input("What is the new priority?: ")
                elif fieldchange.lower() == "r":
                    repeat = input("Would you like to repeat (y/n)?: ")
                elif fieldchange.lower() == "t":
                    time = input("When would you like to repeat (none/daily/weekly/monthly/yearly)?: ")
                elif fieldchange.lower() == "s":
                    start = input("What is the new start date?: ")
                elif fieldchange.lower() == "do":
                    done = input("What is the new finished date?: ")
                else:
                    print("Invalid option put into selection field.")
                editmore = input("Would you like to stop editing input [y] to commit changes and go back to the main menu, input [c] to cancel, input anything else to keep editing: ")
                if editmore == "y":
                    request_editor = False
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
                    init = Data_layer.WorkRequestDL.WorkRequestDL(id=results_final["wreqid"], location=results_final["wreqlocation"])
                    init.change_information_work_request(results_final)
                    return True
                elif editmore == "c":
                    request_editor = False
                    return True
                else:
                    pass


    def create_work_request(self):
        counter = 0
        print("")
        create_work_request_loop = True
        fieldchange = ""
        while create_work_request_loop:
            print(counter)
            if counter != 0:
                print("Is this the correct information?")
                print(f"Work request: {work_request}")
                print(f"Location:     {location}")
                print(f"Properties:   {properties}")
                print(f"Description:  {description}")
                print(f"Worker:       {worker}")
                print(f"Priority:     {priority}")
                print(f"Repeat (y/n): {repeat}")
                print(f"Time:         {time}")
                print(f"Start:        {start}")
                print(f"Done:         {done}")

                rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
                if rightorwrong.lower() == "y":
                    create_work_request_loop = False
                    self.llapi.create_work_request(work_request, location, properties, description, worker, priority, repeat, time, start, done = "")
                    return True
                elif rightorwrong.lower() == "c":
                    create_work_request_loop = False
                    fieldchange = ""
                    return True
                elif rightorwrong.lower() == "n":
                    print("Select a field to change: [w]ork request, [l]ocation, [p]roperties, [d]escription, [wo]rker, [pr]iority, [r]epeat, [t]ime, [s]tart, [do]ne.")
                    fieldchange = input("Input the letter of the field you wish to change: ")
            if counter == 0 or counter !=0 and fieldchange.lower() == "w":
                work_request_comma_check_on = True
                while work_request_comma_check_on:
                    work_request = str(input("What is the work request?: "))
                    comma_check = self.llapi.comma_checker(work_request)
                    if comma_check:
                        print("Please don't have commas in the work request, only use periods, commas mess with our database.")
                    else:
                        work_request_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "l":
                print("")
                available_locations = self.llapi.list_of_location_names_wr()
                location_checker_on = True
                while location_checker_on:
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = string.capwords(input("What location is the work request at?: "))
                    if string.capwords(location) not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_checker_on = False
            if counter == 0 or counter !=0 and fieldchange == "p":
                properties_comma_checkon = True
                while properties_comma_checkon:
                    if location.lower() == "all locations":
                        properties = input("Input all property id numbers the request is for")
                        comma_check = self.llapi.comma_checker(properties)
                        if comma_check:
                            print("Please don't have a comma in the description, only use periods, commas mess with our database")
                        else:
                            properties_comma_checkon = False
                    else:
                        location_split = location.split(" - ")
                        properties = input("What is the property's ID number?: ").lower()
                        propID = self.llapi.get_all_property_ID()                        
                        if properties not in propID:
                            print("Please input an existing property ID.")
                        else:
                            is_it_there = self.llapi.is_it_there(properties, location_split[0])
                            if is_it_there:
                                properties_comma_checkon = False
                            else:
                                print("Property is not in that location")
            if counter == 0 or counter !=0 and fieldchange == "d":            
                description_comma_check_on = True
                while description_comma_check_on:                  
                    description = str(input("What is the work request's description?: "))
                    comma_check = self.llapi.comma_checker(description)
                    if comma_check:
                        print("Please don't have a comma in the description, only use periods, commas mess with our database")
                    else:
                        description_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "wo":
                worker_comma_check_on = True
                while worker_comma_check_on: 
                    worker = input("Who is the worker?: ")
                    comma_check = self.llapi.comma_checker(worker)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        worker_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "pr":
                priority_comma_check_on = True
                while priority_comma_check_on:
                    priority = input("Give the request a priority number from 1 - 10 (1 being priority)?: ")
                    try:
                        prinum = int(priority)
                        if prinum > 10 or prinum < 1:
                            print("please select a number from 1 to 10")
                        else:
                            priority_comma_check_on = False
                    except:
                        print("Please only use whole numbers for priority.")
            if counter == 0 or counter !=0 and fieldchange.lower() == "r":
                repeat_check_on = True
                while repeat_check_on:
                    repeat = input("Repeat (y/n)").lower()
                    if repeat not in ["y", "n"]:
                        print('Please only use a "y" or a "n"')
                    else:
                        repeat_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "t":
                time_check_on = True
                while time_check_on:
                    time = input("When would you like to repeat (none/daily/weekly/monthly/yearly)?: ").lower()
                    if time not in ["none", "daily", "weekly", "montly", "yearly"]:
                        print("Please only select one of the apropriate options and spell them like they are spelled in the input line")
                    else:
                        time_check_on = False
                if counter == 0 or counter !=0 and fieldchange.lower() == "s":
                    start_comma_check_on = True
                    while start_comma_check_on:
                        start = input("What is the start date?: ")
                        comma_check = self.llapi.comma_checker(start)
                        if comma_check:
                            print("Please don't have a comma. It messes with our database")
                        else:
                            start_comma_check_on = False
                if counter == 0 or counter !=0 and fieldchange.lower() == "do":
                    done_comma_check_on = True
                    while done_comma_check_on:
                        done = input("What is the finished date?: ")
                        comma_check = self.llapi.comma_checker(done)
                        if comma_check:
                            print("Please don't have a comma. It messes with our database")
                        else:
                            done_comma_check_on = False
            counter +=1

    
    def create_work_report(self):
        #id,work_request_id,description,location,properties,worker,comment,regular_maintenance,expenses,start,done,approved
        counter = 0
        print("")
        create_work_report_loop = True
        fieldchange = ""
        while create_work_report_loop:
            print(counter)
            if counter != 0:
                print("Is this the correct information?")
                print(f"ID:                        {id}")
                print(f"Work request ID:           {work_request_id}")
                print(f"Description:               {description}")
                print(f"Location:                  {location}")
                print(f"Properties:                {properties}")
                print(f"Worker:                    {worker}")
                print(f"Comment:                   {comment}")
                print(f"Regular maintenance (y/n): {regular_maintenance}")
                print(f"Expenses:                  {expenses}")
                print(f"Start:                     {start}")
                print(f"Done:                      {done}")
                print(f"Approved:                  {approved}")

                rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
                if rightorwrong.lower() == "y":
                    create_work_report_loop = False
                    self.llapi.create_work_report(id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done, approved)
                    return True
                elif rightorwrong.lower() == "c":
                    create_work_report_loop = False
                    fieldchange = ""
                    return True
                elif rightorwrong.lower() == "n":
                    print("Select a field to change: [w]ork request ID, [d]escription, [l]ocation, [p]roperties, [wo]rker, [c]omment, [r]egular maintenance, [e]xpenses, [s]tart, [do]ne, [a]pproved.")
                    fieldchange = input("Input the letter of the field you wish to change: ")
            if counter == 0 or counter !=0 and fieldchange.lower() == "w":
                work_request_id_comma_check_on = True
                while work_request_id_comma_check_on:
                    work_request_id = string.capwords(input("What is the work request ID?: "))
                    comma_check = self.llapi.comma_checker(work_request_id)
                    if comma_check:
                        print("Please don't have commas in the work request ID, commas mess with our database.")
                    else:
                        work_request_id_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "d":            
                description_comma_check_on = True
                while description_comma_check_on:                  
                    description = string.capwords(input("What is the work report´s description?: "))
                    comma_check = self.llapi.comma_checker(description)
                    if comma_check:
                        print("Please don't have a comma in the description, only use periods, commas mess with our database")
                    else:
                        description_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "l":
                print("")
                available_locations = self.llapi.list_of_location_names()
                location_checker_on = True
                while location_checker_on:
                    print("Available locations are as follows:")
                    self.llapi.list_printer(available_locations)
                    location = string.capwords(input("What location was the work request at?: "))
                    if string.capwords(location) not in available_locations:
                        print("Not a valid location, please either create a new location or select an available one")
                    else:
                        location_checker_on = False
            if counter == 0 or counter !=0 and fieldchange == "p":
                properties_comma_checkon = True
                while properties_comma_checkon:
                    properties = input("What is the property´s ID number?: ")
                    comma_check = self.llapi.comma_checker(properties)
                    if comma_check:
                        print("Please don't use commas in the property ID. Commas mess with our database.")
                    else:
                        properties_comma_checkon = False
            if counter == 0 or counter !=0 and fieldchange == "wo":
                worker_comma_check_on = True
                while worker_comma_check_on: 
                    worker = input("Who is the worker?: ")
                    comma_check = self.llapi.comma_checker(worker)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        worker_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "c":
                comment_comma_check_on = True
                while comment_comma_check_on: 
                    comment = input("Comment?: ")
                    comma_check = self.llapi.comma_checker(comment)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        comment_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "r":
                regular_maintenance_comma_check_on = True
                while regular_maintenance_comma_check_on:
                    regular_maintenance = input("Was it a regular maintenance (y/n)?: ")
                    comma_check = self.llapi.comma_checker(regular_maintenance)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        regular_maintenance_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "e":
                expenses_comma_check_on = True
                while expenses_comma_check_on:
                    expenses = input("What were the overall expenses?: ")
                    comma_check = self.llapi.comma_checker(expenses)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        expenses_comma_check_on = False
                if counter == 0 or counter !=0 and fieldchange.lower() == "s":
                    start_comma_check_on = True
                while start_comma_check_on:
                    start = input("What is the start date?: ")
                    comma_check = self.llapi.comma_checker(start)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        start_comma_check_on = False
                if counter == 0 or counter !=0 and fieldchange.lower() == "do":
                    done_comma_check_on = True
                while done_comma_check_on:
                    done = input("What is the finished date?: ")
                    comma_check = self.llapi.comma_checker(done)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        done_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange.lower() == "a":
                approved_comma_check_on = True
                while approved_comma_check_on:
                    approved = input("When was it approved?: ")
                    comma_check = self.llapi.comma_checker(approved)
                    if comma_check:
                        print("Please don't have a comma. It messes with our database")
                    else:
                        approved_comma_check_on = False
            counter +=1

    def mark_work_report_as_done():
        pass

    def accept_finished_work_reports():
        pass
    
    def View_work_requests(self):
        work_request_list = self.llapi.get_work_request_list()
        self.llapi.list_printer(work_request_list)
   
    def View_work_reports(self):
        work_report_list = self.llapi.get_work_report_list()
        self.llapi.list_printer(work_report_list)



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
            return True
        elif selection.lower() == "q":
            return False
        else:
            print("Wrong input!")
            return self.work_report_staff_menu()