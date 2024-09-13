import time

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
    close_addNewLeavePlanconfig_xpath = "(//span[normalize-space()='Close'])[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    config_name_xpath = ".//vrnda-textbox[@labelname='Configuration Name']/mat-form-field/div/div/div[2]/input"
    config_des_xpath = ".//vrnda-textbox[@labelname='Configuration Description']/mat-form-field/div/div/div[2]/input"
    # child_addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[23]"
    child_addbtn_xpath = "(//li[3]/div/button/span[5][@class='mat-mdc-button-touch-target'])[2]"
    AddNewLeavePlanConfigDetails_close_xpath = "(// span[normalize-space() = 'Close'])[1]"
    # max_leavedays_xpath = ".//vrnda-amount[@labelname='Max Leave Days']"
    max_leavedays_xpath = ".//vrnda-amount[@labelname='Max Leave Days']/mat-form-field/div/div/div[2]/input"
    Apply_before_days_xpath = ".//vrnda-amount[@labelname='Apply Before Days']/mat-form-field/div/div/div[2]/input"
    del_leaveplanConfig_xpath = "(//button[@mattooltip='Delete'])[2]"
    del_lpcd_yes_xpath = ".//div[@align='end']/button[1]"
    select_second_row_record_xpath = "(//mat-row[@role='row'])[2]"
    leaveconfig_secondrow_delete_xpath = "(//button[@mattooltip='Delete'])[2]"
    del_lpc_yes_xpath = "(//span[normalize-space()='Yes'])[1]"
    lpcd_delete_all_xpath = "(//button[@mattooltip='Delete'])"
    lpcd_delete_xpath = "(//button[@mattooltip='Delete'])[2]"



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

    # def duplicate_confi

    def Click_Add_LeavePlanConfigurationDetails(self):
        add_child = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.child_addbtn_xpath)))
        add_child.click()

    def validate_AddNewLeavePlanConfigDetailstitle(self):
        current_title = self.driver.find_element(By.XPATH, self.AddNewLeavePlanConfigDetails_Title_xpath).text
        return current_title

    def close_AddNewLeavePlanConfigDetails(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.AddNewLeavePlanConfigDetails_close_xpath)))
        close.click()

    def Insert_Max_leave_Days(self, max_leaves):
        maxi_leaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.max_leavedays_xpath)))
        actions = ActionChains(self.driver)
        actions.click(maxi_leaves)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)
        actions.send_keys(max_leaves)
        actions.perform()

    def Insert_Apply_Before_Days(self, max_days):
        maxi_days = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Apply_before_days_xpath)))
        actions = ActionChains(self.driver)
        actions.click(maxi_days)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)
        actions.send_keys(max_days)
        actions.perform()


    def delete_LeavePlanConfigDetails(self):
        del_lpcd = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_leaveplanConfig_xpath)))
        del_lpcd.click()

        del_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_lpcd_yes_xpath)))
        del_yes.click()

    def delete_LeaveplanConfig(self):
        row_del = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_xpath)))
        row_del.click()

        del_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_lpcd_yes_xpath)))
        del_yes.click()

    def close_AddNewLeavePlanConfig(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_addNewLeavePlanconfig_xpath)))
        close.click()

    def delete_Config_Child(self):
        click_row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_second_row_record_xpath)))
        click_row.click()

        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leaveconfig_secondrow_delete_xpath)))
        delete.click()

        click_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_lpc_yes_xpath)))
        click_yes.click()


    def delete_all_leaveplanconfigdetails(self):
        delete_elements = self.driver.find_elements(By.XPATH, self.lpcd_delete_all_xpath)
        for index in range(1, len(delete_elements)):
            try:
                delete_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.lpcd_delete_xpath))
                )
                time.sleep(2)
                delete_button.click()
                click_yes = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.del_lpc_yes_xpath)))
                click_yes.click()
                time.sleep(2)
                print("Deleted a leave configuration detail.")

                # After each deletion, re-fetch the delete elements as the list might have been updated
                delete_elements = self.driver.find_elements(By.XPATH, "(//button[@mattooltip='Delete'])")
                #
                # # Adjust the index to account for the updated list
                index = 2  # Reset to start deleting from the next third element

            except Exception as e:
                print(f"Error occurred while deleting a leave configuration detail: {e}")
                # Break the loop if an exception occurs to avoid infinite looping or stale element issues
                break

