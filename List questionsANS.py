current_actions=["line","circle","square"]
backup_actions=current_actions
backup_actions.append("Triangle")
print(backup_actions)

cart=["shoes","belt","watch","hat","belt","socks"]
print(cart[:-4:-1])

#SORT ME PHLE SORT LIKHEGE FIR PRINT KRWAYGE JSE ISME NICHE KRA H PHLE SORT KIYA H FIR PRINT KRAYA H 
tags=["banana","vipia","cherry","apple","vipin"]
tags.sort()
print(tags)

#WRITE A CODE TO RETRIEVE EVERY 4TH ELEMENT DATA FROM INDEX 0
number=[0,1,2,3,4,5,6,7,8,9]
print(number[0::4])

#ADD NEW LEYWORD IN LIST AT STARTING POSITION INDEX 0 BY INSERT METHOD
notifications=["Like","Comment"]
notifications.insert(0,"Follow")
print(notifications)

#PRINT 234234 FROM THIS INDEX BY SLICING
log_data=["Vipin","25","Jaipur","302020","True",["Test",43,[23242,[234234]]]]
print(log_data[5][2][1])

#PRINT THE LAST ELEMENT
list=["shubham",90,20,50,True,"Rohit"]
print(list[-1])

#HOW DO YOU REVERSE A LIST WITHOUT LOOP OR REVERSE() METHOD
list2=[10,20,"shubham",70,40,"rohit"]
print(list2[::-1])

#ADD KOHLI AT LAST ELEMENT
list=[10,20,50,"shubham",40,"virat"]
list.append("Kohli")
print(list)

#HOW DO YOU FIND THE TOTAL NO OF ELEMENT IN A LIST
list=[10,20,50,"shubham",40,"virat"]
print(len(list))

#HOW DO YOU FIND THE SUM OF ELEMENTS IN A LIST BY SUM KEYWORD WE ADD LIST ELEMENTS
list=[1,2,3,4,5,6,7,8,9]
list=sum(list)
print(list)

#HOW DO YOU FIND THE LARGEST AND SMALLEST NUMBERS IN A LIST BY MAX MIN KEYWORD
list=[1,2,3,4,5,6,7,8,9]
list=max(list)
print(list)

list=[1,2,3,4,5,6,7,8,9]
list=min(list)
print(list)

#HOW DO YOU COUNT A NUMBERS OCCURS IN A LIST
list=[60,20,60,90,40,60]
list=list.count(60)
print(list)

#HOW DO YOU COMPLETELY EMPTY A LIST (BY CLEAR() KEYWORD)
list=[20,30,40,50,"shubham",40]
list.clear()
print(list)

#HOW WE CHECK pYTHON IS PRESENT IN P OR NOT
p=["shubham",10,20,40,"Python"]
if "Python" in p:
    print("yes")
else:
    print("No")

#WAP TP PRINT TO PRINT EACH ELEMENT OF LIST ON NEW LINE USING A WHILE LOOP
# a=["shubham","rohit","Virat","Kohli","Boss"]
# i=0
# while i<=5:
#     print(a[i])
#     i+=1

#WAP TO FIND THE SUM OF LIST ELEMENTS
b=[1,2,3,10,5,6]
i=0
sum=0
while i<len(b):
    sum+=b[i]
    i+=1
    print(sum)

#WAP TO FIND THE LARGEST NUMBER IN A LIST WITHOUT USING MAX FUNCTION BY USING WHILE LOOP
a=[10,20,90,50,30]
largest=a[0]
i=1
while i<len(a):
    if a[i]>largest:
        largest=a[i]
        print(largest)
    i+=1

#WAP TO FIND THE SMALLEST NUMBER FROM A LIST WITH LOOPING
a=[10,20,90,50,30]
small=a[0]
i=1
while i<len(a):
    if a[i]<small:
        largest=a[i]
        print(small)
    i+=1

#WAP TO COUNT HOW MANY TIME A SPICIFIC ELEMENT APPEAR IN LIST USINF WHILE LOOP
p=[10,20,30,40,40,5,40]
count=0
i=0
while i<len(p):
    if p[i]==40:
        count+=1
        
    i+=1
print(count)

#WAP TO REVERSE THE ELEMENT OF LIST IN PLACE USING A WHILE LOOP
s=[10,20,30,90,80,50]
d=[]
i=len(s)-1
while i>0:
    d.append(s[i])
    i-=1
print(d)

#wap to find and print all even numbers from list of integers by while loop
a=[10,30,40,35,60,70,90]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i])
    i+=1

#WAP TO REMOVE ALL DUPLICATE ITEMS FROM THE LIST USING THE WHILE LOOP
d=[10,20,30,4,10,10,70,70]
s=[]
i=0
while i<len(d):
    if d[i] not in s:
        s.append(d[i])
    i+=1
print(s)

#WAP TO CHECK IF SPEIFIC ELEMENTS EXIST IN A LIST USING LOOP 
s=[20,30,40,60,10,"Shubham"]
i=0
while i<len(s):
    if "Shubham" in s:
     i+=1
print(True)