#   WAP FUNCTION THAT TAKES A LIST OF INTEGERS AND PRINT SUM OF ALL ELEMENTS

def sum():
    a=[10,20,30,40,50]
    total=0
    i=0
    while i<len(a):
        total=total+a[i]
        i+=1
    print(total)
sum()

#WAF THAT TAKES A LIST OF INTEGERS AND PRINTS LARGEST FROM THE LIST

def large():
    a=[1,2,3,4,5,6,7,8,9]
    large=a[0]
    i=0
    while i<len(a):
        if a[i]>large:
            large=a[i]
        i+=1
    print(large)
large()

# WAF THAT TAKES A LIST OF INTEGERS AND PRINT THE SMALLEST NUMBER
def small():
    a=[1,2,3,4,5,6,7,8,9]
    small=a[0]
    i=0
    while i<len(a):
        if a[i]<small:
            small=a[i]
        i+=1
    print(small)
small()

#  WAF THAT TAKES A LIST AND AN ELEMENT AS INPUT AND PRINT    "FOUND"   IF THE ELEMENT EXISTS IN THE LIST, OTHERWISE PRINTS    "NOT FOUND"
def find():
    a=[1,2,3,4,"Shubham",2,5,7,8]
    if "Tushar" in a:
        print("FOUND")
    else:
        print("NOT FOUND")
find()

#  WAF THAT TAKES A LIST OF INTEGERS AND PRINTS HOW MANY EVEN NUMBERS ARE PRESENT IN THE LIST 
#     BY WHILE LOOP
def even():
    a=[1,2,3,4,5,6,7,8,9]
    even=0
    i=0
    while i<len(a):
        if a[i]%2==0:
            even+=1
        i+=1
    print(even)
even()

#      BY FOR LOOP
def even():
    a=[1,2,3,4,5,6,7,8,9]
    even=0
    for i in a:
        if i%2==0:
            even+=1
    print(even)
even()

#    WAF THAT TAKES  A LIST OF INTEGERS AND PRINT HOW MANY ODD NUMBERS ARE PRESENT IN THE LIST
#     BY WHILE LOOP
def odd():
    a=[1,2,3,4,5,6,7,8,9]
    odd=0
    i=0
    while i<len(a):
        if a[i]%2!=0:
            odd+=1
        i+=1
    print(odd)
odd()

#      BY FOR LOOP
def odd():
    a=[1,2,3,4,5,6,7,8,9]
    odd=0
    for i in a:
        if i%2!=0:
            odd+=1
    print(odd)
odd()

#    WAF THAT TAKES A LIST OF INTEGERS AND PRINT THE AVERAGE OF ALL THE NUMBERS
def average():
    a=[10,20,30,40,50]
    total=0
    i=0
    while i<len(a):
            total=total+a[i]
            i+=1
            average=total/len(a)
    print(average)
average()
    

#   WAF THAT TAKES A LIST OF INTEGERS AND PRINT THE COUNT OF POSITIVE NUMBERS AND NEGATIVE NUMBERS SEPERATELY ?
def pos():
    a=[1,2,3,4,-4,-2,-9]
    positive=0
    negative=0
    i=0
    while i<len(a):
        if a[i]>=1:
            positive+=1
        else:
            negative+=1
        i+=1
    print(positive)
    print(negative)
pos()

#   WAF THAT TAKES A LIST A STRING AND PRINT VOWELS FROM IT
def vowels():
    a="iron"
    vowels=0
    i=0
    while i<len(a):
        if a[i] in "aeiouAEIOU":
            vowels+=1
        i+=1
    print(vowels)
vowels()

#   WAF THAT TAKES STRING AND PRINT IT PALINDROME OR NOT
def pal(a):
    if a==a[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
pal('radar')
pal("shubham")

#   WAF THAT TAKES LIST OF INTEGERS AND PRINT ALL NUMBERS DIVISIBLE BY 5
def divide():
    a=[15,5,30,45,60,70,2]
    i=0
    while i<len(a):
        if a[i]%5==0:
            print(a[i])
        i+=1
divide()

#   WAF THAT TAKES TWO LISTS AND PRINT COMMON ELEMNETS BETWEEN THEM
def comm():
    a=["shubham",1,2,3,4,"Rohit"]
    b=["shubham",1,2,8,"Rohit",9]
    i=0
    while i<len(a):
        if a[i] in b:
            print(a[i])
        i+=1
comm()

