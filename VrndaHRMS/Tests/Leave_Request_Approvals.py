import random
from datetime import datetime, timedelta

import pytest

from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel, get_credentials_by_name, get_credentials_by_approver, \
    get_credentials
from PageObjects.LeaveApprovals import LeaveApprovals


@pytest.mark.leave(order=4)
class Test_LeaveRequest_Approvals(BaseTest):
    today_date = datetime.now().strftime("%d-%m-%Y")
    print(today_date)
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

    print("Random From Date (excluding weekends):", formatted_from_date)
    print("Random To Date (excluding weekends):", formatted_to_date)

    app_list = list()
    # approver_list = []
    def leave_req(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leavereq = LeaveReq(self.driver)
        before_leave_req = leavereq.capture_leavebal()
        print(before_leave_req)
        approver_list = leavereq.apply_leaverequest(self.formatted_from_date, self.formatted_to_date, "test")
        # approver_list = leavereq.apply_leaverequest(self.today_date, self.today_date, "test")
        if approver_list:
            self.app_list.append(approver_list)
            print("Approver's name:", self.app_list)
        else:
            print("Failed to retrieve approver's name")
        loginpage.logout()
        return approver_list



    def test_leave_approvals(self):
        approver_list = self.leave_req()
        print(approver_list)
        for approver_name in approver_list:
            approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
            if approver_credentials is not None:
                approver_username, approver_password = approver_credentials
                print("Approver's Username:", approver_username)
                print("Approver's Password:", approver_password)

                # Login to the approver's credentials
                loginpage = Loginpage(self.driver)
                loginpage.enter_username(approver_username)
                loginpage.enter_password(approver_password)
                loginpage.click_login()
                approvals = LeaveApprovals(self.driver)
                approvals.navigate_leave_approval()
                approvals.common_parentsearch("QA T2 Madhu")
                approvals.perform_approve()

                loginpage.logout()

            else:
                print("Failed to retrieve approver's credentials")





# ---------------------------------------commented code-----------------------------------------------------------------------------------
# ----------------------------------------use for references----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

        #
        #
        # # approver = self.test_leave_req()
        # # print("Approver's name:", approver)
        # approver_username, approver_password = self.test_leave_req()  # Get the approver's credentials
        # loginpage.custom_sleep(5)
        # print("Approver's username:", approver_username)
        # print("Approver's password:", approver_password)
        # loginpage.custom_sleep(5)
        # # ?open in anew tab
        # # self.driver.execute_script("window.open('about:blank', '_blank');")
        # # self.driver.switch_to.window(self.driver.window_handles[-1])
        # # loginpage.custom_sleep(5)
        # # new_tab_url = "http://10.11.12.167:5006/#/authentication/signin"  # Replace this with your desired URL
        # # self.driver.get(new_tab_url)
        # loginpage = Loginpage(self.driver)
        # # excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        # # login_username, login_password = excel_data[1]
        # loginpage.enter_username(approver_username)
        # loginpage.enter_password(approver_password)
        # loginpage.click_login()
        # approvals = LeaveApprovals(self.driver)
        # approvals.navigate_leave_approval()
        # approvals.capture_request_list()
        # approvals.common_parentsearch("Madhu")
        # approvals.perform_approve_reject()
        # loginpage.custom.sleep(5)
        # return approver_username, approver_password
        # # self.driver.execute_script("window.open('about:blank', '_blank');")
        # # # Switch to the new tab
        # # self.driver.switch_to.window(self.driver.window_handles[-1])
        # # self.custom.sleep(2)
        # # # self.driver.get(url)
        # #
        # # excel_data = get_credentials_by_name("Excelfiles/Hrms.Cred.xlsx", "Sheet1")
        # # # Read approver's login credentials from Excel sheet using the captured approver's name
        # # for data in excel_data:
        # #     if data[0] == approver_name:  # Assuming approver's name is in the first column
        # #         approver_username, approver_password = data[1], data[2]  # Assuming username and password are in the second and third columns
        # #
        # #         # Perform login using approver's credentials
        # #         loginpage.enter_username(approver_username)
        # #         loginpage.enter_password(approver_password)
        # #         loginpage.click_login()
        #
        #
        # # common_keys = set(before_leave_req.keys()) & set(after_leave_req.keys())
        # # for key in common_keys:
        # #     assert before_leave_req[key] == after_leave_req[key]
        # #
        # # assert set(before_leave_req.keys()) == set(after_leave_req.keys())
        # # print("Dictionaries are equal")
        # # leavereq.custom_sleep(5)
        #

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# import random
# from datetime import datetime, timedelta
# import pytest
# import unittest
# from PageObjects.LeaveRequest import LeaveReq
# from PageObjects.Login import Loginpage
# from Tests.BaseTest import BaseTest
# from Utilities.ExcelUtils import get_data_from_excel, get_credentials_by_name, get_credentials_by_approver, \
#     get_credentials
# from PageObjects.LeaveApprovals import LeaveApprovals
# from deepdiff import DeepDiff
#
# from Utilities.ReadConfigurations import read_config
#
#
# class Test_LeaveRequest(BaseTest):
#     today_date = datetime.now().strftime("%d-%m-%Y")
#     print(today_date)
#     from_date = datetime.now() + timedelta(days=7)
#     # formatted_from_date = from_date.strftime("%d/%m/%Y")
#     to_date = datetime.now() + timedelta(days=7)
#     # formatted_to_date = to_date.strftime("%d/%m/%Y")
#
#     def generate_random_weekday():
#         today_date = datetime.now()
#         while True:
#             random_offset = random.randint(1, 7)  # Random offset from today in days
#             random_date = today_date + timedelta(days=random_offset)
#             if random_date.weekday() < 5:  # Check if it's a weekday (0 to 4 for Monday to Friday)
#                 return random_date.strftime("%d/%m/%Y")
#
#     random_weekday_date = generate_random_weekday()
#     formatted_from_date = random_weekday_date
#     formatted_to_date = random_weekday_date
#
#     print("Random From Date (excluding weekends):", formatted_from_date)
#     print("Random To Date (excluding weekends):", formatted_to_date)
#
#     app_list = list()
#     approver_list = []
#     before_leave_req = {}
#     after_leave_req = {}
#
#     applie_name = "QA T2 Madhu Mothkupally"
#     def test_apply_approve_leave(self):
#
#         login_username, login_password = get_credentials_by_approver("Excelfiles/Hrms.Cred.xlsx", "Sheet1",
#                                                                      self.applie_name)
#
#         print("Applied's Username:", login_username)
#         print("Applied's Password:", login_password)
#
#         loginpage = Loginpage(self.driver)
#         loginpage.enter_username(login_username)
#         loginpage.enter_password(login_password)
#         loginpage.click_login()
#
#         leavereq = LeaveReq(self.driver)
#         before_leave_req = leavereq.capture_leavebal()
#         print("Leave Balance before Leave Request:", self.before_leave_req)
#         approver_list = leavereq.apply_leaverequest(self.formatted_from_date, self.formatted_to_date, "test")
#         if approver_list:
#             self.app_list.append(approver_list)
#             print("Approver's name:", self.app_list)
#         else:
#             print("Failed to retrieve approver's name")
#         print(approver_list)
#         after_leave_req = leavereq.capture_leavebal()
#         print("Leave Balance after Leave Request:", self.after_leave_req)
#
#         diff = DeepDiff(before_leave_req, after_leave_req)
#         print(diff)
#
#         loginpage.custom_sleep(3)
#         # loginpage.logout()
#
#     # ---------------This is working code--------------------------------------------------------------------------------
#     #     approver_credentials = get_credentials_by_approver("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_list[0])
#     #     if approver_credentials is not None:
#     #         approver_username, approver_password = approver_credentials
#     #         print("Approver's Username:", approver_username)
#     #         print("Approver's Password:", approver_password)
#     #         loginpage = Loginpage(self.driver)
#     #         loginpage.enter_username(approver_username)
#     #         loginpage.enter_password(approver_password)
#     #         loginpage.click_login()
#     #         approvals = LeaveApprovals(self.driver)
#     #         approvals.navigate_leave_approval()
#     #         approvals.capture_request_list()
#     #         approvals.common_parentsearch("Madhu")
#     #         approvals.perform_approve_reject()
#     #         loginpage.custom_sleep(3)
#     #     else:
#     #         print("Failed to retrieve approver's credentials")
#  # ---------------This is working code--------------------------------------------------------------------------------
#
#         for approver_name in approver_list:
#             # Open a new tab
#             self.driver.execute_script("window.open('about:blank', '_blank');")
#             self.driver.switch_to.window(self.driver.window_handles[-1])
#
#             # Wait for the new tab to load
#             loginpage.custom_sleep(5)
#             web_url = read_config("basic info", "url")
#             # Get the URL for the new tab
#             # new_tab_url = "http://10.11.12.167:5006/#/authentication/signin"  # Replace this with your desired URL
#             self.driver.get(web_url)
#
#             # Get credentials for the current approver
#             approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
#             if approver_credentials is not None:
#                 approver_username, approver_password = approver_credentials
#                 print("Approver's Username:", approver_username)
#                 print("Approver's Password:", approver_password)
#
#                 # Login to the approver's credentials
#                 loginpage.enter_username(approver_username)
#                 loginpage.enter_password(approver_password)
#                 loginpage.click_login()
#
#                 # Perform the approval process
#                 approvals = LeaveApprovals(self.driver)
#                 approvals.navigate_leave_approval()
#                 emp_list = approvals.capture_request_list()
#                 req_status = approvals.capture_req_status()
#                 combined_dict = dict(zip(emp_list, req_status))
#                 print(combined_dict)
#
#                 approvals.common_parentsearch("QA T2 Madhu")
#                 approvals.perform_approve_reject()
#
#                 loginpage.custom_sleep(3)
#             else:
#                 print("Failed to retrieve approver's credentials")
#
#             # Close the last tab
#         self.driver.close()
#
#         # Switch back to the previous tab
#         self.driver.switch_to.window(self.driver.window_handles[-1])
#
#
#
#     diff = DeepDiff(before_leave_req, after_leave_req)
#     print(diff)
