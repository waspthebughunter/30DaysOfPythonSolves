dog={}
dog["name"]="mydog"
dog["color"]="gold"
dog["breed"]="golden"
dog["legs"]=4
dog["age"]=2

student={
    "first_name":"a",
    "last_name":"b",
    "gender":"m",
    "age":0,
    "is_married":False,
    "skills":["a","b","c","d"],
    "country":"a",
    "city":"b",
    "address":"lorem ipsum dolor sit amet"
}
print(len(student))
print(student["skills"],type(student["skills"]))
student["skills"].append("e")
student_keys=list(student.keys())
student_items=list(student.items())
student_lst=student.items()
student.pop("skills")
del student