from PageObjects.Login import Loginpage
from PageObjects.Employees import Employees
from Tests.BaseTest import BaseTest
from PageObjects.Add_Emp import Add_Emp



class Test_goto_Emp(BaseTest):

    def test_emp(self):
        excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
        login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(login_username)
        loginpage.enter_password(login_password)
        loginpage.click_login()
        print("Logged In successfully")
        emp_page = Employees(self.driver)
        emp_page.goto_emp_details()
        if emp_page.validate_addbtn:
            assert True
        else:
            assert False


