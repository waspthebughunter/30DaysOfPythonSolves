# map() is a returning every values but filter() just returning specific values and reduce() returns just one value

import functools
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print([i for i in countries])
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print([i for i in names])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in numbers])


def change_to_upper(name):
    return name.upper()


countries_uppercase = map(change_to_upper, countries)
print(list(countries_uppercase))

print([i.upper() for i in countries])


def change_to_square(num):
    return num*num


numbers_squared = map(change_to_square, numbers)
print(list(numbers_squared))

names_uppercase = map(lambda x: x.upper(), names)
print(list(names_uppercase))


def is_land(name):
    if "land" in name:
        return True
    else:
        return False


filtered_countries = filter(is_land, countries)
print(list(filtered_countries))


def is_sixchar(name):
    if len(name) == 6:
        return True
    else:
        return False


filtered_countries = filter(is_sixchar, countries)
print(list(filtered_countries))


def is_better_sixchar(name):
    if len(name) >= 6:
        return True
    else:
        return False


filtered_countries = filter(is_better_sixchar, countries)
print(list(filtered_countries))


def is_firstchar_e(name):
    if name[0] == "E":
        return True
    else:
        return False


filtered_countries = filter(is_firstchar_e, countries)
print(list(filtered_countries))


def get_string_lists(a):
    return [i for i in a if type(i) == type("a")]


print(get_string_lists(countries))

print(functools.reduce(lambda x, y: x+y, numbers))

print(functools.reduce(lambda x, y: x+", "+y, countries),
      "are north European countries")

import countries

def fl_country():
    templist=[i[0] for i in countries.countries]
    mydict=dict()
    for i in countries.countries:
        if i[0] not in mydict.keys():
            mydict[i[0]]=templist.count(i[0])
    return mydict

print(fl_country())
            
def get_first_ten_countries():
    return [countries.countries[i] for i in range(10)]

print(get_first_ten_countries())

def get_last_ten_countries():
    countries.countries.reverse()
    return [countries.countries[i] for i in range(10)]

print(get_last_ten_countries())

from countries_data import world



    
print(sorted(world,key=lambda dct:dct["name"])) #by name

print("#####################################################################################")

print(sorted(world,key=lambda dct:dct["capital"])) #by capital

print("#####################################################################################")

print(sorted(world,reverse=True,key=lambda dct:dct["population"]))

print("#####################################################################################")


