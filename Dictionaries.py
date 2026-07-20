#{key:value} these two are used in dictionaries
a={"name":"rohit","age":20,"city":"jaipur"}
print(a)

a={"name":"rohit","age":20,"city":"jaipur"}
print(a["city"])

#ADDING UPDATE DATA
a={"name":"rohit","age":20,"city":"jaipur"}
a["name"]="shubham"
print(a)

a["mob"]=9839213456
print(a)

grades={"math":90,"science":45}
grades["history"]=34
print(grades)

#DELETE DATA BY DEL KEYWORD
grades={"math":90,"science":45}
del grades["science"]
print(grades)


#REMOVE DATA BY POP
grades={"math":90,"science":45}
popvalue=grades.pop("math")
print(grades)

print(grades.pop("english","not found"))

profile={
    "name":"shubham",
    "age":20,
    "gender":"male"
}
print(len(profile))

#GET KEYWORD IS USED 
data={"name":"shubham","age":20}
print(data.get("age"))

data={"name":"shubham","age":20}
print(data.get("mob","Not found"))

#FROM KEY
a=("rohit","vikas","arvind","vipin")
new_dict=dict.fromkeys(a,"BCA")
print(new_dict)

new_dict=dict.fromkeys("aeiou","Vowels")
print(new_dict)

#how do you access a value without causing a keu error in dictionARIES?
a={"name":"shubham","age":20,"city":"jaipur"}
print(a.get("name"))

a={"name":"shubham","age":20,"city":"jaipur"}
print(a.get("roll","not found"))

#HOW DO YOU FIND THE TOTAL NUMBER OF KEY VALUE PAIRS ?
b={"shubham":9530426834,"rohit":93722910194}
print(len(b))

#HOW DO YOU ADD OR UPDATE A KEY VALUE PAIRS 
#ADD
a={"name":"shubham","age":20,"city":"jaipur"}
a["roll"]=23
print(a)

#UPDATE
a={"name":"shubham","age":20,"city":"jaipur"}
a["name"]="Rohit"
print(a)

#HOW DO YOU REMOVE A KEY AND RETURN ITS VALUE AT THE SAME TIME
a={"Name":"Rohit","City":"Jaipur","Roll":30}
poped=a.pop("Roll")
print(a)
print(poped)

#HOW DO YOU CHECK IF A KEY EXISTS WITHOUT LOOPS
a={"Name":"Tushar","Age":30,"Roll":89}
check="Name" in a
print(check)

#HOW DO YOU CLEAR ALL ITEMS FROM A DICTIONARY
a={"name":"Shubham","Roll":90,"City":"Jaipur"}
a.clear()
print(a)

#GIVEN TWO DICTIONARIES, HOW DO YOU MERGE THEM IN SINGLE LINE ?
#WE MERGE IT BY PIPE OPERATOR "|"
A={"Name":"Shubham","City":"Jaipur","Roll":90,"Age":90}
B={"Name":"Shubham","City":"Jaipur","Roll":70,"Age":80}
merge=A | B
print(merge)

#HOW DO YOU EXTRACT ALL KEYS INTO A LIST WITHOUT LOOPS
B={"Name":"Shubham","City":"Jaipur","Roll":70,"Age":80}
C=list(B)
print(C)

#GIVEN A LIST OF KEYS, HOW DO YOU CREATE THE DICTIONARY WITH DEFAULT VALUE 0 IN ON STEP
a=["shubham","Tushar","rohit","Hiten"]
b=dict.fromkeys(a,"BCA")
print(b)

#HOW DO YOU CREATE A SHALLOW COPY OF A DICTIONARY
B={"Name":"Shubham","City":"Jaipur","Roll":70,"Age":80}
copy=B.copy()
print(copy)

a={"name":"shubham","class":"BCA","City":"jaipur"}
print(a.keys())

a={"name":"shubham","class":"BCA","City":"jaipur"}
print(a.items())