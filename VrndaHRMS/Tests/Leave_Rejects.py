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


@pytest.mark.leave(order=3)
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
            first_approver = approver_list[0]
            print("First Approver's name:", first_approver)
            loginpage.logout()
            return first_approver
        else:
            print("Failed to retrieve approver's name")
            loginpage.logout()
            return None

    def test_leave_approvals(self):
        first_approver_name = self.leave_req()
        if first_approver_name:
            approver_credentials = get_credentials("Excelfiles/Hrms.Cred.xlsx", "Sheet1", first_approver_name)
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
                approvals.perform_reject()
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


