from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager


username = ""
password = ""
message = ""

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.linkedin.com/login/'

driver.get(url)

username_input = driver.find_element(By.ID, ("username"))
password_input = driver.find_element(By.ID, ("password"))

username_input.send_keys(username)
password_input.send_keys(password)

sign_in_btn = driver.find_element(By.XPATH, ("//*[@id='organic-div']/form/div[3]/button"))
sign_in_btn.click()

mynetwork_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ("#global-nav > div > nav > ul > li:nth-child(2)")))
    )

mynetwork_link.click()

contacts_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ("section.mn-community-summary > div > div:nth-child(2)")))
    )

contacts_link.click()

contacts_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, ("mn-connection-card__name")))
    )

message_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, ("mn-connection-card__action-container")))
    )

message_buttons = driver.find_elements(By.CLASS_NAME, ("mn-connection-card__action-container"))

for message_button in message_buttons:
    message_button.click()
    time.sleep(1)
    message_box = driver.find_element(By.CLASS_NAME, ("msg-form__contenteditable"))
    message_box.send_keys(message, Keys.CONTROL, Keys.ENTER)
    
    time.sleep(2)
    
    close_friend_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, ("msg-convo-wrapper")))
    )
    
    close_friend_tab = close_friend_tab.find_elements(By.CLASS_NAME, ("msg-overlay-bubble-header__control"))
    
    close_friend_tab[-1].click()
    
    time.sleep(1)

time.sleep(2)
