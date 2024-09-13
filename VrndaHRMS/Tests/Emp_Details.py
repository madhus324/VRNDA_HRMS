import time

import pytest

from PageObjects.App_Roles import AppRoles
from PageObjects.Employees import Employees
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class Test_EmployeeDetails(BaseTest):

    def test_validate_emp_details_screen(self):
        Emp = Employees(self.driver)
        Emp.goto_emp_details()
        # Emp.title()
        Exp_title = "Employee Details"
        if Emp.title() == (Exp_title):
            assert True
            print("Passed : Expected Title matches Actual Title of the page and verified successfully")
        else:
            print("Failed : Expected Title doesnot matches Actual Title of the page and verified successfully")
            assert False

