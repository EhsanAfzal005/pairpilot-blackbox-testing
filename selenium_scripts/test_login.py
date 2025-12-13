from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost:3000/login") 
driver.maximize_window()
time.sleep(2)

email_field = driver.find_element(By.XPATH, "//input[@type='email']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

email_field.send_keys("testuser1@example.com")
password_field.send_keys("password123")

driver.save_screenshot("login_before_submit.png")
print("Screenshot 'login_before_submit.png' saved.")

sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

time.sleep(3)

driver.save_screenshot("login_after_submit.png")
print("Screenshot 'login_after_submit.png' saved.")

input("Press Enter to close...")

driver.quit()
