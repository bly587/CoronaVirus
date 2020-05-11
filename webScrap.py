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
	print("Hi")

	page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
	soup = BeautifulSoup(page.content, 'lxml')
	table = soup.find('table')
	table_rows = table.find_all('tr')
	table1 = []
	#state = input("Input your state: ").capitalize()
	# state = "Hawaii"
	for tr in table_rows:
		td = tr.find_all('td')
		row = [i.text.strip() for i in td]
		table1.append(row)
	for i in range(len(table1)):
		for j in range(len(table1[i])):
			if table1[i][j] == state:
				my_string = "Hello friends,\n\nI hope that you and your family are staying healthy during these uncertain times.\n    Below are the latest statistics about COVID-19 in {}:\n    The total number of cases right now is: {}\n    The total number of deaths is: {}\n    The number of active cases is: {}\n\nPlease visit cdc.gov to follow their guidlines and to stay up to date about the CoronaVirus.\n\nHave a safe and healthy time,\nCVTF".format(state, table1[i][j+1],table1[i][j+3],table1[i][j+5])


				return my_string


# d = getData("Hawaii")
# print(d)
