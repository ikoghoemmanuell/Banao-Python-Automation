from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Initialize the WebDriver 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Check HTTP response code and log response time
    url = "https://atg.party"
    start_time = time.time()
    response = requests.get(url)
    response_time = time.time() - start_time
    
    if response.status_code == 200:
        print(f"HTTP response code: {response.status_code}")
        print(f"Response time: {response_time} seconds")
    else:
        print(f"Failed to load the page, HTTP response code: {response.status_code}")
        driver.quit()
        exit()



    # Open the website
    driver.get(url)

    # Click on  login
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "login-link")))
    login_button = driver.find_element(By.CLASS_NAME, "login-link") 
    login_button.click()

    # Enter email and password
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "email_landing"))) 
    email_input = driver.find_element(By.ID, "email_landing")
    password_input = driver.find_element(By.ID, "password_landing")
    
    email_input.send_keys("wiz_saurabh@rediffmail.com")
    password_input.send_keys("Pass@123")
    
    # # Submit the login form
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)



    # Navigate to the article posting page
    driver.get("https://atg.party/article")

    # # Fill in the title and description
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "title")))
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("Test Article Title")

    description_input = driver.find_element(By.CLASS_NAME, "ce-paragraph")
    description_input.click()
    description_input.send_keys("This is a test article description.")
    description_input.click()
    time.sleep(5)

    # add image
    plus_sign = driver.find_element(By.CLASS_NAME, "ce-toolbar__plus")
    plus_sign.click()
    time.sleep(5)
    description_input = driver.find_element(By.XPATH, "//div[@class='ce-popover-item__title' and text()='Image']")
    description_input.click()
    time.sleep(5)
    # # Type "profile-pic (9)compressed"
    import pyautogui
    pyautogui.typewrite(r"C:\Users\LENOVO\Pictures\profile pics\me")
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(10)

    # post
    post_button = driver.find_element(By.ID, "hpost_btn")
    post_button.click()
    time.sleep(10)

    new_page_url = driver.current_url
    print(f"New article posted at: {new_page_url}")

finally:
    driver.quit()


