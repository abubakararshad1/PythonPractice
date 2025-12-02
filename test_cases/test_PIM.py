import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_Page
from base_pages.PIM_Page import PIM_Page
from utilities.read_properties import Read_Config


class Test_Add_Employee:
    page_url = "https://opensource-demo.orangehrmlive.com/"
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_username()
    firstname = "abubakar"
    middlename = "Arshad"
    lastname = "Mahmood"
    drivinglicense = "12345"
    licenseexpiry = "2015-14-11"

    @pytest.mark.sanity
    def test_add_employee(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_pg = Login_Page(self.driver)
        self.login_pg.enter_username(self.username)
        self.login_pg.enter_password(self.password)
        self.login_pg.click_login()
        time.sleep(5)
        self.pim_pg = PIM_Page(self.driver)
        self.pim_pg.click_PIM()
        self.pim_pg.click_add()
        self.pim_pg.enter_firstname(self.firstname)
        self.pim_pg.enter_middlename(self.middlename)
        self.pim_pg.enter_lastname(self.lastname)
        self.pim_pg.click_save()
        time.sleep(15)
        self.pim_pg.enter_drivinglicense_no(self.drivinglicense)
        self.pim_pg.select_nationality()
        time.sleep(15)
        self.pim_pg.click_pim_save()
        time.sleep(4)

    #     act_dashboard_text = self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
    #     if act_dashboard_text == "Invalid credentials":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
    #         self.driver.close()
    #         assert False
    #
    #
    #
    # def test_valid_admin_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.page_url)
    #     self.login_pg = Login_Page(self.driver)
    #     self.login_pg.enter_username(self.username)
    #     self.login_pg.enter_password(self.password)
    #     self.login_pg.click_login()
    #     time.sleep(5)
    #
    #     act_dashboard_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    #     if act_dashboard_text == "Dashboard":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
    #         self.driver.close()
    #         assert False
    #


