# https://intellipaat.com/community/16524/take-screenshot-of-full-page-with-selenium-python-with-chromedriver  set up classes
# figure out regex
#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

from selenium import webdriver
import time

# Selenium to automate through web
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup


print("Hi")

# page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
# soup = BeautifulSoup(page.content, 'lxml')
# table = soup.find('table')
# table_rows = table.find_all('tr')
# table1 = []
# #state = input("Input your state: ").capitalize()
# state = "Hawaii"
# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text.strip() for i in td]
# 	table1.append(row)
# for i in range(len(table1)):
#     for j in range(len(table1[i])):
#         if table1[i][j] == state :
# 			my_string = "Total number of cases in your state right now is: {}".format(table1[i][j+1])
#             #print("Total number of cases in your state right now is: {}".format(table1[i][j+1]))
# 			return my_string
