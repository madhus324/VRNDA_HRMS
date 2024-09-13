import random
import time
from datetime import datetime, timedelta
import pytest
from PageObjects.Leaves import Leaves
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel, get_credentials
from PageObjects.LeaveApprovals import LeaveApprovals

@pytest.mark.run(order=8)
class Test_LeaveRequest_Reject(BaseTest):

    Approver_list = []
    login_username = ""

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



    def test_Tovalidate_ApplyLeaveRequest(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        loginpage.custom_sleep(2)
        leave_Req = Leaves(self.driver)
        leave_Req.Navigate_Self_Menu()
        leave_Req.Navigate_Leaves_Menu()
        leave_Req.Navigate_LeaveRequest()
        leave_Req.Click_Add()
        leave_Req.Select_LeaveType()
        leave_Req.Enter_FromDate(self.formatted_from_date)
        leave_Req.Enter_ToDate(self.formatted_from_date)
        leave_Req.Enter_Reason("Test Leave Request")
        Test_LeaveRequest_Reject.Approver_list = leave_Req.Get_ApproversDetails()
        print(Test_LeaveRequest_Reject.Approver_list)
        leave_Req.Click_Apply_LeaveReq()
        leave_Req.Click_OK()
        leave_Req.custom_sleep(2)
        leave_Req.logout()
    #
    def test_Tovalidate_Reject_Leave_Request(self):
        first_approver_name = Test_LeaveRequest_Reject.Approver_list[0]
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


