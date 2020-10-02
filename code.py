import requests
from bs4 import BeautifulSoup
url=input("enter url")
r=requests.get(url)
htmc=r.content
soup=BeautifulSoup(htmc,'html.parser')
print(soup.get_text())
