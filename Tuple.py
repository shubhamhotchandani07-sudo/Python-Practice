#TUPLE IS ALWAYS WRITTEN IN () CURLY BRACKETS 
a=(10,20,"shubham",90,50,"rohit")
print(a)


#WAP TO ITERATE THROUGH A TUPLE AND PRINT EACH ELEMENT ON A NEW LINE
# a=(10,50,"shubham",90,"rohit",35)
# i=0
# while i<=6:
#     print(a[i])
#     i+=1

#WAP TO FIND THE SUM OF ALL NUMERICAL ELEMENTS IN TUPLE USING WHILE LOOP
a=(1,2,3,4,5,9,8,7,6)
sum=0
i=0
while i<9:
    sum=sum+a[i]
    i+=1
print(sum)

#GIVEN A TUPLES OF NUMBERS WAP TO COUNT HOW MANY EVEN NUMBERS IT CONTAINS USING A  WHILE LOOP
b=(10,20,30,95,60,55)
even=0
i=0
while i<len(b):
    if b[i]%2==0:
        even+=1
    i+=1
print(even)

#WAP TO CONVERT A TUPLE OF STRINGS INTO SINGLE SENTENCE/STRING USING A WHILE LOOP
r=("shubham","rohit","kishu","tushar","didi")
a=""
i=0
while i<len(r):
    a=a+r[i]+" "
    i+=1
print(a)

w=(1,2,3,4,5,6,7,9,8)
i=0
while i<len(w):
    if 9 in w:
        i+=1
print(True)

#WAP TO FIND THE LRGEST NUMBER FROM THE TUPLE
d=(1,2,3,9,7,6,5,0)
largest=d[0]
i=0
while i<len(d):
    if d[i]>largest:
        largest=d[i]
    i+=1
print(largest)
        
#GIVEN A TUPLE WAP TO COPY ITS ELEMENT INTO TUPLE IN REVERSE ORDER USING WHILE LOOP

#HOW MANY ELEMNETS IN A TUPLE COUNT WITHOUT LOOPS
a=("shubham",40,80,20,90,"rohit")
print(len(a))

#COUNT HOW MANY TIME A SPECIFIC ELEMENTS APPEAR
c=("shubham",30,30,"shubham",20,90)
print(c.count("shubham"))

#POSITION OF OCCURANCE OF SPECIFIC ELEMENTS FROM A TUPPLE WITHOUT LOOPS
d=("shubham",40,60,9,2,0,"rohit")
print(d.index("shubham"))

#GIVEN A INDIVIDUAL TUPLE HOW DO YOU UNPACK ITS ELEMENTS INTO INDIVUDUAL VARIABLES 
a=("shubham",20,"Jaipur")
naam,umar,sahar=a
print("naam:",naam)
print("umar:",umar)
print("sahar:",sahar)

#HOE DO YOU REVERSE A ELEMENT THROUGH SLICING WITHOUT LOOPS
a=(9,0,8,7,6)
slice=a[::-1]
print(slice)

#HOW DO YOU CONCANTATE (JOIN) TWO TUPLES TOGETHER INTO A SINGLE NEW TUPLE?
a=(10,20,60,80,40)
b=(20,90,60,40,10)
print(a+b)

#HOW DO YOU CREATE A TUPLE THAT REPEATS THE ELEMENETS OF AN EXISTING TUPLE 3 TIMES
a=(1,2,3,4,9,8,7,6)
b=a*3
print(b)

#HOW DO YOU EXTRACT A NEW TUPLE CONTAINING ONLY THE FIRST THREE ELEMENTS OF EXISTING ELEMENTS
a=("shubham","virat",50,32,5,6,7,)
b=a[:3]
print(b)

#HOW DO YOU CHECK IF A SPECIFIC ITEM EXISTS INSIDE A TUPLE IN A SINGLE LINE OF CODE IT PRESENT IN TUPLE OR NOT
a=("shubham",8,4,3,21,"rohit")
check="Shubham" in a
print(check)

