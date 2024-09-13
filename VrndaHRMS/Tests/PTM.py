import pdb
import time
from datetime import datetime
from PageObjects.Login import Loginpage
from PageObjects.Projects import Projects
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel


class Test_Projects(BaseTest):

    Projectname = "Python Automation"
    Clientname = "Vrnda"
    Organization = "Vrnda Software Tech"
    TeamName = "Team_Vrnda"
    today_date = datetime.now().strftime("%d-%m-%Y")
    print(today_date)
    listofEmp1 = []
    listofEmp2 = []
    Emp = "28"

    def test_Tovalidate_Project_ScreenTitle(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        projects = Projects(self.driver)
        projects.navigate_projects()
        time.sleep(5)
        Exp_title = "Projects"
        if projects.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False


    def test_Tovalidate_ProjectTeamMembers_Title(self):
        projects = Projects(self.driver)
        projects.common_parentsearch(self.Projectname)
        projects.custom_sleep(2)
        projects.AddNewProjectTeams()
        projects.custom_sleep(2)
        Exp_title = "Project Team Members"
        if projects.ProjectTeamMembers_Title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_Delete_ScrumMaster_Warn(self):
        projects = Projects(self.driver)
        projects.custom_sleep(2)
        projects.Delete_ScrumMaster()
        expected_warn = "Warning! Unable to delete Active Scrum Master"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Records delete warning validation displayed successfully")
        else:
            assert False
            print("Failed : Records delete validation is not displayed")


    def test_Tovalidate_AddNewProjectMembers_Title(self):
        projects = Projects(self.driver)
        projects.click_Add_PTM()
        projects.custom_sleep(2)
        Exp_title = "Add New Project Members"
        if projects.AddNewProjectTeamMembers_Title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_EmployeeSearch_Title(self):
        projects = Projects(self.driver)
        projects.click_Emp_Search()
        projects.custom_sleep(2)
        Exp_title = "Employee Search"
        if projects.EmployeeSearch_Title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Add_ProjectTeamMembers(self):
        projects = Projects(self.driver)
        projects.Click_Retrieve()
        projects.Search_Emp(self.Emp)
        projects.Emp_Row_Select()
        projects.Click_Select()
        # pdb.set_trace()  # Execution will pause here and start the interactive debugger
        projects.custom_sleep(2)
        projects.select_RoleName()
        projects.Save_AddNewProjectMembers()
        expected_warn = "Success! Record Saved Successfully"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            projects.Close_ProjectTeamMembers()
            print("Passed : Records delete warning validation displayed successfully")
        else:
            projects.Close_ProjectTeamMembers()
            print("Failed : Records delete validation is not displayed")
            assert False

        projects.custom_sleep(3)



