#     READ OPERATIONS ON A FILE
a=open(r"C:/Users/ADMIN/OneDrive/Desktop/Catalyst python/Return_Functions.py")
print(a.read())
print(a.readable())
print(a.readline())
print(a.readlines())

a=open("Hello.txt","r")
print(a.readable())
print(a.writable())

b=a.read()
print(b)
#   VOWELS COUNTING
i=0
vowel=0
while i<len(b):
    if  b[i] in "AEIOUaeiou" :
        vowel+=1
    i+=1
print(vowel)

#   Count the total number of words in a file?
i=0
space=0
while i<len(b):
    if b[i] in " ":
        space+=1
    i+=1
print(space)

#   BY COUNT WE ALSO CALCULATE TOTAL WORDS
print(b.count(' '))

#   Count the total number of lines present in a text file?
print(b.count("\n"))

#  Display only the lines in a file that contain the word "India"?
a=open("Hello.txt","r")
b=a.readlines()
i=0
while i<len(b):
    if "India" in b[i]:
        print(b[i])
    i+=1

# Write Mode  APPEND MODE
# a=open("abc.txt",'a')
# print(a.write("\n How are you Boss"))

# b=open(r"C:/Users/ADMIN/Downloads","rb")


# a=open("abc.txt","+r")
# print(a.readable())
# print(a.writable())

# a=open("abc.txt","+a")
# print(a.readable())
# print(a.writable())
# print(a.write("Hello"))

#    COPY PASTE OF FILES USING PYTHON
# a=open("abc.txt")
# b=a.read()

# c=open("Hello.txt","w")
# c.write(b)

#    **Take a word from the user and count how many times that word appears across an entire file?**
# a=open("abc.txt","r")dfddede
# b=a.read()
# print(b)
# c=input("Enter a Word")
# appear=b.count(c)
# print("Total Appear is :",appear)

#    Take 5 words from the user and count how many times each word appears across an entire file?
# a=open("abc.txt","r")
# b=a.read()
# print(b)
# c=input("Enter a Word")
# d=input("Enter a Word")
# e=input("Enter a Word")
# f=input("Enter a Word")
# g=input("Enter a Word")
# appear=b.count(c)
# h=b.count(d)
# i=b.count(e)
# j=b.count(f)
# k=b.count(g)
# print("Total Appear is :",appear)
# print("Total Appear is :",h)
# print("Total Appear is :",i)
# print("Total Appear is :",j)
# print("Total Appear is :",k)

#    Copy non-blank lines from a source file into a clean list of data?
a=open("abc.txt")
b=a.readlines()
c=[]
i=0
while i<len(b):
    if b[i]!=' ':
        c.append(b[i])
    i+=1
print(c)

