from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.BasePage import BasePage


class Leaves(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    self_menu_xpath = "(//a[@class='menu-top menu-toggle ng-star-inserted'])[6]"
    Leaves_main_xpath = "(//a[normalize-space()='Leaves'])[1]"
    Leave_bal_xpath = "(//a[normalize-space()='Leave Balance'])[1]"
    Dashbaord_xpath = "//span[normalize-space()='Dashboard']"
    common_dashboard_xpath = "//a[normalize-space()='Common Dashboard']"
    Leave_request_xpath = "(//a[normalize-space()='Leave Request'])[1]"
    leavetype_table_xpath = "//mat-table[@role='table']/mat-row/mat-cell[1]"
    leavetype_bal_xpath = "//mat-table[@role='table']/mat-row/mat-cell[2]"
    addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    AddNewLeaveReq_Title_xpath = "(//h1[normalize-space()='Add New Leave Request'])[1]"
    leavetype_xpath = "(//input[@role='combobox'])[1]"
    leavetype_lov_xpath = "(//mat-option[@role='option']//span)[2]"
    fromdate_xpath = "(//input[@id='leaveFromDate'])[1]"
    todate_xpath = "(//input[@id='leaveToDate'])[1]"
    reason_xpath = "//textarea[@rows='1']"
    session_xpath = "(//mat-icon[text()='keyboard_arrow_down'])[4]"
    approver_xpath = ".//vrnda-textbox[@labelname='Approver']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    hr_xpath = ".//vrnda-textbox[@labelname='HR']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    applyleave_xpath = "//div[@class='example-button-row']//vrnda-button[1]"
    ok_xpath = "//span[text()='Ok']"
    startdate_table_xpath = ".//table[@class='table table-hover']/tbody/tr/td[1]"
    edit_xpath = "(//span[@class='mat-mdc-button-touch-target'])[7]"
    cancel_leave_xpath = "(//span[normalize-space()='Cancel Leave'])[1]"
    cancel_yes_xpath = "(//span[normalize-space()='Yes'])[1]"
    close_leavereq_xpath = "//span[normalize-space()='Close']"


    def Navigate_Self_Menu(self):

        self_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.self_menu_xpath)))
        self_menu.click()
        self.scroll_down()

    def Navigate_Leaves_Menu(self):
        main_leaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leaves_main_xpath)))
        main_leaves.click()

    def Navigate_LeaveBalance(self):
        leave_bal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_bal_xpath)))
        leave_bal.click()

    def Navigate_LeaveRequest(self):
        leave_req = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_request_xpath)))
        leave_req.click()

    def Navigate_DashBoard(self):
        self.scroll_up()
        dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Dashbaord_xpath)))
        dashboard.click()

        common_dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.common_dashboard_xpath)))
        common_dashboard.click()

    def capture_leavebal(self):
        # self.parent_refresh()
        key_elements = self.driver.find_elements(By.XPATH, self.leavetype_table_xpath)
        value_elements = self.driver.find_elements(By.XPATH, self.leavetype_bal_xpath)

        # leave_data = {}
        # for key_element, value_element in zip(key_elements, value_elements):
        #     leave_data[key_element.text.strip()] = value_element.text.strip()
        # return leave_data

        leave_data = {}
        for key_element, value_element in zip(key_elements, value_elements):
            key = key_element.text.strip()
            value = value_element.text.strip()
            # Convert to float
            value_float = float(value)
            # Convert to integer if the value is a whole number
            if value_float.is_integer():
                value = str(int(value_float))
            else:
                value = str(value_float).rstrip('0').rstrip('.')  # Remove trailing zeros and dot if any
            leave_data[key] = value
        return leave_data

    def Click_Add(self):
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_xpath)))
        add.click()

    def AddNewLeaveReqtitle(self):
        current_title = self.driver.find_element(By.XPATH, self.AddNewLeaveReq_Title_xpath).text
        return current_title

    def Select_LeaveType(self):
        leavetype = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_xpath)))
        leavetype.click()

        select_leave = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leavetype_lov_xpath)))
        select_leave.click()

        leavetype_text = select_leave.text
        return leavetype_text

    def Enter_FromDate(self, fromdate):
        from_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.fromdate_xpath)))
        self.driver.execute_script("arguments[0].value = '';", from_date)
        from_date.send_keys(fromdate)

    def Enter_ToDate(self, todate):
        to_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.todate_xpath)))
        self.driver.execute_script("arguments[0].value = '';", to_date)
        to_date.send_keys(todate)

    def Enter_Reason(self, reason):
        enter_reason = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.reason_xpath)))
        enter_reason.send_keys(reason)

    def Click_Session(self):
        session = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_xpath)))
        session.click()

    def Get_ApproversDetails(self):
        Manager = self.get_approver()
        HR = self.get_hr()
        return Manager, HR

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

    def Click_Apply_LeaveReq(self):
        apply_leave_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.applyleave_xpath)))
        apply_leave_button.click()

    def Click_OK(self):
        OK = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ok_xpath)))
        OK.click()

    def Click_Close(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_leavereq_xpath)))
        close.click()

    def Validate_MyLeaveReq(self):
        req_date = []
        request_elements = self.driver.find_elements(By.XPATH,
                                                     self.startdate_table_xpath)
        for element in request_elements:
            req_date.append(element.text)
            # print(req_date)
            return req_date

    def Click_Edit(self):
        click_edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_xpath)))
        click_edit.click()

    def Click_Cancel(self):
        click_cancel = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cancel_leave_xpath)))
        click_cancel.click()

        cancel_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cancel_yes_xpath)))
        cancel_yes.click()