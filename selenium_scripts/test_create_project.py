from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://localhost:3000/login")
time.sleep(2)

email_field = driver.find_element(By.XPATH, "//input[@type='email']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
email_field.send_keys("testuser1@example.com")
password_field.send_keys("password123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5) 

create_project_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create Project')]"))
)
create_project_button.click()

project_name_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
)
description_field = driver.find_element(By.CSS_SELECTOR, "textarea")

project_name_field.send_keys("Test Project Selenium")
description_field.send_keys("This is a Selenium automated test project.")

driver.save_screenshot("create_project_before_submit.png")
print("Screenshot saved BEFORE submit.")

create_button = driver.find_element(By.XPATH, "//button[@type='submit']")
create_button.click()

time.sleep(5)

driver.save_screenshot("create_project_after_submit.png")
print("Screenshot saved AFTER submit.")

input("Press Enter to close...")

driver.quit()
