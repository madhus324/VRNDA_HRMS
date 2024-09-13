import random
import time
from datetime import datetime, timedelta

import pytest
import unittest
from PageObjects.LeaveApprovals import LeaveApprovals
from PageObjects.LeaveBalance import LeaveBal
from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
from Utilities.ExcelUtils import get_data_from_excel, get_credentials

@pytest.mark.leave(order=2)
class Test_Leaveapprovals(BaseTest):

    def test_leave_approvals(self):

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
                    approvals.perform_approve_reject()

                    loginpage.logout()

                else:
                    print("Failed to retrieve approver's credentials")