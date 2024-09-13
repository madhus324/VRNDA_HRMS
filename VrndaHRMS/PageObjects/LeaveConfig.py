import time

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

import select

from pynput.keyboard import Controller
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from PageObjects.BasePage import BasePage

class LeaveConfig(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Admin_Screen_xpath = "(//span[@class='hide-menu'])[2]"
    Leave_config_xpath = "//a[@class='ml-sub-menu'][normalize-space()='Leave Configurations']"
    Leave_sub_config_xpath = "//a[@class='ml-menu2'][normalize-space()='Leave Configurations']"
    add_btn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    config_name_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/leave-configurations-form-dialog[1]/vrnda-dialog-title[1]/div[1]/vrnda-dialog-content[1]/mat-dialog-content[1]/form[1]/div[1]/div[1]/vrnda-textbox[1]/mat-form-field[1]/div[1]/div[1]/div[2]/input[1]"
    config_desc_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/leave-configurations-form-dialog[1]/vrnda-dialog-title[1]/div[1]/vrnda-dialog-content[1]/mat-dialog-content[1]/form[1]/div[1]/div[2]/vrnda-textbox[1]/mat-form-field[1]/div[1]/div[1]/div[2]/input[1]"
    save_Xpath = "(//vrnda-button[@class='ng-star-inserted'])[1]"
    parent_search_xpath = "(//input[@type='text'])[1]"
    child_search_xpath = "(//input[@type='text'])[2]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    # child_add_xpath = "(//span[@class='mat-mdc-button-touch-target'])[14]"
    child_add_xpath = "//li[2]//div[1]//button[1]//span[5]"
    lt_click_xpath = "(//input[@role='combobox'])[1]"
    select_lov_xpath = "(//mat-option[@role='option']//span)[2]"
    select_lov2_xpath = "(//mat-option[@role='option']//span)[1]"
    recurrence_xpath = "(//input[@role='combobox'])[3]"
    recurrence_lov_xpath = "(//mat-option[@role='option'])[2]"
    no_of_leaves_xpath = ".//vrnda-amount[@labelname='No Of Leaves']/mat-form-field/div/div/div[2]/input"
    child_save_xpath = "//vrnda-button[@class='ng-star-inserted']"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"
    popupscreentitle_xpath = "(//h1[normalize-space()='Add New Leave Configuration'])[1]"
    child_popupscreentitle_xpath = "(//h1[normalize-space()='Add New Leave Configuration Details'])[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    select_second_row_record_xpath = "(//mat-row[@role='row'])[2]"
    name_field_xpath = "(//mat-cell[@role='cell'])[3]"
    selectedrecord_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    child_title_xpath = "//h1[@class='mat-mdc-dialog-title mdc-dialog__title']"
    lateleavewarn_xpath = ".//vrnda-number[@labelname='Late Leave Warnings']/mat-form-field/div/div/div[2]/input"
    lateleavecondi_xpath = "(//input[@role='combobox'])[4]"
    lateleavecond_value_1_xpath = "(//mat-option[@role='option'])[2]"
    lateleavecond_value_xpath = "(//mat-option[@role='option'])[1]"
    ldc_delete_xpath = "(//button[@mattooltip='Delete'])[2]"
    ldc_delete_all_xpath = "(//button[@mattooltip='Delete'])"
    ldc_yes_xpath = "(//span[normalize-space()='Yes'])[1]"
    leaveconfig_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    leaveconfig_secondrow_delete_xpath = "(//button[@mattooltip='Delete'])[2]"
    close_btn_xpath = "(//span[normalize-space()='Close'])[1]"



    def navigate_leave_config(self):
        self.custom_sleep(3)
        admin_screen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Admin_Screen_xpath)))
        admin_screen.click()
        self.custom_sleep(3)


        leave_config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_config_xpath)))
        leave_config.click()

        sub_config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_sub_config_xpath)))
        sub_config.click()

    def click_add(self):
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_btn_xpath)))
        add.click()

    def parentpopupscreentitle(self):
        current_title = self.driver.find_element(By.XPATH, self.popupscreentitle_xpath).text
        return current_title

    def enterconfig_name(self, cname):
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_name_xpath)))
        # name.click()
        # name.clear()
        name.send_keys(cname)

    def enterconfig_desc(self, cdescrption):

        description = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_desc_xpath)))
        # description.click()
        # description.clear()
        description.send_keys(cdescrption)

    def click_save(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_Xpath)))
        save.click()

    def valueofrecord(self):
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()
        text_value = self.driver.find_element(By.XPATH, self.name_field_xpath).text
        return text_value

    def search_parentrecord(self, search_text):
        p_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.parent_search_xpath)))
        p_search.click()
        keyboard = Controller()
        for char in search_text:
            keyboard.press(char)
            keyboard.release(char)
        self.custom_sleep(2)
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()
        self.custom_sleep(3)

    def clear_search(self):
        p_search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_search_xpath)))
        p_search.click()
        p_search.clear()

    def delete_parent_record(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.selectedrecord_delete_xpath)))
        delete.click()

    def click_add_Child(self):
        add_child = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.child_add_xpath)))
        add_child.click()

    def childpopupscreentitle(self):
        current_title = self.driver.find_element(By.XPATH, self.child_popupscreentitle_xpath).text
        return current_title

    def select_leavetype(self):
        click_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lt_click_xpath)))
        click_lov.click()

        lov_options = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_lov_xpath)))
        lov_options.click()

    def select_recurrance(self):
        recurrence = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recurrence_xpath)))
        recurrence.click()

        recurrence_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recurrence_lov_xpath)))
        recurrence_lov.click()

    def enter_leaves(self, n_leaves):
        noofleaves = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.no_of_leaves_xpath)))
        self.custom_sleep(3)
        noofleaves.send_keys(Keys.CONTROL + "a")
        noofleaves.send_keys(Keys.DELETE)
        noofleaves.send_keys(n_leaves)
        self.custom_sleep(2)

    def lateleavecondition(self):
        llc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lateleavecondi_xpath)))
        llc.click()

    def lateleaveconditionvalue(self):
        llc_value = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lateleavecond_value_xpath)))
        textvalue = llc_value.text
        print(textvalue)
        llc_value.click()
        return textvalue


    def enter_lateleaveswarnings(self, noofwarns):
        llw = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lateleavewarn_xpath)))
        llw.click()
        llw.clear()
        llw.send_keys(noofwarns)

    def save(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_Xpath)))
        save.click()



    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    def delete_LeaveconfigDetails(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ldc_delete_xpath)))
        delete.click()

        click_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ldc_yes_xpath)))
        click_yes.click()


    def delete_Leaveconfig(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leaveconfig_delete_xpath)))
        delete.click()

        click_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ldc_yes_xpath)))
        click_yes.click()

    def delete_Config_Child(self):
        click_row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_second_row_record_xpath)))
        click_row.click()

        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.leaveconfig_secondrow_delete_xpath)))
        delete.click()

        click_yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ldc_yes_xpath)))
        click_yes.click()


    def close_AddnewLeaveConfig_window(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_btn_xpath)))
        close.click()


