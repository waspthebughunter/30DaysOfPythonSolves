numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers=[i for i in numbers if i<=0]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dim_list=[j for i in list_of_lists for k in i for j in k]

list_of_tuples=[(i,1,i*1,i**2,i**3,i**4,i**5) for i in range(11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries_list=[[k[0].upper(),k[0][:3].upper(),k[1].upper()] for i in countries for k in i ]
new_countries_dict=[{"country":k[0].upper(),"city":k[1].upper()} for i in countries for k in i]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_names=[k[0]+" "+k[1] for i in names for k in i]

m= lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
print(m(10,9,10,6))