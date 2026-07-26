def add_numbers(a, b):
    print = a + b
    return a+b

ans = add_numbers(5, 3)
print(ans)  


#A function checks a person's age. If the age is 18 or more, it returns True. If you pass the age 15 into this function, what will it return?
a=int(input("Enter Your Age"))
def age_checker(a):
    if a>18:
        print("True")
        return True
    else:
        print("False")
        return False
print(age_checker(a))

 #A function joins two words together. If you give it the inputs "Ice" and "Cream", what final result will it return?
def final(a,b):
    return a+b
print(final("Ice" , "Cream"))

#     A function takes a number and multiplies it by 10. If you pass the number 5 into this function, what value will it return?
a=int(input("Enter a number"))
def multiply(a):
    return a*10
print(multiply(a))

#     Using return: Write a function that takes a list of integers and returns the sum of all the elements.
def sum():
    list=[10,20,30,40,50]
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i+=1
    return sum
print(sum())

#    Using return: Write a function that takes a list of integers and returns the largest number in the list.
def large():
    a=[10,20,30,9,8,7,6]
    biggest=a[0]
    i=0
    while i<len(a):
        if a[i]>biggest:
            biggest=a[i]
        i+=1
    return biggest
print(large())

#   Using return: Write a function that takes a list of integers and returns the smallest number in the list
def small():
    a=[10,20,30,9,8,7,6]
    smallest=a[0]
    i=0
    while i<len(a):
        if a[i]<smallest:
            smallest=a[i]
        i+=1
    return smallest
print(small())

#   Using return: Write a function that takes a list and an element as input and returns True if the element exists in the list, otherwise returns False
a=int(input("Enter a Name"))
def exists():
    list=[10,1,2,3,4,5,6]
    i=0
    while i<(a):
        if a in list:
            return True
        else:
            return False
print(exists())

#    Using return: Write a function that takes a list of integers and returns the count of even numbers present in the list.
def count():
    a=[1,2,3,4,5,6,7,8,9]
    even=0
    i=0
    while i<len(a):
        if a[i] % 2 == 0:
            even+=1
        i+=1
    return even
print(count())

#   Using return: Write a function that takes a list of integers and returns the count of odd numbers present in the list
def count():
    a=[1,2,3,4,5,6,7,8,9]
    odd=0
    i=0
    while i<len(a):
        if a[i] % 2 != 0:
            odd+=1
        i+=1
    return odd
print(count())

#   Using return: Write a function that takes a list of integers and returns the average of all the numbers.

def sum():
    list=[10,30,60]
    i=0
    sum=0
    average=0
    while i<len(list):
        sum=sum+list[i]
        average=sum/len(list)
        i+=1
    return average
print(sum())

#   Using return: Write a function that takes a list of integers and returns the counts of positive numbers and negative numbers.
def pos():
    list=[1,2,3,4,5,6,7,-3,-6,-0,1,2,3,-5]
    i=0
    negative=0
    positive=0
    while i<len(list):
        if list[i]>0:
            positive+=1
        else:
            negative+=1
        i+=1
    return (positive,negative)

print(pos())


#Using return: Write a function that takes a string and returns the number of vowels present in it.
a=(input("Enter a name"))
def checker():
    i=0
    vowel=0
    while i<len(a):
        if a[i] in "aeiouAEIOU" :
            vowel+=1
        i+=1

    return vowel

print(checker())


b=input("Enter a Name")
def pal():
    
        if b == b[::-1]:
            return True
        else:
            return False
        
print(pal())

#    Using return: Write a function that takes a list of integers and returns a list containing all the numbers divisible by 5.

def divide():
    a=[15,5,30,45,60,70,2]
    b=[]
    i=0
    while i<len(a):
        if a[i]%5==0:
            b.append(a[i])
        i+=1
    return b
print(divide())

#    Using return: Write a function that takes two lists and returns a list of common elements between them.
def com():
    a=[1,2,3,8,7,6]
    b=[4,9,10,11,2,1]
    c=[]
    i=0
    while i<len(a):
        if a[i] in b:
            c.append(a[i])
        i+=1
    return c

print(com())

#   Using return: Write a function that takes a list of integers and returns a list containing the factorial of each element.
a=int(input("Enter a number"))
def fact(a):
        fact=1
        i=1
        while i<=a:
            fact=fact*i
            i+=1
        return fact
print(fact(a))

 