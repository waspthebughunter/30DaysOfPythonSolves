mytuple=tuple()
brotpl=("bro1","bro2")
sistpl=("sis1","sis2")
siblings=brotpl+sistpl
print(len(siblings))
lst=list(siblings)
lst.append("mom")
lst.append("dad")
family_members=tuple(lst)
print(family_members)
del family_members
##################################
fruits=("banana","strawberry")
vegetables=("tomato","potato")
animal_products=("milk","honey")
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp[int(len(food_stuff_tp)/2)])
print(food_stuff_tp[0:3],food_stuff_tp[-3:])
del food_stuff_tp
##################################
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
