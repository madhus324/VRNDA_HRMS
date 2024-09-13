import logging
from datetime import datetime

from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LeaveApprovals import LeaveApprovals
from PageObjects.BasePage import BasePage


class LR_Validations(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    self_menu_xpath = "(//a[@class='menu-top menu-toggle ng-star-inserted'])[6]"
    Leaves_main_xpath = "(//a[normalize-space()='Leaves'])[1]"
    Leave_request_xpath = "(//a[normalize-space()='Leave Request'])[1]"
    addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    available_leaves_xpath = ".//vrnda-amount[@labelname='Available Leaves']"
    leavetype_xpath = "(//input[@role='combobox'])[1]"
    leavetype_lov_xpath = "(//mat-option[@role='option']//span)[2]"
    all_leavetype_lov_xpath = "(//mat-option[@role='option']//span)"
    applyleave_xpath = "//div[@class='example-button-row']//vrnda-button[1]"
    fromdate_xpath = "(//input[@id='leaveFromDate'])[1]"
    todate_xpath = "(//input[@id='leaveToDate'])[1]"
    reason_xpath = "//textarea[@rows='1']"
    latereq_xpath = "//h1[text()='Late leave request']"
    llr_yes_xpath = "//span[normalize-space()='Yes']"
    subject_xpath = "//div[@class='ng-star-inserted']"
    ok_xpath = "//span[text()='Ok']"
    approver_xpath = ".//vrnda-textbox[@labelname='Approver']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    hr_xpath = ".//vrnda-textbox[@labelname='HR']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    reject_xpath = "//span[normalize-space()='Reject']"
    Cancel_leave_xpath = "//span[text()='Cancel Leave']"
    startdate_table_xpath = ".//table[@class='table table-hover']/tbody/tr/td[1]"
    Dashbaord_xpath = "//span[normalize-space()='Dashboard']"
    common_dashboard_xpath = "//a[normalize-space()='Common Dashboard']"
    Leave_bal_xpath = "(//a[normalize-space()='Leave Balance'])[1]"
    leavetype_table_xpath = "//mat-table[@role='table']/mat-row/mat-cell[1]"
    leavetype_bal_xpath = "//mat-table[@role='table']/mat-row/mat-cell[2]"
    status_xpath = "//mat-table[@role='table']/mat-row/mat-cell[6]"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"
    page_title_Xpath = "//h4[@class='page-title']"
    adlr_xpath = "//h1[text()='Add New Leave Request']"
    half_full_day_xpath = "(//input[@role='combobox'])[3]"
    session_xpath = "(//mat-icon[text()='keyboard_arrow_down'])[4]"
    close_xpath = "//span[normalize-space()='Close']"
    edit_xpath = "(//span[@class='mat-mdc-button-touch-target'])[7]"
    cancel_xpath = "(//span[normalize-space()='Cancel Leave'])[1]"






    def navigate_leave_request(self):
        self_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.self_menu_xpath)))
        self_menu.click()

        self.scroll_down()

        main_leaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leaves_main_xpath)))
        main_leaves.click()

        self.scroll_down()

        leave_req = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_request_xpath)))
        leave_req.click()


    def click_add(self):
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_xpath)))
        add.click()

    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    def title(self):
        current_title = self.driver.find_element(By.XPATH, self.page_title_Xpath).text
        return current_title

    def validate_newleaverequest_title(self):
        adlr = self.driver.find_element(By.XPATH, self.adlr_xpath).text
        return adlr

    def from_date(self, fromdate):
        from_dte = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.fromdate_xpath)))
        from_dte.send_keys(fromdate)
        session = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_xpath)))
        session.click()

    def to_date(self, todate):
        to_dte = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.todate_xpath)))
        to_dte.send_keys(todate)
        session = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_xpath)))
        session.click()

    def enter_reason(self, reason):
        enter_reason = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.reason_xpath)))
        enter_reason.send_keys(reason)

    def capture_leavebal(self):
        self.custom_sleep(3)

        try:
            # Find the elements containing the leave types and their balances
            key_elements = self.driver.find_elements(By.XPATH, self.leavetype_table_xpath)
            value_elements = self.driver.find_elements(By.XPATH, self.leavetype_bal_xpath)

            # Initialize an empty dictionary to store the leave data
            leave_data = {}

            # Loop through the elements and populate the dictionary
            for key_element, value_element in zip(key_elements, value_elements):
                key = key_element.text.strip()
                value = value_element.text.strip()

                # Try to convert the value to an integer
                try:
                    value = float(value)
                    if value.is_integer():
                        value = int(value)
                except ValueError:
                    # If the value cannot be converted to a number, keep it as a string
                    pass

                leave_data[key] = value

            # Log the captured leave data
            logging.info(f"Captured leave data: {leave_data}")

            # Return the dictionary containing leave types and their balances
            return leave_data

        except Exception as e:
            logging.error(f"Error capturing leave balances: {e}")
            return {}



    def navigate_leavebal(self):

        leave_bal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_bal_xpath)))
        leave_bal.click()
        self.custom_sleep(3)

    def navigate_back_leaverequest(self):
        leave_req = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_request_xpath)))
        leave_req.click()

    def close_anlr(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_xpath)))
        close.click()

    def select_leavetype(self):
        leavetype = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_xpath)))
        leavetype.click()

        select_leave = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_lov_xpath)))
        select_leave.click()
        leavetype_text = select_leave.text
        return leavetype_text

    def cancel_leaverequest(self, text):
        self.common_parentsearch(text)

        click_edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_xpath)))
        click_edit.click()

        click_cancel = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cancel_xpath)))
        click_cancel.click()

        click_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.llr_yes_xpath)))
        click_yes.click()













    def capture_leavetype_status(self):
        # key_elements = []
        # value_elements = []
        # key_elements = self.driver.find_elements(By.XPATH, self.leavetype_table_xpath)
        # value_elements = self.driver.find_elements(By.XPATH, self.status_xpath)
        # applied_leave_data = {}
        # while True:
        #     for key_element, value_element in zip(key_elements, value_elements):
        #         applied_leave_data[key_element.text.strip()] = value_element.text.strip()
        #     print(applied_leave_data)
        #
        #     self.custom_sleep(3)
        #     refresh_data = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']")
        #     self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)
        #     self.custom_sleep(2)
        #     try:
        #         next_page_btn = self.driver.find_element(By.XPATH,
        #                                                  "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']")
        #         next_page_btn.click()
        #         self.custom_sleep(2)
        #     except ElementClickInterceptedException:
        #         break
        #
        # # data_dict = dict(zip(emp, req_status))
        # print(applied_leave_data)
        emp = []
        req_status = []
        try:
            self.custom_sleep(3)
            while True:
                employee_elements = self.driver.find_elements(By.XPATH,
                                                              "//mat-table[@role='table']/mat-row/mat-cell[2]")

                request_elements = self.driver.find_elements(By.XPATH,
                                                             "//mat-table[@role='table']/mat-row/mat-cell[6]")
                for element_emp, element_req in zip(employee_elements, request_elements):
                    emp.append(element_emp.text)
                    req_status.append(element_req.text)

                self.custom_sleep(3)
                refresh_data = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']")
                self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)
                self.custom_sleep(2)
                try:
                    next_page_btn = self.driver.find_element(By.XPATH,
                                                             "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']")
                    next_page_btn.click()
                    self.custom_sleep(2)
                except ElementClickInterceptedException:
                    break
            data_dict = dict(zip(emp, req_status))
            print(data_dict)

        except Exception as e:
            print("Error retrieving leave types:", e)
            # Handle the error, such as returning an empty list or raising an exception
            return {}
        return data_dict

    def apply_leaverequest(self, fromdate, todate, reason):
        self.navigate_leavebal()
        self.capture_leavebal()
        self.scroll_down()

        leave_req = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_request_xpath)))
        leave_req.click()

        # add a new leave request
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_xpath)))
        add.click()

        # Select Lov
        leavetype = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_xpath)))
        leavetype.click()

        select_leave = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_lov_xpath)))
        select_leave.click()

        from_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.fromdate_xpath)))
        from_date.send_keys(fromdate)

        to_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.todate_xpath)))
        to_date.send_keys(todate)

        if from_date == datetime.now().date():

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(By.XPATH, self.llr_yes_xpath))
                # Check if the popup element exists
                if popup_element.is_displayed():
                    # Click the OK button or perform any action needed to handle the popup
                    click_yes = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, self.llr_yes_xpath)))
                    click_yes.click()
                    print("Popup accepted.")
            except NoSuchElementException:
                # Popup element not found, continue with your other actions
                pass
        #     popup = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By.XPATH, self.llr_yes_xpath))
        #     # popup.click()
        #     print("Late Leave Request has opened")
        #     # If popup is present, accept it (click "Yes" button)
        #     click_yes = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, self.llr_yes_xpath)))
        #     click_yes.click()
        #     print("Popup accepted.")
        # else:
        #     pass

        enter_reason = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.reason_xpath)))
        enter_reason.send_keys(reason)

        approver = self.get_approver()
        hr = self.get_hr()

        apply_leave_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.applyleave_xpath)))
        apply_leave_button.click()

        OK = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ok_xpath)))
        OK.click()

        leave_bal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_bal_xpath)))
        leave_bal.click()

        return approver, hr

    def get_approver(self):
        approver = self.driver.find_element(By.XPATH, self.approver_xpath)
        textbox_text = approver.get_attribute("value")
        print("Text from textbox:", textbox_text)
        return textbox_text

    def get_hr(self):
        hr = self.driver.find_element(By.XPATH, self.hr_xpath)
        textbox_text = hr.get_attribute("value")
        print("Text from textbox:", textbox_text)
        return textbox_text

    def validate_myleaverequest(self):
        self.scroll_up()
        dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Dashbaord_xpath)))
        dashboard.click()

        common_dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.common_dashboard_xpath)))
        common_dashboard.click()

        req_date = []
        request_elements = self.driver.find_elements(By.XPATH,
                                                     self.startdate_table_xpath)
        for element in request_elements:
            req_date.append(element.text)
            print(req_date)
            return req_date

    # def warning_popup(self):

    # lov_elements = self.driver.find_elements(By.XPATH, self.all_leavetype_lov_xpath)
    # for lov_element in lov_elements:
    #     self.custom_sleep(3)
    #     selected_lov = lov_element.text.strip()
    #     self.custom_sleep(3)
    #     if selected_lov in leave_data:
    #         self.custom_sleep(3)
    #         leave_balance = leave_data[selected_lov]
    #         print("Leave balance for", selected_lov, "is", leave_balance)
    #     else:
    #         print("Leave type", selected_lov, "not found in dictionary")

    # self.custom_sleep(5)

    # # Perform actions specific to each LOV value
    # # Example: Check if available leaves > 0 and apply leave if true
    # available_leaves = self.get_available_leaves()
    # if available_leaves is not None:
    #     if available_leaves > 0.0:
    #         apply_leave_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.applyleave_xpath)))
    #         apply_leave_button.click()
    #         print("Leave applied successfully for this LOV value")
    #     else:
    #         print("No available leaves for this LOV value")
    # else:
    #     print("Error: Unable to determine available leaves for this LOV value")

    # def navigate_leave_req(self):
    #     self.navigate_leavebal()
    #     self.capture_leavebal()
    #
    #     # self_menu = WebDriverWait(self.driver, 10).until(
    #     #     EC.element_to_be_clickable((By.XPATH, self.self_menu_xpath)))
    #     # self_menu.click()
    #
    #     self.scroll_down()
    #
    #     # main_leaves = WebDriverWait(self.driver, 10).until(
    #     #     EC.element_to_be_clickable((By.XPATH, self.Leaves_main_xpath)))
    #     # main_leaves.click()
    #
    #     leave_req = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.Leave_request_xpath)))
    #     leave_req.click()
    #
    # def click_add(self):
    #     add = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.addbtn_xpath)))
    #     add.click()
    #
    # # def get_available_leaves(self):
    # #     available_leaves_element = self.driver.find_element(By.XPATH, self.available_leaves_xpath)
    # #     available_leaves_text = available_leaves_element.text
    # #     print(available_leaves_text)
    # #     if available_leaves_text.strip():  # Check if text is not empty after stripping whitespace
    # #         try:
    # #             available_leaves = float(available_leaves_text)
    # #             return available_leaves
    # #         except ValueError:
    # #             print("Error: Unable to convert available leaves to a float.")
    # #             # Handle this error scenario according to your application's requirements
    # #             return None
    # #     else:
    # #         # Return a default value or handle the scenario accordingly
    # #         return 0.0  # Assuming default value is a float
    # #
    # def add_leave_req(self):
    #     leavetype = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.leavetype_xpath)))
    #     leavetype.click()
    #
    #     lov_elements = self.driver.find_elements(By.XPATH, self.all_leavetype_lov_xpath)
    #     for lov_element in lov_elements:
    #         lov_element.click()
    #         self.custom_sleep(5)
    #
    #         # Perform actions specific to each LOV value
    #         # Example: Check if available leaves > 0 and apply leave if true
    #         available_leaves = self.get_available_leaves()
    #         if available_leaves is not None:
    #             if available_leaves > 0.0:
    #                 apply_leave_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.applyleave_xpath)))
    #                 apply_leave_button.click()
    #                 print("Leave applied successfully for this LOV value")
    #             else:
    #                 print("No available leaves for this LOV value")
    #         else:
    #             print("Error: Unable to determine available leaves for this LOV value")
    #
    #








