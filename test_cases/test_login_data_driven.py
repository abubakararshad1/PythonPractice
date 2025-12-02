import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import excel_utils
from base_pages.Login_Page import Login_Page
from utilities.read_properties import Read_Config


class Test_Login_Data_driven:
    page_url = "https://opensource-demo.orangehrmlive.com/"
    # username = Read_Config.get_username()
    # password = Read_Config.get_password()
    # invalid_password = Read_Config.get_invalid_username()
    path = ".//test_data//login_data.xlsx"
    status_list = []


    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.page_url)
        self.login_pg = Login_Page(self.driver)

        self.rows = excel_utils.get_row_count(".//test_data//login_data.xlsx", "Sheet1")
        print("no of rows:", self.rows)

        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            time.sleep(5)
            self.login_pg.enter_username(self.username)
            self.login_pg.enter_password(self.password)
            self.login_pg.click_login()
            time.sleep(5)
            act_title = self.driver.title
            print("Act title:", act_title)

            exp_title = "OrangeHRM"
            print("Expected title:", exp_title)
            if act_title == exp_title:

                if self.exp_login == "Yes":
                    print("Test data is passed")
                    self.status_list.append("Pass")
                    excel_utils.write_data(self.path, "Sheet1", r, 4, "Passed")
                    excel_utils.fill_green(self.path, "Sheet1", r, 4)

                    self.login_pg.log_out()
                    time.sleep(2)
                elif self.exp_login == "No":
                    print("Test data is failed")
                    self.status_list.append("Fail")
                    excel_utils.write_data(self.path, "Sheet1", r, 4, "Failed")
                    excel_utils.fill_red(self.path, "Sheet1", r, 4)
                    time.sleep(2)


            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.status_list.append("Fail")
                    time.sleep(2)
                    excel_utils.write_data(self.path, "Sheet1", r, 4, "Failed")
                    excel_utils.fill_red(self.path, "Sheet1", r, 4)
                    # self.login_pg.log_out()

                elif self.exp_login == "No":
                    self.status_list.append("Pass")
                    excel_utils.write_data(self.path, "Sheet1", r, 4, "Passed")
                    excel_utils.fill_green(self.path, "Sheet1", r, 4)
                    time.sleep(2)

        print("Status list is:", self.status_list)
        if "Fail" in self.status_list:
            assert False
        else:
            assert True


