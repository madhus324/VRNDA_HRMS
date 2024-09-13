from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.BasePage import BasePage

class Add_Emp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    addbtn_emp_xpath = "(//span[@class='mat-mdc-button-touch-target'])[3]"
    fname_xpath = "//mat-label[text()='Employee First Name']"
    lname_xpath = "//mat-label[text()='Employee Last Name']"
    dob_xpath = "//mat-label[text()='Date of Birth']"
    fathname_xpath = "(//label[contains(@class,'mdc-floating-label mat-mdc-floating-label')]//mat-label)[5]"
    mothname_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/employee-details-form-dialog[1]/vrnda-dialog-title[1]/div[1]/vrnda-dialog-content[1]/mat-dialog-content[1]/form[1]/div[1]/mat-vertical-stepper[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/vrnda-textbox[1]/mat-form-field[1]/div[1]/div[1]/div[2]/input[1]"
    gender_1_xpath = "(//input[@role='combobox'])[1]"
    sel_gen_xpath = "(//mat-option[@role='option'])[1]"
    blo_grp_xpath = "(//input[@role='combobox'])[2]"
    # sel_blo_xpath =

    def click_add(self):
        # self.driver.find_element(By.XPATH, self.addbtn_emp_xpath).click()

        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.addbtn_emp_xpath)))
        add_btn.click()

    def Insert_fname(self, fname):
        # self.element_click("fname_xpath", self.fname_xpath)
        # self.type_into_element(fname, "fname_xpath", self.fname_xpath)

        firstname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.fname_xpath)))
        firstname.click()
        firstname.clear()
        firstname.send_keys(fname)


    def Insert_lname(self, lname):
        # self.type_into_element(lname, "lname_xpath", self.lname_xpath)

        lastname = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lname_xpath)))
        lastname.click()
        lastname.clear()
        lastname.send_keys(lastname)

    def Insert_dob(self, DOB):
        # self.type_into_element(DOB, "dob_xpath", self.dob_xpath)


        dateofbirth = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dob_xpath)))
        dateofbirth.click()
        dateofbirth.clear()
        dateofbirth.send_keys(DOB)

    def Insert_father(self, fathername):
        # self.type_into_element(father, "fathname_xpath", self.fathname_xpath)

        father = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.fathname_xpath)))
        father.click()
        father.clear()
        father.send_keys(fathername)

    def Insert_mother(self, mothername):
        # self.type_into_element(mother, "mothname_xpath", self.mothname_xpath)

        mother = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.mothname_xpath)))
        mother.click()
        mother.clear()
        mother.send_keys(mothername)

    def select_gender(self):
        self.element_click("gender_1_xpath", self.gender_1_xpath)
        self.custom_sleep(3)
        dropdown = self.driver.find_element(By.XPATH, self.gender_1_xpath)
        dd = Select(dropdown)
        dd.select_by_visible_text("B Positive")

    def get_window_handle(self):
        new_window_timeout = 10
        new_window = WebDriverWait(self.driver, new_window_timeout).until(EC.new_window_is_opened)

        # Switch to the new window
        all_windows = driver.window_handles
        new_window_handle = [window for window in all_windows if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window_handle)