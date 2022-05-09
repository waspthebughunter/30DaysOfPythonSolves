import requests
from bs4 import BeautifulSoup
import json

url="http://www.bu.edu/president/boston-university-facts-stats/"
response=requests.get(url)
content=response.content
soup=BeautifulSoup(content,"html.parser")
headings=[i.get_text() for i in soup.find_all("h5")]
heading_rows=[5,6,3,4,9,3,4,4,0]
values_names=[i.get_text() for i in soup.find_all("p","text")]
values=[i.get_text() for i in soup.find_all("span","value")]

subdict={values_names[i]:values[i] for i in range(len(values))}
mydict={}
a,b=0,7
for i in range(len(headings)):
    mydict[headings[i]]=dict(list(subdict.items())[a:b])
    a+=heading_rows[i]
    b+=heading_rows[i]

mydict_json=json.dumps(mydict,ensure_ascii=False,indent=4)
with open("./day22/boston-university-facts-stats.json","w",encoding='utf-8') as f:
    f.write(mydict_json)

#community=7, campus=5, academics=6, Grant & Contract Awards=3, Undergraduate Financial Aid & Scholarships =4, student life =9,
#research=3, International Community=4, athletics=4

