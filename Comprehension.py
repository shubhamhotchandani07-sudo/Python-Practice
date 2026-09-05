#     In Python, a comprehension is a compact and readable way to create new collections (like lists, dictionaries, or sets) or generators from existing iterables using a single line of code. It replaces multi-line for loops with an expression.
#     # syntax [expression for i in iterable if condition]
#   FOR EXAMPLES
#   WITHOUT COMPREHENSION

n=23
if n>=18:
    print(True)
else:
    print(False)

#   WITH COMPREHENSION  ONLY IF CONDITION
n=2
if n<18:print(True) 

#   WITH COMPOREHENSION HAVING IF AND ELSE CONDITION
n=int(input("Enter a Number"))
print(True) if n>=18 else print(False) 

pas=int(input("Enter a Password"))
print(True) if pas==1234 else print(False)

#   WITH COMPREHENSION HAVING IF ELIF AND ELSE CONDITION
n=int(input("Enter a Number"))
print("Both")  if n%3==0 and n%5==0 else print(3) if n%3==0 else print(5) if n%5==0 else print(None)

grade=int(input("Enter a Grade"))
print("A") if grade>90 else print("B") if grade>80 else print("C") if grade>70 else print("D") if grade>50 else print("Fail")

number1=int(input("Enter a Number"))
number2=int(input("Enter a Number"))
print("A is Greater") if number1>number2 else print("B is Greater") if number2>number1 else print("Invalid Entered")

#     LIST COMPREHENSION 
#     MEANS TO COMPRESS THE LIST

#    WAP TO SQUARE A EACH ELEMENT FROM THE LIST AND PRINT IN NEW LIST
old=[1,2,4,5,6]
new=[]
for i in old:
    new.append(i*i)
print(new)

#BY COMPREHENSIVE
print([i*i for i in old])

print([x*x for x in range(1,11,2)])

# DATA FILTER IN LIST COMORHENSION
a=[12,23,4,7,9,0,123,23]
for x in a:
    if x>=18:
        print(x)

#    WITH COMPREHENSION
print([x for x in a if x>=18])

b=[20,1,3,7,6,5,4,8,10]
print([i for i in b if i % 2==0])

names = ["rahul", "amit", "neha"]
upper_names = [name.upper() for name in names]
print(upper_names)

#  NUMBERS FROM 0 TO 10
print([i for i in range(1,11)])

num=[1,2,3,-3,-4,3,-3,2,-2]
print([i for i in num if i>0])

words = ['Python', 'Code', 'Comprehension']
word_lengths = {word: len(word) for word in words}
print(word_lengths) 

#     Creating a list of squares
print([n*n for n in range(1,6)])


#     How do you filter a list of words to extract only those that start with a vowel 
words=["ahubham","rohit","Tushar","Ink"]
print([x for x in words if x[0] in "aeiouAEIOU"])

#    How do you create a new list containing the length of each word in a word list?
b=["shubham","cat","Rohit","Boss"]
print([  len(x) for x in b ])

#    How do you convert all words in a list to uppercase, but only if the word has more than 4 characters?
b=["shubham","cat","Rohit","Boss"]
print([ x.upper() for x in b if len(x)>4])

#    How do you transform a list of numbers by replacing even numbers with "Even" and odd numbers with "Odd"?
a=[10,2,3,4,5,6,7,8,99,9,93,39]
print([ "Even" if x % 2==0 and "Odd" else  x % 2!=0 for x in a])

#    How do you extract non-blank, clean lines from a list of raw string lines read from a file?
a=open("abc.txt")
b=a.readlines()

print([ x for x in a if x !='\n'])

#   DICTINARY COMPREHENSION
#   How do you convert a list of words into a dictionary mapping each word to its character count?
a=["Shubham","Rohit","Boss"]
print({ x:len(x) for x in a })

#   How do you filter an existing dictionary to keep only the key-value pairs where the numeric value is greater than a threshold (e.g., scores >= 80)?
scores = {
    "Rahul": 75,
    "Shubham": 90,
    "Aman": 82,
    "Rohit": 65
}
print({ x:scores[x] for x in scores if scores[x]>=80  }) 

#   How do you count the frequency of each unique word in a list of words using a dictionary comprehension?
a=["apple", "banana", "apple", "cherry", "banana", "apple"]
print( { x:a.count(x) for x in a } )

#   How do you categorize items in a dictionary based on their values (e.g., marking scores as "Pass" or "Fail")?
a={"Rahul": 85, "Amit": 30, "Priya": 45}
print( { x:"Pass" if a[x] >40 else "Fail" for x in a } )

#   How do you swap (invert) the keys and values of a dictionary?
a={"Arav":86,"Shubham":100,"Rohit":80}
print( { a[x]:x for x in a } )