# __________________________________Just for testing ignore___________________________________________
# __________________________________Just for testing ignore___________________________________________
# __________________________________Just for testing ignore___________________________________________
    def delete_all_leaveconfigdetails(self):
        delete_elements = self.driver.find_elements(By.XPATH, self.ldc_delete_all_xpath)
        for index in range(1, len(delete_elements)):
            try:
                delete_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.ldc_delete_xpath))
                )
                time.sleep(2)
                delete_button.click()
                click_yes = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.ldc_yes_xpath)))
                click_yes.click()
                time.sleep(2)
                print("Deleted a leave configuration detail.")

                # After each deletion, re-fetch the delete elements as the list might have been updated
                delete_elements = self.driver.find_elements(By.XPATH, "(//button[@mattooltip='Delete'])")

                # Adjust the index to account for the updated list
                index = 2  # Reset to start deleting from the next third element

            except Exception as e:
                print(f"Error occurred while deleting a leave configuration detail: {e}")
                # Break the loop if an exception occurs to avoid infinite looping or stale element issues
                break


    def lateleaveconditionvalue2(self):
        llc_value = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lateleavecond_value_1_xpath)))
        textvalue = llc_value.text
        print(textvalue)
        llc_value.click()
        return textvalue


    def add_another_LeaveconfigDetails(self, no_leaves):
        self.click_add_Child()
        click_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lt_click_xpath)))
        click_lov.click()

        lov_options = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_lov2_xpath)))
        lov_options.click()
        self.select_recurrance()
        self.enter_leaves(no_leaves)
        self.lateleavecondition()
        self.lateleaveconditionvalue2()
        self.save()

# __________________________________Just for testing ignore___________________________________________
# __________________________________Just for testing ignore___________________________________________
# __________________________________Just for testing ignore___________________________________________




