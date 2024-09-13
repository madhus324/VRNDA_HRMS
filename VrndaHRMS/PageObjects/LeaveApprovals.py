from datetime import datetime

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.BasePage import BasePage

class LeaveApprovals(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    team_menu_xpath = "(//a[contains(@class,'menu-top menu-toggle')])[5]"
    leave_approvals_xpath = "(//a[normalize-space()='Leave Approvals'])[1]"
    emp_table_xpath = "//mat-table[@role='table']/mat-row/mat-cell[1]"
    req_status_xpath = "//mat-table[@role='table']/mat-row/mat-cell[2]"
    action_edit_xpath = "(//span[@class='mat-mdc-button-touch-target'])[5]"
    approve_xpath = "(//span[normalize-space()='Approve'])[1]"
    reject_xpath = "(//span[normalize-space()='Reject'])[1]"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"


    def navigate_leave_approval(self):
        team = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.team_menu_xpath)))
        team.click()

        approvals = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leave_approvals_xpath)))
        approvals.click()

    def capture_request_list(self):
        emp = []
        req_status = []
        try:
            # refresh = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, self.refresh_xpath)))
            # refresh.click()
            self.custom_sleep(3)
            while True:
                employee_elements = self.driver.find_elements(By.XPATH,
                                                               "//mat-table[@role='table']/mat-row/mat-cell[1]")

                request_elements = self.driver.find_elements(By.XPATH,
                                                              "//mat-table[@role='table']/mat-row/mat-cell[7]")
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

    def capture_req_status(self):
        req_status = []
        try:
            while True:

                employee_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[7]")
                for element in employee_elements:
                    req_status.append(element.text)
                print(req_status)
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
        except Exception as e:
            print("Error retrieving leave types:", e)
            # Handle the error, such as returning an empty list or raising an exception
            return []
        return req_status

    def capture_key_values(self):
        key = self.capture_request_list()
        value = self.capture_req_status()
        combined_data = dict(zip(key, value))
        print(combined_data)

    def perform_approve(self):

        # self.common_parentsearch(empname)

        edit_action = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.action_edit_xpath)))
        edit_action.click()

        approve = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.approve_xpath)))
        approve.click()

    def perform_reject(self):
        edit_action = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.action_edit_xpath)))
        edit_action.click()

        reject = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.reject_xpath)))
        reject.click()

    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    # def approve_cancel(self):








