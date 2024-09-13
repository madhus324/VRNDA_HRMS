import pytest
import unittest

from PageObjects.LeavePlans import LeavePlan
from PageObjects.LeaveTypes import LeaveTypes
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
from Utilities.ExcelUtils import get_data_from_excel, read_LeaveConfig_data


@pytest.mark.run(order=5)
class Test_Leaveplan(BaseTest):
    cname = "LPC01"
    cdesc = "LeavePlan Configuration Test 01"
    # max_leaves = "3"
    # Apply_before_days = "2"
    leaveconfig_data = read_LeaveConfig_data("Excelfiles/LeaveConfig.xlsx", "Sheet1")


    def test_Tovalidate_Leaveplan_Title(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leaveplan = LeavePlan(self.driver)
        leaveplan.navigate_leaveplan()
        loginpage.custom_sleep(1)
        Exp_title = "Leave Plans"
        if leaveplan.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_DefaultConfig_delete_warn(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.delete_defaultconfig_record()
        Exp_Message = "Warning! Default Configuration records cannot be deleted."
        leaveplan.custom_sleep(1)
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)

    def test_Tovalidate_DeleteConfigwithChild_warning(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.delete_Config_Child()
        leaveplan.custom_sleep(1)
        Exp_Message = "FAILED! Unable to delete Configuration, child record may exist"
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Expected warning message matches with Actual Warning message and verified successfully")
        else:
            print("Failed : Expected message does not matches Actual message of the page and verified successfully")
            assert False


    def test_Tovalidte_AddNewLeavePlanConfig_Title(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.click_add()
        leaveplan.custom_sleep(1)
        Exp_title = "Add New Leave Plan Configuration"
        if leaveplan.validate_AddNewLeavePlanConfigtitle() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)


    def test_Tovalidate_AddNewLeavePlanConfig_records_saved(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.add_newplan_config(self.cname, self.cdesc)
        leaveplan.common_save()
        Exp_Message = "Success! Record Saved Successfully."
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)

    def test_ToValidate_Duplicate_config_warn(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.click_add()
        leaveplan.add_newplan_config(self.cname, self.cdesc)
        leaveplan.common_save()
        leaveplan.custom_sleep(1)
        Exp_Message = "Warning! Configuration already exists with same name for selected year."
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            leaveplan.close_AddNewLeavePlanConfig()
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leaveplan.close_AddNewLeavePlanConfig()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)


    def test_Tovalidate_AddNewLeavePlanConfigDetails_Title(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.common_parentsearch(self.cname)
        leaveplan.Click_Add_LeavePlanConfigurationDetails()
        leaveplan.custom_sleep(2)
        Exp_title = "Add New Leave Plan Configuration Details"
        if leaveplan.validate_AddNewLeavePlanConfigDetailstitle() == (Exp_title):
            assert True
            leaveplan.close_AddNewLeavePlanConfigDetails()
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            leaveplan.close_AddNewLeavePlanConfigDetails()
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False


    def test_Tovalidate_AddNewLeavePlanConfigDetails_recordsSaved(self):
        leaveplan = LeavePlan(self.driver)
        for data in self.leaveconfig_data:
            max_leaves = data["max_leaves"]
            apply_before_days = data["apply_before_days"]
            leaveplan.Click_Add_LeavePlanConfigurationDetails()
            leaveplan.Insert_Max_leave_Days(max_leaves)
            leaveplan.Insert_Apply_Before_Days(apply_before_days)
            # leaveplan.custom_sleep(1)
            leaveplan.common_save()
            leaveplan.custom_sleep(2)
            Exp_Message = "Success! Leave plan configuration details saved successfully."
            if leaveplan.validate_toastmessage().text == (Exp_Message):
                assert True
                print("Passed : Records saved validation message is displayed and verified successfully")
            else:
                print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
                assert False
            leaveplan.custom_sleep(2)


    # def test_Delete_LeavePlanConfigDetails_validation(self):
    #     leaveplan = LeavePlan(self.driver)
    #     leaveplan.delete_LeavePlanConfigDetails()
    #     Exp_Message = "Success! Leave plan configuration details deleted successfully."
    #     if leaveplan.validate_toastmessage().text == (Exp_Message):
    #         assert True
    #         print("Passed : Records saved validation message is displayed and verified successfully")
    #     else:
    #         print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
    #         assert False
    #     leaveplan.custom_sleep(2)

    def test_Deleteall_LeavePlanConfigDetails_warn(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.delete_all_leaveplanconfigdetails()
        Exp_Message = "Success! Leave plan configuration details deleted successfully."
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)


    def test_Delete_Leaveplanconfig_warn(self):
        leaveplan = LeavePlan(self.driver)
        leaveplan.delete_LeaveplanConfig()
        leaveplan.custom_sleep(1)
        Exp_Message = "Success! Configuration deleted successfully"
        if leaveplan.validate_toastmessage().text == (Exp_Message):
            assert True
            leaveplan.logout()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leaveplan.logout()
            print("Failed : Expected message does not matches Actual message of the page and verified successfully")
            assert False
        leaveplan.custom_sleep(2)





