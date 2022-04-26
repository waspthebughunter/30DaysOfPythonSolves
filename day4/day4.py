s='Thirty', 'Days', 'Of', 'Python'
print(''.join(s))
#######################################
s='Coding', 'For' , 'All'
print(" ".join(s))
#######################################
company="Coding For All"
print(company)
print(len(company))
company.upper()
company.lower()
company.title()
print(company.strip("Coding"))
company.find("Coding")
company.replace("Coding", "Python")
s="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
s.split(",")
print(company[0])
print(company.index(company[-1]))
print(company[10])
print(company[0]+company[7]+company[11])
print(company.index("C"),company.index("F"))
print(company.rfind("l"))
########################################
s= 'You cannot end a sentence with because because because is a conjunction'
print(s.find("because"))
print(s.rfind("because"))
print(s.replace("because",""))
########################################
print(company.startswith("Coding"))
########################################
s=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(s)+"#")
print("I am enjoying this challenge.\nI just wonder what is next.")
########################################
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
########################################
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'radius = %d\narea = %.2f * radius ** 2\nThe area of circle with a radius %d is %.2f.' %(radius,pi,radius,area)
print(formated_string)
########################################
print("{}+{}={}\n{}-{}={}\n{}*{}={}\n{}/{}={:.2f}\n{}%{}={}\n{}//{}={}\n{}**{}={}".format(8,6,8+6,8,6,8-6,8,6,8*6,8,6,8/6,8,6,8%6,8,6,8//6,8,6,8**6))
