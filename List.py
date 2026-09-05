a=[10,20,30,80,70]
print(a)

print(a[-3])

a=[30,40,"Shubham",90,50]
print(type(a[2]))

data=["shubham",30,40,10]
data[0]="Rohit"
print(data)

a=[20,30,"shubham",[1,2,3],"Rohit"]
b=a[3],a[4]
print(b[0])

c=["shubham",20,40,80,60]
print(c[0][1])

print(c[-1])

abc=["vipin",25,"jaipur",302020,True,[43,9,[23242,[234234]]]]
print(abc)
print(abc[5])
print(abc[5][1])
print(type(abc[1])) 
print(abc[5][2][-1])
print(abc[5][2][-1][-1])

a=[[[[123]]]]
print(a[0][0][0][0])

#REFRENCE VARIABLE
a=34
b=a
print(a,b)
a=26
print(a,b)

a=["shubham",30,60,10]
b=a
print(a,b)
b[0]="rohit"
print(a,b)

#SLICING OF LIST
number=[20,30,40,50,80,10,90]
print(number[2:6:1])

number=[20,30,40,50,80,10,90]
print(number[:6])

number=[20,30,40,50,80,10,90]
print(number[2::])

number=[20,30,40,50,80,10,90]
print(number[::1])

number=[20,30,40,50,80,10,90]
print(number[::])

number=[20,30,40,50,80,10,90]
print(number[::-1])

number=[20,30,40,50,80,10,90]
print(number[:-4:-1])

o=["apple","banana","cherry","date"]
print(o[2:4])

o=["apple","banana","cherry","date"]
print(o[2:-1])

o=["apple","banana","cherry","date"]
o[1]="Pineapple"
print(o)

o=["apple","banana","cherry","date"]
o[2:4]="Mango","Orange"
print(o)

#OPERATIONS ON A LIST
list1=[8,2,"abc"]
list2=[3,4,"abc"]
combined=list1+list2
print(combined)

list1=[8,2,"abc"]
#list2=[3,4,"abc"]
combined=list1*3
print(combined)

#COMPARISON OF LIST
list1=[8,2,"abc"]
list2=[3,4,"abc"]
print(list1>=list2)
print(list1<=list2)
print(list1==list2)

#MEMBERSHIP IN LIST
a=[1,2,3,[4,5]]
print(2 in a)
print(5 in a[-1])

#IDENTITY OPERATOR IN LIST
a=[1,2]
b=a
print(a,b)
print(a is b)