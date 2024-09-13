from datetime import time
import time

from pynput.keyboard import Controller
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    projects_xpath = "(//a[@class='ml-menu'][normalize-space()='Projects'])[1]"
    common_delete_xpath = "(//button[@color='warn']//span)[5]"
    common_save_xpath = "(//vrnda-button[@class='ng-star-inserted'])[1]"
    Admin_Screen_xpath = "(//span[@class='hide-menu'])[2]"
    Leave_config_xpath = "//a[@class='ml-sub-menu'][normalize-space()='Leave Configurations']"
    parent_search_xpath = "(//input[@type='text'])[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    logout_link_xpath = "//img[@alt='User']"
    logout_xpath = "//span[text()[normalize-space()='Logout']]"
    child_refresh_xpath = "(//span[@class='mat-mdc-button-touch-target'])[11]"
    parent_refresh_xpath = "(//button[@color='primary']//span)[5]"
    Dashbaord_xpath = "//span[normalize-space()='Dashboard']"
    page_title_Xpath = "//h4[@class='page-title']"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"

    def custom_sleep(self, seconds):
        time.sleep(seconds)

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        # element.is_displayed()
        element.click()

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_classname"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        return element

    def title(self):
        current_title = self.driver.find_element(By.XPATH, self.page_title_Xpath).text
        return current_title

    def scroll_down(self):
        refresh_data = self.driver.find_element(By.XPATH, self.projects_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)

    def scroll_up(self):
        refresh_data = self.driver.find_element(By.XPATH, self.Dashbaord_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)

    def navigate_leave_config(self):
        self.custom_sleep(3)
        admin_screen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Admin_Screen_xpath)))
        admin_screen.click()

        leave_config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_config_xpath)))
        leave_config.click()



    def common_delete(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.common_delete_xpath)))
        delete.click()

    def common_save(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.common_save_xpath)))
        save.click()

    def common_parentsearch(self, search_text):

        p_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.parent_search_xpath)))
        p_search.click()
        p_search.clear()
        keyboard = Controller()
        for char in search_text:
            keyboard.press(char)
            keyboard.release(char)
        self.custom_sleep(2)
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()


    def logout(self):

        logout_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath)))
        logout_link.click()


        log_out = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.logout_xpath)))
        log_out.click()

    def child_refresh(self):
        refresh = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.child_refresh_xpath)))
        refresh.click()

    def parent_refresh(self):
        refresh = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_refresh_xpath)))
        refresh.click()

    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage
