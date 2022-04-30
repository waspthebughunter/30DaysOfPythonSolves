def add_two_numbers(a,b):
    return a+b

def area_f_circle(r):
    return 3.14*(r**2)

def add_all_nums(*args):
    sums=0
    for i in args:
        if type(i)==type(0):
            sums+=i
        else:
            print("wrong value type",i)
    return sums

def convert_celsius_to_fahrenheit(c):
    return c*(9/5)+32

def check_season(usr_input):
    usr_input=input("Enter month : ")
    if usr_input=="September" or usr_input=="October" or usr_input=="November":
        return "Autumn"
    elif usr_input=="December" or usr_input=="January" or usr_input=="February":
        return "Winter"
    elif usr_input=="March" or usr_input=="April" or usr_input=="May":
        return "Spring"
    elif usr_input=="June" or usr_input=="July" or usr_input=="August":
        return "Summer"
    else:
        return "You entered wrong value"

def calculate_slope(y2,y1,x2,x1):
    return (y2-y1)/(x2-x1)

import cmath
def solve_quadratic_eqn(a,b,c):
    delta=(b*b)-(4*a*c)
    ans1=(-b-cmath.sqrt(delta))/(2*a)
    ans2=(-b+cmath.sqrt(delta))/(2*a)

    return str(ans1)+"\n"+str(ans2)

def print_list(a=list()):
    for i in a:
        print(i)

def reverse_list(a=list()):
    rev_list=list()
    for i in range(len(a)-1,-1,-1):
        rev_list.append(a[i])

    return rev_list

def capitalize_list_items(a=list()):
    capitalized=list()
    for i in a:
        capitalized.append(i.upper())

    return capitalized

def add_item(a,b):
    a.append(b)
    return a

def remove_item(a,b):
    a.remove(b)
    return a

def  sum_of_numbers(a):
    b=0
    for i in range(a+1):
        b+=i

    return b

def  sum_of_odd_numbers(a):
    b=0
    for i in range(a+1):
        if i%2!=0:
            b+=i

    return b

def  sum_of_even_numbers(a):
    b=0
    for i in range(a+1):
        if i%2==0:
            b+=i

    return b

def evens_and_odds(a):
    count_odd,count_even=0,0
    for i in range(a+1):
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1

    return "The number of odds are "+str(count_odd)+"\nThe number of evens are "+str(count_even)

def factorial(a):
    b=1
    for i in range(a,0,-1):
        b*=i
    
    return b

def is_empty(a):
    if len(a)==0:
        return "empty"
    else:
        return "no"

# i passed lv2 task3 bcz we make same thing in past

def is_prime(a):
    if a>1:
        for i in range(2,int(a/2)+1):
            if a%i==0:
               print(a, "is not a prime number")
            break 
        else:
            print(a, "is a prime number")
    else:
        print(a, "is not a prime number")

def is_unique(a):
    not_unique=[]
    for i in a:
        if i not in not_unique:
            if a.count(i)>1:
                not_unique.append(i)
        
    return not_unique

def is_same_type(a):
    not_same=[]
    for i in a:
        if i not in not_same:
            if type(i)!=type(a[0]):
                not_same.append(i)

    return not_same

import string
import keyword

def is_valid(name):
    punctation=[]
    for i in string.punctuation:
        if i!="_":
            punctation.append(i)

    if name[0] in string.digits or name[0] in punctation or name in keyword.kwlist:
        print("name is not valid")


# passing last 2 tasks bcz we make day10