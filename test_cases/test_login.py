import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Page import Login_Page
from utilities.read_properties import Read_Config


class Test_Login:
    page_url = "https://opensource-demo.orangehrmlive.com/"
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_username()

    @pytest.mark.regression
    def test_title_verificaion(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            assert True

            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verificaion.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_pg = Login_Page(self.driver)
        self.login_pg.enter_username(self.username)
        self.login_pg.enter_password(self.invalid_password)
        self.login_pg.click_login()
        time.sleep(5)

        act_dashboard_text = self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        if act_dashboard_text == "Invalid credentials":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_valid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_pg = Login_Page(self.driver)
        self.login_pg.enter_username(self.username)
        self.login_pg.enter_password(self.password)
        self.login_pg.click_login()
        time.sleep(5)

        act_dashboard_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False



