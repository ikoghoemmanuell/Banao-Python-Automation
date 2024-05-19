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
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "login-link")))
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

    # # Click on create
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "create-btn-dropdown")))
    # create_button = driver.find_element(By.ID, "create-btn-dropdown") 
    # create_button.click()
    # # Click on article
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "create-btn-dropdown")))
    # article_button = driver.find_element(By.ID, "create-btn-dropdown") 
    # article_button.click()

    # # Fill in the title and description
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "title")))
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("Test Article Title")

    description_input = driver.find_element(By.CLASS_NAME, "ce-paragraph")
    description_input.click()
    description_input.send_keys("This is a test article description.")
    time.sleep(10)

    # # Upload a cover image
    # image_upload = driver.find_element(By.NAME, "cover_image")
    # image_upload.send_keys("C:/Users/LENOVO/Pictures/profile pics/profile-pic (9)compressed.jpg")

    # # Click on POST
    # post_button = driver.find_element(By.XPATH, "//button[contains(text(), 'POST')]")ce-toolbar__plus
    # post_button.click()

    # # Log the URL of the new page after posting
    # WebDriverWait(driver, 10).until(
    #     EC.url_changes("https://atg.party/article")
    # )
    # new_page_url = driver.current_url
    # print(f"New article posted at: {new_page_url}")

finally:
    driver.quit()
