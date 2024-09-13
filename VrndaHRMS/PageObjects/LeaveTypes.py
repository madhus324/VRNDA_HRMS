from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller

from PageObjects.BasePage import BasePage

class LeaveTypes(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Admin_Screen_xpath = "(//span[@class='hide-menu'])[2]"
    Leave_config_xpath = "//a[@class='ml-sub-menu'][normalize-space()='Leave Configurations']"
    Leave_types_xpath = "(//a[normalize-space()='Leave Types'])[1]"
    addbtn_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    ltcode_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/leave-types-form-dialog[1]/vrnda-dialog-title[1]/div[1]/vrnda-dialog-content[1]/mat-dialog-content[1]/form[1]/div[1]/div[1]/vrnda-textbox[1]/mat-form-field[1]/div[1]/div[1]/div[2]/input[1]"
    ltdescription = ".//vrnda-textbox[@labelname='Leave Type Description']/mat-form-field/div/div/div[2]/input"
    max_leaves_allow_xpath = ".//vrnda-amount[@labelname='Maximum leaves allowed']/mat-form-field/div/div/div[2]/input"
    click_save_xpath = "(//button[@type='submit'])[1]"
    refresh_xpath = "(//span[@class='mat-mdc-button-touch-target'])[4]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    del_btn_xpath = "//button[@mattooltip='Delete']"
    # popup_yes_xpath = "(//button[@color='primary'])[3]"
    popup_yes_xpath = ".//div[@align='end']/button[1]"
    addnewleavetype_title_xpath = "(//h1[normalize-space()='Add New Leave Type'])[1]"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"
    lt_desc_xpath = "(//mat-cell[@role='cell'])[3]"
    searchbar_xpath = "(//input[@type='text'])[1]"
    selectedrecord_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    carrytillYearEnd_checkbox_xpath = "(//div[@class='ng-star-inserted']//span)[1]"
    carrytillYearEnd_xpath = "(//input[@role='combobox'])[1]"
    carrytillYearEnd_value_xpath = "(//mat-option[@role='option'])[1]"
    edit_action_xpath = "(//span[@class='mat-mdc-button-touch-target'])[7]"
    UpdateLeaveType_title_xpath = "//h1[text()='Update Leave Type']"
    close_btn_xpath = "(//span[normalize-space()='Close'])[1]"


    def navigate_leave_config_menu(self):
        admin_screen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Admin_Screen_xpath)))
        admin_screen.click()

        leave_config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_config_xpath)))
        leave_config.click()

    def navigate_leavetype(self):
        leave_types = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Leave_types_xpath)))
        leave_types.click()

    def validate_popupscreentitle(self):
        current_title = self.driver.find_element(By.XPATH, self.addnewleavetype_title_xpath).text
        return current_title

    def click_add(self):
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_xpath)))
        add_btn.click()

    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    def valueofrecord(self):
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()
        text_value = self.driver.find_element(By.XPATH, self.lt_desc_xpath).text
        return text_value

    def search_parentrecord(self, search_text):
        p_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.searchbar_xpath)))
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
            EC.element_to_be_clickable((By.XPATH, self.searchbar_xpath)))
        p_search.click()
        p_search.clear()


    def delete_config_lt_record(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.selectedrecord_delete_xpath)))
        delete.click()


    def Leavetype_list(self):
        leavetype_list = []
        try:
            refresh = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.refresh_xpath)))
            refresh.click()
            self.custom_sleep(3)
            while True:
                leavetype_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[2]")
                for element in leavetype_elements:
                    leavetype_list.append(element.text)
                # print(leavetype_list)
                self.custom_sleep(3)
                refresh_data = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']")
                self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)
                self.custom_sleep(2)
                try:
                    next_page_btn = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']")
                    next_page_btn.click()
                    self.custom_sleep(2)
                except ElementClickInterceptedException:
                    break

        except Exception as e:
            print("Error retrieving leave types:", e)
            # Handle the error, such as returning an empty list or raising an exception
            return []
        # print(leavetype_list)
        return leavetype_list


    def after_Leavetype_list(self):
        after_leavetype_list = []
        self.custom_sleep(3)
        self.driver.find_element(By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[4]").click()
        self.custom_sleep(3)
        while True:

            leavetype_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[2]")
            # self.custom_sleep(3)
            for element in leavetype_elements:
                after_leavetype_list.append(element.text)

            # print(after_leavetype_list)
            self.custom_sleep(3)
            refresh_data = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']")
            self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)
            self.custom_sleep(2)

            try:
                next_page_btn = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']")

                next_page_btn.click()
                self.custom_sleep(2)
            except ElementClickInterceptedException:
                break
        print(after_leavetype_list)
        return after_leavetype_list

    def compare_lists(self, Leavetype_list, after_leavetype_list):
        if Leavetype_list is None:
            print("Leavetype_list is None.")
            return
        if after_leavetype_list is None:
            print("after_leavetype_list is None.")
            return

        if len(Leavetype_list) > len(after_leavetype_list):
            print("Leavetype_list has more elements than after_leavetype_list.")
        elif len(Leavetype_list) < len(after_leavetype_list):
            print("after_leavetype_list has more elements than Leavetype_list.")
        else:
            print("Leavetype_list and after_leavetype_list have the same number of elements.")


    def Enter_Leavetype_code(self, code):
        add_lt = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ltcode_xpath)))
        add_lt.send_keys(code)

    def Enter_Leavetype_description(self, description):
        lt_des = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ltdescription)))
        lt_des.send_keys(description)

    def Enter_max_Leaves(self, max_leaves):
        leaves_allowed = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.max_leaves_allow_xpath)))
        leaves_allowed.click()
        leaves_allowed.clear()
        keyboard = Controller()
        leaves_allowed.send_keys(Keys.CONTROL + "a")
        leaves_allowed.send_keys(Keys.DELETE)
        leaves_allowed.send_keys(max_leaves)

    def select_carrytillYearEnd(self):
        ctye = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.carrytillYearEnd_xpath)))
        ctye.click()

    def select_carrytillYearEnd_value(self):
        ctye_value = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.carrytillYearEnd_value_xpath)))
        ctye_value.click()

    def click_save(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_save_xpath)))
        save.click()

    def Edit_record(self, search_text):
        refresh = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.refresh_xpath)))
        refresh.click()
        self.common_parentsearch(search_text)
        click_edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_action_xpath)))
        click_edit.click()

    def validate_UpdateLeaveTypeTile(self):
        current_title = self.driver.find_element(By.XPATH, self.UpdateLeaveType_title_xpath).text
        return current_title

    def delete_record(self, search_text):
        self.common_parentsearch(search_text)
        del_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_btn_xpath)))
        del_btn.click()
        self.custom_sleep(2)
        yes_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_yes_xpath)))
        yes_btn.click()
        print("selected record deleted successfully")

    def close_AddnewLeavetype_window(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_btn_xpath)))
        close.click()



