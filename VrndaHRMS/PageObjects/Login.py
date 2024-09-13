from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.BasePage import BasePage

class Loginpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_xpath = "//input[@formcontrolname='username']"
    passwrd_xpath = "//input[@formcontrolname='password']"
    Click_login_xpath = "(//vrnda-button)[1]"
    Invalid_xpath = "//div[contains(@class,'alert alert-danger')]"
    invalid_cred_xpath = "//div[text()='Invalid credentials']"
    invalid_user_xpath = "//div[text()='User does not exist.']"
    Dashboard_xpath = "(//span[normalize-space()='Dashboard'])[1]"
    profile_xpath = "//div[@class='cdk-overlay-container']"



    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username_xpath)))
        self.driver.execute_script("arguments[0].value = '';", username_field)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.passwrd_xpath)))
        self.driver.execute_script("arguments[0].value = '';", password_field)
        password_field.send_keys(password)

    def click_login(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Click_login_xpath)))
        login_btn.click()

    def Invalid(self):
        invalid_user = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Invalid_xpath))).text
        return invalid_user

    def Invalid_user(self):
        invalid_user = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.invalid_user_xpath))).text
        return invalid_user
    
    def Invalid_cred(self):
        invalid_cred = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.invalid_cred_xpath))).text
        return invalid_cred

    def validate_homescreen(self):
        current_url = self.driver.current_url
        return current_url



