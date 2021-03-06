import string
from Logic_layer.LLAPI import LLAPI
from Models.WorkReportModel import WorkReport
from Models.WorkRequestModel import WorkRequest
import Data_layer.WorkRequestDL
import Data_layer.WorkReportDL
from datetime import date

class WorkReportMenu:
    def __init__(self, idnumber = "", name = "", email = "", location = "", title = "", logic_api:LLAPI = LLAPI()):
        self.idnumber = idnumber
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.llapi = logic_api
        self.llapi = logic_api
        self.report_location = self.llapi.get_your_location_for_wr(location)

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
            print("Sadly this bugged out on us right before the project was due")
            return self.Work_report_manager_menu()
        elif selection == "3":
            return self.edit_work_request()
        elif selection == "4":
            return self.finalize_work_request()
        elif selection == "5":
            return self.finalize_work_report()
        elif selection == "6":
            return self.view_work_requests()
        elif selection == "7":
            return self.view_work_reports()
        elif selection == "b":
            return True
        elif selection == "q":
            return False
        else:
            print("Wrong input!")
            return self.Work_report_manager_menu()

#id,work_request_id,description,location,properties,worker,comment,regular_maintenance,expenses,start,done
    def finalize_work_report(self):
        print("What work report would you like to approve?")
        work_request_ID = input("What is the ID number of the work report you want to finalize? input [c] to cancel: ")
        if work_request_ID.lower() == "c":
            return True
        work_report_info = self.llapi.dict_search(WorkReport, attribute="id", value=work_request_ID)
        results = work_report_info
        if len(results)<1:
            print("No requests found with that ID")
            return self.finalize_work_report()
        elif string.capwords(results[0]["wroplocation"]) not in [self.report_location[0], "All Locations"]:
            print("You do not have access to this work request")
            return self.finalize_work_report()
        else:
            id = results[0]["wropid"]
            work_request_id = results[0]["wropwork_request_id"]
            description = results[0]["wropdescription"]
            location = results[0]["wroplocation"]
            properties = results[0]["wropproperties"]
            worker = results[0]["wropworker"]
            comment = results[0]["wropcomment"]
            regular_maintenance = results[0]["wropregular_maintenance"]
            expenses = results[0]["wropexpenses"]
            start = results[0]["wropstart"]
            done = results[0]["wropdone"]
            editor = True
            while editor:
                print("")
                print("Please confirm the following details.")
                print("")
                print(f"ID number:           {id}")
                print(f"Work request_id:     {work_request_id}")
                print(f"description:         {description}")
                print(f"location:            {location}")
                print(f"properties:          {properties}")
                print(f"Worker:              {worker}")
                print(f"comment:             {comment}")
                print(f"regular_maintenance: {regular_maintenance}")
                print(f"expenses:            {expenses}")
                print(f"Start:               {start}")
                print(f"Done:                {done}")
                print("")
                approve = string.capwords(input("Do you confirm the details above and wish to approve this work report?(y/n): "))
                if approve == "Y":
                    editor = False
                    results_final = {}
                    results_final["wropid"] = id
                    results_final["wropwork_request_id"] = work_request_id
                    results_final["wropdescription"] = description
                    results_final["wroplocation"] = location
                    results_final["wropproperties"] = properties
                    results_final["wreqworker"] = worker
                    results_final["wropcomment"] = comment
                    results_final["wropregular_maintenance"] = regular_maintenance
                    results_final["wropexpenses"] = expenses
                    results_final["wropstart"] = start
                    results_final["wropdone"] = "done"
                    #Skrifa ?? skr??
                    init = Data_layer.WorkReportDL.WorkReportDL()
                    init.finalize_work_report(results_final)
                    return True
                elif approve == "N":
                    editor = False
                    return True
                else:
                    print("Wrong input")
                    editor = True
     
 
