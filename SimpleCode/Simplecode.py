import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.implicitly_wait(3)
driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://opensource-demo.orangehrmlive.com/")

textbox_username_xpath = "//input[@placeholder='Username']"
textbox_password_xpath = "//input[@placeholder='Password']"
btn_login_xpath = "//button[normalize-space()='Login']"
btn_logout_link_xpath = "//*[@class='oxd-userdropdown-tab']"

textbox_first_name = "firstName"
textbox_middle_name = "middleName"
textbox_last_name = "lastName"
btn_save_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

textbox_license_no_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"


driver.find_element(By.XPATH, textbox_username_xpath).send_keys("Admin")
driver.find_element(By.XPATH, textbox_password_xpath).send_keys("admin123")
driver.find_element(By.XPATH, btn_login_xpath).click()
# driver.find_element(By.LINK_TEXT, select_logout_option_link_text).click()

#click PIM
driver.find_element(By.XPATH, "//span[text()='PIM']").click()
time.sleep(5)

driver.find_element(By.NAME, textbox_first_name).send_keys("abubakar")
driver.find_element(By.NAME, textbox_last_name).send_keys("arshad")
driver.find_element(By.XPATH, btn_save_xpath).click()
driver.find_element(By.XPATH, textbox_license_no_xpath).send_keys("12344")
time.sleep(10)