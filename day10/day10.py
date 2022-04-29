import countries_data as cd
import countries as ct
for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i = i+1

for i in range(10, 0, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i = i-1

for i in range(8):
    for j in range(i):
        print("#", end="")
    print("")

for i in range(9):
    for i in range(9):
        print("#", end=" ")
    print()

for i in range(11):
    print(str(i)+"x"+str(i)+"="+str(i*i))

lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in lst:
    print(i)

for i in range(101):
    if i % 2 == 0:
        print(i)
    else:
        continue

for i in range(101):
    if i % 2 != 0:
        print(i)
    else:
        continue

a = 0
for i in range(101):
    a = a+i

print("The sum of all numbers is : "+str(a))

a, b = 0, 0
for i in range(101):
    if i % 2 == 0:
        a = a+i
    else:
        b = b+i

print("The sum of all evens is : "+str(a) +
      " And the sum of all odds is : "+str(b))


for i in ct.countries:
    if "land" in i:
        print(i)

lst = ['banana', 'orange', 'mango', 'lemon']
rvlst = list()

for i in lst[::-1]:
    rvlst.append(i)

print(lst, rvlst)


templist = list()
for i in range(len(cd.world)):
    templist.append(cd.world[i]["languages"])

dirty_lang_list = list()
for i in templist:
    for j in i:
        dirty_lang_list.append(j)

dirty_lang_list.sort()
print("total number of languages in the data : ", len(dirty_lang_list))

#######################################################################

langdict = dict()
for i in range(len(dirty_lang_list)):
    langdict[dirty_lang_list[i]] = dirty_lang_list.count(dirty_lang_list[i])


langname = []
langcount = []

for i in langdict:
    langname.append(i)
    langcount.append(langdict[i])

lastitem = ""
counter = 0
for i in sorted(langcount, reverse=True):
    if counter == 10:
        break
    else:
        if langname[langcount.index(i)] != lastitem:
            print(langname[langcount.index(i)], i)
            lastitem = langname[langcount.index(i)]
            counter = counter+1

tempdict = dict()
for i in range(len(cd.world)):
    tempdict[cd.world[i]["name"]] = cd.world[i]["population"]

cname = list()
population = list()

for i in tempdict:
    cname.append(i)
    population.append(tempdict[i])

lastitem = ""
counter = 0
for i in sorted(population, reverse=True):
    if counter == 10:
        break
    else:
        if cname[population.index(i)] != lastitem:
            print(cname[population.index(i)], i)
            lastitem = cname[population.index(i)]
            counter = counter+1
