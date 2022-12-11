from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk
import time

PATH = '/Users/aimanmohsin/Downloads/chromedriver'
SERVICE = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=SERVICE)
driver.maximize_window()
driver.get('https://app.dbtune.ai/') 

EMAIL = driver.find_element(By.ID, "email")
EMAIL.send_keys('mumair5393@gmail.com')

PASSWORD = driver.find_element(By.ID, "password")
PASSWORD.send_keys('51478gameon')

PASSWORD.send_keys(Keys.RETURN)
time.sleep(10)
driver.get('https://app.dbtune.ai/start-tuning-database')

try:
    time.sleep(5)
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

except:
    driver.quit()


# SIGN_IN_BUTTON = driver.find_element(By.ID, "sign-in-button")
