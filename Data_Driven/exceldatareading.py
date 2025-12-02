import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import excel_utils

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)

file = "C:\\Users\\Abubakar.Arshad\\PycharmProjects\\Python Practice\\Data_Driven\\Excel_Reading_Data.xlsx"
workbook = openpyxl.load_workbook(file)

row = excel_utils.get_row_count(file, "Sheet2")

for r in range(2, row + 1):
    username = excel_utils.read_data(file, "Sheet2", r, 1)
    password = excel_utils.read_data(file, "Sheet2", r, 2)

    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")

    # Clear existing text and enter new credentials
    username_field.clear()
    username_field.send_keys(username)

    password_field.clear()
    password_field.send_keys(password)

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Check for login messages safely
    try:
        login_fail_msg = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
    except:
        login_fail_msg = None
    try:
        time.sleep(5)
        login_success_msg = driver.find_element(By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']").text
        print("Login success message:", login_success_msg)
    except:
        login_success_msg = None

    # Print login result
    if login_fail_msg == "Invalid credentials":
        print(f"{username}: Invalid login - Fail")
        excel_utils.write_data(file,"Sheet2", r, 3, "Failed")
        excel_utils.fill_red(file,"Sheet2", r, 3)

    elif login_success_msg == "Dashboard":
        print(f"{username}: Valid login credentials")
        excel_utils.write_data(file, "Sheet2", r, 3, "Passed")
        excel_utils.fill_green(file, "Sheet2", r, 3)
    else:
        print(f"{username}: Unknown login status")

    time.sleep(5)