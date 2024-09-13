import unittest

from PageObjects.LeaveApprovals import LeaveApprovals
from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Utilities.ExcelUtils import get_data_from_excel, get_credentials


class TestLeave(unittest.TestCase):
    def setUp(self):
        self.app_list = []  # Initialize an empty list to store approver names

    def test_leave_req(self):
        if not hasattr(self, 'approver_list'):
            excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
            login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
            loginpage = Loginpage(self.driver)
            loginpage.enter_username(login_username)
            loginpage.enter_password(login_password)
            loginpage.click_login()
            leavereq = LeaveReq(self.driver)
            before_leave_req = leavereq.capture_leavebal()
            print(before_leave_req)
            self.approver_list = leavereq.apply_leaverequest(self.formatted_from_date, self.formatted_to_date, "test")
            if self.approver_list:
                self.app_list.extend(self.approver_list)  # Extend instead of append if approver_list is a list
                print("Approvers:", self.app_list)
            else:
                print("Failed to retrieve approver's names")
            loginpage.logout()

    def test_leave_approvals(self):
        self.test_leave_req()  # Call the test_leave_req method to ensure approver_list is populated
        print(self.approver_list)
        for approver_name in self.approver_list:
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


