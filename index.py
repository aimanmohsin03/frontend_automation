from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk

PATH = '/Users/aimanmohsin/Downloads/chromedriver'
SERVICE = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=SERVICE)
driver.maximize_window()
driver.get('http://localhost:3000/') 

EMAIL = driver.find_element(By.ID, "email")
EMAIL.send_keys('aqsa123@mailinator.com')

PASSWORD = driver.find_element(By.ID, "password")
PASSWORD.send_keys('Haierg30_')

PASSWORD.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "db_btn_Continue"))
    )
    element.click()
    element1 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "first-click"))
    )
    element1.click()
    COPIED_TEXT = Tk().clipboard_get()
    KEYS = COPIED_TEXT[-73:]
    print(KEYS)
    COMMAND_SWCLIENT = "python3 __main__.py " + KEYS
    print(COMMAND_SWCLIENT)

    # EC.presence_of_element_located(By.ID, "second-click")
    # getCurlCopied = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.ID, "second-click"))
    # )
    # getCurlCopied.click()

except:
    driver.quit()


# SIGN_IN_BUTTON = driver.find_element(By.ID, "sign-in-button")
