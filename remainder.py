from bs4 import BeautifulSoup
import requests
page = requests.get("https://github.com/Saicharan67")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('svg'))
