from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeaveBal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    self_menu_xpath = "(//a[@class='menu-top menu-toggle ng-star-inserted'])[6]"
    Leaves_main_xpath = "(//a[normalize-space()='Leaves'])[1]"
    Leave_bal_xpath = "(//a[normalize-space()='Leave Balance'])[1]"
    leavetype_xpath = "//mat-table[@role='table']/mat-row/mat-cell[1]"
    leavetype_bal_xpath = "//mat-table[@role='table']/mat-row/mat-cell[2]"


    def navigate_leavebal(self):

        self_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.self_menu_xpath)))
        self_menu.click()

        self.scroll_down()

        main_leaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leaves_main_xpath)))
        main_leaves.click()

        leave_bal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_bal_xpath)))
        leave_bal.click()
        self.custom_sleep(3)

    def capture_leavebal(self):
        # self.parent_refresh()
        self.custom_sleep(3)
        key_elements = self.driver.find_elements(By.XPATH, self.leavetype_xpath)
        value_elements = self.driver.find_elements(By.XPATH, self.leavetype_bal_xpath)

        leave_data = {}
        for key_element, value_element in zip(key_elements, value_elements):
            leave_data[key_element.text.strip()] = value_element.text.strip()
        print(leave_data)




