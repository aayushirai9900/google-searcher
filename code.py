import requests
from bs4 import BeautifulSoup
url=input("Please enter url here: ")
r=requests.get(url)
htmc=r.content
soup=BeautifulSoup(htmc,'html.parser')
print(soup.get_text())
