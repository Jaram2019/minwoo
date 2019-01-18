import requests
from bs4 import BeautifulSoup
import re

list = []
list.appned()
    

rq = requests.get("https://namu.wiki/w/%EB%A6%AC%EB%93%AC%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D")
rqctnt = rq.content
soup = BeautifulSoup(rqctnt,"html.parser")

OMG = str(soup.find_all("p"))

OMG = re.sub('<.+?>', '', OMG, 0).strip()
print(OMG)
