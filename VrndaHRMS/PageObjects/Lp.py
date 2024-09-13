import pyautogui
from pynput.keyboard import Controller
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.BasePage import BasePage
keyboard = Controller()

class LeavePlan(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Admin_Screen_xpath = "(//span[@class='hide-menu'])[2]"
    Leave_config_xpath = "//a[@class='ml-sub-menu'][normalize-space()='Leave Configurations']"
    leaveplan_menu_xpath = "(//a[normalize-space()='Leave Plans'])[1]"
    parent_addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    AddNewLeavePlanConfig_Title_xpath = "(//h1[normalize-space()='Add New Leave Plan Configuration'])[1]"
    AddNewLeavePlanConfigDetails_Title_xpath = "(//h1[normalize-space()='Add New Leave Plan Configuration Details'])[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    config_name_xpath = ".//vrnda-textbox[@labelname='Configuration Name']/mat-form-field/div/div/div[2]/input"
    config_des_xpath = ".//vrnda-textbox[@labelname='Configuration Description']/mat-form-field/div/div/div[2]/input"
    # child_addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[23]"
    child_addbtn_xpath = "(//li[3]/div/button/span[5][@class='mat-mdc-button-touch-target'])[2]"
    # max_leavedays_xpath = ".//vrnda-amount[@labelname='Max Leave Days']/mat-form-field/div/div/div[2]/input"
    max_leavedays_xpath = ".//vrnda-amount[@labelname='Max Leave Days']"


    def navigate_leaveplan(self):
        admin_screen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Admin_Screen_xpath)))
        admin_screen.click()

        self.scroll_down()

        leave_config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_config_xpath)))
        leave_config.click()

        leave_plan = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leaveplan_menu_xpath)))
        leave_plan.click()

    def delete_defaultconfig_record(self):
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()
        row_del = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_xpath)))
        row_del.click()

    def click_add(self):
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_addbtn_xpath)))
        add.click()

    def validate_AddNewLeavePlanConfigtitle(self):
        current_title = self.driver.find_element(By.XPATH, self.AddNewLeavePlanConfig_Title_xpath).text
        return current_title

    def add_newplan_config(self, name, des):

        cname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_name_xpath)))
        cname.clear()
        cname.send_keys(name)

        cname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_des_xpath)))
        cname.clear()
        cname.send_keys(des)


    def Click_Add_LeavePlanConfigurationDetails(self):

        add_child = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.child_addbtn_xpath)))
        add_child.click()

    def validate_AddNewLeavePlanConfigDetailstitle(self):
        current_title = self.driver.find_element(By.XPATH, self.AddNewLeavePlanConfigDetails_Title_xpath).text
        return current_title


    def Insert_AddNewLeavePlanConfigurationDetails(self, max_leaves):
        max_leaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.max_leavedays_xpath)))
        actions = ActionChains(self.driver)
        actions.click(max_leaves)
        self.custom_sleep(3)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        self.custom_sleep(3)
        actions.send_keys(Keys.DELETE)
        self.custom_sleep(3)
        actions.send_keys(max_leaves)
        self.custom_sleep(3)
        actions.perform()
        self.custom_sleep(3)

        # max_leave.click()
        # max_leave.clear()
        # self.custom_sleep(3)
        # max_leave.send_keys(mld)
        # self.custom_sleep(3)
        # max_leave.send_keys(Keys.CONTROL + "a")
        # max_leave.send_keys(Keys.DELETE)
        # max_leave.send_keys(mld)
        # self.driver.execute_script("arguments[0].click();", max_leave)
        # self.custom_sleep(3)
        # self.driver.execute_script("arguments[0].value = '';", max_leave)
        # self.custom_sleep(3)
        # self.driver.execute_script("arguments[0].value = 'mld';", max_leave)
        # self.custom_sleep(3)
        # self.driver.execute_script("arguments[0].dispatchEvent(new Event('keydown', { bubbles: true }));", max_leave)
        # self.driver.execute_script("arguments[0].dispatchEvent(new Event('keypress', { bubbles: true }));", max_leave)
        # self.driver.execute_script("arguments[0].dispatchEvent(new Event('keyup', { bubbles: true }));", max_leave)
        # pyautogui.click(x=443, y=255)
        # self.custom_sleep(3)
        # pyautogui.press('backspace', presses=10)
        self.custom_sleep(3)
        # pyautogui.write(mld)
        # __________Imp Code__________________________
        #
        # __________Imp Code__________________________
