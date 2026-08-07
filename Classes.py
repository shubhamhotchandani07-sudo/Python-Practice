#   In Python, a class is a blueprint or template used to create objects. It bundles data (attributes) and behaviors (methods) into a single, reusable unit.

#    Variable Inside The Class is Called "Attributes"
class Shubham:
    a="Hello Shubham"
    b="HEllo Boss"
Shubham()
print(Shubham.a)
print(Shubham.b)

#    Checking The DataType
a=Shubham()
print(type(a))

class demo:
    a="Hello How Are You"
    b="What is Your Name"

b=demo()
print(b.a, b.b)

#   Function Inside The Class is Called "Methods"
class boss:
    def Shubham(a):
        print("Hello World")

a=boss()
a.Shubham()

class hello():
    SEO="Mark"

    def Insta(self):
        print("Like")

    def FaceBook(self):
        print("Comment")

    def Twitter(self):
        print("Share")

a=hello()
print(a.SEO)

a.Insta()
a.FaceBook()
a.Twitter()


#       SELF IS A MECHANISM TO SHARE DATA 
class boss:
    a="Shubham"

    def hello(self):
        self.b=50
        print("Hello world")

    def shubham(self):
        print(self.b)
        print("Hello Boss")

c=boss()
print(type(c))

c.hello()
c.shubham()

class student:
    name="Shubham"
    roll_number="2345"
    stream="BA"

    def display(self):
        global name,roll_number,stream
        print(self.name,self.roll_number,self.stream)

a=student()
a.display()

class user:

    name='Shubham'
    mob="9530426834"
    addr="Jaipur"

    def display_info(self):
        print(self.name)
        print(self.addr)
        print(self.mob)

a=user()
b=user()
b.name="Rohit"
b.mob=8955395423
b.addr="Khetri"
c=user()
c.name="Vikas"
d=user()
d.name="Shubham"
e=user()
e.name="Boss"

b.display_info()

class dog:

    species="GS"

    def test(self):
        self.a=10
        self.b=50
        self.c=20
        self.d=55

    def hello(self):
        self.b=48
        print("hello World")

    def boss(self):
        print(self.b)
        print("Hello Woof")

a=dog()
b=dog()
print(a.species)
a.test()
a.hello()
a.boss()
b.test()
b.hello()
b.boss()
b.species="Salt"
print(b.species)
