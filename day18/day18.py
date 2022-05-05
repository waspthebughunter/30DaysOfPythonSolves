import re
import collections

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
temp = re.findall(r"[A-Za-z]+", paragraph)
print(collections.Counter(temp).most_common())

print("#####################################################################################")

word = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
regex_pattern = r"[-]?\d\d|[-]?\d"
points = [int(i) for i in re.findall(regex_pattern, word)]
distance = points[-1]-points[0]

print("#####################################################################################")

def is_valid_variable(var_name):
    regex_pattern = r"^[\d\W]|[\W]"
    if len(re.findall(regex_pattern, var_name)) == 0:
        return True
    else:
        return False
print(is_valid_variable("jd1f1klj"))

print("#####################################################################################")

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
pattern=r"[%$@&#;!]"
matches=re.sub(pattern, "", sentence)
temp = re.findall(r"[A-Za-z]+", matches)
print(collections.Counter(temp).most_common())