import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:
    # Locators
    textbox_username_xpath = "//input[@placeholder='Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[normalize-space()='Login']"
    btn_logout_xpath = "//span[@class='oxd-userdropdown-tab']"
    btn_logout_link_xpath = "//*[@class='oxd-userdropdown-tab']"
    select_logout_option_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # up to 10 seconds

    def enter_username(self, username):
        """Enter username/email in the email field"""
        email_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        email_field.clear()
        email_field.send_keys(username)

    def enter_password(self, password):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath)))
        login_btn.click()

    def log_out(self):
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_logout_link_xpath)))
        logout_btn.click()
        time.sleep(5)
        # Wait for the 'Logout' option to appear and click it
        logout_option = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.select_logout_option_link_text)))
        logout_option.click()
