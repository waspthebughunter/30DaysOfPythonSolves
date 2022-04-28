it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update("Reddit","Snapchat","Red Hat")
it_companies.remove("Facebook")

#in remove(); item is not a member of set process returned error and break code
#in discrad(); item is not a member of set process no returned error and not break the code

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.union(B)
B.union(A)
print(A.symmetric_difference(B))
del A
del B

age = [22, 19, 24, 25, 26, 24, 25, 24]
age=set(age)
print(len(age),len(list(age)))

