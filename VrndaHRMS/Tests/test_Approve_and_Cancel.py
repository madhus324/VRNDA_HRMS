import pdb
import random
import time
from datetime import datetime, timedelta

import pytest

from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel, get_credentials_by_name, get_credentials_by_approver, \
    get_credentials
from PageObjects.LeaveApprovals import LeaveApprovals


@pytest.mark.run(order=9)

class Test_LeaveRequest_Approvals(BaseTest):
    app_list1 = []
    app_list2 = []
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




    def test_leave_req(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leavereq = LeaveReq(self.driver)
        before_leave_req = leavereq.capture_leavebal()
        print(before_leave_req)
        Test_LeaveRequest_Approvals.app_list1 = leavereq.apply_leaverequest(self.formatted_from_date, self.formatted_to_date, "test")
        print(Test_LeaveRequest_Approvals.app_list1)
        exp_warning = "Success! Leave request saved successfully"
        if leavereq.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False
        loginpage.logout()

    def test_leave_approvals(self):
        for approver_name in Test_LeaveRequest_Approvals.app_list1:
            approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
            if approver_credentials is not None:
                approver_username, approver_password = approver_credentials
                print("Approver's Username:", approver_username)
                print("Approver's Password:", approver_password)
                loginpage = Loginpage(self.driver)
                loginpage.enter_username(approver_username)
                loginpage.enter_password(approver_password)
                loginpage.click_login()
                approvals = LeaveApprovals(self.driver)
                approvals.navigate_leave_approval()
                approvals.common_parentsearch("QA T2 Madhu")
                approvals.perform_approve()
                exp_warning = "Success! Leave request status updated successfully."
                if approvals.validate_toastmessage().text == (exp_warning):
                    print(
                        "Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
                    assert True
                else:
                    print(
                        "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
                    assert False

                loginpage.logout()

            else:
                print("Failed to retrieve approver's credentials")


    def test_cancel_leave_req(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leavereq = LeaveReq(self.driver)
        leavereq.navigate_leave_request()
        Test_LeaveRequest_Approvals.app_list2 = leavereq.cancel_leaverequest("approved")
        print(Test_LeaveRequest_Approvals.app_list2)
        exp_warning = "Success! Leave cancellation request submitted successfully."
        if leavereq.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False
        loginpage.logout()


    def test_cancel_approved(self):
        for approver_name in Test_LeaveRequest_Approvals.app_list2:
            approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", approver_name)
            if approver_credentials is not None:
                approver_username, approver_password = approver_credentials
                print("Approver's Username:", approver_username)
                print("Approver's Password:", approver_password)
                loginpage = Loginpage(self.driver)
                loginpage.enter_username(approver_username)
                loginpage.enter_password(approver_password)
                loginpage.click_login()
                approvals = LeaveApprovals(self.driver)
                approvals.navigate_leave_approval()
                approvals.common_parentsearch("madhu")
                approvals.perform_approve()
                exp_warning = "Success! Leave request status updated successfully."
                if approvals.validate_toastmessage().text == (exp_warning):
                    print(
                        "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
                    loginpage.logout()
                    assert True
                else:
                    print(
                        "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
                    loginpage.logout()
                    assert False
                time.sleep(3)

            else:
                print("Failed to retrieve approver's credentials")
        else:
            print("No approver name found to proceed with the test")