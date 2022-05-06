import re
import json
import collections

f=open("./day19/obama_speech.txt")
lines=f.read().splitlines()
number_of_lines=len(lines)
words=[re.findall(r"[\w]+", i) for i in lines]
number_of_words=len(words)
f.close()

def most_spoken_languages(file,count):
    f=open(file)
    data=json.load(f)
    languages=[data["world"][i]["languages"] for i in range(len(data["world"]))]
    f.close()
    lang_str=""
    for i in languages:
        if len(i)>1:
            for k in i:
                lang_str+=k+","
        else:
            lang_str+=i[0]+","
    temp = re.findall(r"[A-Za-z]+", lang_str)
    return collections.Counter(temp).most_common(count)

print(most_spoken_languages("./day19/countries_data.json",1))

def most_populated_countries(file,count):
    f=open(file)
    data=json.load(f)
    world=data["world"]
    f.close()
    countries=[]
    for i in range(count):
        countries.append({"country":sorted(world,key=lambda x:x["population"],reverse=True)[i]["name"],
        "population":sorted(world,key=lambda x:x["population"],reverse=True)[i]["population"]})

    return countries

print(most_populated_countries("./day19/countries_data.json",1))

print("#####################################################################################")

def find_email_address():
    f=open("./day19/email_exchanges_big.txt")
    lines=f.read().splitlines()
    f.close()
    dirty_mail_address=[i for i in lines if "@" in i]
    temp=[]
    for i in range(len(dirty_mail_address)):
        if re.findall(r"[A-Za-z]+[.@\w]+\w+", dirty_mail_address[i])[0]=="From":
            temp.append(re.findall(r"[A-Za-z]+[.@\w]+\w+", dirty_mail_address[i])[1])

    clean_mail_address=[]
    for i in temp:
        if i not in clean_mail_address:
            clean_mail_address.append(i)

# passing task5 bcz i cant find sample.txt ¯\(°_o)/¯

def find_most_common_words(file,count):
    f=open(file)
    lines=[f.read().splitlines()]
    paragraph=str(lines)
    temp = re.findall(r"[A-Za-z]+", paragraph)
    return collections.Counter(temp).most_common(count)

print(find_most_common_words("./day19/obama_speech.txt",5))