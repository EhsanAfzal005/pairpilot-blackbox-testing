from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost:3000/register")
time.sleep(2)

email_field = driver.find_element(By.XPATH, "//input[@type='email']")
name_field = driver.find_element(By.XPATH, "//input[@type='text']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

email_field.send_keys("testrameez@example.com")
name_field.send_keys("Testing Rameez")
password_field.send_keys("password123")

driver.save_screenshot("before_submit.png")
print("Screenshot 'before_submit.png' saved.")

sign_up_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_up_button.click()

time.sleep(3)

driver.save_screenshot("after_submit.png")
print("Screenshot 'after_submit.png' saved.")

input("Press Enter to close...")

driver.quit()
