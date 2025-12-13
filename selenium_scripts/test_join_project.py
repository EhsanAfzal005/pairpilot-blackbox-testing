from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

try:
    join_tab_button = driver.find_element(By.XPATH, "//button[contains(text(),'Join Project')]")
    join_tab_button.click()
    time.sleep(2)
except:
    print("Join Project section already visible or no separate tab/button.")

join_project_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.project-id-input"))
)

test_project_id = "b845b172-7ff9-4e5f-8de2-ead98eba24f8" 
join_project_input.send_keys(test_project_id)

driver.save_screenshot("join_project_before_submit.png")
print("Screenshot saved BEFORE Join Project.")

join_project_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Join Project')]")
join_project_button.click()

time.sleep(5)

driver.save_screenshot("join_project_after_submit.png")
print("Screenshot saved AFTER Join Project.")

input("Press Enter to close...")

driver.quit()
