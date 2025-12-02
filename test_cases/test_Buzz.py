import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_Page
from base_pages.Buzz_Page import Buzz_Page
from utilities.read_properties import Read_Config


class Test_Add_Buzz:
    page_url = "https://opensource-demo.orangehrmlive.com/"
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_username()

    post = "this is a test post"

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_post(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_pg = Login_Page(self.driver)
        self.login_pg.enter_username(self.username)
        self.login_pg.enter_password(self.password)
        self.login_pg.click_login()
        time.sleep(5)
        self.buzz_pg = Buzz_Page(self.driver)
        self.buzz_pg.click_Buzz()
        self.buzz_pg.enter_Post(self.post)
        self.buzz_pg.save_post()


