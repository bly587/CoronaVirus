
from selenium import webdriver
import time
import webScrap

# Selenium to automate through web
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



state = input("Input your state: ").capitalize()
email = input("Enter your email: ")
email_body_string = webScrap.getData(state)

# Selenium step by step to send an email through gmail
# First it logs in then clicks all the necessary buttons and writes in the
# email information
driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


driver.find_element_by_id('identifierId').send_keys("CVTFCPSC353@gmail.com")
driver.find_element_by_id('identifierId').send_keys(Keys.ENTER)

time.sleep(7)
driver.find_element_by_name("password").send_keys("Cvtf1231$")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(7)
driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']").click()
time.sleep(4)
driver.find_element_by_xpath("//textarea[@name='to']").send_keys(email)
time.sleep(2)
driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("CoronaVirus Update")
driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']").send_keys(email_body_string)
driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']").click()
time.sleep(5)
driver.quit()
