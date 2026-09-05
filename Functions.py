def hello():
      print("Hello world")
hello()


def shubham():
      a=int(input("Enter a number"))
      b=int(input("Enter a number"))
      print(a+b)
shubham()


def even_odd():
      a=int(input("Enter a number"))
      if a%2==0:
            print("Even")
      else:
            print("Odd")
even_odd()


def divideBy8():
      a=int(input("Engter a number"))
      if a%8==0:
            print("Done")
      else:
            print("Not Done")
divideBy8()


#Function banao jo 3 numbers me se largest number print kare
def largest(a,b,c):
      if a>=b and a>=c:
            print("A is Largest")
      elif b>=a and b>=c:
            print("B is laregest")
      else:
            print("C is Largest")
largest(90,20,0)


#PARAMETER AND ARGUMENTS
def start(a):
    print(a)
    print("Hello how are you")
start(7)

def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def sub(a,b):
    print(a-b)
a=int(input("ENter a number"))
b=int(input("Enter a number"))
add(a,b)
mul(a,b)
sub(a,b)

#   DOC STRING METHOD      DESCIBE WHAT DOES A FUNTION DO IS DESCRIBE BY THE DOC STRING
def string(name):
    "Its used to display the name"
    print(name)
string("Shubham")

def string(course):
    "ITS DESCRIBE THE COURSE OF THE STUDENTS"
    print(course)
string("BCA")

#   POSITIONAL ARGUMNETS 

def display(name,age):
    print(f"Name: {name}, Age: {age}")
display("Shubham",20)

print(1, 2, 3, 4, 5, 6, 7,sep="Faah")


def shubham(a,b):
      shubham("a","b")
try:
      a=int(input("Enter a number"))
      b=int(input("Enter a number"))
      print(a+b)
except:
      print("Enter a Numeric value only Not a Text or a Decimal Value")

def even_odd_checker(a,b):
      even_odd_checker(a)
try:
      a=int(input("Enter a number"))
      if a%2==0:
            print("Even")
      else:
            print("Odd")
except:
      print("Enter a Numeric Value For Even Odd Not a Text Value")

#  SQUARE OF NUMBER BY USING FUNCTION
def square(a):
      a=int(input("Enter a number"))
      print(a*a)
square("a")

#   FUNCTION FOR PRINTING THE TABLE BY TAKING THE INPUT FROM THE USER
def table(n):
      for i in range(1,11):
            print(n,"x",i,"=",n*i)
n=int(input("Enter a number"))
table(n)

#  WAP FUNCTION TO CHECK HOW MANY VOWELS PRESENT IN A CHARACTER
def vowels(shubham):
      count=0
      i=0
      while i<len(shubham):
            if shubham[i] in "aeiouAEIOU":
             count+=1
            i+=1
      print(count)
(vowels("shubham"))

#WAP FUNCTION TO CHECK HOW MANY EVEN NUMBERS PRESENT 
def even():
    a = int(input("Enter a number: "))
    for i in range(1, a + 1):
        if i % 2 == 0:
            print(i)
even()