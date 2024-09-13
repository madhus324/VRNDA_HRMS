from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from selenium.webdriver.support.ui import Select


class AppUsers(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Admin_Screen_Xpath = "(//span[@class='hide-menu'])[2]"
    App_roles_users_linktext = "Application Roles & Users"
    app_users_xpath = "(//a[normalize-space()='Application Users'])[1]"
    add_btn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    click_emp_xpath = "(//input[@role='combobox'])[1]"
    select_emp_xpath = "(//mat-option[@role='option']//span)[1]"
    employees_list_xpath = "//mat-table[@role='table']/mat-row/mat-cell[1]"


    def navigate_appusers(self):
        self.custom_sleep(3)
        self.driver.find_element(By.XPATH, self.Admin_Screen_Xpath).click()
        self.custom_sleep(3)
        self.driver.find_element(By.LINK_TEXT, self.App_roles_users_linktext).click()
        self.custom_sleep(3)
        self.driver.find_element(By.XPATH, self.app_users_xpath).click()

    def click_add(self):
        self.element_click("add_btn_xpath", self.add_btn_xpath)

    def select_emp(self):
        self.driver.find_element(By.XPATH, self.click_emp_xpath).click()
        self.custom_sleep(2)
        self.driver.find_element(By.XPATH, self.select_emp_xpath).click()

    def Emp_list(self):
        emp_list = []

        while True:

            employee_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[1]")
            for element in employee_elements:
                emp_list.append(element.text)
            print(emp_list)
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


