# from bs4 import BeautifulSoup
# import requests
# page = requests.get("https://github.com/Saicharan67")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('svg'))


from datetime import datetime as date
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# path to your chrome driver
cd = 'C:\\Users\\hp\\chromedriver.exe'

Date = date.today()
Todays_Date= str(Date.year)+'-'+str(Date.month)+'-'+str(Date.day)
browser = webdriver.Chrome(cd)
browser.get("https://github.com/Saicharan67")

Todays_Streak = browser.find_element_by_xpath("//*[@data-date='{0}']".format(Todays_Date))
print(Todays_Streak.get_attribute('data-count'))