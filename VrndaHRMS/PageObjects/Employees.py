from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.BasePage import BasePage

class Employees(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    main_employees_xpath = "(//span[@class='hide-menu'])[3]"
    employee_details_xpath = "(//a[@class='ml-menu'])[4]"
    addbtn_emp_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"

    def goto_emp_details(self):
        # self.element_click("main_employees_xpath", self.main_employees_xpath)
        # self.custom_sleep(3)
        # self.element_click("employee_details_xpath", self.employee_details_xpath)

        emp_Menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_employees_xpath)))
        emp_Menu.click()

        emp_details = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.employee_details_xpath)))
        emp_details.click()

    def validate_addbtn(self):
        # self.driver.find_element(By.XPATH, self.addbtn_emp_xpath).click()

        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_emp_xpath)))
        add_btn.click()

    def title(self):
        current_title = self.driver.find_element(By.XPATH, self.page_title_Xpath).text
        return current_title
