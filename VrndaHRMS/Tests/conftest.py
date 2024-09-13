import os.path
import time
from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import ReadConfigurations, ExcelUtils
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.Login import Loginpage
from Utilities.ExcelUtils import get_data_from_excel

driver = None

@pytest.fixture(scope="class")
# @pytest.fixture(scope="session")
def setup_and_teardown(request):
    browser = ReadConfigurations.read_config("basic info", "browser")
    global driver
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name from this list Chrome/Firefox/Edge")
    driver.maximize_window()
    web_url = ReadConfigurations.read_config("basic info", "url")
    driver.get(web_url)
    wait = WebDriverWait(driver, timeout=10)

    # # login_username = ReadConfigurations.read_config("login info", "username")
    # # login_password = ReadConfigurations.read_config("login info", "password")
    
    # --------------------------Necessary Login Code-----------------------------------------------------------------
    # excel_data = get_data_from_excel("Excelfiles/Custodial_cred_dev-v5.xlsx", "Sheet1")
    # login_username, login_password = excel_data[0]  # Assuming the first row contains the username and password
    #
    # # Example login steps (replace with your actual login logic)
    # username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='username']")))
    # password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
    # login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//vrnda-button)[1]")))
    #
    # username_field.send_keys(login_username)
    # password_field.send_keys(login_password)
    # login_button.click()
    # --------------------------Necessary Login Code-----------------------------------------------------------------


    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    driver.quit()

    # driver.execute_script("window.open('about:blank', '_blank');")
    # driver.switch_to.window(driver.window_handles[-1])
    # approver_username = ReadConfigurations.read_config("approver info", "username")
    # approver_password = ReadConfigurations.read_config("approver info", "password")
    # web_url = ReadConfigurations.read_config("approver info", "url")
    # driver.get(web_url)
    #
    # username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='username']")))
    # password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
    # login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//vrnda-button)[1]")))
    #
    # username_field.send_keys(approver_username)
    # password_field.send_keys(approver_password)
    # login_button.click()
    #
    # driver.switch_to.window(driver.window_handles[0])
    # driver.quit()

#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://10.11.12.167:5006/#/authentication/signin"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#

