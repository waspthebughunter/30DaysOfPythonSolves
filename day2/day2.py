'''Day 2: 30 Days of python programming'''

########################################################

first_name = "firstname"
last_name = "lastname"
full_name = first_name+last_name
country = "country"
city = "city"
age = 1
year = 2022
is_married = False
is_true = True
is_light_on = False
a, b, c, d = 1, 2, 3, 4

#################################################################

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(len(first_name))
print(len(last_name))

###################################################

num_one, num_two = 5, 4
total = num_one+num_two
diff = num_one-num_two
product = num_one*num_two
division = num_one/num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one//num_two

###################################################

radius=30
area_of_circle=3.14*(radius**2)
circum_of_circle=(2*3.14)*radius

###################################################

radius=int(input("Please type radius : "))
print("Area of your circle : "+str(3.14*(radius**2)))

###################################################

first_name=input("Type your first name : ")
last_name=input("Type your last name : ")
country=input("Type your country : ")
age=int(input("Type your age : "))

###################################################

help("keywords")