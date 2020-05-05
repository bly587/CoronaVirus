# https://intellipaat.com/community/16524/take-screenshot-of-full-page-with-selenium-python-with-chromedriver  set up classes
# figure out regex

from selenium import webdriver
import time
import os


# Selenium to automate through web
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
soup = BeautifulSoup(page.content, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')
table1 = []
email = input("Enter your email: ")
state = input("Input your state: ").capitalize()

# numCases = ""
for tr in table_rows:
	td = tr.find_all('td')
	row = [i.text.strip() for i in td]
	table1.append(row)
for i in range(len(table1)):
    for j in range(len(table1[i])):
        if table1[i][j] == state:
			# numCases=table1[i][j+1]
            numCases = "Total number of cases in your state right now is: " + str(table1[i][j+1])

f = open("practiceDataBase.txt", "w")
f.write(email)
f.write("\n")
f.write(state)
f.write("\n")
f.write(numCases)
f.write("\n")

f.close()

os.system("sendEmail.py")
