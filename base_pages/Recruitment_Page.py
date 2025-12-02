import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Recruitment_Page:
    # Locators
    btn_recruitment_xpath = "//span[text()='Recruitment']"

    btn_add_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    textbox_firstname_xpath = "//input[@name='firstName']"
    textbox_middlename_xpath = "//input[@name='middleName']"
    textbox_lastname_xpath = "//input[@name='lastName']"
    dropdown_vacancy_xpath = "//div[@class='oxd-select-text-input']"
    dropdown_select_vacancy_xpath = "//div[@role='option']/span[text()='Senior QA Lead']"
    textbox_email_xpath = "//input[@class='oxd-input oxd-input--focus oxd-input--error']"
    check_consent_xpath = "//span[contains(@class,'oxd-checkbox-input')]"
    btn_save_xpath = "//button[contains(normalize-space(.), 'Save')]"

    # btn_add_xpath = "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    # textbox_first_name = "firstName"
    # textbox_middle_name = "middleName"
    # textbox_last_name = "lastName"
    # btn_save_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    #
    # textbox_license_no_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"
    #
    # cal_license_expiry_xpath = "(//input[@class='oxd-input oxd-input--active' and @placeholder='yyyy-dd-mm'])[1]"
    # drop_nationality_xpath = "(//div[@class='oxd-select-text-input' and normalize-space()='-- Select --'])[1]"
    # country_name = "Pakistani"  # or any country you want
    # country_xpath = f"//div[@role='option']//span[normalize-space()='{country_name}']"
    # btn_pim_save_xpath = "//button[normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # up to 10 seconds

    def click_recruitment(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_recruitment_xpath)))
        login_btn.click()


    def enter_firstname(self, firstname):
        """Enter username/email in the email field"""
        email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_firstname_xpath)))
        email_field.clear()
        email_field.send_keys(firstname)

    def enter_middlename(self, middlename):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_middlename_xpath)))
        password_field.clear()
        password_field.send_keys(middlename)

    def enter_lastname(self, lastname):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_lastname_xpath)))
        password_field.clear()
        password_field.send_keys(lastname)



    def select_vacancy(self):
        # Click to open dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_vacancy_xpath))
        )
        dropdown.click()
        time.sleep(2)

        # Wait for option to be clickable
        nationality_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_select_vacancy_xpath))
        )

        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", nationality_option)

        # Click the option
        nationality_option.click()

    def enter_email(self, email):
            """Enter password in the password field"""
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_email_xpath)))
            password_field.clear()
            password_field.send_keys(email)


    def click_consent(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.check_consent_xpath)))
        login_btn.click()


    def click_save(self):
        """Click on the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_save_xpath)))
        login_btn.click()