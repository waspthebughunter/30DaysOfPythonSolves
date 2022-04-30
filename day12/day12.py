import string
import random

char_list=[]

for i in string.ascii_letters:
    char_list.append(i)

for i in string.digits:
    char_list.append(i)

def random_user_id():
    uid=""
    for i in range(6):
        uid+=random.choice(char_list)

    return uid

length=int(input("Plz enter length : "))
nid=int(input("Plz enter how many id if u want : "))

def user_id_gen_by_user():
    uid=""
    for i in range(nid):
        for i in range(length):
            uid+=random.choice(char_list)
        uid+="\n" 

    return uid

def rgb_color_gen():
    rgb=[]
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return "rgb("+str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])+")"

def hex_color_gen():
    color="#"
    for i in range(6):
        color+=random.choice(string.hexdigits)
    
    return color

def generate_colors(col_type,times):
    colors=[]
    if col_type=="hexa":
        for i in range(times):
            colors.append(hex_color_gen())
    elif col_type=="rgb":
        for i in range(times):
            colors.append(rgb_color_gen())
    else:
        return "Wrong color type!"
        
    return colors

def shuffle_list(a):
    random.shuffle(a)
    return a

def last_task():
    num_list=[]
    def choose():
        a=random.choice(string.digits)
        if a not in num_list:
            num_list.append(a)
        else:
            choose()

    for i in range(7):
        choose()

    return num_list

print(last_task())