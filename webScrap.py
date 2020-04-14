# https://intellipaat.com/community/16524/take-screenshot-of-full-page-with-selenium-python-with-chromedriver  set up classes
# figure out regex

from selenium import webdriver
import time

# Selenium to automate through web
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://www.worldometers.info/coronavirus/country/us/")
time.sleep(5)


driver.quit()
