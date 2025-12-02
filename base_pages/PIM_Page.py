import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIM_Page:
    # Locators
    btn_PIM_xpath = "//span[text()='PIM']"     #//span[contains(@class,'oxd-main-menu-item--name') and text()='PIM']
    btn_search_xpath = "//button[normalize-space()='Search']"

    btn_add_xpath = "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    textbox_first_name = "firstName"
    textbox_middle_name = "middleName"
    textbox_last_name = "lastName"
    btn_save_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    textbox_license_no_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"

    cal_license_expiry_xpath = "(//input[@class='oxd-input oxd-input--active' and @placeholder='yyyy-dd-mm'])[1]"
    drop_nationality_xpath = "(//div[@class='oxd-select-text-input' and normalize-space()='-- Select --'])[1]"
    country_name = "Pakistani"  # or any country you want
    country_xpath = f"//div[@role='option']//span[normalize-space()='{country_name}']"
    btn_pim_save_xpath = "//button[normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # up to 10 seconds

    def click_PIM(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_PIM_xpath)))
        login_btn.click()

    def click_add(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_add_xpath)))
        login_btn.click()


    def enter_firstname(self, firstname):
        """Enter username/email in the email field"""
        email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_first_name)))
        email_field.clear()
        email_field.send_keys(firstname)

    def enter_middlename(self, middlename):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_middle_name)))
        password_field.clear()
        password_field.send_keys(middlename)

    def enter_lastname(self, lastname):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_last_name)))
        password_field.clear()
        password_field.send_keys(lastname)

    def click_save(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_save_xpath)))
        login_btn.click()

    def enter_drivinglicense_no(self, drivinglicenseno):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_license_no_xpath)))
        password_field.clear()
        password_field.send_keys(drivinglicenseno)

    def select_nationality(self):
        # Click to open dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.drop_nationality_xpath))
        )
        dropdown.click()
        time.sleep(2)

        # Wait for option to be clickable
        nationality_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.country_xpath))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", nationality_option)

        # Click the option
        nationality_option.click()

    def click_pim_save(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_pim_save_xpath)))
        login_btn.click()