#A user is registering on your website and accidentally types their email with extra spaces at the beginning and end: email = "   alex@gmail.com   ". Write a piece of code to clean this input and extract only the valid email ID

email="   alex@gmail.com   "
print(email.strip())

#You are building a secure web crawler. Given a URL string url = "https://xyz.com", write a line of code to verify if the website protocol starts with "https"

url="https://xyz.com"
print(url.startswith("https"))

#A Python script needs to clean up server log files. Given the line log_entry = "[ERROR]===System Crash===", write a line of code to strip away only the trailing = characters from the right side.

a="[ERROR]===System Crash==="
print(a.strip("="))

#A user uploads a file named document = "final_report.pdf". Write a piece of code to check if this file ends with the appropriate ".pdf" extension

b="final_report.pdf"
print(b.endswith("py"))

#You are building a search bar for an e-commerce store. A user searches for "IPHONE", but the database inventory holds the item as "iphone". Write code to convert the user's search string so it matches the database perfectly, regardless of case

d="IPHONE"
print(d.lower())

#right-justify

a="450"
print(a.rjust(6))

#replace ques
c="This software has nusty bug"
print(c.replace("nusty","bad"))

#startswith
k="# hello world"
print(k.startswith("#"))

#lstrip
s="www.google.com"
print(s.lstrip("www."))

#justify
d="775"
print(d.rjust(6,"0"))

#replace space
f="blue running space"
print(f.replace(" ","-"))

#rstrip
r="KEY123XYZ\n"
print(r.rstrip())

#uppercase
k="sub-domain-01"
print(k.upper())

p="python"
print(len(p))

o="coder_99"
print(o.isalnum())

a="shu bham"
print(a.count(""))
   
text = "Python"
i = 0
while i < 6:
    print(text[i])
    i = i + 1

a="shubham"
i=0
while i<=5:
    print(a[i])
    i+=1

l="rohit"
i=len(l)-1
while i>=0:
    print(l[i])
    i-=1

q="shubham"
vow=0
i=0
while i<len(q):
    if q[i] in "aeiouAEIOU":
        vow+=1
    i+=1
print(vow)

l="hello world how are you"
count=0
i=0
while i<len(l):
    if l[i] in " ":
        count=count+1
    i=i+1
print(count)


g="shubham"
j=""
i=0
while i<len(g):
    b=b+a[i]
    i+=1
print(b)