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

def getData(state):
	page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
	soup = BeautifulSoup(page.content, 'lxml')
	# Locate the table that holds all the info about the us
	table = soup.find('table')
	table_rows = table.find_all('tr')
	table1 = []

	for tr in table_rows:
		td = tr.find_all('td')
		row = [i.text.strip() for i in td]
		table1.append(row)
	# Grab all the useful information fro that state
	for i in range(len(table1)):
		for j in range(len(table1[i])):
			if table1[i][j] == state:
				my_string = "Hello friends,\n\nI hope that you and your family are staying healthy during these uncertain times.\n    Below are the latest statistics about COVID-19 in {}:\n    The total number of cases right now is: {}\n    The total number of deaths is: {}\n    The number of active cases is: {}\n\nPlease visit cdc.gov to follow their guidelines and to stay up to date about the CoronaVirus.\n\nHave a safe and healthy time,\nCVTF".format(state, table1[i][j+1],table1[i][j+3],table1[i][j+5])
				 #When I tried making this line shorter by breaking up the string
				 #it was giving me problemns with selenium


				return my_string
