import pdb
import random
import time
from datetime import datetime, timedelta

import pdp
import pytest
from deepdiff import DeepDiff

from PageObjects.LeaveApprovals import LeaveApprovals
from PageObjects.Leaves import Leaves
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel, get_credentials

@pytest.mark.run(order=7)

class Test_LeaveRequest(BaseTest):

    LeaveBalance_before = {}
    LeaveBalance_after = {}
    LeaveBalance_after_cancel = {}
    approver_list = []
    myLeaveReq_list = []
    selected_leave_value = ()

    def generate_valid_leave_dates():
        today_date = datetime.now()
        while True:
            from_date = today_date + timedelta(days=random.randint(1, 7))
            if from_date.weekday() < 5:
                break
        while True:
            to_date = from_date + timedelta(days=random.randint(2, 7))
            if to_date.weekday() < 5:
                break
        num_days = (to_date - from_date).days + 1
        return from_date, to_date, num_days

    from_date, to_date, num_days = generate_valid_leave_dates()

    print("Valid From Date (excluding weekends):", from_date.strftime("%d/%m/%Y"))
    print("Valid To Date (excluding weekends, at least 2 days later):", to_date.strftime("%d/%m/%Y"))
    print("Number of days between From Date and To Date:", num_days)


    def generate_random_weekday():
        today_date = datetime.now()
        while True:
            random_offset = random.randint(1, 7)  # Random offset from today in days
            random_date = today_date + timedelta(days=random_offset)
            if random_date.weekday() < 5:  # Check if it's a weekday (0 to 4 for Monday to Friday)
                return random_date.strftime("%d/%m/%Y")

    random_weekday_date = generate_random_weekday()
    formatted_from_date = random_weekday_date
    formatted_to_date = random_weekday_date
    reformatted_from_date = datetime.strptime(formatted_from_date, '%d/%m/%Y').strftime('%d-%m-%Y')

    print("Random From Date (excluding weekends):", formatted_from_date)
    print("Random To Date (excluding weekends):", formatted_to_date)

    def test_LeaveBalance_Title(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        loginpage.custom_sleep(2)
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_Self_Menu()
        leave_Req.Navigate_Leaves_Menu()
        leave_Req.Navigate_LeaveBalance()
        leave_Req.custom_sleep(2)
        Exp_Title = "Leave Balance"
        if leave_Req.title() == (Exp_Title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title does not matches Actual Title of the page and verified successfully")
            assert False

    def test_Capture_LeaveBalance(self):
        leave_Req = Leaves(self.driver)
        Test_LeaveRequest.LeaveBalance_before = leave_Req.capture_leavebal()
        print(Test_LeaveRequest.LeaveBalance_before)

    def test_Tovalidate_LeaveRequest_Title(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_LeaveRequest()
        leave_Req.custom_sleep(1)
        Exp_Title = "Leave Request"
        if leave_Req.title() == (Exp_Title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title does not matches Actual Title of the page and verified successfully")
            assert False

    def test_Tovalidate_AddNewLeaveRequest_Title(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Click_Add()
        leave_Req.custom_sleep(1)
        Exp_Title = "Add New Leave Request"
        if leave_Req.AddNewLeaveReqtitle() == (Exp_Title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title does not matches Actual Title of the page and verified successfully")
            assert False


    def test_Tovalidate_FromDate_Warning(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Enter_FromDate("22-06-2024")
        leave_Req.Click_Session()
        leave_Req.custom_sleep(1)
        exp_warning = "Warning! From Date cannot be Weekend date."
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print("Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
            assert True
        else:
            print("Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_Tovalidate_ToDate_Warning(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Enter_ToDate("22-06-2024")
        leave_Req.Click_Session()
        leave_Req.custom_sleep(1)
        exp_warning = "Warning! To Date cannot be Weekend date."
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_Tovalidate_ToDate_cannotbegreaterthan_FromDateWarn(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Enter_FromDate("21-06-2024")
        leave_Req.Enter_ToDate("20-06-2024")
        leave_Req.Click_Session()
        leave_Req.custom_sleep(2)
        exp_warning = "Warning ! To date should be greater than from date"
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_Tovalidate_BackDated_Warning(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Enter_FromDate("03-06-2024")
        leave_Req.Click_Session()
        leave_Req.custom_sleep(1)
        exp_warning = "Warning! Sick Leave request cannot be back dated for more than 1 working days."
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False



    def test_Tovalidate_LeaveBalance_Warning(self):
        # pdb.set_trace()
        leave_Req = Leaves(self.driver)
        leavetype_value = leave_Req.Select_LeaveType()
        print(leavetype_value)
        Test_LeaveRequest.selected_leave_value = Test_LeaveRequest.LeaveBalance_before.get(leavetype_value, "Leave type not found")
        print(f"Value for {leavetype_value}: {self.selected_leave_value}")
        leave_Req.Enter_FromDate(self.from_date.strftime("%d/%m/%Y"))
        leave_Req.Enter_ToDate(self.to_date.strftime("%d/%m/%Y"))
        leave_Req.Click_Session()
        leave_Req.custom_sleep(2)
        exp_warning = f"Warning! Total leaves ({self.num_days}) is more than available leaves({self.selected_leave_value}) and allowed LOP leaves(0)."
        print(exp_warning)
        actual_warning = leave_Req.validate_toastmessage().text
        print(f"Actual warning message: '{actual_warning}'")
        if actual_warning == (exp_warning):
            time.sleep(2)
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            time.sleep(2)
            assert False

    def test_Apply_LeaveRequest(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Enter_FromDate(self.formatted_from_date)
        leave_Req.Enter_ToDate(self.formatted_from_date)
        leave_Req.Enter_Reason("Free Text Comment Box")
        approver_list = leave_Req.Get_ApproversDetails()
        print(approver_list)
        leave_Req.Click_Apply_LeaveReq()
        leave_Req.Click_OK()
        exp_warning = "Success! Leave request saved successfully"
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_Tovalidate_LeaveRequestinDashboard(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_DashBoard()
        leave_Req.custom_sleep(2)
        Test_LeaveRequest.myLeaveReq_list = leave_Req.Validate_MyLeaveReq()
        print(Test_LeaveRequest.myLeaveReq_list)
        if Test_LeaveRequest.myLeaveReq_list:
            print("Date list:", Test_LeaveRequest.myLeaveReq_list)
        else:
            print("Failed to retrieve Start Date list")

        if self.reformatted_from_date in Test_LeaveRequest.myLeaveReq_list[0]:
            print(f"The Applied Leave Request on date: {self.reformatted_from_date} is available in the Dashboard.")
            assert True
        else:
            print(f"The Applied Leave Request on date: {self.reformatted_from_date} is not available in the Dashboard.")
            assert False


    def test_Compare_LeaveBalance(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_Self_Menu()
        leave_Req.Navigate_LeaveBalance()
        Test_LeaveRequest.LeaveBalance_after = leave_Req.capture_leavebal()
        print(Test_LeaveRequest.LeaveBalance_after)
        diff = DeepDiff(Test_LeaveRequest.LeaveBalance_before, Test_LeaveRequest.LeaveBalance_after)
        print(diff)
        if diff:
            print("Dictionaries are different:")
            assert True, "Dictionaries differ!"
        else:

            print("Dictionaries are the same.")
            assert False


    def test_Cancel_LeaveRequest(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_LeaveRequest()
        leave_Req.common_parentsearch("Requested")
        leave_Req.Click_Edit()
        leave_Req.Click_Cancel()
        exp_warning = "Success! Leave cancelled successfully."
        if leave_Req.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_Compare_LeaveBalance_AfterCancel(self):
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_LeaveBalance()
        leave_Req.custom_sleep(1)
        Test_LeaveRequest.LeaveBalance_after_cancel = leave_Req.capture_leavebal()
        print(Test_LeaveRequest.LeaveBalance_after_cancel)
        diff = DeepDiff(Test_LeaveRequest.LeaveBalance_before, Test_LeaveRequest.LeaveBalance_after_cancel)
        print(diff)
        if diff:
            leave_Req.logout()
            print("After Cancelling the Leave, Leave Balance is not effected")
            assert False, "Dictionaries differ!"
        else:
            leave_Req.logout()
            print("After Cancelling the Leave, Leave Balance is credited back the no of Leaves applied")
            assert True

        leave_Req.custom_sleep(2)
#
# class Test_Approve_Leave_Request(BaseTest):
#     LeaveBal_1 = {}
#     LeaveBal_2 = {}
#     Approver_list = []
#
#     def test_ApplyLeaveRequest(self):
#         excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
#         login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
#         loginpage = Loginpage(self.driver)
#         loginpage.enter_username(login_username)
#         loginpage.enter_password(login_password)
#         loginpage.click_login()
#         loginpage.custom_sleep(2)
#         leave_Req = Leaves(self.driver)
#         leave_Req.Navigate_Self_Menu()
#         leave_Req.Navigate_Leaves_Menu()
#         leave_Req.Navigate_LeaveBalance()
#         Test_Approve_Leave_Request.LeaveBal_1 = leave_Req.capture_leavebal()
#         print(Test_LeaveRequest.LeaveBalance_before)
#         leave_Req.Navigate_LeaveRequest()
#         leave_Req.Click_Add()
#         leave_Req.Enter_FromDate(Test_LeaveRequest.formatted_from_date)
#         leave_Req.Enter_ToDate(Test_LeaveRequest.formatted_from_date)
#         leave_Req.Enter_Reason("Test Leave Request")
#         Test_Approve_Leave_Request.Approver_list = leave_Req.Get_ApproversDetails()
#         print(Test_Approve_Leave_Request.Approver_list)
#         leave_Req.Click_Apply_LeaveReq()
#         leave_Req.Click_OK()
#         leave_Req.custom_sleep(2)
#         leave_Req.logout()
#
#     def test_leave_approvals(self):
#         for approver_name in Test_Approve_Leave_Request.Approver_list:
#             approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
#             if approver_credentials is not None:
#                 approver_username, approver_password = approver_credentials
#                 print("Approver's Username:", approver_username)
#                 print("Approver's Password:", approver_password)
#                 loginpage = Loginpage(self.driver)
#                 loginpage.enter_username(approver_username)
#                 loginpage.enter_password(approver_password)
#                 loginpage.click_login()
#                 approvals = LeaveApprovals(self.driver)
#                 approvals.navigate_leave_approval()
#                 approvals.common_parentsearch("QA T2 Madhu")
#                 approvals.perform_approve()
#                 exp_warning = "Success! Leave request status updated successfully."
#                 if approvals.validate_toastmessage().text == (exp_warning):
#                     print(
#                         "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
#                     loginpage.logout()
#                     assert True
#                 else:
#                     print(
#                         "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
#                     loginpage.logout()
#                     assert False
#             else:
#                 print("Failed to retrieve approver's credentials")
#
#
#     def test_Apply_Cancelling_LeaveApproved(self):
#         excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
#         login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
#         loginpage = Loginpage(self.driver)
#         loginpage.enter_username(login_username)
#         loginpage.enter_password(login_password)
#         loginpage.click_login()
#         loginpage.custom_sleep(2)
#         leave_Req = Leaves(self.driver)
#         leave_Req.Navigate_Self_Menu()
#         leave_Req.Navigate_Leaves_Menu()
#         leave_Req.Navigate_LeaveRequest()
#         leave_Req.common_parentsearch("Approved")
#         leave_Req.Click_Edit()
#         leave_Req.Click_Cancel()
#         leave_Req.Click_OK()
#         exp_warning = "Success! Leave cancellation request submitted successfully."
#         if leave_Req.validate_toastmessage().text == (exp_warning):
#             print(
#                 "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
#             loginpage.logout()
#             assert True
#         else:
#             print(
#                 "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
#             loginpage.logout()
#             assert False
#
#
#     def test_Approve_Cancel_ApprovedLeave(self):
#         for approver_name in Test_Approve_Leave_Request.Approver_list:
#             approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
#             if approver_credentials is not None:
#                 approver_username, approver_password = approver_credentials
#                 print("Approver's Username:", approver_username)
#                 print("Approver's Password:", approver_password)
#                 loginpage = Loginpage(self.driver)
#                 loginpage.enter_username(approver_username)
#                 loginpage.enter_password(approver_password)
#                 loginpage.click_login()
#                 approvals = LeaveApprovals(self.driver)
#                 approvals.navigate_leave_approval()
#                 approvals.common_parentsearch("QA T2 Madhu")
#                 approvals.perform_reject()
#                 exp_warning = "Success! Leave request status updated successfully."
#                 if approvals.validate_toastmessage().text == (exp_warning):
#                     print(
#                         "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
#                     loginpage.logout()
#                     assert True
#                 else:
#                     print(
#                         "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
#                     loginpage.logout()
#                     assert False
#             else:
#                 print("Failed to retrieve approver's credentials")
