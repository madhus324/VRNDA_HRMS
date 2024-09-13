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
    Emp = "28"
    today_date = datetime.now().strftime("%d-%m-%Y")
    print(today_date)
    pn_list1 = []
    pn_list2 = []

    def test_Tovalidate_Project_ScreenTitle(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        projects = Projects(self.driver)
        projects.navigate_projects()
        time.sleep(1)
        Exp_title = "Projects"
        if projects.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False


    def test_Tovalidate_AddNewProjectsDetails_Title(self):
        projects = Projects(self.driver)
        Test_Projects.pn_list1 = projects.Project_list()
        print(Test_Projects.pn_list1)
        projects.Add_new_project()
        Exp_title = "Add New Project rDetails"
        if projects.AddnewProjectDetails_Title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False


    def test_Tovalidate_ClientName_validation(self):
        projects = Projects(self.driver)
        projects.enter_proj_name(self.Projectname)
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Enter Client Name"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Project name validation displayed successfully")
        else:
            assert False
            print("Failed : Project name validation is not displayed")

    def test_Tovalidate_Organization_validation(self):
        projects = Projects(self.driver)
        projects.enter_client_name(self.Clientname)
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Select organization"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Client name validation displayed successfully")
        else:
            assert False
            print("Failed : Client name validation is not displayed")


    def test_Tovalidate_Startdate_validation(self):
        projects = Projects(self.driver)
        projects.enter_org(self.Organization)
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Enter Start Date"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Start Date validation displayed successfully")
        else:
            assert False
            print("Failed : Start Date validation is not displayed")


    def test_Tovalidate_Project_Head_validation(self):
        projects = Projects(self.driver)
        projects.enter_startdate(self.today_date)
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Select Project Head"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Project Head validation displayed successfully")
        else:
            assert False
            print("Failed : Project Head validation is not displayed")

    def test_Tovalidate_TeamName_validation(self):
        projects = Projects(self.driver)
        projects.select_proj_head()
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Enter Team Name"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Team name validation displayed successfully")
        else:
            assert False
            print("Failed : Team Name validation is not displayed")

    def test_Tovalidate_ScrumMaster_validation(self):
        projects = Projects(self.driver)
        projects.enter_teamname(self.TeamName)
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Please Enter Scrum Master Name"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Scrum Master validation displayed successfully")
        else:
            assert False
            print("Failed : Scrum Master validation is not displayed")

    def test_ToValidate_Records_saved_validation(self):
        projects = Projects(self.driver)
        projects.select_scrummaster()
        projects.click_save()
        projects.custom_sleep(1)
        expected_warn = "Success! Record saved successfully."
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Records saved validation displayed successfully")
        else:
            assert False
            print("Failed : Records saved validation is not displayed")

    def test_Tovalidate_Project_RecordsSaved(self):
        projects = Projects(self.driver)
        Test_Projects.pn_list2 = projects.Project_list()
        print(Test_Projects.pn_list2)

        if Test_Projects.pn_list1 is not None and Test_Projects.pn_list2 is not None:
            difference = list(set(Test_Projects.pn_list2) - set(Test_Projects.pn_list1))
            print("Difference:", difference)
            if difference:
                print("A new record has been added successfully & Verified")
                assert True
            else:
                print("No new record has been added")
                assert False
        else:
            print("One or both lists are None.")
            print("No new record has been added & Verified")
            assert False

    def test_Tovalidate_ProjectTeamMembers_Title(self):
        projects = Projects(self.driver)
        # ProJdetails_value = projects.valueofrecord()
        # print(ProJdetails_value)
        projects.common_parentsearch(self.Projectname)
        projects.AddNewProjectTeams()
        projects.custom_sleep(2)
        Exp_title = "Project Team Members"
        if projects.ProjectTeamMembers_Title() == (Exp_title):
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


    def test_Tovalidate_Delete_ScrumMaster_Warn(self):
        projects = Projects(self.driver)
        projects.Delete_ScrumMaster()
        expected_warn = "Warning! Unable to delete Active Scrum Master"
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Records delete warning validation displayed successfully")
        else:
            assert False
            print("Failed : Records delete validation is not displayed")





    def test_Tovalidate_projectAssignedDelete_Warn(self):
        projects = Projects(self.driver)
        projects.delete_projdetails_record(self.Projectname)
        expected_warn = "FAILED! Project assigned to a Team cannot be deleted."
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Records delete warning validation displayed successfully")
        else:
            assert False
            print("Failed : Records delete validation is not displayed")



    def test_Tovalidate_Delete_ProjectTeams(self):
        projects = Projects(self.driver)
        projects.common_parentsearch(self.Projectname)
        projects.Delete_Project_Team()
        expected_warn = "Success! Team Members and Team deleted successfully."
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            print("Passed : Records delete warning validation displayed successfully")
        else:
            assert False
            print("Failed : Records delete validation is not displayed")

    def test_Tovalidate_DeleteProjectDetail_withNochild(self):
        projects = Projects(self.driver)
        projects.delete_projdetails_record(self.Projectname)
        projects.custom_sleep(1)
        expected_warn = "Success! Project deleted successfully."
        if projects.validate_toastmessage().text == (expected_warn):
            assert True
            projects.logout()
            print("Passed : Records delete warning validation displayed successfully")
        else:
            projects.logout()
            print("Failed : Records delete validation is not displayed")
            assert False


