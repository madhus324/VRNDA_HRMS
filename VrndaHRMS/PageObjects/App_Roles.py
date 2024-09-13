from pynput import keyboard
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppRoles(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Admin_Screen_xpath = "(//span[@class='hide-menu'])[2]"
    App_roles_xpath = "//a[@href='#/admin/application-roles-users/application-roles']"
    App_roles_users_linktext = "Application Roles & Users"
    page_title_Xpath = "//h4[@class='page-title']"
    add_btn_xpath = "(//span[@class='mat-ripple mat-mdc-button-ripple']/following-sibling::span)[3]"
    name_xpath = ".//vrnda-textbox[@labelname='Name']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    self_xpath = "//span[normalize-space()='Self']"
    projects_xpath = "(//a[@class='ml-menu'][normalize-space()='Projects'])[1]"
    profile_xpath = "//a[normalize-space()='Profile']"
    deprtmt_xpath = "//p[normalize-space()='Information Technology']"
    description_xpath = ".//vrnda-textbox[@labelname='Description']/mat-form-field[@appearance='outline']/div/div/div[2]/input"
    save_btn_xpath = "//span[text()='Save']"
    # rolename_xpath = "//mat-cell[normalize-space()='']"
    # role_xpath = "(//div[@role="button"])[1]"
    role_xpath = "//mat-cell[text()='HRMS_ADMIN']"
    refresh_xpath = "(//span[@class='mat-mdc-button-touch-target'])[4]"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    parent_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    # privileges_xpath = "(//button[contains(@class,'mat-mdc-tooltip-trigger tbl-action-btn')]//span)[4]"
    privileges_xpath = "//mat-row[2]//mat-cell[6]//button[1]//span[4]"
    # privileges_xpath = "html[1]/body[1]/app-root[1]/app-main-layout[1]/div[1]/application-roles[1]/section[1]/div[1]/vrnda-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mat-table[1]/mat-row[1]/mat-cell[6]/button[1]/span[2]"
    Full_access_xpath = "(//label[text()='Full Access'])"
    No_access_xpath = "(//label[text()='No Access'])[1]"
    edit_record_xpath = "(//span[@class='mat-mdc-button-touch-target'])[8]"
    AddNewAppRole_xpath = "(//h1[normalize-space()='Add New Application Role'])[1]"
    config_lov_xpath = "(//input[@role='combobox'])[2]"
    config_lov_no_xpath = "(//mat-option[@role='option']//span)[2]"
    config_lov_yes_xpath = "(//mat-option[@role='option']//span)[1]"
    remove_config_yes_xpath = "//span[text()='Yes']"
    close_AddnewAppRole_xpath = "(//span[normalize-space()='Close'])[1]"
    del_appRole_xpath = "(//span[normalize-space()='Yes'])[1]"



    def navigate_app_roles(self):

        admin_screen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Admin_Screen_xpath)))
        admin_screen.click()

        App_roles_users = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.App_roles_users_linktext)))
        App_roles_users.click()

        App_roles = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.App_roles_xpath)))
        App_roles.click()


    def title(self):
        current_title = self.driver.find_element(By.XPATH, self.page_title_Xpath).text
        return current_title


    def AddNewAppRole_Title(self):
        Popup_title = self.driver.find_element(By.XPATH, self.AddNewAppRole_xpath).text
        return Popup_title


    def navigate_profile(self):
        Self = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.self_xpathh)))
        Self.click()

        self.scroll_down()

        profile = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile.click()

    def scroll_down(self):
        refresh_data = self.driver.find_element(By.XPATH, self.projects_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)

    def click_add(self):

        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_btn_xpath)))
        add_btn.click()

    def enter_name(self, Name):
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.name_xpath)))
        name.click()
        name.clear()
        name.send_keys(Name)


    def enter_description(self, description):
        desc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.description_xpath)))
        desc.click()
        desc.clear()
        desc.send_keys(description)


    def click_save(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_btn_xpath)))
        save_btn.click()


    def Rolename_list(self):
        Role_list = []
        try:
            refresh = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.refresh_xpath)))
            refresh.click()
            self.custom_sleep(3)
            while True:
                role_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[2]")
                for element in role_elements:
                    Role_list.append(element.text)
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
        # print(Role_list)
        return Role_list

    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    def scroll_up(self):
        self.custom_sleep(2)
        try:
            self.driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
            time.sleep(2)
        except Exception as e:
            print(f"Method 1 failed: {e}")
        # self.driver.execute_script("window.scrollBy(203.28, 60)")
        # refresh_data = self.driver.find_element(By.XPATH, "//li[text()='Application Roles']")
        # self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)

    def Delete_Config_record(self, searchtext):
        self.common_parentsearch(searchtext)
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_row_record_xpath)))
        row.click()
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_delete_xpath)))
        delete.click()

    def Delete_Application_Role(self, searchtext):
        self.common_parentsearch(searchtext)
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_row_record_xpath)))
        row.click()
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_delete_xpath)))
        delete.click()

        yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_appRole_xpath)))
        yes.click()


    def Edit_record(self):
        # self.common_parentsearch(searchtext)
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_row_record_xpath)))
        row.click()

        edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_record_xpath)))
        edit.click()

    def Change_Config(self):

        config = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_lov_xpath)))
        config.click()

        config_value = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.config_lov_no_xpath)))
        config_value.click()

    def Remove_Config(self):
        Remove = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.remove_config_yes_xpath)))
        Remove.click()

    def close_AddnewAppRole(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_AddnewAppRole_xpath)))
        close.click()



    def access_privileges(self):
        Privileges = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.privileges_xpath)))
        Privileges.click()
        self.custom_sleep(2)
        # access_radio_buttons = self.driver.find_elements(By.XPATH, self.Full_access_xpath)  # Adjust the XPath as needed
        # for radio_button in access_radio_buttons:
        #     if not radio_button.is_selected():
        #         radio_button.click()




    # def verify_record(self):
        # elements = self.driver.find_elements(By.XPATH, self.rolename_xpath)
        # print(elements)
        # if "DEV" in elements:
        #     print("Records has saved")
        # else:
        #     print("No Record is avaiable")


    # def is_new_record_added(self, new_record_data):
    #     try:
    #         # Wait for the new record to appear in the grid
    #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
    #             (By.XPATH, f"//table[@id='{self.grid_table_id}']//td[text()='{new_record_data}']")))
    #         return True
    #     except TimeoutException:
    #         return False
