count=1
while count<=10:
    if count==5:
        break
    print(count)
    count+=1 


while "shubham":
    number=int(input("enter a number"))
    if number%2!=0:
        break
    
i=1
while i<=20:
    number=int(input("enter a number"))
    if number<0:
        break
    print(i)
    i+=1

while "Kohli":
    number=int(input("Enter a number"))
    if number<0:
        break

while "Kohli":
    number=(input("Enter a number"))
    print(number)
    if number=="stop":
        break

i=1
sum=0
while i<=10:
    numbers=int(input("Enter  a number"))
    sum=sum+i
    print(sum)
    i+=1

i=1
a=1
while i<=5:
    a=a*i
    print(a)
    i+=1

count=1
while count<=10:
    number=int(input("Enter a number"))
    print(number)
    if number%2!=0:
        break
    count+=1


while "true":
    numbers=int(input("Enter a number"))
    if numbers==0:
        break

count=1
sum=0
while count<=50:
    sum=sum+count
    if sum>200:
        break
    print(count)
    count+=1
print("cumulative sum =",sum)

#EVEN NUMBERS SUM STOP WHEN SUM EXCEEDS 150
i=0
sum=0
while i<=50:
    sum=sum+i
    if sum>=150:
        break
    print(i)
    i=i+2


#PRINT MULTIPLES OF 3 FROM 1 TO 60 STOP WHEN SUM EXCEEDS 150

i=1
sum=0
while i<=60:
    multiple=i*3
    sum=sum+multiple
    if sum>150:
        break
    print(multiple)
    i+=1

while "true":
    char=input("Enter a Password")
    if char=="python":
        break

#Print the multiplication table of 5, but stop after printing 5 × 7

count=1
while count<=10:
    print(count*5)
    if count==7:
        break
    count+=1

#Find the first number between 1 and 100 that is divisible by 17. Print it and stop the loop

i=1
while i<=100:
    print(i)
    if i%17==0:
        break
    i+=1

#Keep taking marks from the user. If the marks are greater than 100 or less than 0, stop the loop

while "true":
    marks=int(input("Enter a marks"))
    if marks>100 or marks<0:
        break

#Ask the user to enter integers. Calculate their sum. Stop when the user enters -1

i=1
sum=0
while i<=50:
    number=int(input("Enter a number"))
    sum=sum+i
    print(sum)
    if number<0:
        break
    i+=1
