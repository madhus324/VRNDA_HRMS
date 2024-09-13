import time

import pytest
import unittest

from PageObjects.LeaveTypes import LeaveTypes
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel

@pytest.mark.run(order=3)
class Test_Leavetype(BaseTest):

    new_lt_code = "TL02"
    lt_description = "Test Leave 02"
    max_leaves_allowed = "18"
    lt_list1 = []
    lt_list2 = []

    def test_Tovalidate_LeaveTypes_Title(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        loginpage.custom_sleep(2)
        leavetype = LeaveTypes(self.driver)
        leavetype.navigate_leave_config_menu()
        leavetype.navigate_leavetype()
        loginpage.custom_sleep(1)
        Exp_title = "Leave Types"
        if leavetype.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_Delete_Config_records_warn(self):
        leavetype = LeaveTypes(self.driver)
        value_text = leavetype.valueofrecord()
        print(value_text)
        leavetype.search_parentrecord(value_text)
        # time.sleep(3)
        leavetype.delete_config_lt_record()
        # time.sleep(3)
        Exp_Message = "Warning! Configuration records cannot be deleted."
        if leavetype.validate_toastmessage().text == (Exp_Message):
            assert True
            leavetype.clear_search()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leavetype.clear_search()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leavetype.custom_sleep(2)

    def test_listofLeaveTypes(self):
        leavetype = LeaveTypes(self.driver)
        Test_Leavetype.lt_list1 = leavetype.Leavetype_list()
        print("Leave Types List Before Adding:", Test_Leavetype)

    def test_Tovalidate_AddNewLeaveType_popup_title(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.click_add()
        leavetype.custom_sleep(1)
        leavetype.validate_popupscreentitle()
        Exp_title = "Add New Leave Type"
        if leavetype.validate_popupscreentitle() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_AddNewLeaveType_Records(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.Enter_Leavetype_code(self.new_lt_code)
        leavetype.Enter_Leavetype_description(self.lt_description)
        leavetype.Enter_max_Leaves(self.max_leaves_allowed)
        leavetype.click_save()
        Exp_Message = "Success! Record Saved Successfully."
        if leavetype.validate_toastmessage().text == (Exp_Message):
            assert True
            leavetype.clear_search()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leavetype.clear_search()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leavetype.custom_sleep(2)

    def test_Tovalidate_listofLeaveTypes_afteradding(self):
        leavetype = LeaveTypes(self.driver)
        Test_Leavetype.lt_list2 = leavetype.Leavetype_list()
        print("Leave Types List Before Adding:", Test_Leavetype.lt_list2)

        if Test_Leavetype.lt_list1 and Test_Leavetype.lt_list2:
            difference = [item for item in Test_Leavetype.lt_list2 if item not in Test_Leavetype.lt_list1]
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
        time.sleep(5)

    def test_ToValidate_UpdateLeaveTypeTitle(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.Edit_record(self.new_lt_code)
        leavetype.custom_sleep(2)
        Exp_title = "Update Leave Type"
        if leavetype.validate_UpdateLeaveTypeTile() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_UpdateLeaveType(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.select_carrytillYearEnd()
        leavetype.select_carrytillYearEnd_value()
        leavetype.click_save()
        Exp_Message = "Success! Leave Type updated successfully."
        if leavetype.validate_toastmessage().text == (Exp_Message):
            assert True
            leavetype.clear_search()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leavetype.clear_search()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leavetype.custom_sleep(2)

    def test_Tovalidate_Duplicate_Warn(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.click_add()
        leavetype.Enter_Leavetype_code(self.new_lt_code)
        leavetype.Enter_Leavetype_description(self.lt_description)
        leavetype.Enter_max_Leaves(self.max_leaves_allowed)
        leavetype.click_save()
        Exp_Message = "Failed! A records already exists with Leave Type Code."
        if leavetype.validate_toastmessage().text == (Exp_Message):
            assert True
            leavetype.close_AddnewLeavetype_window()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leavetype.close_AddnewLeavetype_window()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leavetype.custom_sleep(2)

    def test_Tovalidate_Delete_no_config_records(self):
        leavetype = LeaveTypes(self.driver)
        leavetype.delete_record(self.new_lt_code)
        Exp_Message = "Success! Leave Type deleted successfully."
        if leavetype.validate_toastmessage().text == (Exp_Message):
            assert True
            leavetype.clear_search()
            print("Passed : Records saved validation message is displayed and verified successfully")
        else:
            leavetype.clear_search()
            print("Failed : Expected message doesnot matches Actual message of the page and verified successfully")
            assert False
        leavetype.custom_sleep(2)





#
# if __name__ == "__main__":
#     unittest.main()


