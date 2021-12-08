import Ui_layer.MainMenuMANUI
import Ui_layer.MainMenuEMPUI
class WorkReportMenu:
    def __init__(self, name, email, location, title):
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def Work_report_manager_menu(self):
        print("1. Create work request")
        print("2. Create maintenance report")
        print("3. Change maintenance report")
        print("4. Mark meaitenance or work report as ready for closing")
        print("5. Accept finished maintenance and work reports")
        print("6. View work and maintenance reports")
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
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "b":
            current_user = Ui_layer.MainMenuMANUI.ManagerUI(self.name, self.email, self.location, self.title)
            current_user.managers_menu()
        elif selection == "q":
            pass
        else:
            print("Wrong input!")
            self.Work_report_manager_menu()

            
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
            current_user = Ui_layer.MainMenuEMPUI.EmployeeUI(self.name, self.email, self.location, self.title)
            current_user.staff_menu()
        elif selection.lower() == "q":
            pass
        else:
            print("Wrong input!")
            self.work_report_staff_menu()