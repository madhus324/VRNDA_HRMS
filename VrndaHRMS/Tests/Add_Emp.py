from PageObjects.Login import Loginpage
from PageObjects.Employees import Employees
from Tests.BaseTest import BaseTest
from PageObjects.Add_Emp import Add_Emp



class Test_Add_Emp(BaseTest):

    def test_emp_det(self):
        loginpage = Loginpage(self.driver)
        loginpage.enter_username("Madhusudhan.mothkupally@vrnda.com")
        loginpage.enter_password("88011@Madhu")
        loginpage.click_login()
        loginpage.custom_sleep(3)
        print("Logged In successfully")
        emp_page = Employees(self.driver)
        emp_page.custom_sleep(3)
        emp_page.goto_emp_details()
        add_emp = Add_Emp(self.driver)
        add_emp.click_add()
        emp_page.custom_sleep(3)
        add_emp.get_window_handle()
        emp_page.custom_sleep(3)
        add_emp.Insert_fname("Sachin")
        emp_page.custom_sleep(3)
        add_emp.Insert_lname("Tendulkar")
        emp_page.custom_sleep(3)
        add_emp.Insert_dob("01/01/1990")
        emp_page.custom_sleep(3)
        add_emp.Insert_father("Father")
        emp_page.custom_sleep(3)
        add_emp.Insert_mother("Mother")


