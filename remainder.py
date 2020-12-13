from bs4 import BeautifulSoup
from datetime import datetime as date

import requests
page = requests.get("https://github.com/Saicharan67")
soup = BeautifulSoup(page.content, 'html.parser')


Date = date.today()
Todays_Date= str(Date.year)+'-'+str(Date.month)+'-'+str(Date.day)
Todays_Streak = soup.find_all('rect',attrs={'data-date':Todays_Date})


print(Todays_Streak[0]['data-count'])