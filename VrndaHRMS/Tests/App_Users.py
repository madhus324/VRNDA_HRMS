import pytest

from PageObjects.App_Roles import AppRoles
from PageObjects.App_Users import AppUsers
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class Test_AppUsers(BaseTest):

    def test_appusers(self):
        loginpage = Loginpage(self.driver)
        loginpage.custom_sleep(5)
        loginpage.enter_username("Madhusudhan.mothkupally@vrnda.com")
        loginpage.custom_sleep(3)
        loginpage.enter_password("88011@Madhu")
        loginpage.custom_sleep(3)
        loginpage.click_login()
        loginpage.custom_sleep(3)
        print("Logged In successfully")
        appusers = AppUsers(self.driver)
        appusers.navigate_appusers()
        loginpage.custom_sleep(3)
        # appusers.click_add()
        # loginpage.custom_sleep(5)
        # appusers.select_emp()
        loginpage.custom_sleep(3)
        appusers.Emp_list()









