emptylist=list()
anotherlist=[1,2,3,4,5]
print(len(anotherlist))
print(anotherlist[0],anotherlist[int(len(anotherlist)/2)],anotherlist[-1])
mixed_data_types=["name",1,10,"alone","my adress"]
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[int(len(it_companies)/2)],it_companies[-1])
it_companies[2]="Reddit"
print(it_companies)
it_companies.append("Red Hat")
it_companies[-1].upper()
print('#;  '.join(it_companies)+'#;  ')
print("Oracle" in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies[3:])
print(it_companies[:-3])
it_companies.remove(it_companies[int(len(it_companies)/2)])
it_companies.remove(it_companies[0])
it_companies.remove(it_companies[int(len(it_companies)/2)])
it_companies.remove(it_companies[-1])
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
full_stack.append("Python")
full_stack.append("SQL")
full_stack.append("Redux")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0],ages[-1])
print(ages[int(len(ages)/2)])
x=0
x=x+ages[0]
x=x+ages[1]
x=x+ages[2]
x=x+ages[3]
x=x+ages[4]
x=x+ages[5]
x=x+ages[6]
x=x+ages[7]
x=x+ages[8]
x=x+ages[9]
print("Average : ",x/len(ages))
print(abs(ages[0]-x/len(ages)),abs(ages[-1]-x/len(ages)))
import countries 
print(countries.countries[int(len(countries.countries)/2)])
print(countries.countries[:int(len(countries.countries)/2)],countries.countries[int(len(countries.countries)/2):])
cl=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandanic_countries=cl[3:]
print(scandanic_countries)


