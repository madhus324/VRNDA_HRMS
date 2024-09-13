import pdb
import random
import time
from datetime import datetime, timedelta
from PageObjects.LR_Validation import LR_Validations
from PageObjects.LeaveApprovals import LeaveApprovals
from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtils import get_data_from_excel, get_credentials_by_name, get_credentials_by_approver, \
    get_credentials


class Test_LeaveRequest(BaseTest):
    today_date = datetime.now().strftime("%d-%m-%Y")
    print(today_date)
    app_list = list()
    start_date = []
    app_list1 = []
    app_list2 = []

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
    # reformatted_from_date = datetime.strptime(formatted_from_date, '%d/%m/%Y').strftime('%d-%m-%Y')

    print("Random From Date (excluding weekends):", formatted_from_date)
    print("Random To Date (excluding weekends):", formatted_to_date)


    def generate_valid_leave_dates():
        # Get today's date
        today_date = datetime.now()

        # Find the next valid weekday for the "From Date"
        while True:
            from_date = today_date + timedelta(days=random.randint(1, 7))
            if from_date.weekday() < 5:  # Check if it's a weekday (0 to 4 for Monday to Friday)
                break

        # Find the next valid weekday for the "To Date"
        while True:
            to_date = from_date + timedelta(days=random.randint(2, 7))  # Ensure at least 2 days gap
            if to_date.weekday() < 5:  # Check if it's a weekday (0 to 4 for Monday to Friday)
                break

        # Calculate the number of days between the dates
        num_days = (to_date - from_date).days+1

        return from_date, to_date, num_days

    # Generate valid leave dates and calculate the number of days
    from_date, to_date, num_days = generate_valid_leave_dates()

    # Print the generated dates and the number of days
    print("Valid From Date (excluding weekends):", from_date.strftime("%d/%m/%Y"))
    print("Valid To Date (excluding weekends, at least 2 days later):", to_date.strftime("%d/%m/%Y"))
    print("Number of days between From Date and To Date:", num_days)

    def generate_random_weekend():
        today_date = datetime.now()
        while True:
            random_offset = random.randint(1, 7)  # Random offset from today in days
            random_date = today_date + timedelta(days=random_offset)
            if random_date.weekday() >= 5:  # Check if it's a weekend (5 for Saturday, 6 for Sunday)
                return random_date.strftime("%d/%m/%Y")

    random_weekend_date = generate_random_weekend()
    formatd_from_date = random_weekend_date
    formatd_to_date = random_weekend_date
    reformatd_from_date = datetime.strptime(formatted_from_date, '%d/%m/%Y').strftime('%d-%m-%Y')

    # print(f"Formatted from date: {formatted_from_date}")
    # print(f"Reformatted from date: {reformatted_from_date}")
    # print(f"Formatted to date: {formatted_to_date}")




    def test_LeaveRequestTitle(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        leavreq = LR_Validations(self.driver)
        leavreq.navigate_leave_request()
        time.sleep(2)
        Exp_title = "Leave Request"
        if leavreq.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

    def test_AddNewLeaveReqTitle(self):
        leavreq = LR_Validations(self.driver)
        leavreq.click_add()
        Exp_title = "Add New Leave Request"
        if leavreq.validate_newleaverequest_title() == (Exp_title):
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
            assert True
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

        time.sleep(2)

    def test_validate_date_warning_one(self):
        leavreq = LR_Validations(self.driver)
        leavreq.from_date(self.random_weekend_date)
        exp_warning = "Warning! From Date cannot be Weekend date."
        if leavreq.validate_toastmessage().text == (exp_warning):
            print("Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
            assert True
        else:
            print("Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False
        time.sleep(3)

    def test_validate_date_warning_two(self):
        leavreq = LR_Validations(self.driver)
        leavreq.to_date(self.random_weekend_date)
        exp_warning = "Warning! To Date cannot be Weekend date."
        if leavreq.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False

    def test_validate_date_warning_three(self):
        time.sleep(3)
        leavreq = LR_Validations(self.driver)
        leavreq.from_date("03-06-2024")
        exp_warning = "Warning! Sick Leave request cannot be back dated for more than 1 working days."
        if leavreq.validate_toastmessage().text == (exp_warning):
            print(
                "Passed : Expected warning messagesmatches Actual warning message of the page and verified successfully")
            assert True
        else:
            print(
                "Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            assert False
        time.sleep(3)

    def test_validate_date_warning_four(self):
        time.sleep(2)
        leavreq = LR_Validations(self.driver)
        leavreq.close_anlr()
        leavreq.navigate_leavebal()
        leave_balance = leavreq.capture_leavebal()
        print("Captured Leave Balance:", leave_balance)
        leavreq.navigate_back_leaverequest()
        leavreq.click_add()
        time.sleep(1)
        leavetype_value = leavreq.select_leavetype()
        print(leavetype_value)
        selected_leave_value = leave_balance.get(leavetype_value, "Leave type not found")
        print(f"Value for {leavetype_value}: {selected_leave_value}")
        # pdb.set_trace()
        leavreq.from_date(self.from_date.strftime("%d/%m/%Y"))
        leavreq.to_date(self.to_date.strftime("%d/%m/%Y"))
        exp_warning = f"Warning! Total leaves ({self.num_days}) is more than available leaves ({selected_leave_value}) and allowed LOP leaves (0)."
        actual_warning = leavreq.validate_toastmessage().text
        print(f"Actual warning message: '{actual_warning}'")
        if actual_warning.strip() == (exp_warning).strip():
            time.sleep(2)
            print("Passed : Expected warning messages matches Actual warning message of the page and verified successfully")
            leavreq.close_anlr()
            leavreq.logout()
            assert True
        else:
            print("Failed : Expected warning message doesnot matches Actual warning message of the page and verified successfully")
            time.sleep(5)
            leavreq.close_anlr()
            leavreq.logout()
            print("Logout successfully")
            assert False

    # app_list = list()

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
        self.app_list1 = leavereq.apply_leaverequest(self.formatted_from_date, self.formatted_to_date, "test")
        print(self.app_list1)
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
        self.test_leave_approvals()
        # self.test_cancel_leave_req()
        # self.test_cancel_approved()
        return self.app_list1

    def test_leave_approvals(self):
        # pdb.set_trace()
        print("call test_leave_approvals()",self.app_list1)

        for approver_name in self.app_list1:
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
        self.app_list2 = leavereq.cancel_leaverequest("approved")
        print(self.app_list2)
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
        self.test_cancel_approved()

        return self.app_list2

    def test_cancel_approved(self):
        for approver_name in self.app_list2:
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