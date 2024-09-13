import time

import pytest
import unittest

from selenium.common import TimeoutException
from webdriver_manager.core import driver
from PageObjects.LeaveConfig import LeaveConfig
from PageObjects.LeaveTypes import LeaveTypes
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
from PageObjects.BasePage import BasePage
from Utilities.ExcelUtils import get_data_from_excel


@pytest.mark.run(order=4)
class Test_LeaveConfig(BaseTest):
    c_name = "LC02"
    c_description = "Leave Config 02"
    no_of_leaves = "4"
    noofwarns = "2"

    def test_Tovalidate_leaveconfigurationsTitle(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        time.sleep(2)
        Leave_config = LeaveConfig(self.driver)
        Leave_config.navigate_leave_config()
        time.sleep(2)
        Leave_config.title()
        Exp_title = "Leave Configurations"
        if Leave_config.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_AddNewLeaveConfigurationtitle(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.click_add()
        # time.sleep(2)
        Leave_config.parentpopupscreentitle()
        Exp_title = "Add New Leave Configuration"
        if Leave_config.parentpopupscreentitle() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_AddNewLeaveConfiguration(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.enterconfig_name(self.c_name)
        Leave_config.enterconfig_desc(self.c_description)
        Leave_config.click_save()
        Exp_Message = "Success! Record Saved Successfully."
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)

    def test_Tovalidate_Duplicate_LeaveConfiguration_warn(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.click_add()
        Leave_config.enterconfig_name(self.c_name)
        Leave_config.click_save()
        Exp_Message = "Warning! Configuration already exists with same name for selected year."
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            assert True
            Leave_config.close_AddnewLeaveConfig_window()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            Leave_config.close_AddnewLeaveConfig_window()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)

    def test_Tovalidate_ConfigwithChild_warn(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.delete_Config_Child()
        time.sleep(1)
        Exp_Message = "FAILED! Unable to delete Configuration, child record may exist"
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False



    def test_Tovalidate_deleteconfigurationparentrecord(self):
        Leave_config = LeaveConfig(self.driver)
        value_text = Leave_config.valueofrecord()
        print(value_text)
        Leave_config.search_parentrecord(value_text)
        Leave_config.delete_parent_record()
        Exp_Message = "Warning! Default Configuration records cannot be deleted."
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            assert True
            Leave_config.clear_search()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            Leave_config.clear_search()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)


    def test_Tovalidate_AddNewLeaveConfigurationDetailsTitle(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.search_parentrecord(self.c_name)
        Leave_config.click_add_Child()
        time.sleep(2)
        Leave_config.childpopupscreentitle()
        Exp_title = "Add New Leave Configuration Details"
        if Leave_config.childpopupscreentitle() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_add_AddNewLeaveConfigurationDetails(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.select_leavetype()
        # time.sleep(2)
        Leave_config.select_recurrance()
        # time.sleep(2)
        Leave_config.enter_leaves(self.no_of_leaves)
        time.sleep(2)
        Leave_config.lateleavecondition()
        lateleavecondition = Leave_config.lateleaveconditionvalue()
        print(lateleavecondition)
        expected_value = "Allowed"
        try:
            if lateleavecondition == expected_value:
                Leave_config.enter_lateleaveswarnings(self.noofwarns)
                print("Value matched. Clicked on the element.")
                time.sleep(3)
                Leave_config.save()
                Exp_Message = "Success! Record saved successfully."
                if Leave_config.validate_toastmessage().text == (Exp_Message):
                    assert True
                    # Leave_config.clear_search()
                    print("Passed : Records saved validation message is displayed and verified successfully")
                else:
                    # Leave_config.clear_search()
                    print(
                        "Failed : Expected message doesnot matches Actual message of the page and verified successfully")
                    assert False
                time.sleep(2)
                return lateleavecondition
            else:
                print("Value didn't match. Skipping the next step.")
                Leave_config.save()
                Exp_Message = "Success! Record saved successfully."
                if Leave_config.validate_toastmessage().text == (Exp_Message):
                    assert True
                    # Leave_config.clear_search()
                    print("Passed : Records saved validation message is displayed and verified successfully")
                else:
                    # Leave_config.clear_search()
                    print(
                        "Failed : Expected message doesnot matches Actual message of the page and verified successfully")
                    assert False


                return None  # or raise an exception, depending on your requirement

        except TimeoutException:
            print("Timeout occurred while waiting for the element to be clickable.")
            return None  # or raise an exception, depending on your requirement


    def test_Tovalidate_addnewleaveconfigtwo(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.add_another_LeaveconfigDetails(self.no_of_leaves)

    def test_Tovalidate_Duplicate_LeaveType_Config_Warn(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.click_add_Child()
        Leave_config.select_leavetype()
        time.sleep(1)
        Exp_Message = "Error ! Another record already exists with the selected Leave Type."
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            Leave_config.close_AddnewLeaveConfig_window()
            assert True
            print("Passed : Records delete validation message is displayed and verified successfully")
        else:
            Leave_config.close_AddnewLeaveConfig_window()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)


    def test_Tovalidate_delete_leaveconfigdetails_record(self):
        time.sleep(3)
        Leave_config = LeaveConfig(self.driver)
        Leave_config.delete_all_leaveconfigdetails()
        time.sleep(1)
        Exp_Message = "Success! Leave Config details deleted successfully."
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            assert True
            print("Passed : Records delete validation message is displayed and verified successfully")
        else:
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)

    def test_Tovalidate_delete_Leaveconfig_nochild(self):
        Leave_config = LeaveConfig(self.driver)
        Leave_config.delete_Leaveconfig()
        time.sleep(1)
        Exp_Message = "Success! Configuration deleted successfully"
        if Leave_config.validate_toastmessage().text == (Exp_Message):
            Leave_config.logout()
            assert True
            print("Passed : Records delete validation message is displayed and verified successfully")
        else:
            Leave_config.logout()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        time.sleep(2)






