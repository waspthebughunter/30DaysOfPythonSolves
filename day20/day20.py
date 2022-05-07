import requests
import re
import collections
from bs4 import BeautifulSoup

url="https://www.gutenberg.org/files/1112/1112.txt"
r=requests.get(url)
pattern=r"[\w]+"
words=re.findall(pattern, r.text)
#print(collections.Counter(words).most_common(10))

url="https://api.thecatapi.com/v1/breeds"
r=requests.get(url)
cats=r.json()
weights=[cats[i]["weight"]["metric"] for i in range(len(cats))]
pattern=r"\d"
temp=[re.findall(pattern, i) for i in weights]
temp2=[k for i in temp for k in i]
minimum=min(temp2)
maximum=max(temp2)

int_temp2=[int(i) for i in temp2]
mean=sum(int_temp2)/len(int_temp2)
median=int_temp2[int(len(int_temp2)/2)]
#print(minimum,maximum,mean,median)

life_span=[cats[i]["life_span"] for i in range(len(cats))]
pattern=r"\d"
temp=[re.findall(pattern, i) for i in life_span]
temp2=[k for i in temp for k in i]
minimum=min(temp2)
maximum=max(temp2)

int_temp2=[int(i) for i in temp2]
mean=sum(int_temp2)/len(int_temp2)
median=int_temp2[int(len(int_temp2)/2)]
#print(minimum,maximum,mean,median)

#i cant do task3 bcz api not accessiable

url="https://archive.ics.uci.edu/ml/datasets.php"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.title.string)