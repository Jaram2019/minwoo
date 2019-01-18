import requests
from bs4 import BeautifulSoup
import re

rq = requests.get("https://play.google.com/store/apps/category/GAME_MUSIC?hl=ko")
rqctnt = rq.content
soup = BeautifulSoup(rqctnt,"html.parser")
soup = soup.find_all(attrs={'class':'title'})

blacklsit = ["앱","영화/TV","음악","도서","기기","엔터테인먼트","음악"]

for link in soup:
    if link.text.strip() in blacklsit:
        pass
    else:
        print(link.text.strip())
