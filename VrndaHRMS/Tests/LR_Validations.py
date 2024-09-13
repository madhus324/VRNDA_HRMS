import pdb
import random
import time
from datetime import datetime, timedelta
from PageObjects.LR_Validation import LR_Validations
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
    formatted_from_date = random_weekend_date
    formatted_to_date = random_weekend_date
    reformatted_from_date = datetime.strptime(formatted_from_date, '%d/%m/%Y').strftime('%d-%m-%Y')

    print(f"Formatted from date: {formatted_from_date}")
    print(f"Reformatted from date: {reformatted_from_date}")
    print(f"Formatted to date: {formatted_to_date}")




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
        # leavreq.capture_screenshot()
        exp_warning = f"Warning! Total leaves ({self.num_days}) is more than available leaves({selected_leave_value}) and allowed LOP leaves(0)."
        actual_warning = leavreq.validate_toastmessage().text
        # leavreq.capture_screenshot()
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

