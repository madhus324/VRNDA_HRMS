import random
from datetime import datetime, timedelta

import pytest

from PageObjects.LR_Validation import LR_Validations
from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel


@pytest.mark.leave(order=1)
class Test_LeaveRequest(BaseTest):
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
    reformatted_from_date = datetime.strptime(formatted_from_date, '%d/%m/%Y').strftime('%d-%m-%Y')

    print("Random From Date (excluding weekends):", formatted_from_date)
    print("Random To Date (excluding weekends):", formatted_to_date)

    app_list = list()
    start_date = []

    def test_apply_leave_req(self):
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
        loginpage.custom_sleep(3)
        self.start_date.append(leavereq.validate_myleaverequest())
        if self.start_date:
            # self.start_date.append(date_list)
            print("Date list:", self.start_date)
        else:
            print("Failed to retrieve Start Date list")
        print(f"line 59 : {type(self.reformatted_from_date)}")

        if self.reformatted_from_date in self.start_date[0]:
            print(f"The Applied Leave Request on date: {self.reformatted_from_date} is available in the Dashboard.")
            loginpage.logout()
            assert True
        else:
            print(f"The Applied Leave Request on date: {self.reformatted_from_date} is not available in the Dashboard.")
            loginpage.logout()
            assert False
        # loginpage.logout()



    def test_cancel_leaverequest(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leavereq = LR_Validations(self.driver)
        leavereq.navigate_leave_request()
        leavereq.cancel_leaverequest("request")
        exp_warning = "Success! Leave cancelled successfully."
        if leavereq.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False
        loginpage.logout()



