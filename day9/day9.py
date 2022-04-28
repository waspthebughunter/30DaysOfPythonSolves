age = int(input("Enter your age : "))
print("You are old enough to learn to drive.") if age >= 18 else print(
    " You need more "+str(18-age)+" years to learn to drive.")

my_age = 30
your_age = int(input("Enter your age : "))
print("You are "+str(your_age-my_age)+" years older than me.") if your_age > my_age else print(
    "I am "+str(my_age-your_age)+" years older than you.")

a = int(input("Enter number one : "))
b = int(input("Enter number two : "))
if a > b:
    print(str(a)+" is greater than "+str(b))
elif a < b:
    print(str(a)+" is less than "+str(b))
else:
    print(str(a)+" is equal to "+str(b))

score=int(input("Enter your score : "))
if score >=80 and score<=100:
    print("A")
elif score >=70 and score<=79:
    print("B")
elif score >=60 and score<=69:
    print("C")
elif score >=50 and score<=59:
    print("D")
elif score >=0 and score<=49:
    print("F")
else:
    print("You entered wrong value")

usr_input=input("Enter month : ")
if usr_input=="September" or usr_input=="October" or usr_input=="November":
    print("Season is Autumn")
elif usr_input=="December" or usr_input=="January" or usr_input=="February":
    print("Season is Winter")
elif usr_input=="March" or usr_input=="April" or usr_input=="May":
    print("Season is Spring")
elif usr_input=="June" or usr_input=="July" or usr_input=="August":
    print("Season is Summer")
else:
    print("You entered wrong value")

usr_input=input("Enter fruit : ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if usr_input not in fruits:
    fruits.append(usr_input)
    print("Modified list : ",fruits)
else:
    print('That fruit already exist in the list')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person.keys():
    print(person["skills"][int(len(person["skills"])/2)])

if "skills" in person.keys():
    if "Python" in person["skills"]:
        print("Person have Python skill")

if "Javascript" in person["skills"] and "React" in person["skills"] and len(person["skills"]) <= 2:
    print('He is a front end developer')
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"] and len(person["skills"]) == 3:
    print('He is a back end developer')
elif "Node" in person["skills"] and "React" in person["skills"] and "MongoDB" in person["skills"]:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person["is_marred"]==True and person["country"]=="Finland":
    print(person["first_name"]+" "+person["last_name"]+" lives in "+person["country"]+". He is married.")
