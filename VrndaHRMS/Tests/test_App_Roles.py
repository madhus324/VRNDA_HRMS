import time

import pytest

from PageObjects.App_Roles import AppRoles
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
from Utilities.ExcelUtils import get_data_from_excel

@pytest.mark.run(order=2)
class Test_AppRoles(BaseTest):
    Role = "QA"
    Description = "Software Testing"
    Edited_description = "Software Test Engineer"
    role_list1 = []
    role_list2 = []


    def test_Tovalidate_Approles_Title(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        approles = AppRoles(self.driver)
        approles.navigate_app_roles()
        approles.custom_sleep(1)
        Exp_title = "Application Roles"
        if approles.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_Add_NewAppRoles(self):
        approles = AppRoles(self.driver)
        approles.custom_sleep(2)
        Test_AppRoles.role_list1 = approles.Rolename_list()
        print(Test_AppRoles.role_list1)

    def test_Tovalidate_Add_NewAppRole_Title(self):
        approles = AppRoles(self.driver)
        approles.scroll_up()
        approles.click_add()
        approles.custom_sleep(2)
        Exp_title = "Add New Application Role"
        if approles.AddNewAppRole_Title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_AddNewAppRole_Records_Validation(self):
        approles = AppRoles(self.driver)
        approles.custom_sleep(2)
        approles.enter_name(self.Role)
        approles.enter_description(self.Description)
        approles.click_save()
        approles.custom_sleep(2)
        Exp_Message = "Success! Application Role saved successfully."
        if approles.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)

    def test_Tovalidate_New_AppRole_Added_Scuuessfully(self):
        approles = AppRoles(self.driver)
        Test_AppRoles.role_list2 = approles.Rolename_list()
        print("Role List After Adding:", Test_AppRoles.role_list2)
        if Test_AppRoles.role_list1 is not None and Test_AppRoles.role_list2 is not None:
            difference = list(set(Test_AppRoles.role_list2) - set(Test_AppRoles.role_list1))
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
        # time.sleep(2)

    def test_Tovalidate_Delete_Config_warn(self):
        approles = AppRoles(self.driver)
        approles.Delete_Config_record(self.Description)
        Exp_Message = "Warning! Configuration records cannot be deleted."
        if approles.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Warning validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False

    def test_Tovalidate_AppRole_Update_validation(self):
        approles = AppRoles(self.driver)
        approles.Edit_record()
        approles.enter_description(self.Edited_description)
        approles.Change_Config()
        approles.click_save()
        approles.Remove_Config()
        Exp_Message = "Success! Application Role updated successfully"
        approles.custom_sleep(2)
        if approles.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Warning validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False


    def test_Tovalidate_Duplicate_Approle_validation(self):
        approles = AppRoles(self.driver)
        approles.click_add()
        approles.custom_sleep(2)
        approles.enter_name(self.Role)
        approles.enter_description(self.Edited_description)
        approles.click_save()
        approles.custom_sleep(2)
        Exp_Message = "Failed! An Application role already exists with same Application Role Name."
        if approles.validate_toastmessage().text == (Exp_Message):
            approles.close_AddnewAppRole()
            assert True
            print("Passed : Duplicate Records validation message is displayed and verified successfully")
        else:
            approles.close_AddnewAppRole()()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False


    def test_Tovalidate_AppRole_Delete_Validation(self):
        approles = AppRoles(self.driver)
        approles.Delete_Application_Role(self.Edited_description)
        approles.custom_sleep(2)
        # approles.click_save()
        Exp_Message = "Success! Application Role deleted successfully."
        if approles.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Duplicate Records validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
    # def test_access(self):
    #     approles = AppRoles(self.driver)
    #     approles.access_privileges
    #     time.sleep(5)







