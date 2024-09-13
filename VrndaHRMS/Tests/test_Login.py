import pytest
import allure
import unittest

from allure_commons.types import AttachmentType

from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
#
#
# @allure.severity(allure.severity_level.NORMAL)
@pytest.mark.run(order=1)
class Test_Login(BaseTest):

    @pytest.mark.parametrize("email_address, password",
                             ExcelUtils.get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1"))
    def test_login(self, email_address, password):
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(email_address)
        loginpage.enter_password(password)
        loginpage.custom_sleep(1)

        loginpage.click_login()
        loginpage.custom_sleep(2)
        exp_url = "http://10.11.12.167:5006/#/dashboard/dashboard"
        invalid_users = "User does not exist."
        invalid_creds = "Invalid credentials"
        if loginpage.validate_homescreen() == (exp_url):
            assert True
            loginpage.logout()
        elif loginpage.Invalid() == (invalid_users):
            assert True
        elif loginpage.Invalid() == (invalid_creds):
            assert True
        else:
            # allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            assert False

    # def test_Invalid_cred(self):
    #     loginpage = Loginpage(self.driver)
    #     loginpage.enter_username("Madhusudhan.mothkupally@vrnda.com")
    #     loginpage.enter_password("88011@Madhus")
    #     loginpage.click_login()
    #     assert loginpage.Invalid_cred()
    #
    #
    # def test_Invalid_Account(self):
    #     loginpage = Loginpage(self.driver)
    #     loginpage.enter_username("Madhusudhan@vrnda.com")
    #     loginpage.enter_password("88011@Madhus")
    #     loginpage.click_login()
    #     assert loginpage.Invalid_user()
    #
    # @pytest.mark.parametrize("email_address, password",
    #                          ExcelUtils.get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1"))
    # def test_valid_cred(self, email_address, password):
    #     loginpage = Loginpage(self.driver)
    #     loginpage.enter_username(email_address)
    #     loginpage.enter_password(password)
    #     loginpage.click_login()
    #     loginpage.custom_sleep(3)
    #     print("Logged In successfully")
    #     exp_url = "http://10.11.12.167:5006/#/dashboard/dashboard"
    #     if loginpage.validate_homescreen() == (exp_url):
    #         assert True
    #     else:
    #         assert False
    #     loginpage.logout()

    # def __init__(self):
    #     # self.driver = None