#id,work_request,location,properties,description,worker,priority,repeat,time,start,done
    def finalize_work_request(self):
        work_request_ID = input("What is the ID number of the work request you would like to finalize? input [c] to cancel: ")
        if work_request_ID.lower() == "c":
            return True
        work_request_id = (input("Enter work request ID number: "))
        work_request_info = self.llapi.dict_search(WorkRequest, attribute="id", value=work_request_id)
        results = work_request_info
        if len(results)<1:
            print("No requests found with that ID")
            return self.finalize_work_request()
        elif string.capwords(results[0]["wroplocation"]) not in [self.report_location[0], "All Locations"]:
            print("You do not have access to this work request")
            return self.finalize_work_report()
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
                    results_final["wreqdone"] = "done"
                     #Skrifa ?? skr??
                    print(results_final)
                    init = Data_layer.WorkRequestDL.WorkRequestDL()
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
        work_request_ID = input("What is the work requests ID number? input [c] to cancel: ")
        if work_request_ID.lower() == "c":
            return True
        Work_requestinfo = self.llapi.dict_search(WorkRequest,  attribute="id", value=work_request_ID)
        results = Work_requestinfo
        if len(results) < 1:
            print("No requests found with that ID")
            return self.edit_work_request() 
        elif results[0]["wreqlocation"] not in self.report_location:
            print("You do not have access to edit this work request")
            print(results[0]["wreqlocation"], self.report_location)
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
                if fieldchange.lower() == "l":
                    all_or_your = input("do you want this to apply multiple locations y/n?: ")
                    if all_or_your.lower() == "y":
                        location = "All Locations"
                    else:
                        location = self.report_location[0]
                if fieldchange.lower() == "p":
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
                            properties = input("What is the property's ID number?: ").lower()
                            propID = self.llapi.get_all_property_ID()                        
                            if properties not in propID:
                                print("Please input an existing property ID.")
                            else:
                                is_it_there = self.llapi.is_it_there(properties, self.location)
                                if is_it_there:
                                    properties_comma_checkon = False
                                else:
                                    print("Property is not in that location")
                elif fieldchange.lower() == "wo":
                    worker_comma_check_on = True
                    while worker_comma_check_on: 
                        worker = string.capwords(input("Who is the worker?: "))
                        exists = self.llapi.list_all_employees_names()
                        print(exists)
                        if worker not in exists:
                            print("please make sure the worker exists")
                        elif location.lower() == "all locations":
                            worker_comma_check_on = False
                        else:
                            does_he_work_there = self.llapi.does_he_work_there(worker, self.location)
                            print(does_he_work_there)
                            if does_he_work_there:
                                worker_comma_check_on = False
                            else:
                                print("Employee does not work there")
                elif fieldchange.lower() == "pr":
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
                elif fieldchange.lower() == "r":
                        repeat_check_on = True
                        while repeat_check_on:
                            repeat = input("Repeat (y/n)").lower()
                            if repeat not in ["y", "n"]:
                                print('Please only use a "y" or a "n"')
                            else:
                                repeat_check_on = False
                elif fieldchange.lower() == "t":
                        time_check_on = True
                        while time_check_on:
                            time = input("When would you like to repeat (none/daily/weekly/monthly/yearly)?: ").lower()
                            if time not in ["none", "daily", "weekly", "montly", "yearly"]:
                                print("Please only select one of the apropriate options and spell them like they are spelled in the input line")
                            else:
                                time_check_on = False
                elif fieldchange in ["w", "d", "t", "s", "do"]:
                    comma_check_on = True
                    while comma_check_on:
                        changed_into = input("What would you like it changed to?: ")
                        comma_check = self.llapi.comma_checker(changed_into)
                        if comma_check:
                            print("Please don't have a comma in the input it will mess with our database.")
                        else:
                            comma_check_on = False
                    if fieldchange.lower() == "w":
                        work_request = changed_into 
                    elif fieldchange.lower() == "d":
                        description = changed_into
                    elif fieldchange.lower() == "s":
                        start = changed_into
                    elif fieldchange.lower() == "do":
                        done = changed_into
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
                        #Skrifa ?? skr??
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
                all_or_your = input("do you want this to apply multiple locations y/n?: ")
                if all_or_your.lower() == "y":
                    location = "All Locations"
                else:
                    location = self.report_location[0]
            if counter == 0 or counter !=0 and fieldchange == "p":
                properties_comma_checkon = True
                while properties_comma_checkon:
                    if location.lower() == "all locations":
                        properties = input("Input all property id numbers the request is for: ")
                        comma_check = self.llapi.comma_checker(properties)
                        if comma_check:
                            print("Please don't have a comma in the description, only use periods, commas mess with our database")
                        else:
                            properties_comma_checkon = False
                    else:
                        properties = input("What is the property's ID number?: ").lower()
                        propID = self.llapi.get_all_property_ID()                        
                        if properties not in propID:
                            print("Please input an existing property ID.")
                        else:
                            is_it_there = self.llapi.is_it_there(properties, self.location)
                            if is_it_there:
                                properties_comma_checkon = False
                            else:
                                print("Property is not in your location")
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
                if location == "All Locations":
                    worker = "Any available"
                else:
                    worker_comma_check_on = True
                    while worker_comma_check_on: 
                        worker = string.capwords(input("Who is the worker?: "))
                        exists = self.llapi.list_all_employees_names()
                        if worker not in exists:
                            print("please make sure the worker exists")
                        elif location.lower() == "all locations":
                            worker_comma_check_on = False
                        else:
                            does_he_work_there = self.llapi.does_he_work_there(worker, self.location)
                            if does_he_work_there:
                                worker_comma_check_on = False
                            else:
                                print("Employee does not work there")
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
                    repeat = input("Repeat (y/n)?: ").lower()
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
        #id,work_request_id,description,location,properties,worker,comment,regular_maintenance,expenses,start,done
        #h??tti a?? virka r??tt fyrir skil. 
        counter = 0
        print("")
        create_work_report_loop = True
        fieldchange = ""
        while create_work_report_loop:
            if counter != 0:
                print("Is this the correct information?")
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


                rightorwrong = input("Is this information correct [y]es, [n]o, [c]ancel: ")
                if rightorwrong.lower() == "y":
                    create_work_report_loop = False
                    self.llapi.create_work_report(work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done)
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
                    description = string.capwords(input("What is the work report's description?: "))
                    comma_check = self.llapi.comma_checker(description)
                    if comma_check:
                        print("Please don't have a comma in the description, only use periods, commas mess with our database")
                    else:
                        description_comma_check_on = False
            if counter == 0 or counter !=0 and fieldchange == "l":
                all_or_your = input("do you want this to apply multiple locations y/n?: ")
                if all_or_your.lower() == "y":
                    location = "All Locations"
                else:
                    location = self.report_location[0]
            if counter == 0 or counter !=0 and fieldchange == "p":
                properties_comma_checkon = True
                while properties_comma_checkon:
                    properties = input("What is the property's ID number?: ")
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


        #work_request_ID = input("What is the work request??s ID number you would like to mark as done?: ")
       # Work_requestinfo = self.llapi.dict_search(WorkRequest,  attribute="id", value=work_request_ID)
        #results = Work_requestinfo
       # WorkRequest.mark_as_done(results)
    """
        def mark_work_request_as_done(self):
            print("Mark work request as done")
            work_request_ID = input("What is the work request's ID number?: ")
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

                #Set done to today's date
                done = date.today()

                editmore = input("Would you like to mark this work request as done on today's date (y/n)?:  ")
                if editmore == "y":
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
                    #Write to a file
                    init = Data_layer.WorkRequestDL.WorkRequestDL()
                    init.change_information_work_request(results_final)
                    #self.managers_menu()
                elif editmore == "n":
                    return True
                else:
                    pass
    """
    
    def view_work_requests(self):
        print("Closed work requests:")
        print("")
        closed_work_request_list = self.llapi.get_closed_work_request_list()
        self.llapi.list_printer(closed_work_request_list)
        print("Open work requests:")
        print("")
        open_work_requests_list = self.llapi.get_open_work_request_list()
        self.llapi.list_printer(open_work_requests_list)
        return True

   
    def view_work_reports(self):
        print("Approved work reports:")
        print("")
        closed_work_report_list = self.llapi.get_closed_work_report_list()
        self.llapi.list_printer(closed_work_report_list)
        print("Open work reports:")
        print("")
        open_work_report_list = self.llapi.get_open_work_report_list()
        self.llapi.list_printer(open_work_report_list)
        return True

    def work_report_staff_menu(self):
        print("1. Create work request")
        print("2. Change work request")
        print("3. Browse work reports")
        print("b. Back to main menu")
        print("q. Quit")
        selection = input("Input selection: ")
        if selection == "1":
            return self.create_work_request()
        elif selection == "2":
            return self.edit_work_request()
        elif selection == "3":
            return self.view_work_reports()
        elif selection.lower() == "b":
            return True
        elif selection.lower() == "q":
            return False
        else:
            print("Wrong input!")
            return self.work_report_staff_menu()
    