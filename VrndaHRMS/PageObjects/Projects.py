from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.BasePage import BasePage

class Projects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Projects_Main_xpath = "//span[text()='Projects ']"
    Projects_sub_xpath = "//a[normalize-space()='Projects Teams & Members']"
    Projects_title_xpath = "//h2[normalize-space()='Project Details']"
    Parent_addbtn_xpath = "(//button[@color='primary']//span)[5]"
    ProjectName_xpath = "(.//vrnda-textbox[@labelname='Project Name']/mat-form-field/div/div/div[2]/input)[1]"
    ClientName_xpath = "(.//vrnda-textbox[@labelname='Client Name']/mat-form-field/div/div/div[2]/input)[1]"
    Startdate_xpath = "//input[@id='startDate']"
    Organization_xpath = "(.//vrnda-textbox[@labelname='Organization']/mat-form-field/div/div/div[2]/input)[1]"
    ProjHead_xpath = "(.//vrnda-lov[@labelname='Project Head']/mat-form-field/div/div/div[2]/input)[1]"
    Projhead_lov_xpath = "(// mat-option[@ role='option']//span)[9]"
    nxt_btn_xpath = "//span[normalize-space()='Next']"
    Teamname_xpath = "(.//vrnda-textbox[@labelname='Team Name']/mat-form-field/div/div/div[2]/input)[1]"
    Scrummaster_xpath = "(.//vrnda-lov[@labelname='Scrum Master']/mat-form-field/div/div/div[2]/input)[1]"
    Scrummaster_lov_xpath = "(// mat-option[@ role='option']//span)[9]"
    save_btn_xpath = "//span[text()='Save']"
    toast_message_xpath = "//simple-snack-bar[@class='mat-mdc-simple-snack-bar ng-star-inserted']//div[1]"
    select_row_record_xpath = "(//mat-row[@role='row'])[1]"
    parent_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    click_yes_xpath = "//span[normalize-space()='Yes']"
    AddnewProjectDetails_Title_xpath = "(//h1[normalize-space()='Add New Project rDetails'])[1]"
    select_teams_record_xpath = "(//mat-row[@role='row'])[2]"
    parent_delete_xpath = "(//button[@mattooltip='Delete'])[1]"
    projteam_delete_xpath = "(//button[@mattooltip='Delete'])[2]"
    del_ProjTeam_yes_xpath = "(//span[normalize-space()='Yes'])[1]"
    Clientname_value_xpath = "(//mat-cell[@role='cell'])[3]"
    teammembers_xpath = "(//span[@class='mat-mdc-button-touch-target'])[14]"
    ProjectTeamMembers_xpath = "(//h1[normalize-space()='Project Team Members'])[1]"
    Delete_screummaster_xpath = "(//span[@class='mat-mdc-button-touch-target'])[25]"
    Addbtn_PTM_xpath = "(//span[@class='mat-mdc-button-touch-target'])[20]"
    AddNewProjMembers_Title_xpath = "//h1[normalize-space()='Add New Project Members']"
    Employee_search_xpath = "//mat-icon[text()='search']"
    Emp_Search_Title_xpath = "//h1[normalize-space()='Employee Search']"
    Retrieve_xpath = "//span[text()='Retrieve']"
    Search_field_xpath = "(//input[@placeholder='Search'])[4]"
    Emp_row_select_xpath = ".//employee-search-dialog/vrnda-dialog-title/div/vrnda-dialog-content/mat-dialog-content/div[2]/vrnda-table/div/div/div/div/div/mat-table/mat-row/mat-cell[3]"
    select_btn_xpath = "//span[normalize-space()='Select']"
    RoleName_xpath = "(.//vrnda-lov[@labelname='Role Name']/mat-form-field/div/div/div[2]/input)[1]"
    RoleName_value_xpath = "(//mat-option[@ role='option']//span)[26]"
    Save_ProjMem_xpath = "//span[text()='Save']"
    close_ProjMem_xpath = "//span[normalize-space()='Close']"






    def validate_toastmessage(self):
        toastmessage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.toast_message_xpath)))
        return toastmessage

    def navigate_projects(self):
        self.custom_sleep(2)
        main_proj = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Projects_Main_xpath)))
        main_proj.click()

        sub_proj = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Projects_sub_xpath)))
        sub_proj.click()

    def Add_new_project(self):
        add_parent = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Parent_addbtn_xpath)))
        add_parent.click()

    def AddnewProjectDetails_Title(self):
        current_title = self.driver.find_element(By.XPATH, self.AddnewProjectDetails_Title_xpath).text
        return current_title

    def enter_proj_name(self, Proj_name):
        Projcet_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ProjectName_xpath)))
        Projcet_name.send_keys(Proj_name)

    def enter_client_name(self, Clientname):
        Client_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClientName_xpath)))
        Client_name.send_keys(Clientname)

    def clear_client_name(self):
        Client_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClientName_xpath)))
        Client_name.clear()


    def enter_startdate(self, startdate):
        Start_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Startdate_xpath)))
        Start_date.send_keys(startdate)

    def enter_org(self, Organization):
        organzn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Organization_xpath)))
        organzn.send_keys(Organization)

    def enter_teamname(self, Teamname):
        Team_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Teamname_xpath)))
        Team_name.send_keys(Teamname)

    def select_proj_head(self):
        Projhead = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ProjHead_xpath)))
        Projhead.click()

        self.custom_sleep(2)
        Projhead_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Projhead_lov_xpath)))
        Projhead_lov.click()

    def select_scrummaster(self):
        Scrum_master = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Scrummaster_xpath)))
        Scrum_master.click()

        Scrum_master_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Scrummaster_lov_xpath)))
        Scrum_master_lov.click()

    def click_next(self):
        Next = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.nxt_btn_xpath)))
        Next.click()


    def Delete_Project_Assigned(self):
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_row_record_xpath)))
        row.click()
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_delete_xpath)))
        delete.click()

        yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_appRole_xpath)))
        yes.click()



    def enter_project_details(self, Proj_name, Clientname, startdate, Organization, Teamname):
        Projcet_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ProjectName_xpath)))
        Projcet_name.send_keys(Proj_name)

        Client_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClientName_xpath)))
        Client_name.send_keys(Clientname)

        Start_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Startdate_xpath)))
        Start_date.send_keys(startdate)

        organzn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Organization_xpath)))
        organzn.send_keys(Organization)

        Projhead = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ProjHead_xpath)))
        Projhead.click()

        self.custom_sleep(2)
        Projhead_lov =  WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Projhead_lov_xpath)))
        Projhead_lov.click()

        Next = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.nxt_btn_xpath)))
        Next.click()

        Team_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Teamname_xpath)))
        Team_name.send_keys(Teamname)

        Scrum_master = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Scrummaster_xpath)))
        Scrum_master.click()

        Scrum_master_lov = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Scrummaster_lov_xpath)))
        Scrum_master_lov.click()

    def Project_list(self):
        Projectname_list = []
        try:
            refresh = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[4]")))
            refresh.click()
            self.custom_sleep(2)
            while True:
                leavetype_elements = self.driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[2]")
                for element in leavetype_elements:
                    Projectname_list.append(element.text)
                self.custom_sleep(3)
                refresh_data = self.driver.find_element(By.XPATH, "(//button[@aria-label='Next page'])[1]")
                # self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)
                self.custom_sleep(2)
                try:
                    next_page_btn = self.driver.find_element(By.XPATH, "(//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target'])[1]")
                    next_page_btn.click()
                    self.custom_sleep(2)
                except ElementClickInterceptedException:
                    break

        except Exception as e:
            print("Error retrieving leave types:", e)
            return []
        return Projectname_list

    def click_save(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_btn_xpath)))
        save.click()

    def click_ProjectDetails_Refresh(self):
        refresh = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[4]")))
        refresh.click()

    def delete_projdetails_record(self, searchtext):
        self.click_ProjectDetails_Refresh()
        self.common_parentsearch(searchtext)
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_row_record_xpath)))
        row.click()
        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.parent_delete_xpath)))
        delete.click()

        yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_yes_xpath)))
        yes.click()

    def Delete_Project_Team(self):
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_teams_record_xpath)))
        row.click()

        delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.projteam_delete_xpath)))
        delete.click()

        yes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_yes_xpath)))
        yes.click()

        self.custom_sleep(2)
        delete_team_confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.del_ProjTeam_yes_xpath)))
        delete_team_confirm.click()


    def AddNewProjectTeams(self):
        Team_mem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.teammembers_xpath)))
        Team_mem.click()

    def ProjectTeamMembers_Title(self):
        current_title = self.driver.find_element(By.XPATH, self.ProjectTeamMembers_xpath).text
        return current_title

    def valueofrecord(self):
        self.driver.find_element(By.XPATH, self.select_row_record_xpath).click()
        text_value = self.driver.find_element(By.XPATH, self.Clientname_value_xpath).text
        return text_value

    def Delete_ScrumMaster(self):
        Team_mem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Delete_screummaster_xpath)))
        Team_mem.click()

    def click_Add_PTM(self):
        add_Btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Addbtn_PTM_xpath)))
        add_Btn.click()

    def AddNewProjectTeamMembers_Title(self):
        current_title = self.driver.find_element(By.XPATH, self.AddNewProjMembers_Title_xpath).text
        return current_title

    def click_Emp_Search(self):
        Search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Employee_search_xpath)))
        Search_btn.click()

    def EmployeeSearch_Title(self):
        current_title = self.driver.find_element(By.XPATH, self.Emp_Search_Title_xpath).text
        return current_title

    def Click_Retrieve(self):
        Retrieve_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Retrieve_xpath)))
        Retrieve_btn.click()

    def Search_Emp(self, Emp):
        search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Search_field_xpath)))
        search.send_keys(Emp)

    def Emp_Row_Select(self):
        row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Emp_row_select_xpath)))
        row.click()

    def Click_Select(self):
        select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_btn_xpath)))
        select.click()

    def select_RoleName(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.RoleName_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

        # role.click()
        self.custom_sleep(2)

        Role_value = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.RoleName_value_xpath)))
        Role_value.click()

    def Save_AddNewProjectMembers(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Save_ProjMem_xpath)))
        save.click()

    def Close_ProjectTeamMembers(self):
        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_ProjMem_xpath)))
        close.click()
